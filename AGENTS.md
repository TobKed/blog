# AGENTS.md

This file is the canonical guide for AI coding agents working in this repository (`CLAUDE.md`, `GEMINI.md`, and `.cursorrules` all point here).

## Project overview

Personal blog (blog.tobked.dev) built with [Hugo](https://github.com/gohugoio/hugo). Content is
Markdown with YAML front matter in `content/`, theme is `ups-and-downs` under `themes/` (written
for this blog, lives in-repo). Output is generated into `public/` and deployed to the `gh-pages` branch by CI.

Requires Hugo **extended** 0.146 or newer; CI pins 0.165.0. `mise.toml` pins Hugo locally
(`mise install`); Python is pinned in `.python-version` and managed with `uv`
(`uv venv && uv pip install -r requirements.txt`). Both match CI.

## Commands

Build/serve (via Makefile, wraps `hugo`):

- `make serve` — `hugo server -D -M`, serve + live reload at http://localhost:1313, includes drafts — normal way to preview edits
- `make build` — build into `public/`
- `make publish` — production build (`--gc --minify`) plus the pagefind search index
- `make preview` — run `make publish` and serve `public/` at http://localhost:1314 (use this to test Pagefind search locally)
- `make clean` — remove `public/`
- `make resize_images` — run `scripts/resize_photos/main.py` (resizes `scripts/resize_photos/input/` → `output/`, max 1024x1024 @ 300dpi)
- `make generate_post` — run `scripts/generate_post.py` to scaffold a new monthly links post
- `make check_links` — run `scripts/check_duplicate_links.py` to report duplicated links across posts in `content/post/`
- `make check_theme` — run `scripts/check_mobile.mjs` against a running `make preview` to verify mobile/desktop layout and theme regressions
- `make ssh_blog` — serve the blog over SSH at `localhost:2222` (`cd scripts/ssh_blog && go run .`)

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
- `content/pages/*.md` — static and curated topic pages, served at `/pages/<slug>/`:
  - `content/pages/links.md` (`/pages/links/`) is the main navbar hub page linking to all curated topic sub-pages (`ai.md`, `async.md`, `microservices.md`, `python.md`, `sleep.md`, `writing.md`).
  - See `content/pages/AGENTS.md` for the topic page catalog, entry formatting rules (`- **[Title](URL)**: Description`), and instructions for adding or updating curated topic pages.
- `content/images/posts/YYYY/` — post cover and inline images
- `content/tags/`, `content/categories/` — term stubs that only carry `aliases` redirecting the old Pelican `/tag/<x>` and `/category/<x>` URLs
- `content/search.md` — the search page; `ups-and-downs` renders it with pagefind, so results only appear in a build that ran `npx pagefind` (`make publish` / `make preview` / CI), not under `make serve`
- `static/images/`, `static/audio/` — static assets, copied verbatim to the site root
- `layouts/home.rss.xml`, `layouts/home.atom.xml` — feeds published at `/feeds/all.rss.xml` and `/feeds/all.atom.xml` (the URLs the Pelican site used)
- `hugo.toml` — all configuration: permalinks, menus, social links, feeds, highlighting

### Front matter

YAML, delimited by `---`. Keys in use: `title`, `date`, `slug`, `summary`, `tags`, `categories`,
`image` (per-post header cover) with optional `image_alt` (alt text; falls back to the title),
`image_caption` (the line under the cover, as written; e.g. where it was taken, or "Photo by …"
for someone else's photo), `draft`, and `build` (used on curated topic pages that must render at
their `/pages/<slug>/` URL with `build: { list: never, render: always }` so they stay out of post lists, menus, and feeds).

### Monthly "links" posts & Curated topic pages

A large fraction of posts are recurring monthly link round-ups, filename
`YYYY_MM_DD_<month>_links.md` (dated the last day of the month), with `draft: true` until publish.
`content/post/2026_xx_xx_template_links.md` is the template with the standard section headers
(Articles, Productivity, AI, Security, Python, Django, Python libraries, Django libraries, Go,
Tools, Cloud, Other stuff, Podcasts, Videos).

Routes for curating these:

- `scripts/generate_post.py` — scaffolds a new month's post from the template (used by `make generate_post`)
- `scripts/blog_automation_2/` — CLI tool (`insert_links_tool.py` for a single URL, `bulk_process_links.py` for a batch file) that fetches a URL via `crawl4ai`, uses an LLM (LangChain/OpenAI) to generate title/summary/tags, dedupes against every existing post via `link_registry.py`, and inserts formatted Markdown into the right section of the target post. Core logic lives in `link_processing/`; tests are under `scripts/blog_automation_2/tests/` (run with `PYTHONPATH=. pytest` from that directory, after `pip install -r requirements-dev.txt`).
- The `add-link-to-blog` skill (see "Agent instructions & skills" below; invocable as `/add-link-to-blog`) encodes the workflow (fetch → dedupe across `content/post/` and `content/pages/` → categorize into a monthly post section and any matching curated topic pages in `content/pages/AGENTS.md` → ask user to confirm targets and snippet vs. AI summary → write to the confirmed files) for use directly by an agent.

When adding links by hand, match the existing formatting in a recent `*_links.md` post (standard link vs. YouTube video) and `content/pages/AGENTS.md` (for curated topic pages).
YouTube videos in posts use the theme's `{{<youtube-lite id="…" title="…">}}` shortcode: a click-to-play
preview whose thumbnail is fetched at build time, so no request reaches YouTube until a reader
presses play. Write it without a space after `{{<` and with typographic quotes (`“ ”`) in the title;
mdformat (pre-commit) escapes `{{< ` and `\"`, which breaks the shortcode.
If a link is intentionally repeated within `content/post/` (for example, discussed in `## Some thoughts` and also listed in `## Articles`), mark the inline mention line with `<!-- dup-ok -->` so `make check_links` skips it.

## Other scripts & Python conventions

- `scripts/resize_photos/` — Pillow-based image resizer, `input/` → `output/`; resized files are copied into `content/images/posts/YYYY/` (see `scripts/resize_photos/AGENTS.md`)
- `scripts/test_links/` — link checker described above under Commands (see `scripts/test_links/AGENTS.md`)
- `scripts/ssh_blog/` — serves the published posts and pages over SSH as a terminal app (Go, Charm's `wish`/`bubbletea`/`glamour`), live at `ssh ssh.blog.tobked.dev` on Fly.io. `make ssh_blog`, then `ssh -p 2222 localhost`. Tests: `go test ./...` from that directory. `.github/workflows/ssh_blog.yml` redeploys it on pushes to `master`; see its README. Note that `ssh_blog` parses every `.md` file in `content/post/` and `content/pages/` and requires YAML front matter (`---`) at the top of each file.
- `scripts/check_mobile.mjs` — `make check_theme`, run against a serving `make preview`. Drives headless Chrome over CDP (no dependencies; needs Node 22+ for the built-in `WebSocket`) to assert the theme's layout rules at a 390px phone viewport and at desktop.
- **Python code conventions**: Add type annotations (including return types) and descriptive docstrings to Python functions and classes, format with `black` and `isort`, test with `pytest`, and preserve existing comments.

## Notes

- `themes/ups-and-downs/` is the theme and is committed to this repo; `.gitignore` ignores `themes/*` and allows it by name.
- `themes/ups-and-downs/hugo.toml` holds the theme's default params, which Hugo merges under the site's `hugo.toml` — the site only has to set what it changes. `[params.colorScheme]` and `[params.coverImages]` each take a `default` (what a visitor first sees) and a `toggle` (whether the header offers a button, whose result is remembered per reader). `[params.linkSections]` folds long round-up sections: `foldAfter` links stay visible (0 never folds), `keepFirstOpen` leaves the first section whole.
- The theme tells post kinds apart by slug (`_partials/post-kind.html`): `*-links` is a monthly round-up, `*-summary` a year summary, anything else an essay; front matter `kind` overrides. Round-ups are rendered from `_partials/roundup.html`, which parses their `## Section` / `### [title](url)` structure, so keep new round-ups in that shape. The About page is whichever page sets `layout: about`.
- **Agent instructions & skills**:
  - Project-level instructions live once in `AGENTS.md` (and subdirectory `AGENTS.md` files such as `content/pages/AGENTS.md` and `scripts/*/AGENTS.md`). `CLAUDE.md`, `GEMINI.md`, and `.cursorrules` point to `AGENTS.md` so instructions are never duplicated.
  - Every agent tool looks in a different directory for skills, so the skill body lives once in `.agents/skills/<name>/SKILL.md` (read natively by Codex CLI and Antigravity) while `.claude/skills/<name>/SKILL.md` (Claude Code) and `.cursor/skills/<name>/SKILL.md` (Cursor) hold short stubs that carry the frontmatter and point at it. Symlinks are deliberately not used — Claude Code's skill discovery does not follow them. Edit the `.agents/` copy; the stubs only carry frontmatter. `.agents/skills/` is excluded from mdformat in `.pre-commit-config.yaml` so the instruction text is not reformatted.
- Secrets (OpenAI key, etc.) are loaded via `.env`/`python-dotenv`, consumed by `scripts/blog_automation_2/config.py` (`GOOGLE_ANALYTICS`, `ACCESS_TOKEN` come from CI secrets for deploy).
