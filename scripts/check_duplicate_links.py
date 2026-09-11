#!/usr/bin/env python3
"""Report duplicated links within a post and across all posts in content/post/."""

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

POSTS_DIR = Path(__file__).resolve().parent.parent / "content" / "post"
TEMPLATE = "template_links"
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
    frag = f"#{p.fragment}" if p.fragment else ""
    if host in ("youtube.com", "m.youtube.com", "youtube-nocookie.com"):
        vid = parse_qs(p.query).get("v")
        if vid:
            return "youtu.be/" + vid[0]
    if host == "youtu.be":
        return "youtu.be" + path
    query = urlencode(
        sorted(
            (k, v) for k, v in parse_qs(p.query).items() if k.lower() not in TRACKING
        ),
        doseq=True,
    )
    return f"{host}{path}" + (f"?{query}" if query else "") + frag


def links(path):
    """Yield (normalized_url, raw_url, line_number, silenced_by_dup_ok)."""
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marked = "dup-ok" in line
        for url in LINK_RE.findall(line):
            yield normalize(url), url, n, marked


def main(argv):
    warn_only = "--warn" in argv
    argv = [a for a in argv if a != "--warn"]
    targets = [Path(a) for a in argv] or sorted(POSTS_DIR.glob("*.md"))
    missing = [p for p in targets if not p.exists()]
    if missing:
        sys.exit(f"no such file: {', '.join(map(str, missing))}")
    targets = [p for p in targets if TEMPLATE not in p.name]

    elsewhere = defaultdict(set)
    for post in POSTS_DIR.glob("*.md"):
        if TEMPLATE in post.name:
            continue
        for key, _, _, _ in links(post):
            elsewhere[key].add(post.name)

    failed = False
    for post in targets:
        seen = defaultdict(list)
        for key, url, line, marked in links(post):
            if not marked:
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
    assert normalize("https://d.com/c#one") != normalize("https://d.com/c#two")
    assert normalize("https://d.com/c?b=1&a=2") == normalize("https://d.com/c?a=2&b=1")
    print("ok")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        sys.exit(main(sys.argv[1:]))
