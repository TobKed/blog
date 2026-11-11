---
name: add-link-to-blog
description: Use when adding one or more URLs or YouTube videos to the blog (monthly round-up posts and/or curated topic pages in content/pages/).
---

# Add Link to Blog Skill

You are a blog curation assistant. Take one or more URLs, check them against everything already on the blog, draft entries for the current month's round-up post (and, sparingly, for curated topic pages), get the user's sign-off, then write them.

The user usually pastes a batch of links and wants a quick, scannable review, not an essay per link. Keep every message to the user compact and spend words only where a decision is needed.

Work directly in the main checkout on `master`: no worktree, no branch. The draft monthly post is edited there continuously (often with unpushed commits and `make serve` running), so a branch would start from a stale copy and need merging back. This applies only to adding links; other work in this repo may use worktrees and branches.

## 1. Normalize and dedupe

Run the bundled script on all input URLs first:

```bash
python3 .agents/skills/add-link-to-blog/scripts/find_links.py URL [URL ...]
```

It prints each URL in its cleaned form (fragments such as `#install` and tracking parameters such as `utm_*` or `si` removed) and lists every `file:line` in `content/post/` and `content/pages/` where it already appears. YouTube links are compared by video ID, so `youtu.be/ID`, `watch?v=ID` and `{{<youtube-lite id="ID">}}` all match. It also flags URLs repeated within the input itself.

- Always write the **cleaned** URL into the blog, so the same page never ends up under two spellings.
- A hit in `content/post/` means it was already shared in a monthly post: flag it, and propose skipping it unless the user says otherwise.
- A hit in `content/pages/<page>.md` means it is already on that topic page: never add it there again.
- An input repeated within the batch is silently collapsed to one entry; mention it in one line.
- If a link is intentionally repeated within `content/post/` (e.g. discussed in `## Some thoughts` and listed below), mark the inline mention line with `<!-- dup-ok -->` so `make check_links` skips it.

## 2. Gather details for each link

**Standard links:**
- **Title:** prefix with the source so readers can tell who wrote it: `Source Name: Title` (e.g. `Architecture Weekly: {Title}`, `Daniel Miessler: {Title}`). If the source sits at the end of the page title (`Title | Site`), move it to the front. For a product homepage use `Product: tagline` (e.g. `ntfy: Send push notifications to your phone via PUT/POST`).
- **GitHub repos:** `GitHub - owner/repo` in monthly posts (no description, no "· GitHub" suffix); `owner/repo` on topic pages.
- **Snippet:** a 1-2 sentence quote, copied **verbatim** from the page, that shows what the link is about. Page fetchers backed by a small model sometimes paraphrase; if a quote looks smoothed over, confirm it against the raw page (`curl -sL URL | grep -F "phrase"`) before using it.

**YouTube videos:**
- Get the title and channel from oEmbed, which is reliable and needs no browser:
  `curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json"`
- Use the video title as-is. Append ` - Channel` only when the title gives no hint of who made it (a talk title that already names the speaker or event needs nothing).

**AI summaries are opt-in.** Recent posts use snippets exclusively, so default to the snippet and only write a `#### AI generated summary` block when the user asks for one (or when the page has no quotable sentence, in which case say so in the review).

## 3. Choose targets

### Monthly post
- Target: `content/post/YYYY_MM_DD_monthname_links.md`, where `DD` is the last day of the current month (e.g. `content/post/2026_03_31_march_links.md`).
- If it doesn't exist, create it with `make generate_post` (or `python scripts/generate_post.py`) rather than by hand, so front matter and section headers match the template.
- Pick one section: `## Articles`, `## Productivity`, `## AI`, `## Security`, `## Python`, `## Django`, `## Python libraries`, `## Django libraries`, `## Go`, `## Tools`, `## Cloud`, `## Other stuff`, `## Podcasts`, `## Videos`. YouTube goes under `## Videos`, or `## 🇵🇱 Polish Corner 🇵🇱` if in Polish.

### Curated topic pages (be conservative)
Topic pages are evergreen reference lists, so they should only collect things a reader would still reach for in a year: repositories, tools, skill collections, curated lists, books, and the occasional landmark article or talk. One-off blog posts, news, launch announcements and most videos belong in the monthly post only.

Read `content/pages/AGENTS.md` for the page catalog, the `##` sections of each page and the entry format. Propose a topic page only when the link clearly fits; when in doubt, leave it out and let the user add it.

## 4. Review with the user

Print one compact table covering every link, then short notes only for the links that need a decision:

| # | Entry title | Monthly post section | Topic page |
|---|---|---|---|
| 1 | GitHub - owner/repo | `## AI` | `ai.md` → `## Skills` |
| 2 | Source: Title | `## Tools` | - |

Below the table, list only:
- **Duplicates / skipped:** which inputs were already on the blog (with file) or repeated within the batch.
- **Uncertain calls:** a section or topic page you are unsure about, with your recommendation.
- **Topic page entries:** the proposed `- **[Title](URL)**: one sentence` line for each.

Then ask, in one short list: are the targets and sections right, should the duplicates be skipped, and anything to change. Don't print snippets yet: they come in the next step, where the user sees them in place.

## 5. Show the exact changes, then write

Once the user confirms targets, show the exact Markdown that will be inserted, grouped by file and section, with where it goes (e.g. "after the Nick Taylor entry"). Call out any small judgment calls you made (a dropped fragment, an appended channel name). Write only after the user approves.

### Monthly post formats

Standard link (default):
```markdown
### [{Title}]({URL})

> {Snippet}
```

Standard link with AI summary (only when asked):
```markdown
### [{Title}]({URL})

#### AI generated summary

{Summary}
```

YouTube video (no snippet or summary):
```markdown
### [{Video Title}]({URL})

{{<youtube-lite id="{VIDEO_ID}" title="{Video Title}">}}
```

In the shortcode title, write double quotes as typographic “ ” and keep no space after `{{<`; otherwise mdformat escapes it to `{{\<`, which breaks the shortcode.

### Ordering within a monthly post section
1. Standalone links come first.
2. Links on a shared sub-topic (e.g. agent orchestration, note-taking) sit next to each other; add a matching link beside its cluster.
3. Source series (several links with the same prefix, like `Langfuse:` or `DEF CON 34:`) go together at the **end** of the section so one source doesn't dominate the top. Add a series link at the end of its group; add anything else before the series.

### Topic page entries
Follow `content/pages/AGENTS.md`: `- **[{Title}]({URL})**: {one sentence}`, inserted in case-insensitive alphabetical order by title within the section, replacing `_(No resources yet)_` if present.

## 6. Verify

After writing:
1. `pre-commit run --files <changed files>` must pass. It catches mdformat rewriting a shortcode or list.
2. Rerun `find_links.py` on the added URLs: each should now appear exactly once per target file.
3. Report what was added where, in a few lines, and anything skipped.
