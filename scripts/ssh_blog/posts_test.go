package main

import (
	"regexp"
	"strings"
	"testing"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

func TestToTerminal(t *testing.T) {
	got := toTerminal(`{{<youtube-lite id="abc" title="A talk">}} and [x](/git-history/)`)
	want := "▶ [A talk](https://youtu.be/abc) and [x](https://blog.tobked.dev/git-history/)"
	if got != want {
		t.Fatalf("got %q", got)
	}
}

func TestClampsClientWindowSize(t *testing.T) {
	var m tea.Model = newModel(nil, lipgloss.NewRenderer(nil))
	m, _ = m.Update(tea.WindowSizeMsg{Width: 8000, Height: 8000})
	if vp := m.(model).vp; vp.Width != 300 || vp.Height != 149 {
		t.Fatalf("viewport is %dx%d", vp.Width, vp.Height)
	}
}

func TestReaderShowsFrontMatterTitle(t *testing.T) {
	m := newModel(nil, lipgloss.NewRenderer(nil))
	m.vp.Width = 80
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
