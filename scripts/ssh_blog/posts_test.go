package main

import (
	"regexp"
	"strings"
	"testing"

	tea "charm.land/bubbletea/v2"
)

func TestToTerminal(t *testing.T) {
	got := toTerminal(`{{<youtube-lite id="abc" title="A talk">}} and [x](/git-history/)`)
	want := "▶ [A talk](https://youtu.be/abc) and [x](https://blog.tobked.dev/git-history/)"
	if got != want {
		t.Fatalf("got %q", got)
	}
}

func TestToTerminalKeepsImageCaption(t *testing.T) {
	got := toTerminal("![Alt](/a.jpg \"A [link](https://x.org) caption\")\n")
	want := "![Alt](https://blog.tobked.dev/a.jpg)\n\n*A [link](https://x.org) caption*\n"
	if got != want {
		t.Fatalf("got %q", got)
	}
}

func TestClampsClientWindowSize(t *testing.T) {
	var m tea.Model = newModel(nil)
	m, _ = m.Update(tea.WindowSizeMsg{Width: 8000, Height: 8000})
	if vp := m.(model).vp; vp.Width() != 300 || vp.Height() != 149 {
		t.Fatalf("viewport is %dx%d", vp.Width(), vp.Height())
	}
}

func TestReaderShowsFrontMatterTitle(t *testing.T) {
	m := newModel(nil)
	m.vp.SetWidth(80)
	plain := func(p post) string { return regexp.MustCompile(`\x1b\[[0-9;]*m`).ReplaceAllString(m.render(p), "") }
	if out := plain(post{Title: "Django on GCP", Body: "# Repository with code\n\ntext"}); !strings.Contains(out, "Django on GCP") {
		t.Errorf("title missing:\n%s", out)
	}
	if out := plain(post{Title: "Same", Body: "# Same\n\ntext"}); strings.Count(out, "Same") != 1 {
		t.Errorf("title repeated:\n%s", out)
	}
}

func TestLoadRealSite(t *testing.T) {
	all, err := loadSite("../..")
	if err != nil {
		t.Fatal(err)
	}
	about := all[0]
	if about.Path != "/pages/about-me/" || !about.page {
		t.Fatalf("first entry is %q, want About", about.Title)
	}
	for _, want := range []string{"## Elsewhere", "github.com/TobKed", siteURL + "/feeds/all.rss.xml"} {
		if !strings.Contains(about.Body, want) {
			t.Errorf("About is missing %q", want)
		}
	}

	links := all[1]
	if links.Path != "/pages/links/" || !links.page {
		t.Fatalf("second entry is %q (%s), want Links", links.Title, links.Path)
	}
	if len(links.subpages) < 6 {
		t.Fatalf("Links has %d subpages, want at least 6", len(links.subpages))
	}
	wantSubpages := map[string]bool{
		"/pages/ai-resources/": false,
		"/pages/async-multithreading-and-multiprocessing-resources/": false,
		"/pages/microservices-resources/":                            false,
		"/pages/python-django-resources/":                            false,
		"/pages/sleep/":                                              false,
		"/pages/writing/":                                            false,
	}
	for _, sub := range links.subpages {
		if !sub.page || sub.Title == "" || sub.Body == "" {
			t.Errorf("bad subpage %+v", sub)
		}
		if _, ok := wantSubpages[sub.Path]; ok {
			wantSubpages[sub.Path] = true
		}
	}
	for path, seen := range wantSubpages {
		if !seen {
			t.Errorf("Links is missing subpage %s", path)
		}
	}

	var posts []post
	for _, p := range all {
		if p.Draft || p.Title == "" || strings.Contains(p.Body, "{{<") {
			t.Errorf("bad entry %q", p.Title)
		}
		if p.page {
			if p.Path == "/pages/sleep/" || p.Path == "/pages/blogs/" {
				t.Errorf("unlisted or draft page %s is shown", p.Path)
			}
			continue
		}
		posts = append(posts, p)
	}
	if len(posts) < 50 {
		t.Fatalf("only %d posts", len(posts))
	}
	for i, p := range posts {
		if len(p.Date) < 10 || p.Path != "/"+p.Slug+"/" {
			t.Errorf("bad post %q (%s, %s)", p.Title, p.Date, p.Path)
		}
		if i > 0 && posts[i-1].Date < p.Date {
			t.Errorf("not sorted at %q", p.Title)
		}
	}
}

func TestNavigateLinksSubpagesAndVimKeys(t *testing.T) {
	all, err := loadSite("../..")
	if err != nil {
		t.Fatal(err)
	}
	var tm tea.Model = newModel(all)
	tm, _ = tm.Update(tea.WindowSizeMsg{Width: 100, Height: 20})

	press := func(k tea.KeyPressMsg) model {
		tm, _ = tm.Update(k)
		return tm.(model)
	}
	runeKey := func(r rune) tea.KeyPressMsg {
		return tea.KeyPressMsg{Code: r, Text: string(r)}
	}

	// Move down from About to Links with 'j' and open Links with Enter.
	m := press(runeKey('j'))
	m = press(tea.KeyPressMsg{Code: tea.KeyEnter})
	if m.sublist == nil || m.reading != nil {
		t.Fatalf("expected Links sublist to be open, got sublist=%v reading=%v", m.sublist, m.reading)
	}

	// Navigate to the last subpage with 'G', then first with 'g', then second with 'j'.
	m = press(runeKey('G'))
	if got := m.sublist.Index(); got != len(all[1].subpages)-1 {
		t.Fatalf("after G: index=%d, want %d", got, len(all[1].subpages)-1)
	}
	m = press(runeKey('g'))
	if got := m.sublist.Index(); got != 0 {
		t.Fatalf("after g: index=%d, want 0", got)
	}
	m = press(runeKey('j'))
	if got := m.sublist.Index(); got != 1 {
		t.Fatalf("after j: index=%d, want 1", got)
	}

	// Open the selected subpage with Enter.
	m = press(tea.KeyPressMsg{Code: tea.KeyEnter})
	if m.reading == nil || m.reading.Path != all[1].subpages[1].Path {
		t.Fatalf("expected reading subpage %s, got %+v", all[1].subpages[1].Path, m.reading)
	}
	// Verify OSC 8 hyperlink sequences are emitted in rendered content.
	if !strings.Contains(m.render(*m.reading), "\x1b]8;") {
		t.Fatalf("rendered subpage missing OSC 8 hyperlink sequence")
	}

	// Jump to bottom with 'G' and back to top with 'g' inside the reader.
	m = press(runeKey('G'))
	if !m.vp.AtBottom() {
		t.Fatalf("expected viewport at bottom after G")
	}
	m = press(runeKey('g'))
	if !m.vp.AtTop() {
		t.Fatalf("expected viewport at top after g")
	}

	// Press 'h' to return from the subpage reader to the Links sublist.
	m = press(runeKey('h'))
	if m.reading != nil || m.sublist == nil {
		t.Fatalf("expected to return to Links sublist after h, got reading=%v sublist=%v", m.reading, m.sublist)
	}

	// Press 'h' again to return from Links sublist to the main list.
	m = press(runeKey('h'))
	if m.sublist != nil || m.reading != nil {
		t.Fatalf("expected to return to main list after h, got sublist=%v reading=%v", m.sublist, m.reading)
	}
}
