"""One-off: replace the videoWrapper YouTube iframes in posts with {{<youtube-lite>}}.

Usage: python scripts/migrate_youtube_lite.py [--dry-run]
"""

import re
import sys
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "content" / "post"

EMBED = re.compile(
    r'<div class="videoWrapper"[^>]*>\s*'
    r'<iframe[^>]*\ssrc="https://www\.youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]+)[^"]*"[^>]*>\s*</iframe>\s*'
    r"</div>"
)
LINK = re.compile(r"\[(.+)\]\(<?[^)\s>]+>?\)")
HTML_LINK = re.compile(r"<a [^>]*>(.+?)</a>")
MD_ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>])")


def title_for(text: str, start: int) -> tuple[str, bool]:
    """Title for an embed: the nearest `### [Title](url)` heading above it, unless
    another linked heading, a list item or a bare link comes first - essays list
    the video before embedding it. The flag is False for those, so they can be
    reviewed."""
    for line in reversed(text[:start].splitlines()):
        line = line.strip()
        if line.startswith("### "):
            line = line[4:].strip()
            match = LINK.fullmatch(line)
            return (match.group(1) if match else line), True
        if line.startswith("#"):
            match = LINK.search(line)
            if match:
                return match.group(1), False
            break
        if line.startswith(("- ", "* ", "<li", "[")):
            match = LINK.search(line) or HTML_LINK.search(line)
            if match:
                return match.group(1), False
    raise ValueError(f"no title for the embed at offset {start}")


def shortcode(video_id: str, title: str) -> str:
    title = MD_ESCAPE.sub(r"\1", title)
    # Typographic quotes: an escaped \" stops mdformat reading the line as a tag.
    title = re.sub(r'"([^"]*)"', "\u201c\\1\u201d", title).replace('"', "\u201d")
    return f'{{{{<youtube-lite id="{video_id}" title="{title}">}}}}'


def migrate(text: str) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        title, from_heading = title_for(text, match.start())
        if not from_heading:
            print(f"  not under a ### heading: {match.group(1)} -> {title}")
        count += 1
        return shortcode(match.group(1), title)

    return EMBED.sub(replace, text), count


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    total = files = 0
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        new, count = migrate(text)
        if count:
            files += 1
            total += count
            if not dry_run:
                path.write_text(new, encoding="utf-8")
        if "videoWrapper" in new:
            print(f"left unconverted: {path.name}", file=sys.stderr)
            return 1
    print(
        f"{'would replace' if dry_run else 'replaced'} {total} embeds in {files} posts"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
