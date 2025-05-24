#!/usr/bin/env python3
"""
Main CLI script to analyze URLs, generate descriptions and categories,
and insert them into a markdown blog post using a CrewAI-based system.
"""

from config import (
    load_environment,
    parse_arguments,
    setup_logging,
    setup_paths,
    validate_markdown_file,
)
from link_processing.file_updater import (
    get_available_sections,
    insert_link_into_markdown_file,
)
from link_processing.link_registry import LinkRegistry
from link_processing.url_analyser import UrlAnalyser
from link_processing.url_processor import process_urls
from loguru import logger


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

    # Get available sections from the markdown file
    available_sections = get_available_sections(markdown_file)

    # Initialize analyser
    link_processor = UrlAnalyser()

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
        result = link_processor.analyze_url(metadata.cleaned_url, available_sections)
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
