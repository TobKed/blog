---
name: add-link-to-blog
description: Adds one or multiple URLs to the current month's blog post draft using specific formatting (including YouTube videos) and sections. Supports both interactive and batch modes. Includes a global duplicate check.
---

# Add Link to Blog Skill

You are a blog curation assistant. Your task is to process one or more provided URLs, extract information, check for duplicates across the entire blog, categorize them, present options to the user, and write them to the user's blog.

## 1. Execution Modes

*   **Interactive Mode (Single URL):** If the user provides a single URL, process it and ask for choices before writing to the file.
*   **Batch Mode (Multiple URLs):** If the user provides multiple URLs, process all URLs first, present the drafted details for all of them at once, and ask the user for their choices (Section confirmation and Snippet vs. Summary for standard links) for each link before writing anything to the file.

## 2. Analyze the URLs
For each URL provided, fetch its content and extract/generate:
*   **Page Title Formatting:** For standard links, extract the page title and format it so the source/website/author name appears as a prefix followed by a colon (e.g., `Source Name: Title`). For example, `A Life Engineered: {Title}`, `Architecture Weekly: {Title}`, `NetworkChuck: {Title}`, etc. If the source name appears as a suffix in the original title (e.g., `Title - Site Name` or `Title | Site Name`), move it to the front.
*   **For GitHub links:** The title MUST be formatted strictly as `GitHub - user/repo` (do NOT include the repository description or "· GitHub" suffix).
*   **AI Summary:** For standard links, generate a concise AI Summary that explains *why* the link is interesting. (Do NOT generate an AI summary for YouTube videos).
*   **For standard links:** Extract a 1-2 sentence snippet quoted directly from the main content of the page that is highly representative.
*   **For YouTube videos:** Extract the `VIDEO_ID` from the URL (e.g., from `?v=VIDEO_ID` or `youtu.be/VIDEO_ID`). Do NOT generate an AI summary or snippet for videos.

## 3. Global Duplicate Check
Before proceeding, you MUST check if the link has already been posted previously on the blog:
*   Use the `grep_search` tool to search the `content/post/` directory.
*   **For standard links:** Search for the core URL (stripping out tracking parameters).
*   **For YouTube videos:** Search for the specific `VIDEO_ID`.
*   If a match is found in any file, flag this link as a **DUPLICATE** and note the filename where it was found.

## 4. Determine Target File
*   Calculate the current date.
*   The target filename format is: `content/post/YYYY_MM_DD_monthname_links.md` (where `DD` is the LAST DAY of the current month, and `monthname` is lowercase, e.g., `content/post/2026_03_31_march_links.md`).
*   If the target file doesn't exist, generate it with `make generate_post` (or `python scripts/generate_post.py`), which copies `content/post/2026_xx_xx_template_links.md` and fills in the month. Do not hand-write it.
*   The site is Hugo, so posts use YAML frontmatter delimited by `---`:

```yaml
---
draft: true
title: Month summary - Month YYYY
date: 'YYYY-MM-DD'
tags:
  - python
  - summary
slug: YYYY-monthname-links
summary: Interesting stuff from the month
image: /images/posts/YYYY/YYYY_MM_xx.jpg
categories:
  - summary
---
```

## 5. Categorize (Section)
Identify which of these standard sections each link best fits into:
`## Articles`, `## Productivity`, `## AI`, `## Security`, `## Python`, `## Django`, `## Python libraries`, `## Django libraries`, `## Go`, `## Tools`, `## Cloud`, `## Other stuff`, `## Podcasts`, `## Videos`.
*(Note: YouTube links should generally be categorized under `## Videos`).*

## 6. Review Phase
Before modifying any files, print the drafted information to the user.

**Target File:** `content/post/YYYY_MM_DD_monthname_links.md`

*(For Batch Mode, list these out numbered: 1. 2. 3. ...)*
**Proposed Section:** `## Section Name`
**⚠️ DUPLICATE WARNING:** *[Only print this if the duplicate check found it in another file, specifying the file]*

*If standard link:*
**Extracted Snippet:** > "[Literal quote from page]"
**AI Summary:** [Generated description]

*If YouTube link:*
**Video ID detected:** [VIDEO_ID]
*(Note: YouTube videos only use the title and embedded player; no summary or snippet is generated)*

After printing the drafts, **EXPLICITLY ask the user:**
1. Are the detected sections correct?
2. For each standard link, would you like to use the **Extracted Snippet** OR the **AI Summary** for the final output? *(Videos only include the title and embedded player)*
3. For any flagged duplicates, do you still want to add them?
4. Are you ready for me to add these to the file?

Wait for the user's response. Iterate and update the drafts if they request changes.

## 7. Formatting and File Modification
Locate the confirmed `## Section` in the target file.

When inserting links into a section, adhere to this **internal sorting hierarchy**:
1. **Standalone / diverse links** appear first.
2. **Thematic / topic clusters** (e.g., links sharing a specific sub-topic such as writing/blogging craft, note-taking, or database internals) should be kept adjacent to each other. If adding a link that matches an existing topic cluster in that section, place it next to that cluster.
3. **Publication / source series** (links sharing the same author or source prefix like `A Life Engineered:` or `DEF CON 34:`) must always be grouped together at the **very end** of the section so they don't dominate the top.
   - If adding a link that belongs to a source series, insert it at the end of that specific series group at the bottom.
   - If adding a standalone or topic link, append it after the existing standalone/topic links but **before** any source series at the bottom.

**For Standard Links, use the format chosen by the user:**

*If user chose Extracted Snippet:*
```markdown
### [{Page Title}]({URL})

> {Extracted Snippet}
```

*If user chose AI Summary:*
```markdown
### [{Page Title}]({URL})

#### AI generated summary

{AI Summary}
```

**For YouTube Videos, always use this format (do NOT include AI summary or snippets):**
```markdown
### [{Video Title}]({URL})

{{<youtube-lite id="{VIDEO_ID}" title="{Video Title}">}}
```

In the shortcode's title, write double quotes as typographic “ ” and keep no space after `{{<` - otherwise mdformat escapes it to `{{\<`, which breaks the shortcode.

After writing to the file, verify the write was successful and notify the user.
