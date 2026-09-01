### [blog.tobked.dev](https://blog.tobked.dev/)

[![Deploy blog to gh-pages](https://github.com/TobKed/blog/actions/workflows/main.yml/badge.svg)](https://github.com/TobKed/blog/actions/workflows/main.yml)

##### Blog made with Hugo

- https://github.com/gohugoio/hugo

used theme (git submodule under `themes/`):

- https://github.com/CaiJimmy/hugo-theme-stack

Requires Hugo **extended** 0.146+ (CI pins 0.165.0).

Hugo is pinned in `mise.toml`, Python in `.python-version`:

```bash
mise install    # or: brew install hugo
uv venv
uv pip install -r requirements.txt
git submodule update --init --recursive
```

```bash
make serve     # http://localhost:1313, includes drafts
make build     # build into public/
make publish   # production build + pagefind search index
make check_links  # report duplicated links across posts
```

`scripts/check_duplicate_links.py` warns when a URL is repeated within a post or
across `content/post/*.md`. It also runs as a pre-commit hook, warn-only — it
prints findings but never blocks a commit, and it is skipped in CI so it only
reports on the posts you are actually committing. Put `dup-ok` anywhere on a line
(e.g. `<!-- dup-ok -->`) to silence an intentional repeat, as the yearly
summary posts need.

Deployment is automatic: pushing to `master` runs `.github/workflows/main.yml`,
which builds the site and publishes `public/` to the `gh-pages` branch.
