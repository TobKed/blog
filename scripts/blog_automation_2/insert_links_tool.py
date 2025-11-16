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
from link_processing.core import process_single_link
from link_processing.exceptions import (
    DuplicateLinkError,
    SectionNotFoundError,
    URLProcessingError,
)
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

    # Initialize analyser
    link_processor = UrlAnalyser()

    # Process each URL from the command line
    for url in args.urls:
        logger.info(f"Processing URL: {url}")
        try:
            process_single_link(
                url=url,
                markdown_file=markdown_file,
                link_registry=link_registry,
                link_processor=link_processor,
            )
        except (DuplicateLinkError, URLProcessingError, SectionNotFoundError) as e:
            logger.error(f"Failed to process link: {e}")


if __name__ == "__main__":
    main()
