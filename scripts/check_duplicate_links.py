#!/usr/bin/env python3
"""Report duplicated links within a post and across all posts in content/post/."""

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qs, urlparse

POSTS_DIR = Path(__file__).resolve().parent.parent / "content" / "post"
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
TRACKING = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "msclkid",
}


def normalize(url):
    p = urlparse(url)
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/")
    if host in ("youtube.com", "m.youtube.com", "youtube-nocookie.com"):
        vid = parse_qs(p.query).get("v")
        if vid:
            return "youtu.be/" + vid[0]
    if host == "youtu.be":
        return "youtu.be" + path
    query = sorted(
        (k, v) for k, v in parse_qs(p.query).items() if k.lower() not in TRACKING
    )
    return f"{host}{path}" + (f"?{query}" if query else "")


def links(path):
    """Yield (normalized_url, raw_url, line_number), skipping lines marked dup-ok."""
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "dup-ok" in line:
            continue
        for url in LINK_RE.findall(line):
            yield normalize(url), url, n


def main(argv):
    warn_only = "--warn" in argv
    argv = [a for a in argv if a != "--warn"]
    targets = [Path(a) for a in argv] or sorted(POSTS_DIR.glob("*.md"))
    targets = [p for p in targets if p.suffix == ".md" and p.exists()]

    elsewhere = defaultdict(set)
    for post in POSTS_DIR.glob("*.md"):
        for key, _, _ in links(post):
            elsewhere[key].add(post.name)

    failed = False
    for post in targets:
        seen = defaultdict(list)
        for key, url, line in links(post):
            seen[key].append((url, line))
        for key, hits in seen.items():
            if len(hits) > 1:
                failed = True
                lines = ", ".join(f"line {n}" for _, n in hits)
                print(f"{post}: duplicate within file: {hits[0][0]} ({lines})")
            others = sorted(elsewhere[key] - {post.name})
            if others:
                failed = True
                print(f"{post}:{hits[0][1]}: also in {', '.join(others)}: {hits[0][0]}")
    if failed:
        print("\nMark an intentional repeat with a `dup-ok` comment on that line.")
    return 1 if failed and not warn_only else 0


def self_test():
    assert normalize("https://www.youtube.com/watch?v=abc") == "youtu.be/abc"
    assert normalize("https://youtu.be/abc") == "youtu.be/abc"
    assert normalize("https://Example.com/x/?utm_source=n") == normalize(
        "http://www.example.com/x"
    )
    assert normalize("https://example.com/a") != normalize("https://example.com/b")
    print("ok")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        sys.exit(main(sys.argv[1:]))
