# TODO: devcontainer branch review follow-ups

Source: code review of `feat/devcontainer` (2026-11-13). Nothing below has been fixed yet.

## 1. Remove `scripts/blog_automation` and `scripts/blog_automation_2`

Neither tool is needed any more (the `add-link-to-blog` skill covers the workflow).
`scripts/blog_automation/` is untracked locally, so just delete it.
`scripts/blog_automation_2/` is tracked; removing it also needs these cleanups:

- \[ \] `.devcontainer/devcontainer.json`
  - drop the `blog-dc-automation-venv` mount
  - drop `PLAYWRIGHT_BROWSERS_PATH` (only crawl4ai/Playwright used it; the value `/usr/bin` was wrong anyway)
  - re-check whether `OPENAI_API_KEY` in `remoteEnv` is still needed (probably not)
- \[ \] `.devcontainer/Dockerfile`: drop `/workspaces/blog/scripts/blog_automation_2/.venv` from the `mkdir -p` list
- \[ \] `.devcontainer/post-create.sh`: drop the blog_automation_2 venv provisioning block
- \[ \] `.devcontainer/verify.sh`: drop the `blog_automation_2 pytest suite passed` check
- \[ \] `.pre-commit-config.yaml:34`: drop the `^scripts/blog_automation_2/README.md` exclude
- \[ \] `AGENTS.md`
  - remove the `scripts/blog_automation_2/` bullet (around line 74) and its mention under "Monthly links posts"
  - fix the Secrets note (around line 100), which points at `scripts/blog_automation_2/config.py`
- \[ \] Check `requirements.txt` for deps only used by the automation (langchain, openai, crawl4ai, python-dotenv, ...)
- \[ \] Mark the old specs and plans as obsolete or delete them
  - `docs/superpowers/specs/2026-03-15-quick-cli-add-link-design.md`
  - `docs/superpowers/plans/2026-03-15-quick-cli-add-link-plan.md`
  - mentions in the devcontainer spec and plan
- \[ \] Possibly `.env` itself, if nothing else reads it

## 2. Bugs to fix in the devcontainer

- \[ \] **`verify.sh` exits early if `make publish` fails** (`verify.sh` ~line 144). Under `set -e`, the bare `make publish >/dev/null` makes the script exit without printing FAIL or the summary. Wrap it in `if ...; then pass; else fail; fi` like the other checks.
- \[ \] **`pipefail` + `grep -q` can give false FAILs** (`verify.sh` hugo/python version checks). Capture the output first (`v=$(hugo version)`), then test the variable.
- \[ \] **Selenium link checker (`scripts/test_links/test_links_selenium.py`) can't run in the container**
  - `--no-sandbox` is commented out and no binary location is set
  - Selenium Manager will download Chrome for Testing instead of using `/usr/bin/chromium` + `chromium-driver`
  - the Chrome sandbox can't start under `--cap-drop=ALL`
  - **Decided:** keep test_links host/CI-only. Remove the `blog-dc-testlinks-venv` mount, its `mkdir` in the Dockerfile and its block in `post-create.sh`, and note in `scripts/test_links/AGENTS.md` that it doesn't run in the devcontainer. `chromium-driver` can then be dropped from the Dockerfile.

## 3. Security and hardening

### Decided

- \[ \] **Secrets out of the repo:** once `blog_automation_2` is gone, delete `.env`; keep any remaining secrets outside the repo (password manager or `~/.config`), so agents in the container have nothing to read.
- \[ \] **Mount `.git/hooks` read-only** in `devcontainer.json`. Agents can still commit, but can't plant a hook that runs on the host. Add a `verify.sh` check that `core.hooksPath` is unset.
- \[ \] **Remove the `OPENAI_API_KEY` passthrough** from `remoteEnv`, together with `blog_automation_2`.
- \[ \] **Pinning in the `Dockerfile`, selectively:**
  - pin `pagefind` to the same version CI uses (it changes the published output)
  - pin `ghcr.io/astral-sh/uv` to a tag instead of `latest`
  - drop the `npm install -g npm@latest` step (Node 22's bundled npm is fine)
  - leave `claude-code`, `gemini-cli` and `agy` floating; `make dc-rebuild` is the update step

### Done on `feat/devcontainer` (not yet tested in a rebuilt container)

- \[x\] **Permission-skipping shell aliases removed.** Prompts are skipped only via `make dc-claude` / `make dc-agy`. `verify.sh --static` checks the Dockerfile has none.
- \[x\] **No egress firewall (accepted risk).** An allowlist firewall was tried and dropped: the container is used to add links, so agents must fetch arbitrary websites, and any rule that allows that also allows exfiltration. Exposure is limited because the repo is public, there are no SSH keys or git push credentials, and `.env` is going away. The remaining target is the Claude/Gemini OAuth tokens, which can be revoked by logging out.
- \[ \] Run `make dc-rebuild && make dc-verify` on the host.
- \[ \] Update the devcontainer spec (`docs/superpowers/specs/2026-11-13-devcontainer-design.md`): record the no-egress-control decision above and the removed aliases.

## 4. Smaller issues

- \[ \] `UV_PYTHON_INSTALL_DIR=/opt/python` is root-owned. If `.python-version` is ever pinned to a patch version that isn't installed, `uv venv` fails with a permission error. Make `/opt/python` vscode-owned or unset the variable at runtime.
- \[ \] `make dc-exec CMD=...`: `$(CMD)` is split by the host shell, so pipes and redirects run on the host. Use `bash -lc '$(CMD)'` or document "simple commands only".
- \[ \] `verify.sh` starts its own `http.server` on 1314. It collides silently with a running `make preview`, and the fixed `sleep 1` is racy; poll with `curl` until the server answers.
- \[ \] `verify.sh --static` has no Makefile target. Add something like `dc-verify-static` that runs on the host (or in CI) without building the container.
- \[ \] Docs out of date
  - `AGENTS.md` is missing `dc-stop`, `dc-rebuild`, `dc-claude`, `dc-agy` and the `HUGO_BIND` / `SSH_BLOG_ADDR` variables
  - the devcontainer spec doesn't mention agy, the YOLO aliases, `dc-stop` or `dc-rebuild`
- \[ \] `check_docker` says "start Docker Desktop" even on Linux/CI, and it now also guards `ssh_blog_fly`. Use a neutral message.
- \[ \] Port 2222 is forwarded from the container and also used by host `make ssh_blog`, so running both conflicts. Add a note.
