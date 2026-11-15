FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG TARGETARCH

ENV DEBIAN_FRONTEND=noninteractive

# 1. System packages (chromium pulls in its own runtime libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    chromium \
    curl \
    fonts-liberation \
    git \
    jq \
    make \
    ripgrep \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 2. Node 22 from the official image + agent CLIs (unpinned; `make dc-rebuild` updates them)
COPY --from=node:22.23.5-bookworm-slim /usr/local/ /usr/local/
RUN npm install -g @anthropic-ai/claude-code @google/gemini-cli \
    && node /usr/local/lib/node_modules/@anthropic-ai/claude-code/install.cjs \
    && claude --version \
    && npm cache clean --force

# 3. Hugo Extended, version from mise.toml, checked against the sha256 sums pinned here.
#    After a Hugo bump the build stops and prints how to update them.
RUN --mount=type=bind,source=mise.toml,target=/tmp/mise.toml \
    HUGO_VERSION=$(sed -n 's/^hugo-extended = "\(.*\)"/\1/p' /tmp/mise.toml) \
    && release="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}" \
    && case "${TARGETARCH}" in \
        amd64) sha=f43494894cdf4a8630a201d5c828051c77f523cc66bb3938b30806835470ac20 ;; \
        arm64) sha=f40ebc44dfda3896cecd3ae7ed44f5c44c4b4a30a2b7d976ece6da62da699a58 ;; \
    esac \
    && curl -fsSL -o /tmp/hugo.tar.gz "${release}/hugo_extended_${HUGO_VERSION}_linux-${TARGETARCH}.tar.gz" \
    && { echo "${sha}  /tmp/hugo.tar.gz" | sha256sum -c - || { printf '%s\n' "" \
        "Hugo ${HUGO_VERSION} (from mise.toml) does not match the sha256 sums pinned in .devcontainer/Dockerfile." \
        "To update them after a Hugo bump:" \
        "  1. Run on the host:" \
        "       curl -fsSL ${release}/hugo_${HUGO_VERSION}_checksums.txt | grep -E 'extended_${HUGO_VERSION}_linux-(amd64|arm64).tar.gz'" \
        "  2. In step 3 of .devcontainer/Dockerfile, replace the amd64) and arm64) sums with the two it prints." \
        "  3. Run: make dc-rebuild" ""; exit 1; }; } \
    && tar -xzf /tmp/hugo.tar.gz -C /usr/local/bin hugo \
    && rm /tmp/hugo.tar.gz

# 4. Go from the official image. Only a bootstrap: GOTOOLCHAIN=auto fetches whatever
#    scripts/ssh_blog/go.mod asks for.
COPY --from=golang:1.27.3-bookworm /usr/local/go /usr/local/go
ENV PATH="/home/vscode/.local/bin:/usr/local/go/bin:/home/vscode/go/bin:${PATH}"
ENV GOTOOLCHAIN=auto

# 5. uv + the Python from .python-version
COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /usr/local/bin/
ENV UV_PYTHON_INSTALL_DIR=/opt/python
RUN --mount=type=bind,source=.python-version,target=.python-version \
    uv python install \
    && ln -sf "$(uv python find)" /usr/local/bin/python3 \
    && ln -sf /usr/local/bin/python3 /usr/local/bin/python

# 5b. Neovim; its config and plugins are installed as vscode at the end
ARG NVIM_VERSION=0.12.6
RUN case "${TARGETARCH}" in \
        amd64) arch=x86_64 sha=474430d53e6264f6d6dd18db42d6dc9df3a1b56ca9e88a325bbf860e1a811d87 ;; \
        arm64) arch=arm64 sha=8f1f64a0bdb97247034038c3823c6cbad5bdf9ecd5751b85494b71c3ee04c815 ;; \
        *) echo "No Neovim build for TARGETARCH=${TARGETARCH}" >&2; exit 1 ;; \
    esac \
    && curl -fsSL -o /tmp/nvim.tar.gz "https://github.com/neovim/neovim/releases/download/v${NVIM_VERSION}/nvim-linux-${arch}.tar.gz" \
    && { echo "${sha}  /tmp/nvim.tar.gz" | sha256sum -c - || { printf '%s\n' "" \
        "Neovim ${NVIM_VERSION} does not match the sha256 sums pinned in .devcontainer/Dockerfile." \
        "To update them after a Neovim bump:" \
        "  1. Run on the host:" \
        "       curl -fsSL https://api.github.com/repos/neovim/neovim/releases/tags/v${NVIM_VERSION} | grep -E '\"(name|digest)\"' | grep -A1 -E 'linux-(x86_64|arm64)\\.tar\\.gz\"'" \
        "  2. In step 5b of .devcontainer/Dockerfile, replace the amd64) and arm64) sums with the two it prints." \
        "  3. Run: make dc-rebuild" ""; exit 1; }; } \
    && mkdir /opt/nvim && tar -xzf /tmp/nvim.tar.gz -C /opt/nvim --strip-components=1 \
    && ln -s /opt/nvim/bin/nvim /usr/local/bin/nvim \
    && rm /tmp/nvim.tar.gz

# 6. Headless Chromium wrapper for unprivileged container (--cap-drop=ALL)
RUN printf '#!/bin/sh\nexec /usr/bin/chromium --no-sandbox --disable-dev-shm-usage "$@"\n' \
    > /usr/local/bin/chromium-headless \
    && chmod +x /usr/local/bin/chromium-headless

# 7. Pre-create volume mount directories owned by vscode:vscode so root/sudo is never needed at runtime.
#    The venv dir is 777: updateRemoteUserUID re-owns only /home/vscode on Linux hosts.
RUN mkdir -p \
    /workspaces/blog/.venv \
    /home/vscode/.claude \
    /home/vscode/.gemini \
    /home/vscode/.cache \
    /home/vscode/go \
    && chown -R vscode:vscode /workspaces /home/vscode /opt/python \
    && chmod 777 /workspaces/blog/.venv

# 8. Install Antigravity CLI (agy) as vscode and symlink to /usr/local/bin/agy
RUN su - vscode -c "curl -fsSL https://antigravity.google/cli/install.sh | bash" \
    && ln -sf /home/vscode/.local/bin/agy /usr/local/bin/agy

# 9. Strip passwordless sudo from vscode user so runtime processes cannot escalate to root
RUN rm -f /etc/sudoers.d/vscode \
    && sed -i '/vscode/d' /etc/sudoers

USER vscode

# 10. Neovim config; the first headless start installs its plugins into the image.
#     nvim exits 0 on config errors, so a second start must print nothing.
COPY --chown=vscode:vscode .devcontainer/nvim/init.lua /home/vscode/.config/nvim/init.lua
RUN nvim --headless +qa && out=$(nvim --headless +qa 2>&1) && [ -z "$out" ] || { echo "$out" >&2; exit 1; }

WORKDIR /workspaces/blog
