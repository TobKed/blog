# SSH blog

Serves the blog over SSH as a terminal app: the About page (with the social links from
`hugo.toml`), the Links page, then every published post. Drafts and unlisted pages are skipped.

## Run locally

```sh
make ssh_blog            # go run, needs Go
ssh -p 2222 localhost
```

## Run in Docker

```sh
make ssh_blog_docker     # build the image, start the container on 127.0.0.1:2222
ssh -p 2222 127.0.0.1
docker logs ssh-blog     # connections are logged here
docker rm -f ssh-blog    # stop
```

The image holds only the binary, `hugo.toml`, `content/post/` and `content/pages/`. The server's host key is generated
on first start and kept in the `ssh-blog-data` volume, so the fingerprint survives restarts.
Rebuild after editing posts.

## Share with a friend

Needs [bore](https://github.com/ekzhang/bore) (`brew install bore-cli`) and the container running.

```sh
make ssh_blog_share      # prints "listening at bore.pub:<port>"
```

Send them `ssh -p <port> bore.pub`; the port changes on every run. Get the fingerprint
for them to compare on first connect:

```sh
ssh-keyscan -t ed25519 -p 2222 127.0.0.1 2>/dev/null | ssh-keygen -lf -
```

The port is public while bore runs: anyone who finds it can read the blog, nothing more
(no shell, no SFTP, no port forwarding). Ctrl+C stops sharing.
