from pathlib import Path

from loguru import logger

from .exceptions import DuplicateLinkError, URLProcessingError
from .file_updater import get_available_sections, insert_link_into_markdown_file
from .link_registry import LinkRegistry
from .markdown_formatter import get_formatter
from .url_analyser import UrlAnalyser
from .url_processor import process_urls


def process_single_link(
    url: str,
    markdown_file: Path,
    link_registry: LinkRegistry,
    link_processor: UrlAnalyser,
) -> str:
    """
    Processes a single URL and inserts it into the specified markdown file.

    Args:
        url (str): The URL to process.
        markdown_file (Path): The path to the markdown file.
        link_registry (LinkRegistry): The link registry instance.
        link_processor (UrlAnalyser): The URL analyser instance.

    Returns:
        str: The cleaned URL that was successfully processed and added.

    Raises:
        URLProcessingError: If the URL cannot be processed or analyzed.
        DuplicateLinkError: If the URL is a duplicate.
    """
    # Process URL to get metadata
    try:
        processed_urls = process_urls([url])
        if not processed_urls:
            raise URLProcessingError(
                f"URL processing failed to produce metadata for {url}."
            )
        metadata = processed_urls[0]
    except Exception as e:
        logger.error(f"Error processing URL {url}: {e}")
        raise URLProcessingError(str(e)) from e

    # Check for duplicates
    if link_registry.is_duplicate(metadata.cleaned_url):
        duplicate_info = link_registry.get_duplicate_info(metadata.cleaned_url)
        message = (
            f"Duplicate link found: {metadata.cleaned_url}. "
            f"Previously added to {duplicate_info.post_file} on {duplicate_info.added_date}"
        )
        raise DuplicateLinkError(message)

    # Get available sections from the markdown file
    available_sections = get_available_sections(markdown_file)

    # Analyze URL content
    result = link_processor.analyze_url(metadata.cleaned_url, available_sections)

    if not result:
        raise URLProcessingError(
            f"Failed to analyze URL content for: {metadata.cleaned_url}"
        )

    # Use the formatter to generate the markdown string
    formatter = get_formatter(metadata.link_type)
    markdown_string, section_to_insert = formatter.format(metadata, result)

    # Insert the markdown string into the file
    insert_link_into_markdown_file(
        markdown_file_path=markdown_file,
        section_name=section_to_insert,
        markdown_to_insert=markdown_string,
    )

    # Add the new link to the registry
    link_registry.add_link(
        url=metadata.cleaned_url,
        original_url=metadata.original_url,
        post_file=str(markdown_file),
        title=result.og_title or result.title,
    )

    logger.info(f"Successfully added link: {metadata.cleaned_url}")
    return metadata.cleaned_url
