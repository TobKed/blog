#!/usr/bin/env bash
set -euo pipefail

FAILURES=0

# check LABEL CMD...: rerun CMD by hand to see why it failed
check() {
  local label=$1
  shift
  if "$@" >/dev/null 2>&1 </dev/null; then
    printf "  ok   %s\n" "$label"
  else
    printf " FAIL  %s\n" "$label"
    FAILURES=$((FAILURES + 1))
  fi
}

echo "=== In-Container Security & Toolchain Checks ==="
check "running as vscode" test "$(id -un)" = vscode
check "passwordless sudo is disabled" bash -c '! sudo -n true'
check "NoNewPrivs is active" grep -q '^NoNewPrivs:[[:space:]]*1' /proc/self/status
check "no effective Linux capabilities" grep -q '^CapEff:[[:space:]]*0*$' /proc/self/status
check "SSH_AUTH_SOCK is empty" test -z "${SSH_AUTH_SOCK:-}"
# git on the host runs hooks and config-defined commands from .git
check ".git is read-only" bash -c 'p=$(git rev-parse --git-common-dir)/verify-probe; ! touch "$p" || { rm "$p"; false; }'
check "git can read the repository" git rev-parse HEAD
check "/home/vscode/.ssh is not mounted" test ! -d /home/vscode/.ssh

hugo_want=$(sed -n 's/^hugo-extended = "\(.*\)"/\1/p' mise.toml)
check "hugo extended v$hugo_want from mise.toml installed (if not: make dc-rebuild)" bash -c "[ -n '$hugo_want' ] && hugo version | grep -q 'v$hugo_want.*extended'"
check "python $(cat .python-version) from .python-version installed (if not: make dc-rebuild)" bash -c 'python3 --version | grep -q "^Python $(cat .python-version)"'

for cmd in "uv --version" "go version" "node --version" "npx --version" \
  "claude --version" "gemini --version" "agy --version" "chromium-headless --version"; do
  check "$cmd runs" $cmd
done

echo "=== End-to-End Blog Workflow Checks ==="
check "make publish built site and Pagefind index" bash -c 'make publish && [ -d public/_pagefind ]'

# 1315, not 1314, so a running `make preview` doesn't collide
python3 -m http.server -d public 1315 >/dev/null 2>&1 &
trap 'kill $! 2>/dev/null || true' EXIT
for _ in $(seq 50); do curl -fs -o /dev/null http://localhost:1315/ && break; sleep 0.1; done
check "make check_theme passed via headless Chromium" make check_theme URL=http://localhost:1315

# the full check_links exits non-zero on duplicates in the content, which is not a container fault
check "check_duplicate_links self-test passed" python3 scripts/check_duplicate_links.py --self-test
check "ssh_blog go test passed" bash -c 'cd scripts/ssh_blog && go test ./...'

if [ "$FAILURES" -gt 0 ]; then
  echo "Verification failed with $FAILURES error(s)."
  exit 1
fi

echo "All checks passed."
