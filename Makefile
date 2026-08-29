PY?=python3
HUGO?=hugo

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/public

GITHUB_PAGES_BRANCH=gh-pages

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo 'Makefile for a Hugo Web site                                              '
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo ''

.PHONY: html
html: ## (re)generate the web site
	$(HUGO)

.PHONY: clean
clean: ## remove the generated files
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

.PHONY: regenerate
regenerate: ## regenerate files upon modification
	$(HUGO) server -w

.PHONY: serve
serve: ## serve site at http://localhost:1313
	$(HUGO) server

.PHONY: devserver
devserver: ## serve and regenerate together with drafts
	$(HUGO) server -D -w

.PHONY: publish
publish: ## generate using production settings
	$(HUGO) --minify

.PHONY: github
github: publish ## upload the web site via gh-pages
	ghp-import -m "Generate Hugo site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: resize_images
resize_images: ## resize images in scripts/resize_photos/input
	$(PY) scripts/resize_photos/main.py

.PHONY: generate_post
generate_post: ## generate a new post
	$(PY) scripts/generate_post.py
