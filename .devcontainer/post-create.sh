#!/usr/bin/env bash
set -euo pipefail

echo "==> Provisioning root Python virtualenv (/workspaces/blog/.venv)..."
uv venv /workspaces/blog/.venv --allow-existing
uv pip install --python /workspaces/blog/.venv/bin/python -r /workspaces/blog/requirements.txt

echo "==> Pre-warming Go modules for scripts/ssh_blog..."
(cd /workspaces/blog/scripts/ssh_blog && go mod download)

echo "==> Pre-warming pre-commit hook environments..."
/workspaces/blog/.venv/bin/pre-commit install-hooks

echo "==> Dev Container setup complete."
