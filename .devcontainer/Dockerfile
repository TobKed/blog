FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG TARGETARCH
ARG HUGO_VERSION=0.165.0
ARG GO_VERSION=1.27.3
ARG NODE_MAJOR=22

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

# 2. Node.js 22 LTS + global CLIs (pagefind, claude-code, gemini-cli)
RUN curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g \
        pagefind \
        @anthropic-ai/claude-code \
        @google/gemini-cli \
    && node /usr/lib/node_modules/@anthropic-ai/claude-code/install.cjs \
    && claude --version \
    && npm cache clean --force \
    && rm -rf /var/lib/apt/lists/*

# 3. Hugo Extended 0.165.0
RUN curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${TARGETARCH}.tar.gz" \
    | tar -xz -C /usr/local/bin hugo \
    && chmod +x /usr/local/bin/hugo

# 4. Go toolchain (with GOTOOLCHAIN=auto so go 1.27.3 in scripts/ssh_blog/go.mod works seamlessly)
RUN curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-${TARGETARCH}.tar.gz" \
    | tar -xz -C /usr/local
ENV PATH="/home/vscode/.local/bin:/usr/local/go/bin:/home/vscode/go/bin:${PATH}"
ENV GOTOOLCHAIN=auto

# 5. uv + Python 3.13
COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /usr/local/bin/
ENV UV_PYTHON_INSTALL_DIR=/opt/python
RUN uv python install 3.13 \
    && ln -sf "$(uv python find 3.13)" /usr/local/bin/python3 \
    && ln -sf /usr/local/bin/python3 /usr/local/bin/python

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
WORKDIR /workspaces/blog
