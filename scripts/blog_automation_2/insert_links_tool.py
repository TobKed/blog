#!/usr/bin/env python3
"""
Main CLI script to analyze URLs, generate descriptions and categories,
and insert them into a markdown blog post using a CrewAI-based system.

Assumes the following project structure:
project_root/
├── scripts/
│   ├── insert_links_tool.py  (this script)
│   └── link_processing/
│   └── prompts/
├── content/
│   └── posts/
├── .env
└── requirements.txt
"""
import argparse
import os
import sys
from pathlib import Path
from typing import List

from dotenv import load_dotenv

# --- Path Setup ---
# Ensure the script can find the link_processing module
try:
    # This assumes the script is in project_root/scripts/
    # SCRIPT_DIR = Path(__file__).resolve().parent
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = SCRIPT_DIR.parent.parent
    sys.path.append(str(PROJECT_ROOT))  # Add project root to Python path
    # print(f"Project root added to path: {PROJECT_ROOT}")
except NameError:
    # Fallback if __file__ is not defined (e.g., in some interactive environments)
    PROJECT_ROOT = Path.cwd()
    # SCRIPT_DIR = PROJECT_ROOT / "scripts" # Assuming standard structure
    SCRIPT_DIR = (
        PROJECT_ROOT / "scripts" / "blog_automation_2"
    )  # Assuming standard structure
    # print(f"Warning: __file__ not defined. Assuming project root: {PROJECT_ROOT}")
    if not (SCRIPT_DIR / "link_processing").exists():
        print(
            "Error: Could not reliably find the 'link_processing' directory. "
            "Please run from the project root or ensure script is in 'scripts/' subdir.",
            file=sys.stderr,
        )
        sys.exit(1)

from link_processing.crew import LinkProcessingCrew
from link_processing.file_updater import (
    get_available_sections,
    insert_link_into_markdown_file,
)

# Load environment variables from .env file in the project root
# dotenv_path = PROJECT_ROOT / ".env"
dotenv_path = SCRIPT_DIR / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
    # print(f"Loaded .env file from: {dotenv_path}")
else:
    print(
        f"Warning: .env file not found at {dotenv_path}. API keys should be set in environment."
    )


def main():
    """Main function to orchestrate link processing and insertion."""
    parser = argparse.ArgumentParser(
        description="Analyzes URLs, generates descriptions and categories, "
        "and inserts them into a markdown blog post.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "target_markdown_file",
        type=str,  # Keep as string to allow relative paths from project_root
        help="Path to the target markdown blog post file (relative to project root, e.g., content/posts/file.md).",
    )
    parser.add_argument(
        "urls",
        type=str,
        nargs="+",
        help="One or more URLs to process.",
    )
    parser.add_argument(
        "--llm-provider",
        choices=["openai"],  # Add more as implemented (e.g., "anthropic")
        default=os.getenv("DEFAULT_LLM_PROVIDER", "openai"),
        help="Specify the LLM provider to use. Can also be set via DEFAULT_LLM_PROVIDER in .env.",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default=os.getenv("DEFAULT_MODEL_NAME"),  # e.g. OPENAI_MODEL_NAME from .env
        help="Specify the model name for the LLM provider. Overrides environment variables like OPENAI_MODEL_NAME.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output from the CrewAI tasks.",
    )

    args = parser.parse_args()

    # Resolve target markdown file path relative to project root
    target_markdown_path = PROJECT_ROOT / args.target_markdown_file
    if not target_markdown_path.is_file():
        print(
            f"Error: Target markdown file not found: {target_markdown_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Processing {len(args.urls)} URL(s) for '{target_markdown_path.name}'...")

    # 1. Get available sections from the target markdown file
    available_sections = get_available_sections(target_markdown_path)
    if not available_sections:
        print(
            f"Warning: Could not find any H2 sections (e.g., '## Section Name') in {target_markdown_path}. "
            "Categorization might be limited or default to 'Other stuff'.",
            file=sys.stderr,
        )
        # Proceeding, as "Other stuff" can be a fallback.
    else:
        print(f"Available sections in blog: {available_sections}")

    # 2. Initialize and run the CrewAI crew for each URL
    try:
        link_crew = LinkProcessingCrew(
            llm_provider=args.llm_provider,
            model_name=args.model_name,
            verbose_level=2 if args.verbose else 0,
        )
    except ValueError as e:
        print(f"Error initializing LinkProcessingCrew: {e}", file=sys.stderr)
        sys.exit(1)

    successful_insertions = 0
    for url in args.urls:
        print(f"\n--- Processing URL: {url} ---")
        try:
            processed_data = link_crew.process_url(url, available_sections)

            if (
                processed_data
                and processed_data.get("category")
                and processed_data.get("markdown_string")
            ):
                print(f"  Title: {processed_data['title']}")
                print(f"  Description: {processed_data['description']}")
                print(f"  Keywords: {processed_data.get('keywords', 'N/A')}")
                print(f"  Categorized under: {processed_data['category']}")

                # 3. Insert into markdown file
                if insert_link_into_markdown_file(
                    markdown_file_path=target_markdown_path,
                    section_name=processed_data["category"],
                    markdown_to_insert=processed_data["markdown_string"],
                ):
                    print(f"  Successfully inserted into '{target_markdown_path.name}'")
                    successful_insertions += 1
                else:
                    print(f"  Failed to insert link for {url} into the markdown file.")
            elif (
                processed_data is None
            ):  # Explicitly None means an error occurred in crew
                print(f"  Processing failed for URL {url} within the crew.")
            else:
                print(
                    f"  Could not fully process URL {url}. Missing essential data. Skipping insertion. Data: {processed_data}"
                )

        except Exception as e:
            print(
                f"An unexpected error occurred while processing URL {url}: {e}",
                file=sys.stderr,
            )
            # Consider adding more robust error handling or logging (e.g., traceback)

    print(f"\n--- Finished processing ---")
    print(f"{successful_insertions} link(s) successfully processed and inserted.")
    if successful_insertions < len(args.urls):
        print(
            f"{len(args.urls) - successful_insertions} link(s) could not be processed or inserted fully."
        )


if __name__ == "__main__":
    main()
