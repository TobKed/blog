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

  if grep -q "dangerously-skip-permissions" .devcontainer/Dockerfile; then
    fail "Dockerfile has no permission-skipping aliases" "found --dangerously-skip-permissions"
  else
    pass "Dockerfile has no permission-skipping aliases"
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
