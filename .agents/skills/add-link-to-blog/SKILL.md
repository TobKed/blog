---
name: add-link-to-blog
description: Adds one or multiple URLs to the current month's blog post draft using specific formatting (including YouTube videos) and sections. Supports both interactive and batch modes. Includes a global duplicate check.
---

# Add Link to Blog Skill

You are a blog curation assistant. Your task is to process one or more provided URLs, extract information, check for duplicates across the entire blog, categorize them, present options to the user, and write them to the user's blog.

## 1. Execution Modes

*   **Interactive Mode (Single URL):** If the user provides a single URL, process it and ask for choices before writing to the file.
*   **Batch Mode (Multiple URLs):** If the user provides multiple URLs, process all URLs first, present the drafted details for all of them at once, and ask the user for their choices (Section confirmation and Snippet vs. Summary) for each link before writing anything to the file.

## 2. Analyze the URLs
For each URL provided, fetch its content and extract/generate:
*   **Page Title:** For standard links, use the page title. For GitHub links, the title MUST be formatted strictly as `GitHub - user/repo` (do NOT include the repository description or "· GitHub" suffix).
*   **AI Summary:** Generate a concise AI Summary that explains *why* the link is interesting.
*   **For standard links:** Extract a 1-2 sentence snippet quoted directly from the main content of the page that is highly representative.
*   **For YouTube videos:** Extract the `VIDEO_ID` from the URL (e.g., from `?v=VIDEO_ID` or `youtu.be/VIDEO_ID`).

## 3. Global Duplicate Check
Before proceeding, you MUST check if the link has already been posted previously on the blog:
*   Use the `grep_search` tool to search the `content/posts/` directory.
*   **For standard links:** Search for the core URL (stripping out tracking parameters).
*   **For YouTube videos:** Search for the specific `VIDEO_ID`.
*   If a match is found in any file, flag this link as a **DUPLICATE** and note the filename where it was found.

## 4. Determine Target File
*   Calculate the current date.
*   The target filename format is: `content/posts/YYYY_MM_DD_monthname_links.md` (where `DD` is the LAST DAY of the current month, and `monthname` is lowercase, e.g., `content/posts/2026_03_31_march_links.md`).
*   If the target file doesn't exist, create it with standard frontmatter (`Title: Month summary - Month YYYY`, `Date`, `Category: summary`, `Status: draft`, etc.) and basic section headers.

## 5. Categorize (Section)
Identify which of these standard sections each link best fits into:
`## Articles`, `## Productivity`, `## AI`, `## Security`, `## Python`, `## Django`, `## Python libraries`, `## Django libraries`, `## Go`, `## Tools`, `## Cloud`, `## Other stuff`, `## Podcasts`, `## Videos`.
*(Note: YouTube links should generally be categorized under `## Videos`).*

## 6. Review Phase
Before modifying any files, print the drafted information to the user.

**Target File:** `content/posts/YYYY_MM_DD_monthname_links.md`

*(For Batch Mode, list these out numbered: 1. 2. 3. ...)*
**Proposed Section:** `## Section Name`
**⚠️ DUPLICATE WARNING:** *[Only print this if the duplicate check found it in another file, specifying the file]*

*If standard link:*
**Extracted Snippet:** > "[Literal quote from page]"
**AI Summary:** [Generated description]

*If YouTube link:*
**Video ID detected:** [VIDEO_ID]
**AI Summary:** [Generated description]

After printing the drafts, **EXPLICITLY ask the user:**
1. Are the detected sections correct?
2. For each link, would you like to use the **Extracted Snippet** OR the **AI Summary** for the final output? *(If it's a YouTube video, it will always be the summary)*
3. For any flagged duplicates, do you still want to add them?
4. Are you ready for me to add these to the file?

Wait for the user's response. Iterate and update the drafts if they request changes.

## 7. Formatting and File Modification
Locate the confirmed `## Section` in the target file. Append the markdown directly under the section header.

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

**For YouTube Videos, always use this format:**
```markdown
### [{Video Title}]({URL})

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/{VIDEO_ID}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### AI generated summary

{AI Summary}
```

After writing to the file, verify the write was successful and notify the user.
