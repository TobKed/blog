package main

import (
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

func TestLoadRealPosts(t *testing.T) {
	posts, err := loadPosts("../../content/post")
	if err != nil {
		t.Fatal(err)
	}
	if len(posts) < 50 {
		t.Fatalf("only %d posts", len(posts))
	}
	for i, p := range posts {
		if p.Draft || p.Title == "" || len(p.Date) < 10 || strings.Contains(p.Body, "{{<") {
			t.Errorf("bad post %q (%s)", p.Title, p.Date)
		}
		if i > 0 && posts[i-1].Date < p.Date {
			t.Errorf("not sorted at %q", p.Title)
		}
	}
}
