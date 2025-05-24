#!/usr/bin/env python3
"""
Helper script to bulk process URLs from a markdown file and insert them into a target blog post.
Generates a report of successfully added and failed/skipped links.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

from loguru import logger  # Import Loguru logger

# Determine the project root (assuming this script is in scripts/blog_automation_2/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
INSERT_LINKS_TOOL_PATH = (
    PROJECT_ROOT / "scripts" / "blog_automation_2" / "insert_links_tool.py"
)


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


def run_insert_tool_for_url(
    target_post: str, url: str, verbose_tool: bool
) -> tuple[bool, str]:
    """
    Runs the insert_links_tool.py for a single URL and captures its output.

    Args:
        target_post (str): The markdown file to insert the link into (relative to project root).
        url (str): The URL to process.
        verbose_tool (bool): Whether to run the insert_links_tool.py in verbose mode.

    Returns:
        tuple[bool, str]: A tuple containing (success_status, status_message).
                          success_status is True if the link was added, False otherwise.
                          status_message contains the reason for failure/skip or success.
    """
    command = [
        "python",
        str(INSERT_LINKS_TOOL_PATH),
        "--markdown_file",
        target_post,
        url,
    ]
    if verbose_tool:
        command.append("--verbose")

    try:
        # Run the command from the project root
        logger.debug(f"Running command: {' '.join(command)}")
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
            check=False,  # Don't raise exception for non-zero exit codes
        )

        output = process.stdout + "\\n" + process.stderr
        logger.debug(f"Output from insert_links_tool for {url}:\n{output.strip()}")

        if re.search(r"Successfully added link:", output, re.IGNORECASE):
            return True, f"Successfully added: {url}"
        elif re.search(r"Duplicate link found:", output, re.IGNORECASE):
            reason = re.search(r"Duplicate link found:.*", output, re.IGNORECASE)
            return False, reason.group(0) if reason else f"Duplicate link: {url}"
        elif re.search(r"Failed to process URL:", output, re.IGNORECASE):
            reason = re.search(r"Failed to process URL:.*", output, re.IGNORECASE)
            return False, reason.group(0) if reason else f"Failed to process: {url}"
        elif process.returncode != 0:
            return (
                False,
                f"Failed with exit code {process.returncode}. Output: {output.strip()}",
            )
        else:
            # Fallback if no specific message is found but tool seemed to succeed
            if "error" in output.lower() or "failed" in output.lower():
                return (
                    False,
                    f"Processing finished with unclear status. Output: {output.strip()}",
                )
            return (
                True,
                f"Processed (status unclear from output, assumed success): {url}",
            )

    except FileNotFoundError:
        logger.error(f"Could not find insert_links_tool.py at {INSERT_LINKS_TOOL_PATH}")
        logger.error("Please ensure the script path is correct and it's executable.")
        return False, "Helper script error: insert_links_tool.py not found."
    except Exception as e:
        logger.error(f"Error running insert_links_tool.py for {url}: {e}")
        return False, f"Error running insert_links_tool.py for {url}: {e}"


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
            f.write(f"Target Post: {target_post_file}\\n\\n")

            f.write("## Successfully Added Links\\n")
            if added_links:
                for link_detail in added_links:
                    url_match = re.search(r"(https?://[^\s]+)", link_detail)
                    url_to_list = url_match.group(1) if url_match else link_detail
                    f.write(f"- {url_to_list}\\n")
            else:
                f.write("No links were successfully added.\\n")
            f.write("\\n")

            f.write("## Failed or Skipped Links\\n")
            if failed_links:
                for link_detail in failed_links:
                    f.write(f"- {link_detail}\\n")
            else:
                f.write("No links failed or were skipped.\\n")

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
        help="Enable verbose logging for this script and run the insert_links_tool.py in verbose mode.",
    )
    args = parser.parse_args()

    # Setup logging for this script
    setup_logging(args.verbose)

    input_file_path = args.input_file.resolve()  # Ensure absolute path

    target_post_file, urls_to_process = parse_input_file(input_file_path)

    logger.info(f"Processing links for target post: {target_post_file}")
    logger.info(
        f"Found {len(urls_to_process)} URLs to process from {input_file_path.name}"
    )

    added_links_details = []
    failed_links_details = []

    for i, url in enumerate(urls_to_process):
        logger.info(f"Processing URL {i+1}/{len(urls_to_process)}: {url} ...")
        # Pass args.verbose to run_insert_tool_for_url to control verbosity of the tool itself
        success, message = run_insert_tool_for_url(target_post_file, url, args.verbose)
        if success:
            logger.info(f"  \\_ Status: Success ({message})")
            added_links_details.append(url)
        else:
            logger.warning(
                f"  \\_ Status: Failed/Skipped ({message})"
            )  # Use warning for user-facing non-critical failures
            failed_links_details.append(
                f"{url} (Reason: {message.replace(url, '').strip().lstrip(':').strip()})"
            )

    generate_report_file(
        input_file_path, target_post_file, added_links_details, failed_links_details
    )
    logger.info("Bulk processing complete.")


if __name__ == "__main__":
    main()
