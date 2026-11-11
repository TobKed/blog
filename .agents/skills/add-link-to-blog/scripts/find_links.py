#!/usr/bin/env python3
"""Normalize candidate URLs and report where each already appears in content/post/ and content/pages/."""

import re
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

ROOT = Path(__file__).resolve().parents[4]
DIRS = [ROOT / "content" / "post", ROOT / "content" / "pages"]
URL_RE = re.compile(r"https?://[^\s)<>\"']+")
YT_ID_RE = re.compile(r'youtube-lite id="([^"]+)"')
TRACKING = {"fbclid", "gclid", "msclkid", "si", "ref_src"}


def clean(url: str) -> str:
    """Return the URL without fragment and tracking parameters, as it should be written in a post."""
    p = urlparse(url)
    query = [
        (k, v)
        for k, v in parse_qsl(p.query)
        if not (k.lower().startswith("utm_") or k.lower() in TRACKING)
    ]
    return urlunparse(p._replace(query=urlencode(query), fragment=""))


def key(url: str) -> str:
    """Return a comparison key: YouTube URLs collapse to their video ID, others to host+path+query."""
    p = urlparse(clean(url))
    host = p.netloc.lower().removeprefix("www.").removeprefix("m.")
    if host in ("youtube.com", "youtube-nocookie.com"):
        vid = dict(parse_qsl(p.query)).get("v")
        if vid:
            return "yt:" + vid
    if host == "youtu.be":
        return "yt:" + p.path.strip("/")
    return f"{host}{p.path.rstrip('/')}" + (f"?{p.query}" if p.query else "")


def index() -> dict[str, list[str]]:
    """Map every link key found in the content directories to its file:line locations."""
    found: dict[str, list[str]] = {}
    for d in DIRS:
        for md in sorted(d.glob("*.md")):
            for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
                keys = {key(u) for u in URL_RE.findall(line)}
                keys |= {"yt:" + v for v in YT_ID_RE.findall(line)}
                for k in keys:
                    found.setdefault(k, []).append(f"{md.relative_to(ROOT)}:{n}")
    return found


def main(urls: list[str]) -> None:
    """Print each input's cleaned URL, whether it repeats an earlier input, and existing locations."""
    found = index()
    seen: dict[str, str] = {}
    for url in urls:
        k = key(url)
        print(clean(url))
        if k in seen:
            print(f"  REPEATED IN INPUT: same as {seen[k]}")
            continue
        seen[k] = url
        for loc in found.get(k, []):
            print(f"  DUPLICATE: {loc}")


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if a.strip()])
