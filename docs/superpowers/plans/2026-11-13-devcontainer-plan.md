# Hardened Dev Container Environment Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a security-hardened Dev Container environment (`.devcontainer/`) managed via `@devcontainers/cli` on Docker Desktop that isolates AI coding agents (`claude`, `gemini`) and blog toolchains from the macOS host while preserving subscription logins and full blog/script/theme workflows.

**Architecture:** A multi-arch Debian Bookworm `.devcontainer/Dockerfile` installs pinned versions of Hugo Extended (`0.165.0`), Python (`3.13`) + `uv`, Go (`1.27.3`), Node.js (`22`), system Chromium with an unprivileged wrapper (`/usr/local/bin/chromium-headless`), Pagefind, Claude Code, and Gemini CLI, then strips runtime `sudo` privileges. `.devcontainer/devcontainer.json` enforces `--cap-drop=ALL`, `--security-opt=no-new-privileges:true`, blocks `SSH_AUTH_SOCK`, maps loopback ports (`1313`, `1314`, `2222`), and isolates virtualenvs and agent subscription state into named Docker volumes.

**Tech Stack:** Dev Containers (`@devcontainers/cli`), Docker Desktop, Debian Bookworm, Hugo Extended `0.165.0`, Python `3.13` + `uv`, Go `1.27.3`, Node.js `22`, Chromium, GNU Make, Bash.

______________________________________________________________________

## File Structure

| Action | Path                              | Responsibility                                                                                                                                                     |
| ------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create | `.devcontainer/verify.sh`         | Executable verification suite checking security invariants, tool versions, and blog build/test workflows inside the container (or static config checks from host). |
| Create | `.devcontainer/Dockerfile`        | Deterministic multi-arch container image with pinned toolchains, Chromium wrapper, pre-owned volume target directories, and stripped `sudo`.                       |
| Create | `.devcontainer/post-create.sh`    | Idempotent lifecycle script that provisions the three Python virtual environments via `uv` and installs `pre-commit` hooks.                                        |
| Create | `.devcontainer/devcontainer.json` | Dev Container specification locking down runtime privileges, volume mounts, loopback ports, and environment variables.                                             |
| Modify | `Makefile`                        | Adds `HUGO_BIND`, `SSH_BLOG_ADDR`, and convenience `dc-up`, `dc-shell`, `dc-exec`, and `dc-verify` targets.                                                        |
| Modify | `AGENTS.md`                       | Documents the Dev Container workflow and `make dc-*` targets under Commands.                                                                                       |

______________________________________________________________________

## Chunk 1: Verification Suite, Container Image, Spec Config, and Host Integration

### Task 1: Create `.devcontainer/verify.sh` Verification Script

**Files:**

- Create: `.devcontainer/verify.sh`

- \[ \] **Step 1: Write `.devcontainer/verify.sh` with both static config checks (`--static`) and in-container runtime checks**

