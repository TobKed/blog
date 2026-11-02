package main

import (
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"

	"gopkg.in/yaml.v3"
)

const siteURL = "https://blog.tobked.dev"

type post struct {
	Title   string   `yaml:"title"`
	Date    string   `yaml:"date"`
	Slug    string   `yaml:"slug"`
	Summary string   `yaml:"summary"`
	Tags    []string `yaml:"tags"`
	Draft   bool     `yaml:"draft"`
	Body    string   `yaml:"-"`
}

func (p post) day() string { return p.Date[:min(10, len(p.Date))] }

// item adapts a post to bubbles' list.DefaultItem.
type item struct{ p post }

func (i item) Title() string       { return i.p.Title }
func (i item) Description() string { return i.p.day() + "  " + i.p.Summary }
func (i item) FilterValue() string { return i.p.Title + " " + strings.Join(i.p.Tags, " ") }

var (
	youtube   = regexp.MustCompile(`\{\{<\s*youtube-lite\b([^>]*)>\}\}`)
	attr      = regexp.MustCompile(`(\w+)="([^"]*)"`)
	localLink = regexp.MustCompile(`\]\(/`)
)

// toTerminal rewrites Hugo-only syntax into plain Markdown.
func toTerminal(md string) string {
	md = youtube.ReplaceAllStringFunc(md, func(s string) string {
		a := map[string]string{}
		for _, m := range attr.FindAllStringSubmatch(s, -1) {
			a[m[1]] = m[2]
		}
		return fmt.Sprintf("▶ [%s](https://youtu.be/%s)", a["title"], a["id"])
	})
	return localLink.ReplaceAllString(md, "]("+siteURL+"/")
}

func loadPosts(dir string) ([]post, error) {
	files, err := filepath.Glob(filepath.Join(dir, "*.md"))
	if err != nil {
		return nil, err
	}
	var posts []post
	for _, f := range files {
		raw, err := os.ReadFile(f)
		if err != nil {
			return nil, err
		}
		parts := bytes.SplitN(raw, []byte("---\n"), 3)
		if len(parts) != 3 {
			return nil, fmt.Errorf("%s: no front matter", f)
		}
		var p post
		if err := yaml.Unmarshal(parts[1], &p); err != nil {
			return nil, fmt.Errorf("%s: %w", f, err)
		}
		if p.Draft {
			continue
		}
		p.Body = toTerminal(string(parts[2]))
		posts = append(posts, p)
	}
	sort.Slice(posts, func(i, j int) bool { return posts[i].Date > posts[j].Date })
	return posts, nil
}
