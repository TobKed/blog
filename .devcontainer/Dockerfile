FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG TARGETARCH
ARG HUGO_VERSION=0.165.0
ARG GO_VERSION=1.27.3
ARG NODE_MAJOR=22

ENV DEBIAN_FRONTEND=noninteractive

# 1. System packages & Headless Chromium dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    chromium \
    chromium-driver \
    curl \
    fonts-liberation \
    git \
    jq \
    libasound2 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libgbm1 \
    libnss3 \
    libxkbcommon0 \
    make \
    ripgrep \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 2. Node.js 22 LTS + global CLIs (npm, pagefind, claude-code, gemini-cli)
RUN curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g npm@latest \
    && npm install -g \
        pagefind \
        @anthropic-ai/claude-code \
        @google/gemini-cli \
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
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/
ENV UV_PYTHON_INSTALL_DIR=/opt/python
RUN uv python install 3.13 \
    && ln -sf "$(uv python find 3.13)" /usr/local/bin/python3 \
    && ln -sf /usr/local/bin/python3 /usr/local/bin/python

# 6. Headless Chromium wrapper for unprivileged container (--cap-drop=ALL)
RUN printf '#!/bin/sh\nexec /usr/bin/chromium --no-sandbox --disable-dev-shm-usage "$@"\n' \
    > /usr/local/bin/chromium-headless \
    && chmod +x /usr/local/bin/chromium-headless

# 7. Pre-create volume mount directories owned by vscode:vscode so root/sudo is never needed at runtime
RUN mkdir -p \
    /workspaces/blog/.venv \
    /workspaces/blog/scripts/blog_automation_2/.venv \
    /workspaces/blog/scripts/test_links/.venv \
    /home/vscode/.claude \
    /home/vscode/.gemini \
    /home/vscode/.cache \
    /home/vscode/go \
    && chown -R vscode:vscode /workspaces /home/vscode

# 8. Strip passwordless sudo from vscode user so runtime processes cannot escalate to root
RUN rm -f /etc/sudoers.d/vscode \
    && sed -i '/vscode/d' /etc/sudoers

USER vscode

# 9. Install Antigravity CLI (agy) into /home/vscode/.local/bin/agy and configure YOLO mode aliases
RUN curl -fsSL https://antigravity.google/cli/install.sh | bash \
    && printf '\nalias claude="claude --dangerously-skip-permissions"\nalias agy="agy --dangerously-skip-permissions"\n' >> /home/vscode/.bashrc \
    && printf '\nalias claude="claude --dangerously-skip-permissions"\nalias agy="agy --dangerously-skip-permissions"\n' >> /home/vscode/.zshrc

WORKDIR /workspaces/blog