```bash
#!/usr/bin/env bash
set -euo pipefail

MODE="${1:---runtime}"
FAILURES=0

pass() {
  printf "  ok   %s\n" "$1"
}

fail() {
  printf " FAIL  %s (%s)\n" "$1" "$2"
  FAILURES=$((FAILURES + 1))
}

check_static() {
  echo "=== Static Dev Container Configuration Checks ==="

  for f in .devcontainer/Dockerfile .devcontainer/devcontainer.json .devcontainer/post-create.sh; do
    if [ -f "$f" ]; then
      pass "$f exists"
    else
      fail "$f exists" "missing file"
    fi
  done

  if [ -f .devcontainer/devcontainer.json ]; then
    if jq -e '.runArgs | index("--cap-drop=ALL")' .devcontainer/devcontainer.json >/dev/null 2>&1; then
      pass "devcontainer.json drops ALL capabilities"
    else
      fail "devcontainer.json drops ALL capabilities" "missing --cap-drop=ALL"
    fi

    if jq -e '.runArgs | index("--security-opt=no-new-privileges:true")' .devcontainer/devcontainer.json >/dev/null 2>&1; then
      pass "devcontainer.json enforces no-new-privileges"
    else
      fail "devcontainer.json enforces no-new-privileges" "missing no-new-privileges:true"
    fi

    if jq -e '.remoteEnv.SSH_AUTH_SOCK == ""' .devcontainer/devcontainer.json >/dev/null 2>&1; then
      pass "devcontainer.json clears SSH_AUTH_SOCK"
    else
      fail "devcontainer.json clears SSH_AUTH_SOCK" "SSH_AUTH_SOCK not empty"
    fi

    if jq -e '.containerEnv.CLAUDE_CONFIG_DIR == "/home/vscode/.claude"' .devcontainer/devcontainer.json >/dev/null 2>&1; then
      pass "devcontainer.json sets CLAUDE_CONFIG_DIR=/home/vscode/.claude"
    else
      fail "devcontainer.json sets CLAUDE_CONFIG_DIR=/home/vscode/.claude" "missing CLAUDE_CONFIG_DIR"
    fi
  fi

  if [ -f .devcontainer/Dockerfile ]; then
    if grep -q "rm -f /etc/sudoers.d/vscode" .devcontainer/Dockerfile; then
      pass "Dockerfile removes passwordless sudo for vscode"
    else
      fail "Dockerfile removes passwordless sudo for vscode" "sudoers removal missing"
    fi
  fi
}

check_runtime() {
  echo "=== In-Container Security & Toolchain Checks ==="

  if [ "$(id -u)" -ne 0 ] && [ "$(id -un)" = "vscode" ]; then
    pass "running as non-root user vscode ($(id -u))"
  else
    fail "running as non-root user vscode" "uid=$(id -u) user=$(id -un)"
  fi

  if sudo -n true 2>/dev/null; then
    fail "passwordless sudo is disabled" "sudo -n true succeeded"
  else
    pass "passwordless sudo is disabled"
  fi

  if grep -q "^NoNewPrivs:[[:space:]]*1" /proc/self/status; then
    pass "NoNewPrivs is active (1)"
  else
    fail "NoNewPrivs is active" "$(grep '^NoNewPrivs:' /proc/self/status || echo 'missing')"
  fi

  if grep -q "^CapEff:[[:space:]]*0000000000000000" /proc/self/status; then
    pass "effective Linux capabilities are 0000000000000000"
  else
    fail "effective Linux capabilities are 0000000000000000" "$(grep '^CapEff:' /proc/self/status || echo 'missing')"
  fi

  if [ -z "${SSH_AUTH_SOCK:-}" ]; then
    pass "SSH_AUTH_SOCK is empty"
  else
    fail "SSH_AUTH_SOCK is empty" "SSH_AUTH_SOCK=${SSH_AUTH_SOCK}"
  fi

  if [ ! -d /home/vscode/.ssh ]; then
    pass "/home/vscode/.ssh is not mounted"
  else
    fail "/home/vscode/.ssh is not mounted" "directory exists"
  fi

  if hugo version | grep -q "v0.165.0" && hugo version | grep -q "extended"; then
    pass "hugo extended v0.165.0 installed"
  else
    fail "hugo extended v0.165.0 installed" "$(hugo version 2>&1 || true)"
  fi

  if python3 --version | grep -q "Python 3.13"; then
    pass "python 3.13 installed"
  else
    fail "python 3.13 installed" "$(python3 --version 2>&1 || true)"
  fi

  for cmd in uv go node npx pagefind claude gemini /usr/local/bin/chromium-headless; do
    if command -v "$cmd" >/dev/null 2>&1; then
      pass "$cmd is available"
    else
      fail "$cmd is available" "not found in PATH"
    fi
  done

  if /usr/local/bin/chromium-headless --version >/dev/null 2>&1; then
    pass "chromium-headless --version runs under dropped capabilities"
  else
    fail "chromium-headless --version runs under dropped capabilities" "execution failed"
  fi

  echo "=== End-to-End Blog Workflow Checks ==="
  make publish >/dev/null
  if [ -d public/_pagefind ]; then
    pass "make publish built site and Pagefind index"
  else
    fail "make publish built site and Pagefind index" "public/_pagefind missing"
  fi

  (cd public && python3 -m http.server 1314 >/dev/null 2>&1) &
  HTTP_PID=$!
  trap 'kill "$HTTP_PID" 2>/dev/null || true' EXIT
  sleep 1
  if make check_theme >/dev/null; then
    pass "make check_theme passed via headless Chromium"
  else
    fail "make check_theme passed via headless Chromium" "check_theme failed"
  fi
  kill "$HTTP_PID" 2>/dev/null || true
  trap - EXIT

  if make check_links >/dev/null; then
    pass "make check_links passed"
  else
    fail "make check_links passed" "non-zero exit"
  fi

  if PYTHONPATH=scripts/blog_automation_2 /workspaces/blog/scripts/blog_automation_2/.venv/bin/pytest scripts/blog_automation_2/tests >/dev/null; then
    pass "blog_automation_2 pytest suite passed"
  else
    fail "blog_automation_2 pytest suite passed" "pytest failed"
  fi

  if (cd scripts/ssh_blog && go test ./...) >/dev/null; then
    pass "ssh_blog go test passed"
  else
    fail "ssh_blog go test passed" "go test failed"
  fi
}

if [ "$MODE" = "--static" ]; then
  check_static
else
  check_static
  check_runtime
fi

if [ "$FAILURES" -gt 0 ]; then
  echo "Verification failed with $FAILURES error(s)."
  exit 1
fi

echo "All checks passed."
```

