# Interactive CLI Add-Link Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an interactive `make add-link "URL"` command driven entirely by a new Gemini skill that extracts content and adds it to the appropriate section of the current month's blog post.

**Architecture:** A Makefile target will launch the Gemini CLI in chat mode, explicitly loading a new skill. The skill instructs Gemini how to fetch the URL, what information to extract (meta description, snippet, AI summary, category), how to calculate the target file path, and how to verify with the user before appending the markdown to the correct section.

**Tech Stack:** Makefile, Gemini CLI, Markdown

______________________________________________________________________

## Chunk 1: Creating the Gemini Skill

**Files:**

- Create: `.agents/skills/add-link-to-blog/SKILL.md`

- \[ \] **Step 1: Write the skill file**

Create the directory if it doesn't exist: `mkdir -p .agents/skills/add-link-to-blog`

File: `.agents/skills/add-link-to-blog/SKILL.md`

````markdown
---
name: add-link-to-blog
description: Interactively adds a URL link to the current month's blog post draft using specific formatting and sections.
---

# Add Link to Blog Skill

You are a blog curation assistant. Your task is to process a provided URL, extract information, categorize it, get user approval, and then write it to the user's blog.

## 1. Analyze the URL
Fetch the content of the provided URL. Extract:
- The Page Title.
- The raw `<meta name="description">` (or equivalent).
- A 1-2 sentence snippet quoted directly from the main content of the page that is highly representative.
- Generate a concise AI Summary that explains *why* the link is interesting.

## 2. Determine Target File
- Calculate the current date.
- The target filename format is: `content/posts/YYYY_MM_DD_monthname_links.md` (where `DD` is the LAST DAY of the current month, and `monthname` is lowercase, e.g., `content/posts/2026_03_31_march_links.md`).

## 3. Categorize (Section)
Identify which of these standard sections the link best fits into:
`## Articles`, `## Productivity`, `## AI`, `## Security`, `## Python`, `## Django`, `## Python libraries`, `## Django libraries`, `## Go`, `## Tools`, `## Cloud`, `## Other stuff`, `## Podcasts`, `## Videos`.

## 4. Interactive Review Phase
Print the extracted/drafted information to the user exactly like this:

**Target File:** `content/posts/YYYY_MM_DD_monthname_links.md`
**Proposed Section:** `## Section Name`

**Page Meta Description:**
> [Raw description from site]

**Extracted Snippet:**
> "[Literal quote from page]"

**AI Summary:**
[Generated description]

After printing this, **EXPLICITLY ask the user:**
1. Is the detected section (`## Section Name`) correct, or should it be changed?
2. Does the AI Summary look good, or should it be made shorter/modified?
3. Are you ready for me to add this to the file?

Wait for the user's response. Iterate and update the draft if they request changes. Do NOT touch any files until they explicitly approve.

## 5. File Modification (Post-Approval)
Once the user approves:
1. Check if the target file exists. If it doesn't exist, create it with standard frontmatter (Title: Month summary - Month YYYY, etc.) and basic section headers.
2. Locate the confirmed `## Section` in the file.
3. Append the final markdown directly under that section header in this format:
```markdown
### [{Page Title}]({URL})

> {Extracted Snippet}

{AI Summary}
````

4. Verify the write was successful and let the user know. Exit the task.

````

- [ ] **Step 2: Run a quick syntax check (optional)**
Ensure the markdown file was created correctly.

- [ ] **Step 3: Commit**

```bash
git add .agents/skills/add-link-to-blog/SKILL.md
git commit -m "feat(skill): add add-link-to-blog skill"
````

## Chunk 2: Makefile Integration

**Files:**

- Modify: `Makefile`

- \[ \] **Step 1: Update the Makefile**

Append the following to the `Makefile` (ensure proper tab indentation):

```makefile
.PHONY: add-link
add-link: ## Interactively add a link to the current month's post. Usage: make add-link "https://..."
	@URL="$(filter-out $@,$(MAKECMDGOALS))"; \
	if [ -z "$$URL" ]; then \
		echo "Error: URL is required. Usage: make add-link \"https://...\""; \
		exit 1; \
	fi; \
	echo "Launching Gemini to process $$URL..."; \
	gemini chat --message "I want to add this link to my blog: $$URL. Please use the add-link-to-blog skill to process it."

%:
	@:
```

- \[ \] **Step 2: Commit**

```bash
git add Makefile
git commit -m "feat: add make add-link interactive target"
```

## Chunk 3: Testing & Verification

- \[ \] **Step 1: Test missing URL error**

Run: `make add-link`
Expected: `Error: URL is required. Usage: make add-link "https://..."` and exit code 1.

- \[ \] **Step 2: Test Interactive Execution**

Run: `make add-link "https://simonwillison.net/20...haiku/"` (or similar valid URL)
Expected: Gemini opens, loads the skill, fetches the content, and outputs the proposed draft and section, then pauses for confirmation.
Action: Approve the draft. Verify that `content/posts/2026_03_31_march_links.md` was correctly modified and the snippet is under the correct section header.
