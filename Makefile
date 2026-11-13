PY?=python3
HUGO?=hugo
FLY?=fly
DEVCONTAINER?=$(shell command -v devcontainer 2>/dev/null || echo "npx -y @devcontainers/cli")
HUGO_BIND?=127.0.0.1
SSH_BLOG_ADDR?=localhost:2222

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
	$(HUGO) server -D -M --bind $(HUGO_BIND)

.PHONY: publish
publish: ## generate using production settings (deploys happen in CI)
	$(HUGO) --gc --minify
	npx -y pagefind@1.6.0 --site $(OUTPUTDIR) --output-subdir _pagefind

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
ssh_blog: ## serve the blog over SSH at localhost:2222
	cd scripts/ssh_blog && go run . -addr $(SSH_BLOG_ADDR)

.PHONY: check_docker
check_docker:
	@docker info >/dev/null 2>&1 || { echo "Error: Docker is not running."; exit 1; }

.PHONY: dc-up
dc-up: check_docker ## build and start the hardened Dev Container
	$(DEVCONTAINER) up --workspace-folder .

.PHONY: dc-stop
dc-stop: check_docker ## stop the running Dev Container
	@cid=$$(docker ps -q --filter "label=devcontainer.local_folder=$(BASEDIR)"); \
	if [ -n "$$cid" ]; then docker stop $$cid; else echo "Dev Container is not running."; fi

.PHONY: dc-rebuild
dc-rebuild: check_docker ## rebuild and recreate the hardened Dev Container
	$(DEVCONTAINER) up --workspace-folder . --remove-existing-container

.PHONY: dc-shell
dc-shell: check_docker ## open an interactive shell inside the Dev Container
	$(DEVCONTAINER) exec --workspace-folder . bash

# herdr recognises agents by process name, so docker runs via a symlink named after the agent
define dc_agent
	@mkdir -p .devcontainer/.bin && ln -sf "$$(command -v docker)" .devcontainer/.bin/$(1)
	$(DEVCONTAINER) exec --docker-path $(CURDIR)/.devcontainer/.bin/$(1) --workspace-folder . $(1) --dangerously-skip-permissions
endef

.PHONY: dc-claude
dc-claude: check_docker ## launch Claude Code (YOLO mode) inside the Dev Container
	$(call dc_agent,claude)

.PHONY: dc-agy
dc-agy: check_docker ## launch Antigravity CLI (YOLO mode) inside the Dev Container
	$(call dc_agent,agy)

.PHONY: dc-exec
dc-exec: check_docker ## run a command inside the Dev Container (e.g. make dc-exec CMD="make publish")
	$(DEVCONTAINER) exec --workspace-folder . bash -lc '$(CMD)'

.PHONY: dc-verify
dc-verify: check_docker ## verify security invariants, toolchains, and tests inside the Dev Container
	$(DEVCONTAINER) exec --workspace-folder . bash .devcontainer/verify.sh

.PHONY: ssh_blog_docker
ssh_blog_docker: check_docker ## run the SSH blog in Docker at 127.0.0.1:2222
	docker build -f scripts/ssh_blog/Dockerfile -t ssh-blog .
	docker rm -f ssh-blog 2>/dev/null || true
	docker run -d --name ssh-blog --read-only --cap-drop ALL --security-opt no-new-privileges \
		-p 127.0.0.1:2222:2222 -v ssh-blog-data:/data ssh-blog

.PHONY: ssh_blog_fly
ssh_blog_fly: check_docker ## deploy the SSH blog to Fly.io (see scripts/ssh_blog/README.md)
	img=registry.fly.io/tobked-ssh-blog:$$(date +%Y%m%d%H%M%S) && \
	docker build --platform linux/amd64 -f scripts/ssh_blog/Dockerfile -t $$img . && \
	$(FLY) auth docker && docker push $$img && \
	$(FLY) deploy -c scripts/ssh_blog/fly.toml --image $$img --ha=false
