# Project Overview

This project is a Python script for checking broken links on a website. It's designed to crawl a given URL, identify all internal and external links, and then verify that they are not broken.

The script uses a two-phase approach:

1. **Initial Check with `requests`:** It first uses the `requests` library to quickly check the status of all links. This is fast but may not be accurate for all websites, especially those that rely heavily on JavaScript.
2. **Verification with `selenium`:** For any links that appear to be broken, the script uses `selenium` and a headless Chrome browser to re-check them. This is slower but more reliable, as it can execute JavaScript and render the page like a real browser.

The script also takes screenshots of the pages it checks with `selenium`, which can be helpful for debugging.

# Building and Running

This is a Python script and does not require a formal build process. To run the script, you will need to have Python installed, along with the dependencies listed in `requirements.txt`.

Runs on the host or in CI only, not in the Dev Container (see `.devcontainer/README.md`).

## Key Commands

- **`pip install -r requirements.txt`**: Installs the required Python dependencies.
- **`python test_links.py`**: Runs the link checker.

## How it Works

1. The script starts by crawling the website specified in the `URL` variable in `test_links.py`.
2. It uses the `RequestsLinkVerifier` to find all links on the site and performs an initial check.
3. Any links that fail the initial check are then passed to the `SeleniumChecker`.
4. The `SeleniumChecker` uses a headless Chrome browser to open each link and verify its content. It uses the `selenium_links_registry` in `test_links_registry.py` to know what to look for on each page.
5. The script outputs a JSON file (`invalid_links_YYYYMMDD_HHMM.json`) containing a list of all the broken links it found. It also creates a log file (`test_links_YYYYMMDD_HHMM.log`) and a directory of screenshots.

# Development Conventions

- The main entry point of the script is `test_links.py`.
- Configuration, such as the starting URL and lists of known-to-be-invalid links, is managed in `test_links.py` and `test_links_registry.py`.
- The script is divided into modules with specific responsibilities:
  - `test_links.py`: Main script logic.
  - `test_links_requests.py`: Link checking with `requests`.
  - `test_links_selenium.py`: Link checking with `selenium`.
  - `test_links_registry.py`: Data for the link checkers.
  - `logger.py`: Logging configuration.
- The script is designed to be run from the command line.
