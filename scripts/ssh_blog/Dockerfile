# Build from the repo root: docker build -f scripts/ssh_blog/Dockerfile .
FROM golang:1.27-alpine AS build
WORKDIR /src
COPY scripts/ssh_blog/go.mod scripts/ssh_blog/go.sum ./
RUN go mod download
COPY scripts/ssh_blog/*.go ./
RUN CGO_ENABLED=0 go build -o /ssh_blog . && mkdir /data

FROM scratch
COPY --from=build /ssh_blog /ssh_blog
COPY hugo.toml /site/
COPY content/post /site/content/post
COPY content/pages /site/content/pages
# Mount a volume here to keep the host key across restarts.
COPY --from=build --chown=65532:65532 /data /data
USER 65532:65532
WORKDIR /data
EXPOSE 2222
ENTRYPOINT ["/ssh_blog", "-addr", ":2222", "-site", "/site"]
