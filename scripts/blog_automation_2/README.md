# Blog Link Automation Tool

A Python-based command-line tool to streamline the process of curating and adding links to markdown-based blog posts. This tool analyzes a given URL, uses an AI model to generate a title, summary, and relevant tags, and then formats this information into a markdown snippet. Finally, it intelligently inserts the snippet into the appropriate section of a specified blog post.

## Key Features

- **AI-Powered Content Analysis**: Leverages LangChain and OpenAI to extract titles and generate summaries for any given URL.
- **Handles Multiple Link Types**: Automatically detects and formats different types of links, including standard articles, YouTube videos (with embedded player), and YouTube playlists.
- **Duplicate Prevention**: Scans all existing blog posts to maintain a registry of links, preventing the same URL from being added twice.
- **Intelligent Section Insertion**: Analyzes the content to determine the most appropriate section (e.g., "Python", "AI", "Articles") and inserts the link there.
- **Bulk Processing**: Efficiently process a list of URLs from a file in a single run, with a generated report of successes and failures.
- **Robust and Efficient**: Refactored for high performance, eliminating slow sub-process calls and incorporating a robust, exception-based error handling system.

## Architecture

The project is designed with a modular and maintainable architecture:

- **`link_processing/`**: A directory containing the core logic of the application.
  - **`core.py`**: The heart of the application, containing the main `process_single_link` function.
  - **`url_analyser.py`**: Uses `crawl4ai` and an LLM to analyze a URL and extract its metadata.
  - **`file_updater.py`**: Handles reading and writing to the markdown files.
  - **`link_registry.py`**: Manages the database of all links to prevent duplicates.
  - **`markdown_formatter.py`**: A modular system for formatting the extracted link information into different markdown structures.
  - **`data_models.py`**: Defines the Pydantic data models used throughout the application.
  - **`exceptions.py`**: Defines custom exceptions for specific error conditions.
- **`insert_links_tool.py`**: A command-line wrapper for processing a single link.
- **`bulk_process_links.py`**: The entry point for processing a batch of links from a file.
- **`config.py`**: Handles configuration, including command-line arguments and environment variables.

## Setup and Installation

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the project root by copying the example file:
    ```bash
    cp .env.example .env
    ```
    Then, edit the `.env` file and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your-api-key"
    ```

## Usage

There are two ways to run the tool:

### 1. Single Link Insertion

To insert a single link into a blog post, use the `insert_links_tool.py` script.

**Syntax:**
```bash
python insert_links_tool.py <path_to_markdown_file> "<url_to_process>"
```

**Example:**
```bash
python insert_links_tool.py content/posts/my-awesome-post.md "https://example.com/cool-article"
```
You can also process multiple URLs in one go:
```bash
python insert_links_tool.py content/posts/my-awesome-post.md "https://example.com/article-1" "https://example.com/article-2"
```

**More Examples:**
```bash
# Insert a single link with verbose output
python insert_links_tool.py content/posts/2025_05_test.md "https://www.doliver.org/articles/rss-as-a-skill" --verbose

# Insert multiple links at once
python insert_links_tool.py content/posts/2025_05_test.md "https://csirmazbendeguz.github.io/2025/04/15/you-dont-need-composite-primary-keys.html" "https://djangochat.com/episodes/michael-kennedy" --verbose

# Example with YouTube links
python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/watch?v=wz0GQbkrr1Q" "https://adamj.eu/tech/2025/04/07/django-whats-new-5.2/" "https://youtu.be/oP49EHjMTHc" --verbose

# Example with YouTube playlist and mixed links
python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/playlist?list=PL0MRiRrXAvRiSmPn_LDdhDbtZwu6g4xct/" "https://www.youtube.com/watch?v=-Zp5ffZDaRc" "https://m.youtube.com/watch?v=CIBmVXteOcI" "https://den.dev/blog/pihole/" --verbose
```

### 2. Bulk Processing

To process a batch of links from a file, use the `bulk_process_links.py` script.

1.  Create a markdown file (e.g., `batch_links.md`) with the following format. The first line must specify the target post, followed by the URLs, each on a new line.

    ```markdown
    Target Post: content/posts/my-awesome-post.md

    https://example.com/link1
    https://example.com/link2
    https://youtube.com/watch?v=somevideo
    ```

2.  Run the script:
    ```bash
    python bulk_process_links.py batch_links.md
    ```
    A report file (`batch_links_report.md`) will be generated in the same directory, summarizing which links were added and which failed.

## Development and Testing

This project includes a suite of automated tests using `pytest`.

1.  **Install development dependencies:**
    ```bash
    pip install -r requirements-dev.txt
    ```

2.  **Run tests:**
    To ensure all components are working correctly, run the test suite from the project root:
    ```bash
    PYTHONPATH=. pytest
    ```
