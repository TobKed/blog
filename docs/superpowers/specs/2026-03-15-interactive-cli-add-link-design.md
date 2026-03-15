# Design Spec: Interactive CLI for Adding Links via Gemini Skill

## Goal

Provide a user-friendly, interactive way to add a curated link to the current month's blog post draft using a simple `make` command powered completely by a Gemini CLI skill.

## Approach Selected

An interactive `make` target (`make add-link "https://..."`) that launches a Gemini CLI `chat` session equipped with a specific "Add Link to Blog" skill. Gemini will fetch the content, draft the markdown snippet, present it to the user for review alongside the raw page description, and then save it to the correct section of the correct file.

## Components

### 1. `Makefile` Update

Add a new target that invokes the Gemini CLI. The URL will be passed directly as the first argument to `make add-link` rather than using a named `URL=` variable.

```makefile
.PHONY: add-link
# Usage: make add-link "https://..."
# Note: In Make, passing loose arguments requires a workaround to prevent Make from interpreting the URL as a target.
# A common trick:
add-link: ## Interactively add a link to the current month's post. Usage: make add-link "https://..."
	@URL="$(filter-out $@,$(MAKECMDGOALS))"; \
	if [ -z "$$URL" ]; then \
		echo "Error: URL is required. Usage: make add-link \"https://...\""; \
		exit 1; \
	fi; \
	echo "Launching Gemini to process $$URL..."; \
	gemini chat --message "I want to add this link to my blog: $$URL. Please use the add-link-to-blog skill to process it."

# Catch-all target to silently ignore the URL argument so Make doesn't complain "No rule to make target 'https://...'"
%:
	@:
```

### 2. New Gemini Skill: `.agents/skills/add-link-to-blog/SKILL.md`

Create a new skill that tells Gemini exactly how to handle this request.

**Skill Responsibilities & Workflow:**

1. **Analyze the URL:** Fetch the content of the provided URL.
2. **Determine Target File:**
   - Calculate the current date.
   - Determine the filename for the current month's link post: `content/posts/YYYY_MM_DD_monthname_links.md` (where `DD` is the last day of the month).
3. **Section Classification:**
   - Identify which of the following standard blog sections the link best belongs in:
     - `## Articles`
     - `## Productivity`
     - `## AI`
     - `## Security`
     - `## Python`
     - `## Django`
     - `## Python libraries`
     - `## Django libraries`
     - `## Go`
     - `## Tools`
     - `## Cloud`
     - `## Other stuff`
     - `## Podcasts`
     - `## Videos`
4. **Draft Content Generation:**
   - Extract the raw `<meta name="description">` or equivalent from the webpage.
   - Find a highly relevant 1-2 sentence snippet quoted directly from the page text.
   - Generate a custom AI Summary (if necessary) to explain *why* the link is interesting or to contextualize it.
   - Generate 3-5 relevant tags.
5. **Interactive Review Phase:**
   - Print the following information to the terminal for the user to review:
     ```markdown
     **Target File:** `content/posts/YYYY_MM_DD_monthname_links.md`
     **Proposed Section:** `## Section Name`

     **Page Meta Description:**
     > [Raw description from site]

     **Extracted Snippet:**
     > "[Literal quote from page]"

     **AI Summary:**
     [Generated description]

     **Tags:** tag1, tag2, tag3
     ```
   - EXPLICITLY ask the user the following questions:
     1. *Is the detected section (`## Section Name`) correct, or should it be changed?*
     2. *If an AI Summary was provided, does it look good, or should it be made shorter/modified?*
     3. *Are you ready for me to add this to the file?*
6. **File Modification:**
   - Once the user approves or finishes tweaks, check if the calculated target file exists. (If not, prompt user or create from template).
   - Find the specified `## Section` in the file.
   - Append the finalized markdown snippet (formatting: Title linked to URL, snippet/summary blockquote, tags) directly under that section.
   - Exit the task.

## Data Flow

1. User runs `make add-link "https://example.com/foo"`.
2. `make` starts a `gemini chat` session requesting the skill.
3. Gemini loads the `add-link-to-blog` skill.
4. Gemini fetches the URL, drafts the content, and categorizes it.
5. Gemini prints the draft info (Meta Description, Snippet, AI Summary, Section) to the terminal.
6. Gemini asks the user for approval on the section and the AI summary length.
7. User reviews and iterates (e.g., "Change section to Python", "Make AI desc shorter", "Looks good").
8. Upon approval, Gemini injects the markdown under the appropriate `## Section` in the `content/posts/..._links.md` file.

## Deletion of Old Code

Since this replaces the existing tool entirely, we can delete the `scripts/blog_automation_2/` directory and related Python scripts/tests, as Gemini is now orchestrating the whole flow natively.

## Testing Plan

1. Apply Makefile changes and create the skill file.
2. Run `make add-link "https://simonwillison.net/2024/Mar/22/claude-3-haiku/"`.
3. Verify Gemini fetches the link and presents the draft including Meta Description, Snippet, and AI Summary.
4. Verify Gemini correctly guesses the section (e.g., `## AI`).
5. Tell Gemini to make the AI description shorter.
6. Approve the final draft.
7. Open the appropriate `content/posts/..._links.md` file and verify the markdown was inserted under the correct section heading.
