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

## Host on Fly.io

About $2/month: the dedicated IPv4 (raw TCP does not work on Fly's shared one). The machine
stops when nobody is connected, so the first connection takes a few seconds to start it.

One-time setup:

```sh
brew install flyctl && fly auth login
fly apps create tobked-ssh-blog           # name must match fly.toml and the Makefile
ssh-keygen -t ed25519 -N "" -C ssh-blog -f ssh_blog_key
fly secrets set -a tobked-ssh-blog --stage SSH_HOST_KEY="$(cat ssh_blog_key)"
ssh-keygen -lf ssh_blog_key.pub           # fingerprint to give friends
rm ssh_blog_key ssh_blog_key.pub          # or keep a copy in a password manager
fly ips allocate-v4 -a tobked-ssh-blog    # dedicated, $2/month
fly ips allocate-v6 -a tobked-ssh-blog    # free
```

Deploy (and redeploy after new posts), from the repo root:

```sh
make ssh_blog_fly
ssh tobked-ssh-blog.fly.dev
```

CI (`.github/workflows/ssh_blog.yml`) runs the tests on PRs and `make ssh_blog_fly` on pushes to
`master` that touch posts, pages, `hugo.toml` or this folder. It needs a deploy token scoped to the app:
`fly tokens create deploy -a tobked-ssh-blog | gh secret set FLY_API_TOKEN`.

The image is built locally, so only the files in `Dockerfile.dockerignore` leave the machine.
For a custom name, point `A`/`AAAA` records (e.g. `ssh.blog.tobked.dev`) at the addresses
from `fly ips list -a tobked-ssh-blog`. Logs: `fly logs -a tobked-ssh-blog`. Take it down:
`fly apps destroy tobked-ssh-blog`.