- \[ \] **Step 2: Make `.devcontainer/verify.sh` executable and run `--static` to confirm it fails before the remaining files exist**

Run: `chmod +x .devcontainer/verify.sh && bash .devcontainer/verify.sh --static`
Expected: FAIL with missing `.devcontainer/Dockerfile`, `.devcontainer/devcontainer.json`, and `.devcontainer/post-create.sh`.

______________________________________________________________________

### Task 2: Create `.devcontainer/Dockerfile` and `.devcontainer/post-create.sh`

**Files:**

- Create: `.devcontainer/Dockerfile`

- Create: `.devcontainer/post-create.sh`

- \[ \] **Step 1: Write `.devcontainer/Dockerfile`**

```dockerfile
FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG TARGETARCH
ARG HUGO_VERSION=0.165.0
ARG GO_VERSION=1.27.3
ARG NODE_MAJOR=22

ENV DEBIAN_FRONTEND=noninteractive

# 1. System packages & Headless Chromium dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    chromium \
    chromium-driver \
    curl \
    fonts-liberation \
    git \
    jq \
    libasound2 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libgbm1 \
    libnss3 \
    libxkbcommon0 \
    make \
    ripgrep \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 2. Node.js 22 LTS + global CLIs (pagefind, claude-code, gemini-cli)
RUN curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g \
        pagefind \
        @anthropic-ai/claude-code \
        @google/gemini-cli \
    && npm cache clean --force \
    && rm -rf /var/lib/apt/lists/*

# 3. Hugo Extended 0.165.0
RUN curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${TARGETARCH}.tar.gz" \
    | tar -xz -C /usr/local/bin hugo \
    && chmod +x /usr/local/bin/hugo

# 4. Go toolchain (with GOTOOLCHAIN=auto so go 1.27.3 in scripts/ssh_blog/go.mod works seamlessly)
RUN curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-${TARGETARCH}.tar.gz" \
    | tar -xz -C /usr/local
ENV PATH="/usr/local/go/bin:/home/vscode/go/bin:${PATH}"
ENV GOTOOLCHAIN=auto

# 5. uv + Python 3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/
ENV UV_PYTHON_INSTALL_DIR=/opt/python
RUN uv python install 3.13 \
    && ln -sf "$(uv python find 3.13)" /usr/local/bin/python3 \
    && ln -sf /usr/local/bin/python3 /usr/local/bin/python

# 6. Headless Chromium wrapper for unprivileged container (--cap-drop=ALL)
RUN printf '#!/bin/sh\nexec /usr/bin/chromium --no-sandbox --disable-dev-shm-usage "$@"\n' \
    > /usr/local/bin/chromium-headless \
    && chmod +x /usr/local/bin/chromium-headless

# 7. Pre-create volume mount directories owned by vscode:vscode so root/sudo is never needed at runtime
RUN mkdir -p \
    /workspaces/blog/.venv \
    /workspaces/blog/scripts/blog_automation_2/.venv \
    /workspaces/blog/scripts/test_links/.venv \
    /home/vscode/.claude \
    /home/vscode/.gemini \
    /home/vscode/.cache \
    /home/vscode/go \
    && chown -R vscode:vscode /workspaces /home/vscode

# 8. Strip passwordless sudo from vscode user so runtime processes cannot escalate to root
RUN rm -f /etc/sudoers.d/vscode \
    && sed -i '/vscode/d' /etc/sudoers

USER vscode
WORKDIR /workspaces/blog
```

