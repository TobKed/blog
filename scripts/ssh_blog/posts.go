package main

import (
	"bytes"
	"cmp"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"

	"github.com/BurntSushi/toml"
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
	Build   struct {
		List   string `yaml:"list"`
		Render string `yaml:"render"`
	} `yaml:"build"`

	// About page only.
	Layout string `yaml:"layout"`
	Name   string `yaml:"name"`
	Talks  []struct {
		Title, Where, When, URL string
	} `yaml:"talks"`
	Certifications []struct {
		Year              any
		Name, Issuer, URL string
	} `yaml:"certifications"`

	Body     string `yaml:"-"`
	Path     string `yaml:"-"` // URL path on the website
	page     bool
	subpages []post
}

type siteConfig struct {
	Params struct {
		Tagline  string
		Epigraph struct{ Title, Text, Cite string }
	}
	Menu struct {
		Social []struct {
			Name, URL string
			Weight    int
		}
	}
}

func (p post) day() string { return p.Date[:min(10, len(p.Date))] }

// item adapts a post to bubbles' list.DefaultItem.
type item struct{ p post }

func (i item) Title() string { return i.p.Title }
func (i item) Description() string {
	if i.p.page {
		if i.p.Summary != "" {
			return "page · " + i.p.Path + "  " + i.p.Summary
		}
		return "page · " + i.p.Path
	}
	return i.p.day() + "  " + i.p.Summary
}
func (i item) FilterValue() string { return i.p.Title + " " + strings.Join(i.p.Tags, " ") }

var (
	youtube  = regexp.MustCompile(`\{\{<\s*youtube-lite\b([^>]*)>\}\}`)
	attr     = regexp.MustCompile(`(\w+)="([^"]*)"`)
	figure   = regexp.MustCompile(`(?m)^(!\[[^\]]*\]\([^\s)]+) "([^"]*)"\)[ \t]*$`)
	pageLink = regexp.MustCompile(`\(` + regexp.QuoteMeta(siteURL) + `(/pages/[^)\s]+)\)`)
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
	md = figure.ReplaceAllString(md, "$1)\n\n*$2*")
	return strings.ReplaceAll(md, "](/", "]("+siteURL+"/")
}

func absURL(u string) string {
	if strings.HasPrefix(u, "/") {
		return siteURL + u
	}
	return u
}

// loadSite returns the listed pages (About first) followed by posts, newest first.
func loadSite(root string) ([]post, error) {
	var cfg siteConfig
	if _, err := toml.DecodeFile(filepath.Join(root, "hugo.toml"), &cfg); err != nil {
		return nil, err
	}
	sort.SliceStable(cfg.Menu.Social, func(i, j int) bool { return cfg.Menu.Social[i].Weight < cfg.Menu.Social[j].Weight })

	allPages, err := loadDir(filepath.Join(root, "content/pages"), "/pages/")
	if err != nil {
		return nil, err
	}
	allPosts, err := loadDir(filepath.Join(root, "content/post"), "/")
	if err != nil {
		return nil, err
	}
	byPath := make(map[string]post, len(allPages))
	for i := range allPages {
		allPages[i].page = true
		if allPages[i].Layout == "about" {
			allPages[i].Body = aboutMarkdown(allPages[i], cfg)
		}
		byPath[allPages[i].Path] = allPages[i]
	}
	var pages []post
	for _, p := range allPages {
		if p.Build.List == "never" {
			continue
		}
		for _, m := range pageLink.FindAllStringSubmatch(p.Body, -1) {
			if sub, ok := byPath[m[1]]; ok && sub.Build.List == "never" {
				p.subpages = append(p.subpages, sub)
			}
		}
		pages = append(pages, p)
	}
	var posts []post
	for _, p := range allPosts {
		if p.Build.List != "never" {
			posts = append(posts, p)
		}
	}
	sort.SliceStable(pages, func(i, j int) bool { return pages[i].Layout == "about" && pages[j].Layout != "about" })
	sort.SliceStable(posts, func(i, j int) bool { return posts[i].Date > posts[j].Date })
	return append(pages, posts...), nil
}

// loadDir reads the published, rendered Markdown files in dir.
func loadDir(dir, urlPrefix string) ([]post, error) {
	files, err := filepath.Glob(filepath.Join(dir, "*.md"))
	if err != nil {
		return nil, err
	}
	var out []post
	for _, f := range files {
		raw, err := os.ReadFile(f)
		if err != nil {
			return nil, err
		}
		rest, ok := bytes.CutPrefix(raw, []byte("---\n"))
		fm, body, ok2 := bytes.Cut(rest, []byte("\n---\n"))
		if !ok || !ok2 {
			return nil, fmt.Errorf("%s: no front matter", f)
		}
		var p post
		if err := yaml.Unmarshal(fm, &p); err != nil {
			return nil, fmt.Errorf("%s: %w", f, err)
		}
		if p.Draft || p.Build.Render == "never" {
			continue
		}
		p.Body = toTerminal(string(body))
		p.Path = urlPrefix + p.Slug + "/"
		out = append(out, p)
	}
	return out, nil
}

// aboutMarkdown mirrors the theme's about.html, which builds the page from
// front matter and hugo.toml rather than the Markdown body.
func aboutMarkdown(p post, cfg siteConfig) string {
	var b strings.Builder
	fmt.Fprintf(&b, "# %s\n\n%s\n\n%s\n\n## Elsewhere\n\n", cmp.Or(p.Name, p.Title), cfg.Params.Tagline, p.Body)
	for _, s := range cfg.Menu.Social {
		u := absURL(s.URL)
		if addr, ok := strings.CutPrefix(u, "mailto:"); ok {
			u = "`" + addr + "`" // glamour would print an autolinked address twice
		}
		fmt.Fprintf(&b, "- **%s** %s\n", s.Name, u)
	}
	if e := cfg.Params.Epigraph; e.Text != "" {
		fmt.Fprintf(&b, "\n## %s\n\n> “%s”\n>\n> — %s\n", e.Title, e.Text, e.Cite)
	}
	if len(p.Talks) > 0 {
		b.WriteString("\n## Talks\n\n")
		for _, t := range p.Talks {
			fmt.Fprintf(&b, "- **%s** — %s, %s", t.Title, t.Where, t.When)
			if t.URL != "" {
				fmt.Fprintf(&b, " %s", absURL(t.URL))
			}
			b.WriteString("\n")
		}
	}
	if len(p.Certifications) > 0 {
		b.WriteString("\n## Certifications\n\n")
		for _, c := range p.Certifications {
			fmt.Fprintf(&b, "- %v **%s** — %s\n", c.Year, c.Name, c.Issuer)
		}
	}
	return b.String()
}
