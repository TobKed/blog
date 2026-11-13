# Hardened Dev Container Environment Design

**Date:** 2026-11-13
**Topic:** Isolated, security-hardened Dev Container environment for blog development, scripts, theme testing, and AI coding agents.

## 1. Overview & Goals

This project adds a security-hardened [Development Container](https://github.com/devcontainers/spec) environment (`.devcontainer/`) managed via `@devcontainers/cli` on Docker Desktop for macOS.

### Primary Goals

1. **Isolate AI coding agents (`claude`, `gemini`) and third-party dependencies** so they can only access the repository workspace (`/workspaces/blog`) and cannot read or modify the macOS host `$HOME` (`~/.ssh`, `~/.aws`, `~/.config`, browser profiles, or other repositories).
2. **Keep blog toolchains off the macOS host** by encapsulating Hugo Extended, Python 3.13 + `uv`, Go, Node.js 22, Pagefind, and Headless Chromium inside the container image.
3. **Protect host credentials and secrets** by blocking automatic `SSH_AUTH_SOCK` forwarding, omitting host credential mounts, removing runtime `sudo` access inside the container, and keeping `git push` and `fly deploy` strictly on the macOS host.
4. **Support both interactive container shells and host-driven commands** via `Makefile` targets (`make dc-up`, `make dc-shell`, `make dc-exec`).

### Non-Goals

- Running Docker-in-Docker or mounting `/var/run/docker.sock` inside the Dev Container (`make ssh_blog_docker` and `make ssh_blog_fly` remain host-only operations).
- Automatic `git push` or production deployments from inside the container.

______________________________________________________________________

## 2. Architecture & Component Boundaries

The system consists of five well-bounded units:

| Component                                    | Path                              | Responsibility                                                                                                                                                                                   | Interface / Consumers                                                                          |
| -------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Container Image Definition**               | `.devcontainer/Dockerfile`        | Builds a deterministic Debian Bookworm image with pinned toolchains, Chromium wrapper, AI agent CLIs, and stripped runtime `sudo`.                                                               | Consumed by `.devcontainer/devcontainer.json` during `devcontainer up` / `devcontainer build`. |
| **Dev Container Spec Config**                | `.devcontainer/devcontainer.json` | Declares container security flags (`runArgs`), loopback port mappings (`appPort`), isolated named volumes (`mounts`), environment variables (`containerEnv` / `remoteEnv`), and lifecycle hooks. | Consumed by `@devcontainers/cli` (and any Dev Container-compatible IDE).                       |
| **Post-Create Setup Script**                 | `.devcontainer/post-create.sh`    | Idempotently provisions Python virtual environments via `uv` and installs `pre-commit` hooks inside the mounted workspace/volumes.                                                               | Executed automatically by `postCreateCommand` in `devcontainer.json`.                          |
| **Security & Toolchain Verification Script** | `.devcontainer/verify.sh`         | Asserts that all pinned tools exist, security invariants hold (non-root, no `sudo`, empty `SSH_AUTH_SOCK`), and repo build/test commands succeed.                                                | Invoked manually or via `make dc-verify`.                                                      |
| **Host Makefile Integration**                | `Makefile`                        | Exposes `HUGO_BIND` for container port forwarding and provides `dc-up`, `dc-shell`, `dc-exec`, and `dc-verify` convenience targets on the host.                                                  | Invoked by the developer from macOS or inside the container.                                   |

______________________________________________________________________

## 3. Detailed Component Design

### 3.1 `.devcontainer/Dockerfile`

- **Base Image:** `mcr.microsoft.com/devcontainers/base:bookworm` (multi-arch `linux/arm64` and `linux/amd64`, provides standard unprivileged `vscode` user with UID/GID `1000`).
- **System Packages (`apt-get`):**
  - `chromium` (pulls in its own runtime libraries) and `fonts-liberation`, for `scripts/check_mobile.mjs`.
  - `git`, `curl`, `ca-certificates`, `make`, `jq`, `ripgrep`, `unzip`.
- **Pinned Toolchains (Multi-Arch Aware via `TARGETARCH`):**
  - **Hugo Extended `0.165.0`:** Downloaded from official GitHub release tarball (`hugo_extended_0.165.0_linux-${TARGETARCH}.tar.gz`) into `/usr/local/bin/hugo`.
  - **Go `1.27.3`:** Installed (or latest official Go toolchain compatible with `go.mod`, using `GOTOOLCHAIN=auto` with Go pre-fetched during build so `go 1.27.3` in `scripts/ssh_blog/go.mod` is cached in `/usr/local/go`).
  - **Node.js `22.x LTS`:** Installed via NodeSource / official binary tarball; globally installs `@anthropic-ai/claude-code`, `@google/gemini-cli`, and `pagefind` so `npx pagefind` and agent CLIs work without runtime downloads.
  - **Python `3.13` & `uv`:** Installed via `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/` and `uv python install 3.13` into `/opt/python` (`UV_PYTHON_INSTALL_DIR=/opt/python`), symlinked to `/usr/local/bin/python3` and `/usr/local/bin/python`.
- **Headless Chromium Wrapper (`/usr/local/bin/chromium-headless`):**
  - Because the container runs with `--cap-drop=ALL` and `--security-opt=no-new-privileges:true`, Chromium's internal setuid/user-namespace sandbox cannot initialize inside the already-sandboxed container.
  - `/usr/local/bin/chromium-headless` is an executable shell wrapper:
    ```sh
    #!/bin/sh
    exec /usr/bin/chromium --no-sandbox --disable-dev-shm-usage "$@"
    ```
- **Privilege Removal (Final Dockerfile Stage):**
  - Deletes `/etc/sudoers.d/vscode` and any `NOPASSWD` sudo rules before switching to `USER vscode`.
  - Ensures runtime processes cannot execute `sudo` or modify system paths.

### 3.2 `.devcontainer/devcontainer.json`

- **User Configuration:**
  - `"remoteUser": "vscode"`
  - `"containerUser": "vscode"`
  - `"updateRemoteUserUID": true`
- **Hardened Runtime Arguments (`runArgs`):**
  - `"--cap-drop=ALL"`
  - `"--security-opt=no-new-privileges:true"`
  - `"--shm-size=1gb"`
- **Workspace & Volume Mounts:**
  - `"workspaceMount": "source=${localWorkspaceFolder},target=/workspaces/blog,type=bind,consistency=cached"`
  - `"workspaceFolder": "/workspaces/blog"`
  - `"mounts"`:
    - `source=blog-dc-venv,target=/workspaces/blog/.venv,type=volume` (isolates root Linux Python virtualenv from macOS host)
    - `source=blog-dc-automation-venv,target=/workspaces/blog/scripts/blog_automation_2/.venv,type=volume`
    - `source=blog-dc-claude,target=/home/vscode/.claude,type=volume` (persists Claude Code state)
    - `source=blog-dc-gemini,target=/home/vscode/.gemini,type=volume` (persists Gemini CLI state)
    - `source=blog-dc-cache,target=/home/vscode/.cache,type=volume` (persists `uv`, `pre-commit`, and Go build caches)
- **Port Binding (`appPort`):**
  - `"127.0.0.1:1313:1313"` (Hugo dev server)
  - `"127.0.0.1:1314:1314"` (Pagefind preview server)
  - `"127.0.0.1:2222:2222"` (`ssh_blog` server)
- **Environment Variables:**
  - `"containerEnv"`:
    - `"HUGO_BIND": "0.0.0.0"`
    - `"SSH_BLOG_ADDR": "0.0.0.0:2222"`
    - `"CHROME": "/usr/local/bin/chromium-headless"`
    - `"UV_LINK_MODE": "copy"` (prevents hardlink warnings across volume boundaries)
    - `"CLAUDE_CONFIG_DIR": "/home/vscode/.claude"` (keeps all Claude Code subscription OAuth tokens and config inside the persistent `blog-dc-claude` volume)
  - `"remoteEnv"`:
    - `"SSH_AUTH_SOCK": ""` (explicitly neutralizes host SSH agent forwarding)
    - `"PATH": "/workspaces/blog/.venv/bin:${containerEnv:PATH}"`
    - `"OPENAI_API_KEY": "${localEnv:OPENAI_API_KEY}"` (passes `OPENAI_API_KEY` for `scripts/blog_automation_2` only if explicitly set in the invoking host shell; `claude` and `gemini` use subscription OAuth persisted in `/home/vscode/.claude` and `/home/vscode/.gemini`)
- **Lifecycle Hook:**
  - `"postCreateCommand": "bash .devcontainer/post-create.sh"`

### 3.3 `.devcontainer/post-create.sh`

Executed as `vscode` after container creation:

1. Fixes ownership of mounted named volumes (`/workspaces/blog/.venv`, `/workspaces/blog/scripts/blog_automation_2/.venv`, `/home/vscode/.claude`, `/home/vscode/.gemini`, `/home/vscode/.cache`) if Docker initialized them as `root`—handled via a pre-seeded directory in the image or `Dockerfile` pre-created mount targets owned by `vscode:vscode` so `root` is never needed at runtime.
   - *Design detail:* Docker initializes empty named volumes with the ownership and permissions of the target directory inside the image. Therefore, `.devcontainer/Dockerfile` will `mkdir -p` and `chown -R vscode:vscode` all five mount target paths during build time before dropping `root`.
2. Creates and syncs Python virtual environments using `uv`:
   - Root `.venv`: `uv venv /workspaces/blog/.venv --allow-existing && uv pip install --python /workspaces/blog/.venv/bin/python -r requirements.txt`
   - `scripts/blog_automation_2/.venv`: `uv venv /workspaces/blog/scripts/blog_automation_2/.venv --allow-existing && uv pip install --python /workspaces/blog/scripts/blog_automation_2/.venv/bin/python -r scripts/blog_automation_2/requirements.txt -r scripts/blog_automation_2/requirements-dev.txt`
3. Warms up `pre-commit` environments (`pre-commit install-hooks`).

### 3.4 `Makefile` & Documentation Updates

- **`Makefile` updates:**
  - Add `HUGO_BIND ?= 127.0.0.1` and update `serve` target to `$(HUGO) server -D -M --bind $(HUGO_BIND)`.
  - Add `SSH_BLOG_ADDR ?= localhost:2222` and update `ssh_blog` target to `cd scripts/ssh_blog && go run . -addr $(SSH_BLOG_ADDR)`.
  - Add Dev Container helper targets:
    - `dc-up`: `devcontainer up --workspace-folder .`
    - `dc-shell`: `devcontainer exec --workspace-folder . bash`
    - `dc-exec`: `devcontainer exec --workspace-folder . $(CMD)`
    - `dc-verify`: `devcontainer exec --workspace-folder . bash .devcontainer/verify.sh`
- **Documentation (`AGENTS.md`):**
  - Document the `.devcontainer/` setup and `make dc-*` targets under Commands in `AGENTS.md`.

______________________________________________________________________

## 4. Data Flow & Security Model

```text
+-----------------------------------------------------------------------+
| macOS Host (Docker Desktop)                                           |
|                                                                       |
|  ~/.ssh, ~/.aws, ~/.config  --[ BLOCKED / NOT MOUNTED ]               |
|  SSH_AUTH_SOCK              --[ OVERRIDDEN TO ""      ]               |
|  git push / fly deploy      --[ RUNS ONLY ON HOST     ]               |
|                                                                       |
|  127.0.0.1:1313, :1314, :2222 <===> Container Ports                   |
|  ./ (repo root)               <===> /workspaces/blog (bind mount)     |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  | Hardened Dev Container (user: vscode, cap-drop: ALL, no sudo)   |  |
|  |                                                                 |  |
|  |  Tools: hugo 0.165.0, python 3.13 + uv, go 1.27.3, node 22,     |  |
|  |         chromium-headless, pagefind, claude, gemini             |  |
|  |                                                                 |  |
|  |  Named Volumes:                                                 |  |
|  |   - /workspaces/blog/.venv (and scripts/*/.venv)                |  |
|  |   - /home/vscode/.claude & /home/vscode/.gemini                 |  |
|  |   - /home/vscode/.cache                                         |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

______________________________________________________________________

## 5. Error Handling & Edge Cases

1. **Named Volume Ownership Without `sudo`:**
   - Because `sudo` is removed from the image for security, `post-create.sh` cannot run `sudo chown`.
   - *Mitigation:* `.devcontainer/Dockerfile` pre-creates `/workspaces/blog/.venv`, `/workspaces/blog/scripts/blog_automation_2/.venv`, `/home/vscode/.claude`, `/home/vscode/.gemini`, and `/home/vscode/.cache` owned by `vscode:vscode` (`1000:1000`) at image build time. Docker copies existing directory ownership into newly created named volumes. The two venv directories are also `chmod 777`: on Linux hosts `updateRemoteUserUID` changes the `vscode` UID but re-owns only `/home/vscode`.
2. **Leftover `.venv` Directories in Bind Mount:**
   - When Docker mounts a named volume onto `/workspaces/blog/.venv`, an empty `.venv/` directory placeholder may be created on the host filesystem if it didn't already exist.
   - *Mitigation:* `.venv` is already listed in `.gitignore`, so Git status and `make build` are unaffected.
3. **Go `1.27.3` Availability in `scripts/ssh_blog/go.mod`:**
   - `scripts/ssh_blog/go.mod` specifies `go 1.27.3`.
   - *Mitigation:* The `Dockerfile` installs Go `1.27.3` directly (or uses `GOTOOLCHAIN=go1.27.3+auto` during `docker build` to download and bake the exact `go1.27.3` toolchain into `/usr/local/go` / Go cache).
4. **Chromium Shared Memory & Sandbox Failures:**
   - Headless Chrome crashes in default 64MB `/dev/shm` containers and refuses to start without user namespaces when `--cap-drop=ALL` is active.
   - *Mitigation:* `--shm-size=1gb` in `runArgs` and `/usr/local/bin/chromium-headless` passing `--no-sandbox --disable-dev-shm-usage`.

______________________________________________________________________

## 6. Verification & Testing Strategy

`.devcontainer/verify.sh` will execute inside the running container and assert:

1. **Identity & Privilege Checks:**
   - `id -u` equals `1000` (`vscode`), not `0`.
   - `sudo -n true` fails (no passwordless `sudo`).
   - `grep NoNewPrivs /proc/self/status` shows `1`.
   - `grep CapEff /proc/self/status` shows `0000000000000000` (all capabilities dropped).
2. **Credential Isolation Checks:**
   - `[ -z "${SSH_AUTH_SOCK:-}" ]` (SSH agent socket is empty).
   - `[ ! -d /home/vscode/.ssh ]` (no host SSH directory mounted).
3. **Toolchain Checks:**
   - `hugo version` reports the version pinned in `mise.toml` and `+extended`.
   - `python3 --version` matches `.python-version`.
   - `uv --version`, `node --version` (`v22.*`), `go version`, `claude --version`, `gemini --version`, and `/usr/local/bin/chromium-headless --version` all succeed.
4. **End-to-End Blog Workflows:**
   - `make publish` builds `public/` and indexes Pagefind (`public/_pagefind/`).
   - `make check_links` passes.
   - `public/` served on :1315 (so a running `make preview` doesn't collide) + `make check_theme` runs headless Chromium mobile/desktop layout assertions and passes.
   - `PYTHONPATH=. /workspaces/blog/scripts/blog_automation_2/.venv/bin/pytest scripts/blog_automation_2/tests` passes.
   - `cd scripts/ssh_blog && go test ./...` passes.

______________________________________________________________________

## 7. Decisions

1. **No egress firewall (accepted risk).** An allowlist firewall was tried and dropped: agents in the container add links, so they must fetch arbitrary websites, and any rule that allows that also allows exfiltration. Exposure is limited: the repo is public, there are no SSH keys or git push credentials, and `.env` is going away. The remaining target is the Claude/Gemini OAuth tokens, which can be revoked by logging out.
2. **No permission-skipping shell aliases.** `claude` and `agy` prompt as usual; prompts are skipped only via `make dc-claude` / `make dc-agy`.
3. **`scripts/test_links` stays host/CI-only.** Its Selenium checker downloads Chrome for Testing, whose sandbox can't start under `--cap-drop=ALL`, so the container provisions no venv or `chromium-driver` for it.