- \[ \] **Step 2: Write `.devcontainer/post-create.sh` and make it executable**

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "==> Provisioning root Python virtualenv (/workspaces/blog/.venv)..."
uv venv /workspaces/blog/.venv --python 3.13 --allow-existing
uv pip install --python /workspaces/blog/.venv/bin/python -r /workspaces/blog/requirements.txt

echo "==> Provisioning blog_automation_2 virtualenv..."
uv venv /workspaces/blog/scripts/blog_automation_2/.venv --python 3.13 --allow-existing
uv pip install --python /workspaces/blog/scripts/blog_automation_2/.venv/bin/python \
  -r /workspaces/blog/scripts/blog_automation_2/requirements.txt \
  -r /workspaces/blog/scripts/blog_automation_2/requirements-dev.txt

echo "==> Provisioning test_links virtualenv..."
uv venv /workspaces/blog/scripts/test_links/.venv --python 3.13 --allow-existing
uv pip install --python /workspaces/blog/scripts/test_links/.venv/bin/python \
  -r /workspaces/blog/scripts/test_links/requirements.txt

echo "==> Pre-warming Go modules for scripts/ssh_blog..."
(cd /workspaces/blog/scripts/ssh_blog && go mod download)

echo "==> Pre-warming pre-commit hook environments..."
/workspaces/blog/.venv/bin/pre-commit install-hooks

