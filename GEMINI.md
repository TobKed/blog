# Blog

This is a personal blog created with [Hugo](https://github.com/gohugoio/hugo), a static site
generator written in Go. The blog content is written in Markdown with YAML front matter and the
theme is [hugo-theme-stack](https://github.com/CaiJimmy/hugo-theme-stack), vendored
as a git submodule under `themes/`.

All configuration lives in `hugo.toml`. The content is located in the `content/` directory, with
posts in `content/post/` and pages in `content/pages/`. Static assets (images, audio, css) live in
`static/` and are copied verbatim to the site root. The build output goes to `public/`.

Hugo **extended** 0.146 or newer is required; CI pins 0.165.0.

## Commands

- **`make serve`**: Serves the site at http://localhost:1313 with live reload, including drafts.
- **`make build`**: Builds the site into `public/`.
- **`make publish`**: Production build (`--gc --minify`) plus the pagefind search index.
- **`make clean`**: Removes `public/`.
- **`make generate_post`**: Scaffolds a new monthly links post from the template.
- **`make resize_images`**: Resizes images in `scripts/resize_photos/input/`.

## Posts

Posts live in `content/post/` and are named `YYYY_MM_DD_post-title.md`. The published URL comes
from the `slug` front matter field, not the filename. Front matter is YAML:

```yaml
---
draft: true
title: Month summary - March 2026
date: '2026-03-31'
tags:
  - python
  - summary
slug: 2026-march-links
summary: Interesting stuff from the month
image: /images/posts/2026/2026_03_xx.jpg
categories:
  - summary
---
```

Set `draft: true` while a post is unfinished — Hugo excludes drafts from the build entirely
(`make serve` shows them, `make build` does not).

## Deployment

Pushing to `master` triggers `.github/workflows/main.yml`, which runs pre-commit, builds with
Hugo, generates the pagefind search index and publishes `public/` to the `gh-pages` branch
(custom domain `blog.tobked.dev`).
