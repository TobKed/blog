#!/usr/bin/env bash
set -euo pipefail

FAILURES=0

pass() {
  printf "  ok   %s\n" "$1"
}

fail() {
  printf " FAIL  %s (%s)\n" "$1" "$2"
  FAILURES=$((FAILURES + 1))
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

  hugo_want=$(sed -n 's/^hugo-extended = "\(.*\)"/\1/p' mise.toml)
  hugo_got=$(hugo version 2>&1 || true)
  if [[ $hugo_got == *"v$hugo_want"*extended* ]]; then
    pass "hugo extended v$hugo_want installed"
  else
    fail "hugo extended v$hugo_want installed" "$hugo_got"
  fi

  py_want=$(cat .python-version)
  py_got=$(python3 --version 2>&1 || true)
  if [[ $py_got == "Python $py_want"* ]]; then
    pass "python $py_want installed"
  else
    fail "python $py_want installed" "$py_got"
  fi

  for cmd in uv go node npx pagefind claude gemini agy /usr/local/bin/chromium-headless; do
    if command -v "$cmd" >/dev/null 2>&1; then
      pass "$cmd is available"
    else
      fail "$cmd is available" "not found in PATH"
    fi
  done

  if claude --version >/dev/null 2>&1; then
    pass "claude --version executes cleanly"
  else
    fail "claude --version executes cleanly" "execution failed"
  fi

  if agy --version >/dev/null 2>&1; then
    pass "agy --version executes cleanly"
  else
    fail "agy --version executes cleanly" "execution failed"
  fi

  if /usr/local/bin/chromium-headless --version >/dev/null 2>&1; then
    pass "chromium-headless --version runs under dropped capabilities"
  else
    fail "chromium-headless --version runs under dropped capabilities" "execution failed"
  fi

  echo "=== End-to-End Blog Workflow Checks ==="
  if make publish >/dev/null && [ -d public/_pagefind ]; then
    pass "make publish built site and Pagefind index"
  else
    fail "make publish built site and Pagefind index" "make publish failed or public/_pagefind missing"
  fi

  # 1315, not 1314, so a running `make preview` doesn't collide
  python3 -m http.server -d public 1315 >/dev/null 2>&1 &
  HTTP_PID=$!
  trap 'kill "$HTTP_PID" 2>/dev/null || true' EXIT
  for _ in $(seq 50); do curl -fs -o /dev/null http://localhost:1315/ && break; sleep 0.1; done
  if make check_theme URL=http://localhost:1315 >/dev/null; then
    pass "make check_theme passed via headless Chromium"
  else
    fail "make check_theme passed via headless Chromium" "check_theme failed"
  fi
  kill "$HTTP_PID" 2>/dev/null || true
  trap - EXIT

  if make check_links FILES=content/post/2025_11_30_november_links.md >/dev/null; then
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

check_runtime

if [ "$FAILURES" -gt 0 ]; then
  echo "Verification failed with $FAILURES error(s)."
  exit 1
fi

echo "All checks passed."