echo "==> Dev Container setup complete."
```

Run: `chmod +x .devcontainer/post-create.sh && bash -n .devcontainer/post-create.sh`
Expected: Exit code 0 (valid bash syntax).

______________________________________________________________________

### Task 3: Create `.devcontainer/devcontainer.json`

**Files:**

- Create: `.devcontainer/devcontainer.json`

- \[ \] **Step 1: Write `.devcontainer/devcontainer.json`**

```json
{
  "name": "blog-hardened-devcontainer",
  "build": {
    "dockerfile": "Dockerfile",
    "context": "."
  },
  "remoteUser": "vscode",
  "containerUser": "vscode",
  "updateRemoteUserUID": true,
  "runArgs": [
    "--cap-drop=ALL",
    "--security-opt=no-new-privileges:true",
    "--shm-size=1gb"
  ],
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspaces/blog,type=bind,consistency=cached",
  "workspaceFolder": "/workspaces/blog",
  "mounts": [
    "source=blog-dc-venv,target=/workspaces/blog/.venv,type=volume",
    "source=blog-dc-automation-venv,target=/workspaces/blog/scripts/blog_automation_2/.venv,type=volume",
    "source=blog-dc-testlinks-venv,target=/workspaces/blog/scripts/test_links/.venv,type=volume",
    "source=blog-dc-claude,target=/home/vscode/.claude,type=volume",
    "source=blog-dc-gemini,target=/home/vscode/.gemini,type=volume",
    "source=blog-dc-cache,target=/home/vscode/.cache,type=volume"
  ],
  "appPort": [
    "127.0.0.1:1313:1313",
    "127.0.0.1:1314:1314",
    "127.0.0.1:2222:2222"
  ],
  "containerEnv": {
    "HUGO_BIND": "0.0.0.0",
    "SSH_BLOG_ADDR": "0.0.0.0:2222",
    "CHROME": "/usr/local/bin/chromium-headless",
    "PLAYWRIGHT_BROWSERS_PATH": "/usr/bin",
    "UV_LINK_MODE": "copy",
    "CLAUDE_CONFIG_DIR": "/home/vscode/.claude"
  },
  "remoteEnv": {
    "SSH_AUTH_SOCK": "",
    "PATH": "/workspaces/blog/.venv/bin:${containerEnv:PATH}",
    "OPENAI_API_KEY": "${localEnv:OPENAI_API_KEY}"
  },
  "postCreateCommand": "bash .devcontainer/post-create.sh"
}
```

- \[ \] **Step 2: Run static verification script to confirm `.devcontainer/*` passes all static checks**

Run: `bash .devcontainer/verify.sh --static`
Expected: `All checks passed.`

- \[ \] **Step 3: Commit `.devcontainer/` files**

```bash
git add .devcontainer/Dockerfile .devcontainer/devcontainer.json .devcontainer/post-create.sh .devcontainer/verify.sh
git commit -m "feat(devcontainer): add hardened devcontainer spec and setup scripts"
```

______________________________________________________________________

### Task 4: Update `Makefile` and `AGENTS.md`

**Files:**

- Modify: `Makefile`

- Modify: `AGENTS.md`

- \[ \] **Step 1: Update `Makefile` with `HUGO_BIND`, `SSH_BLOG_ADDR`, and `dc-*` helper targets**

Update `Makefile` so `HUGO_BIND` and `SSH_BLOG_ADDR` default to localhost on the host (`127.0.0.1` and `localhost:2222`) while respecting container overrides, and add `dc-up`, `dc-shell`, `dc-exec`, and `dc-verify`:

```makefile
PY?=python3
HUGO?=hugo
FLY?=fly
DEVCONTAINER?=devcontainer
HUGO_BIND?=127.0.0.1
SSH_BLOG_ADDR?=localhost:2222
```

In `serve`:

```makefile
.PHONY: serve
serve: ## serve site locally at http://localhost:1313 (with drafts)
	# -M renders to memory: without it the server serves public/ from disk, so a
	# concurrent `make build` overwrites it with production (blog.tobked.dev) URLs.
	$(HUGO) server -D -M --bind $(HUGO_BIND)
```

In `ssh_blog`:

```makefile
.PHONY: ssh_blog
ssh_blog: ## serve the blog over SSH at localhost:2222
	cd scripts/ssh_blog && go run . -addr $(SSH_BLOG_ADDR)
```

At the end of `Makefile`:

```makefile
.PHONY: dc-up
dc-up: ## build and start the hardened Dev Container
	$(DEVCONTAINER) up --workspace-folder .

.PHONY: dc-shell
dc-shell: ## open an interactive shell inside the Dev Container
	$(DEVCONTAINER) exec --workspace-folder . bash

.PHONY: dc-exec
dc-exec: ## run a command inside the Dev Container (e.g. make dc-exec CMD="make publish")
	$(DEVCONTAINER) exec --workspace-folder . $(CMD)

.PHONY: dc-verify
dc-verify: ## verify security invariants, toolchains, and tests inside the Dev Container
	$(DEVCONTAINER) exec --workspace-folder . bash .devcontainer/verify.sh
```

- \[ \] **Step 2: Document the Dev Container workflow in `AGENTS.md`**

Add a brief bullet list under `## Commands` in `AGENTS.md` describing `make dc-up`, `make dc-shell`, `make dc-exec CMD="..."`, and `make dc-verify`.

- \[ \] **Step 3: Verify `make help` outputs the new targets and run `pre-commit` on modified files**

Run: `make help`
Expected: Lists `dc-up`, `dc-shell`, `dc-exec`, and `dc-verify`.

- \[ \] **Step 4: Commit `Makefile` and `AGENTS.md`**

```bash
git add Makefile AGENTS.md
git commit -m "feat(devcontainer): add Makefile targets and document workflow"
```
