package main

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestToTerminal(t *testing.T) {
	got := toTerminal(`{{<youtube-lite id="abc" title="A talk">}} and [x](/git-history/)`)
	want := "▶ [A talk](https://youtu.be/abc) and [x](https://blog.tobked.dev/git-history/)"
	if got != want {
		t.Fatalf("got %q", got)
	}
}

func TestFrontMatterMustOpenFile(t *testing.T) {
	dir := t.TempDir()
	os.WriteFile(filepath.Join(dir, "x.md"), []byte("intro\n---\ntitle: x\n---\nbody\n"), 0o644)
	if _, err := loadDir(dir, "/"); err == nil {
		t.Fatal("accepted a file without leading front matter")
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
	for _, want := range []string{"github.com/TobKed", "linkedin.com/in/tobiaszkedzierski", "## Talks", "Terraform Associate", siteURL + "/feeds/all.rss.xml"} {
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
