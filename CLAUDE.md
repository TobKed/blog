# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal blog (blog.tobked.dev) built with [Hugo](https://github.com/gohugoio/hugo). Content is
Markdown with YAML front matter in `content/`, theme is the `hugo-theme-stack` git submodule
under `themes/`. Output is generated into `public/` and deployed to the `gh-pages` branch by CI.

Requires Hugo **extended** 0.146 or newer; CI pins 0.165.0.

## Commands

Build/serve (via Makefile, wraps `hugo`):

- `make serve` — `hugo server -D`, serve + live reload at http://localhost:1313, includes drafts — normal way to preview edits
- `make build` — build into `public/`
- `make publish` — production build (`--gc --minify`) plus the pagefind search index
- `make clean` — remove `public/`
- `make resize_images` — run `scripts/resize_photos/main.py` (resizes `scripts/resize_photos/input/` → `output/`, max 1024x1024 @ 300dpi)
- `make generate_post` — run `scripts/generate_post.py` to scaffold a new monthly links post

Equivalent `invoke` tasks exist in `tasks.py` (`build`, `serve`, `publish`, `clean`) but the Makefile is the primary interface.

Pre-commit (black, isort, mdformat, trailing-whitespace, etc.) runs in CI on every push/PR — run `pre-commit run --all-files` locally before committing if unsure.

Deployment is handled by GitHub Actions (`.github/workflows/main.yml`): pre-commit checks run
always; the `build` job runs on push to `master`, builds with Hugo, generates the pagefind index,
and publishes `public/` to `gh-pages` via `peaceiris/actions-gh-pages` (CNAME `blog.tobked.dev`).
The `GOOGLE_ANALYTICS` secret is injected as `HUGO_SERVICES_GOOGLEANALYTICS_ID`. A second workflow
(`test-links` / `scripts/test_links/`) is manually triggered to crawl the live site and check for
broken links (two-phase: fast `requests` pass, then `selenium` re-check of failures).

## Content structure

- `content/post/*.md` — blog posts, filename convention `YYYY_MM_DD_slug.md`; the URL comes from the `slug` front matter field, not the filename
- `content/pages/*.md` — static pages, served at `/pages/<slug>/`
- `content/tags/`, `content/categories/` — term stubs that only carry `aliases` redirecting the old Pelican `/tag/<x>` and `/category/<x>` URLs
- `content/search/_index.md` — the pagefind search page
- `static/images/`, `static/audio/`, `static/css/` — static assets, copied verbatim to the site root
- `layouts/home.rss.xml`, `layouts/home.atom.xml` — feeds published at `/feeds/all.rss.xml` and `/feeds/all.atom.xml` (the URLs the Pelican site used)
- `hugo.toml` — all configuration: permalinks, menus, social links, feeds, highlighting

### Front matter

YAML, delimited by `---`. Keys in use: `title`, `date`, `slug`, `summary`, `tags`, `categories`,
`image` (per-post header cover), `draft`, and `build` (used on a few pages that must render at
their URL but stay out of lists, menus and feeds).

### Monthly "links" posts

A large fraction of posts are recurring monthly link round-ups, filename
`YYYY_MM_DD_<month>_links.md` (dated the last day of the month), with `draft: true` until publish.
`content/post/2026_xx_xx_template_links.md` is the template with the standard section headers
(Articles, Productivity, AI, Security, Python, Django, Python libraries, Django libraries, Go,
Tools, Cloud, Other stuff, Podcasts, Videos).

Two routes exist for curating these:

- `scripts/generate_post.py` — scaffolds a new month's post from the template (used by `make generate_post`)
- `scripts/blog_automation_2/` — CLI tool (`insert_links_tool.py` for a single URL, `bulk_process_links.py` for a batch file) that fetches a URL via `crawl4ai`, uses an LLM (LangChain/OpenAI) to generate title/summary/tags, dedupes against every existing post via `link_registry.py`, and inserts formatted Markdown into the right section of the target post. Core logic lives in `link_processing/`; tests are under `scripts/blog_automation_2/tests/` (run with `PYTHONPATH=. pytest` from that directory, after `pip install -r requirements-dev.txt`).
- The `add-link-to-blog` skill (see "Agent skills" below; invocable as `/add-link-to-blog`) encodes the same workflow (fetch → dedupe → categorize into a section → ask user to confirm snippet vs. AI summary → append to `content/post/YYYY_MM_DD_monthname_links.md`) for use directly by an agent instead of the scripts above.

Both routes converge on the same target-file/section conventions, so when adding links by hand,
match the existing formatting in a recent `*_links.md` post (standard link vs. YouTube embed block).
YouTube embeds are raw HTML `<div class="videoWrapper">` blocks, which work because
`markup.goldmark.renderer.unsafe` is enabled in `hugo.toml`.

## Other scripts

- `scripts/resize_photos/` — Pillow-based image resizer, `input/` → `output/`; resized files are copied by hand into `static/images/posts/YYYY/`
- `scripts/test_links/` — link checker described above under Commands

## Notes

- `hugo-theme-stack` (theme) is a git submodule; `git submodule update --init --recursive` if it's missing.
- Agent skills: every agent tool used here looks in a different project directory, so the skill body
  lives once in `.agents/skills/<name>/SKILL.md` (read natively by Codex CLI and Antigravity) and
  `.claude/skills/<name>/SKILL.md` (Claude Code) and `.cursor/skills/<name>/SKILL.md` (Cursor) hold
  short stubs that carry the frontmatter and point at it. Symlinks are deliberately not used —
  Claude Code's skill discovery does not follow them. Edit the `.agents/` copy; the stubs never
  change. `.agents/skills/` is excluded from mdformat in `.pre-commit-config.yaml` so the
  instruction text is not reformatted.
- Secrets (OpenAI key, etc.) are loaded via `.env`/`python-dotenv`, consumed by `scripts/blog_automation_2/config.py` (`GOOGLE_ANALYTICS`, `ACCESS_TOKEN` come from CI secrets for deploy).
