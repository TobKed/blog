# Dev Container

A hardened container with everything the blog needs (Hugo extended, Python + uv, Go, Node,
Pagefind, headless Chromium) and the `claude`, `gemini` and `agy` CLIs. It keeps toolchains and
coding agents off the host: an agent inside sees only this repository, not your `$HOME`.

Needs Docker. The Makefile uses a global `devcontainer` CLI if present, otherwise
`npx @devcontainers/cli`.

## Usage

| Command                  | What it does                                                    |
| ------------------------ | --------------------------------------------------------------- |
| `make dc-up`             | build and start the container                                   |
| `make dc-claude`         | Claude Code inside, permission prompts skipped                  |
| `make dc-agy`            | Antigravity CLI inside, permission prompts skipped              |
| `make dc-shell`          | interactive shell                                               |
| `make dc-exec CMD="..."` | run one command (pipes and redirects run inside the container)  |
| `make dc-verify`         | check the security invariants, toolchains, build and tests      |
| `make dc-stop`           | stop the container                                              |
| `make dc-rebuild`        | rebuild the image and recreate the container (updates the CLIs) |

`make serve`, `make preview` and `make ssh_blog` inside the container are reachable on the host at
`localhost:1313`, `:1314` and `:2222`; don't run the host versions at the same time.

Agent logins and caches persist in named volumes (`blog-dc-*`), so they survive `dc-rebuild`.
`dc-claude` and `dc-agy` run `docker` through a symlink named after the agent
(`.devcontainer/.bin/`), so terminal multiplexers that detect agents by process name, such as
herdr, recognise them.

## Security model

- Runs as `vscode` with all capabilities dropped, `no-new-privileges` and no `sudo`.
- No SSH agent, SSH keys, git push credentials or host env secrets are passed in. Commit inside,
  push from the host.
- `.git/hooks` and `.git/config` are mounted read-only, so an agent can't plant something your
  host `git` would execute (a hook, `core.fsmonitor`, `core.hooksPath`).
- No outbound traffic filtering, on purpose: agents fetch arbitrary sites to add links, and any
  rule that allows that also allows exfiltration. What's inside is a public repo and the agents'
  own OAuth tokens, which you can revoke by logging out.
- Prompts are skipped only via `make dc-claude` / `make dc-agy`; plain `claude` and `agy` inside
  the container ask as usual.

Not run inside: `scripts/test_links` (its Selenium Chrome sandbox can't start without
capabilities), Docker-based targets and deploys.
