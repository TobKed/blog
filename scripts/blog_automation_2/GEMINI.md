# Project Overview

This project is a Python-based command-line tool for automating the process of adding links to markdown-based blog posts. It analyzes a given URL, extracts its title, and generates a summary and relevant tags using an AI model. It then formats this information into a markdown snippet and inserts it into the appropriate section of a specified blog post. The tool is designed to streamline the curation of content for a blog.

## Main Technologies

- **Python 3**: The core language for all scripts.
- **LangChain & OpenAI**: Used for content analysis and generation of summaries and tags.
- **Loguru**: For logging and monitoring script execution.
- **python-dotenv**: To manage environment variables, particularly API keys.
- **crawl4ai**: For crawling and extracting web page content.

## Architecture

The project has been refactored for better performance, maintainability, and robustness. The architecture is now centered around a core processing module that is utilized by both the bulk and single-link entry points.

- **`bulk_process_links.py`**: A lightweight command-line script that reads a list of URLs from a file and processes them in batch. It imports and calls the core processing logic directly, making it highly efficient.
- **`insert_links_tool.py`**: A simple command-line wrapper for processing a single link. It takes a markdown file path and a URL as input and uses the same core logic as the bulk processor.
- **`config.py`**: Handles configuration, including command-line argument parsing, environment variable loading, and path setup.
- **`link_processing/`**: A directory containing the core logic for the tool.
  - **`core.py`**: The heart of the application. Contains the `process_single_link` function that orchestrates the entire process of analyzing a URL, checking for duplicates, generating content, and inserting it into the markdown file.
  - **`url_analyser.py`**: Uses `crawl4ai` and an LLM to analyze a URL and extract its title, summary, and other metadata.
  - **`file_updater.py`**: Contains functions for reading and writing to the markdown files, including inserting the new link content into the correct section.
  - **`link_registry.py`**: Manages a registry of all links that have been added to the blog to prevent duplicates. It scans the existing blog posts to build an initial database of links.
  - **`url_processor.py`**: Contains helper functions for processing and cleaning URLs.
  - **`markdown_formatter.py`**: A modular system for formatting the extracted link information into different markdown structures (e.g., for articles, YouTube videos, and playlists).
  - **`data_models.py`**: Defines the Pydantic data models used throughout the application.
  - **`exceptions.py`**: Defines custom exceptions for specific error conditions, such as duplicate links or missing sections.

# Building and Running

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY="your-api-key"
   ```

## Running the tool

There are two main ways to run the tool:

1. **Bulk processing**:
   Create a markdown file (e.g., `batch_links.md`) with the following format:

   ```markdown
   Target Post: content/posts/your-post.md

   https://example.com/link1
   https://example.com/link2
   ```

   Then run the `bulk_process_links.py` script:

   ```bash
   python bulk_process_links.py batch_links.md
   ```

2. **Single link insertion**:
   To insert a single link, run the `insert_links_tool.py` script directly:

   ```bash
   python insert_links_tool.py content/posts/your-post.md "https://example.com/link"
   ```

# Development Conventions

- **Logging**: The project uses `loguru` for logging. Verbose logging can be enabled with the `--verbose` flag.
- **Error Handling**: The application now uses a robust, exception-based error handling system. Custom exceptions are defined in `link_processing/exceptions.py` and are raised for specific failure scenarios (e.g., `DuplicateLinkError`, `SectionNotFoundError`).
- **Modularity**: The core logic is highly modular and separated into distinct components within the `link_processing` directory, promoting code reuse and maintainability.
- **Testing**: The project includes a suite of automated tests using `pytest`. Tests are located in the `tests/` directory and cover the core logic, utility functions, and markdown formatting. To run the tests, install the development dependencies (`pip install -r requirements-dev.txt`) and then run `pytest`.
- **Configuration**: Project configuration is centralized in the `config.py` module.
