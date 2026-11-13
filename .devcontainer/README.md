# Dev Container

A hardened container with everything the blog needs (Hugo extended, Python + uv, Go, Node,
Pagefind, headless Chromium) and the `claude`, `gemini` and `agy` CLIs. It keeps toolchains and
coding agents off the host: an agent inside sees only this repository, not your `$HOME`.

Needs Docker. The Makefile uses a global `devcontainer` CLI if present, otherwise
`npx @devcontainers/cli`. Start it through the `make` targets: `devcontainer.json` takes the git
directory to mount from the Makefile.

## Usage

| Command                  | What it does                                                   |
| ------------------------ | -------------------------------------------------------------- |
| `make dc-up`             | build and start the container                                  |
| `make dc-claude`         | Claude Code inside, permission prompts skipped                 |
| `make dc-agy`            | Antigravity CLI inside, permission prompts skipped             |
| `make dc-shell`          | interactive shell                                              |
| `make dc-exec CMD="..."` | run one command (pipes and redirects run inside the container) |
| `make dc-verify`         | check the security invariants, toolchains, build and tests     |
| `make dc-stop`           | stop the container                                             |
| `make dc-rebuild`        | rebuild the image without cache and recreate the container     |

`make serve`, `make preview` and `make ssh_blog` inside the container are reachable on the host at
`localhost:1313`, `:1314` and `:2222`. Those host ports are claimed at start, so stop the host
`make serve` first, and only one container (git worktrees included) runs at a time.

The agent CLIs can't update themselves; `make dc-rebuild` installs their latest. Agent logins and
caches persist in named volumes (`blog-dc-*`) and survive it.
`dc-claude` and `dc-agy` run `docker` through a symlink named after the agent
(`.devcontainer/.bin/`), so terminal multiplexers that detect agents by process name, such as
herdr, recognise them.

## Updating versions

| What                   | Bump it in                 | Then, for the container                               |
| ---------------------- | -------------------------- | ----------------------------------------------------- |
| Hugo                   | `mise.toml`                | update the two sha256 sums (below), `make dc-rebuild` |
| Python                 | `.python-version`          | `make dc-rebuild`                                     |
| Python packages        | `requirements.txt`         | `make dc-rebuild`                                     |
| Pagefind               | `Makefile`                 | nothing                                               |
| Go                     | `scripts/ssh_blog/go.mod`  | nothing (Go fetches the toolchain `go.mod` asks for)  |
| `claude`, `gemini`     | not pinned                 | `make dc-rebuild` installs the latest                 |
| Node, uv, Go bootstrap | `.devcontainer/Dockerfile` | `make dc-rebuild`                                     |

CI reads Hugo and Python from the same files. `make dc-verify` fails on a Hugo or Python mismatch,
which means the image is older than the pin: run `make dc-rebuild`.

Hugo's download is checked against sha256 sums pinned in step 3 of the `Dockerfile`, one for
`amd64` and one for `arm64`. After changing the version in `mise.toml`:

1. Print the new sums (replace `X.Y.Z` with the new version):

   ```sh
   curl -fsSL https://github.com/gohugoio/hugo/releases/download/vX.Y.Z/hugo_X.Y.Z_checksums.txt \
     | grep -E 'extended_X.Y.Z_linux-(amd64|arm64).tar.gz'
   ```

2. In step 3 of `.devcontainer/Dockerfile`, replace the `amd64)` and `arm64)` sums with them.

3. Run `make dc-rebuild`.

If you skip this, `make dc-rebuild` stops at step 3 and prints the same instructions with the
version filled in.

## Security model

- Runs as `vscode` with all capabilities dropped, `no-new-privileges` and no `sudo`.
- No SSH agent, SSH keys, git push credentials or host env secrets are passed in.
- `.git` is mounted read-only: `git status`, `diff` and `log` work inside, but nothing there can
  stage or commit, or plant a hook or config your host `git` would execute. Commit and push from
  the host.
- The working tree itself is shared read-write, so an agent can edit anything you later run on the
  host: the `Makefile`, scripts, `.pre-commit-config.yaml`, `.claude/` settings. Read `git status`
  and `git diff` before committing or running repo code on the host.
- No outbound traffic filtering, on purpose: agents fetch arbitrary sites to add links, and any
  rule that allows that also allows exfiltration. What's inside is a public repo and the agents'
  own OAuth tokens, which you can revoke by logging out.
- Prompts are skipped only via `make dc-claude` / `make dc-agy`; plain `claude` and `agy` inside
  the container ask as usual.

Not run inside: `scripts/test_links` (its Selenium Chrome sandbox can't start without
capabilities), Docker-based targets and deploys.
