PY?=python3
HUGO?=hugo

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/public

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo 'Makefile for a Hugo Web site                                              '
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo ''

.PHONY: build
build: ## build the web site
	$(HUGO) --gc

.PHONY: clean
clean: ## remove the generated files
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

.PHONY: serve
serve: ## serve site locally at http://localhost:1313 (with drafts)
	# -M renders to memory: without it the server serves public/ from disk, so a
	# concurrent `make build` overwrites it with production (blog.tobked.dev) URLs.
	$(HUGO) server -D -M

.PHONY: publish
publish: ## generate using production settings (deploys happen in CI)
	$(HUGO) --gc --minify
	npx -y pagefind --site $(OUTPUTDIR) --output-subdir _pagefind

.PHONY: preview
preview: publish ## build like production (incl. search index) and serve public/ at :1314
	# `make serve` renders to memory, so /_pagefind/ does not exist there and the
	# search page is an empty box. Use this to exercise search locally.
	cd $(OUTPUTDIR) && $(PY) -m http.server 1314

.PHONY: resize_images
resize_images: ## resize images in scripts/resize_photos/input
	$(PY) scripts/resize_photos/main.py

.PHONY: generate_post
generate_post: ## generate a new post
	$(PY) scripts/generate_post.py

.PHONY: check_links
check_links: ## report duplicated links across posts
	$(PY) scripts/check_duplicate_links.py $(FILES)

.PHONY: check_theme
check_theme: ## theme regression checks against a running `make preview`
	node scripts/check_mobile.mjs $(URL)

.PHONY: ssh_blog
ssh_blog: ## serve the blog over SSH at localhost:2222 (prototype)
	cd scripts/ssh_blog && go run .

.PHONY: ssh_blog_docker
ssh_blog_docker: ## run the SSH blog in Docker at 127.0.0.1:2222
	docker build -f scripts/ssh_blog/Dockerfile -t ssh-blog .
	docker rm -f ssh-blog 2>/dev/null || true
	docker run -d --name ssh-blog --read-only --cap-drop ALL --security-opt no-new-privileges \
		-p 127.0.0.1:2222:2222 -v ssh-blog-data:/data ssh-blog

.PHONY: ssh_blog_share
ssh_blog_share: ## expose the running SSH blog publicly via bore.pub
	bore local 2222 --local-host 127.0.0.1 --to bore.pub
