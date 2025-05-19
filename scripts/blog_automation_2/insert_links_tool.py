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

from loguru import logger

from link_processing.crew import LinkProcessingCrew
from link_processing.file_updater import (
    get_available_sections,
    insert_link_into_markdown_file,
)
from link_processing.url_processor import process_url, LinkMetadata

from config import (
    CommandLineArgs,
    setup_paths,
    load_environment,
    parse_arguments,
    validate_markdown_file,
    setup_logging,
)


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
    """Main function to orchestrate link processing and insertion."""
    # Parse command line arguments first to get verbose flag
    args: CommandLineArgs = parse_arguments()

    # Setup logging with appropriate verbosity
    setup_logging(verbose=args.verbose)

    # Setup paths and environment
    project_root, script_dir = setup_paths()
    load_environment(script_dir)

    # Validate target markdown file
    target_markdown_path = validate_markdown_file(
        project_root, args.target_markdown_file
    )

    logger.info(
        f"Processing {len(args.urls)} URL(s) for '{target_markdown_path.name}'..."
    )

    # Process URLs to clean them and extract metadata
    processed_urls = process_urls(args.urls)
    if not processed_urls:
        logger.error("No URLs were successfully processed. Exiting.")
        sys.exit(1)

    # 1. Get available sections from the target markdown file
    available_sections = get_available_sections(target_markdown_path)

    # 2. Initialize and run the CrewAI crew for each URL
    try:
        link_crew = LinkProcessingCrew(
            llm_provider=args.llm_provider,
            model_name=args.model_name,
            verbose_level=2 if args.verbose else 0,
        )
    except ValueError as e:
        logger.error(f"Error initializing LinkProcessingCrew: {e}")
        sys.exit(1)

    successful_insertions = 0
    for metadata in processed_urls:
        logger.info(f"Processing URL: {metadata.cleaned_url}")
        logger.debug(f"\tmetadata: {metadata=}")
        try:
            processed_data = link_crew.process_url(
                metadata.cleaned_url, available_sections
            )

            if (
                processed_data
                and processed_data.get("category")
                and processed_data.get("markdown_string")
            ):
                logger.info(f"Title: {processed_data['title']}")
                logger.info(f"Description: {processed_data['description']}")
                logger.info(f"Keywords: {processed_data.get('keywords', 'N/A')}")
                logger.info(f"Categorized under: {processed_data['category']}")

                # 3. Insert into markdown file
                if insert_link_into_markdown_file(
                    markdown_file_path=target_markdown_path,
                    section_name=processed_data["category"],
                    markdown_to_insert=processed_data["markdown_string"],
                ):
                    logger.success(
                        f"Successfully inserted into '{target_markdown_path.name}'"
                    )
                    successful_insertions += 1
                else:
                    logger.error(
                        f"Failed to insert link for {metadata.cleaned_url} into the markdown file."
                    )
            elif (
                processed_data is None
            ):  # Explicitly None means an error occurred in crew
                logger.error(
                    f"Processing failed for URL {metadata.cleaned_url} within the crew."
                )
            else:
                logger.warning(
                    f"Could not fully process URL {metadata.cleaned_url}. "
                    f"Missing essential data. Skipping insertion. Data: {processed_data}"
                )

        except Exception as e:
            logger.exception(
                f"An unexpected error occurred while processing URL {metadata.cleaned_url}"
            )

    logger.info("Finished processing")
    logger.info(f"{successful_insertions} link(s) successfully processed and inserted.")
    if successful_insertions < len(processed_urls):
        logger.warning(
            f"{len(processed_urls) - successful_insertions} link(s) could not be processed or inserted fully."
        )


if __name__ == "__main__":
    main()
