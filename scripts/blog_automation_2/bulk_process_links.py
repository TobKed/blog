#!/usr/bin/env python3
"""
Helper script to bulk process URLs from a markdown file and insert them into a target blog post.
Generates a report of successfully added and failed/skipped links.
"""
import argparse
import sys
from pathlib import Path

from config import setup_paths, validate_markdown_file
from link_processing.core import process_single_link
from link_processing.exceptions import (
    DuplicateLinkError,
    SectionNotFoundError,
    URLProcessingError,
)
from link_processing.link_registry import LinkRegistry
from link_processing.url_analyser import UrlAnalyser
from loguru import logger  # Import Loguru logger

# Determine the project root (assuming this script is in scripts/blog_automation_2/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def setup_logging(verbose: bool) -> None:
    """Configure Loguru logger."""
    logger.remove()  # Remove default handler
    log_level = "DEBUG" if verbose else "INFO"
    logger.add(
        sys.stderr,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )


def parse_input_file(input_file_path: Path) -> tuple[str, list[str]]:
    """
    Parses the input markdown file to extract the target post and URLs.

    Args:
        input_file_path (Path): Path to the input markdown file.

    Returns:
        tuple[str, list[str]]: Target post file path (relative to project root) and a list of URLs.
    """
    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.error(f"Input file not found: {input_file_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error reading input file {input_file_path}: {e}")
        sys.exit(1)

    if not lines:
        logger.error(f"Input file {input_file_path} is empty.")
        sys.exit(1)

    target_post_header = "Target Post:"
    if not lines[0].startswith(target_post_header):
        logger.error(
            f"First line of input file must be '{target_post_header} path/to/post.md'"
        )
        sys.exit(1)

    target_post_file = lines[0][len(target_post_header) :].strip()
    urls_to_process = lines[1:]

    if not target_post_file:
        logger.error(f"Target post file path is missing in {input_file_path}")
        sys.exit(1)

    if not urls_to_process:
        logger.error(f"No URLs found in {input_file_path} to process.")
        sys.exit(1)

    return target_post_file, urls_to_process


def generate_report_file(
    input_file_path: Path,
    target_post_file: str,
    added_links: list[str],
    failed_links: list[str],
) -> None:
    """
    Generates a markdown report file.

    Args:
        input_file_path (Path): Path of the original input file.
        target_post_file (str): Target post file path.
        added_links (list[str]): List of successfully added link details.
        failed_links (list[str]): List of failed/skipped link details.
    """
    report_file_name = input_file_path.stem + "_report.md"
    report_file_path = input_file_path.parent / report_file_name

    try:
        with open(report_file_path, "w", encoding="utf-8") as f:
            f.write(f"Target Post: {target_post_file}\n")

            f.write("## Successfully Added Links\n")
            if added_links:
                for link_detail in added_links:
                    f.write(f"- {link_detail}\n")
            else:
                f.write("No links were successfully added.\n")
            f.write("\n")

            f.write("## Failed or Skipped Links\n")
            if failed_links:
                for link_detail in failed_links:
                    f.write(f"- {link_detail}\n")
            else:
                f.write("No links failed or were skipped.\n")

        logger.info(f"Report generated: {report_file_path}")
    except Exception as e:
        logger.error(f"Failed to generate report file {report_file_path}: {e}")


def main():
    """Main function to orchestrate the bulk link processing."""
    parser = argparse.ArgumentParser(
        description="Bulk process URLs from a markdown file and insert them into a target blog post."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input markdown file containing URLs to process.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging for this script.",
    )
    args = parser.parse_args()

    # Setup logging for this script
    setup_logging(args.verbose)

    input_file_path = args.input_file.resolve()  # Ensure absolute path

    target_post_file_rel, urls_to_process = parse_input_file(input_file_path)

    # Setup paths and validate markdown file
    paths = setup_paths()
    target_post_file_abs = validate_markdown_file(
        paths.project_root / target_post_file_rel
    )

    # Initialize components once
    posts_dir = paths.project_root / "content" / "posts"
    link_registry = LinkRegistry(posts_dir)
    link_processor = UrlAnalyser()

    logger.info(f"Processing links for target post: {target_post_file_rel}")
    logger.info(
        f"Found {len(urls_to_process)} URLs to process from {input_file_path.name}"
    )

    added_links_details = []
    failed_links_details = []

    for i, url in enumerate(urls_to_process):
        logger.info(f"Processing URL {i+1}/{len(urls_to_process)}: {url} ...")
        try:
            cleaned_url = process_single_link(
                url=url,
                markdown_file=target_post_file_abs,
                link_registry=link_registry,
                link_processor=link_processor,
            )
            logger.info(f"  \\_ Status: Success ({cleaned_url})")
            added_links_details.append(cleaned_url)
        except (DuplicateLinkError, URLProcessingError, SectionNotFoundError) as e:
            logger.warning(f"  \\_ Status: Failed/Skipped ({e})")
            failed_links_details.append(f"{url} (Reason: {e})")

    generate_report_file(
        input_file_path, target_post_file_rel, added_links_details, failed_links_details
    )
    logger.info("Bulk processing complete.")


if __name__ == "__main__":
    main()
