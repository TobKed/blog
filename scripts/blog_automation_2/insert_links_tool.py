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
import sys
from pathlib import Path
from typing import List

from config import (
    CommandLineArgs,
    load_environment,
    parse_arguments,
    setup_logging,
    setup_paths,
    validate_markdown_file,
)
from link_processing.crew import LinkProcessingCrew
from link_processing.file_updater import (
    get_available_sections,
    insert_link_into_markdown_file,
)
from link_processing.link_registry import LinkRegistry
from link_processing.url_processor import LinkMetadata, process_url
from loguru import logger


def process_urls(urls: List[str]) -> List[LinkMetadata]:
    """
    Process a list of URLs to extract metadata and clean them.

    Args:
        urls (List[str]): List of URLs to process

    Returns:
        List[LinkMetadata]: List of processed URL metadata
    """
    processed_urls: List[LinkMetadata] = []
    for url in urls:
        try:
            metadata = process_url(url)
            processed_urls.append(metadata)
            logger.info(
                f"Processed URL: {metadata.original_url} -> {metadata.cleaned_url} "
                f"(Type: {metadata.link_type.value})"
            )
        except Exception as e:
            logger.exception(f"Error processing URL {url}")
            # Continue with other URLs even if one fails
            continue
    return processed_urls


def main() -> None:
    """Main function to run the link processing script."""
    # Parse command line arguments
    args = parse_arguments()

    # Setup logging
    setup_logging(args.verbose)

    # Load environment variables
    load_environment()

    # Setup paths
    paths = setup_paths()

    # Validate markdown file
    markdown_file = validate_markdown_file(paths.project_root / args.markdown_file)

    # Initialize link registry with posts directory
    posts_dir = paths.project_root / "content" / "posts"
    link_registry = LinkRegistry(posts_dir)

    # Process URLs
    processed_urls = process_urls(args.urls)

    # Initialize crew
    crew = LinkProcessingCrew(
        llm_provider=args.llm_provider,
        model_name=args.model_name,
        verbose_level=args.verbose,
    )

    # Get available sections from the markdown file
    available_sections = get_available_sections(markdown_file)

    # Process each URL
    for metadata in processed_urls:
        # Check for duplicates
        if link_registry.is_duplicate(metadata.cleaned_url):
            duplicate_info = link_registry.get_duplicate_info(metadata.cleaned_url)
            logger.warning(
                f"Duplicate link found: {metadata.cleaned_url}\n"
                f"Previously added to {duplicate_info.post_file} on {duplicate_info.added_date}"
            )
            continue

        # Process URL with crew
        result = crew.process_url(metadata.cleaned_url, available_sections)
        if result:
            # Insert link into markdown file
            insert_link_into_markdown_file(
                markdown_file, result["category"], result["markdown_string"]
            )
            # Add to registry
            link_registry.add_link(
                url=metadata.cleaned_url,
                original_url=metadata.original_url,
                post_file=str(markdown_file),
                title=result["title"],
            )
            logger.info(f"Successfully added link: {metadata.cleaned_url}")
        else:
            logger.error(f"Failed to process URL: {metadata.cleaned_url}")


if __name__ == "__main__":
    main()
