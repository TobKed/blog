# Design Spec: Quick CLI for Adding Links

## Goal
Provide a user-friendly, friction-free way to add a curated link to the current month's blog post draft using a simple `make` command.

## Approach Selected (Option C)
A parameterized `make` target (`make add-link URL="https://..."`) that automatically calculates the current month's link post and delegates the actual processing to the existing `insert_links_tool.py` script.

## Components

### 1. `scripts/blog_automation_2/get_current_month_post.py`
A new, small Python utility script.
**Responsibility:** Determine the absolute or relative path to the current month's link post based on the current date and the blog's naming convention.
**Logic:**
- Get current date (e.g., 2026-03-15).
- Construct the expected filename format: `content/posts/YYYY_MM_DD_month_links.md`.
  *(Note: The `DD` in the filename is typically the last day of the month for monthly links, e.g., `2026_03_31_march_links.md`)*
- Calculate the last day of the current month.
- Map the current month number to its English lowercase name (e.g., 3 -> `march`).
- Return the full constructed path. If the file doesn't exist, it can either create it with a basic template or just return the path for `insert_links_tool.py` to handle/error out on. *We will just return the path and let the user create the template if missing, or we can add a flag to auto-scaffold it.*

### 2. `Makefile` Update
Add a new target:
```makefile
.PHONY: add-link
add-link: ## add a link to the current month's post. Usage: make add-link URL="https://..."
	@if [ -z "$(URL)" ]; then \
		echo "Error: URL is required. Usage: make add-link URL=\"https://...\""; \
		exit 1; \
	fi
	@POST_PATH=$$($(PY) scripts/blog_automation_2/get_current_month_post.py); \
	echo "Adding link to $$POST_PATH..."; \
	source scripts/blog_automation_2/venv/bin/activate && \
	$(PY) scripts/blog_automation_2/insert_links_tool.py "$$POST_PATH" "$(URL)"
```

## Data Flow
1. User runs `make add-link URL="https://example.com/foo"` from the project root.
2. Make validates that `URL` is provided.
3. Make executes `get_current_month_post.py` to get the string `content/posts/2026_03_31_march_links.md`.
4. Make sources the virtual environment where `crawl4ai` and dependencies are installed.
5. Make executes `insert_links_tool.py content/posts/2026_03_31_march_links.md "https://example.com/foo"`.
6. The existing tool fetches the content, generates LLM summaries, and appends the markdown to the file.

## Edge Cases
- **Post Doesn't Exist Yet:** `get_current_month_post.py` will accurately calculate what the filename *should* be. If `insert_links_tool.py` fails on a non-existent file, we will add a small check in the bash script to ensure the file exists beforehand, or update `insert_links_tool.py` to handle it.
- **Wrong Python Environment:** The `Makefile` explicitly sources the `scripts/blog_automation_2/venv` before running the tool to ensure all heavy ML/LangChain dependencies are available without polluting the global `make regenerate` environment.

## Testing Plan
1. Run `make add-link URL="https://simonwillison.net/2024/Mar/22/claude-3-haiku/"`
2. Verify it accurately calculates `content/posts/2026_03_31_march_links.md`.
3. Verify the link is appended correctly to the file.
