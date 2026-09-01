### [blog.tobked.dev](https://blog.tobked.dev/)

[![Deploy blog to gh-pages](https://github.com/TobKed/blog/actions/workflows/main.yml/badge.svg)](https://github.com/TobKed/blog/actions/workflows/main.yml)

##### Blog made with Hugo

- https://github.com/gohugoio/hugo

used theme (git submodule under `themes/`):

- https://github.com/CaiJimmy/hugo-theme-stack

Requires Hugo **extended** 0.146+ (CI pins 0.165.0).

```bash
brew install hugo
git submodule update --init --recursive
```

```bash
make serve     # http://localhost:1313, includes drafts
make build     # build into public/
make publish   # production build + pagefind search index
```

Deployment is automatic: pushing to `master` runs `.github/workflows/main.yml`,
which builds the site and publishes `public/` to the `gh-pages` branch.
