"""
Link registry for tracking and managing links across blog posts.

This module provides functionality to:
1. Track links that have been added to blog posts
2. Check for duplicate links
3. Maintain a registry of links with their metadata
4. Parse existing blog posts for links
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set

from loguru import logger

from .url_utils import clean_url


@dataclass
class LinkEntry:
    """
    Data class for storing link entry information.

    Attributes:
        url (str): The cleaned URL
        original_url (str): The original URL before cleaning
        post_file (str): The blog post file where the link was added
        added_date (str): The date when the link was added
        title (Optional[str]): The title of the content (if available)
    """

    url: str
    original_url: str
    post_file: str
    added_date: str
    title: Optional[str] = None


class LinkRegistry:
    """
    Registry for tracking and managing links across blog posts.

    This class maintains a registry of links that have been added to blog posts
    and provides methods to check for duplicates and manage the registry.
    """

    def __init__(self, posts_dir: Path):
        """
        Initialize the LinkRegistry.

        Args:
            posts_dir (Path): Directory containing blog post files
        """
        self.posts_dir = posts_dir
        self.registry: Dict[str, LinkEntry] = {}
        self._parse_existing_posts()

    def _parse_existing_posts(self) -> None:
        """Parse all existing blog posts to find links."""
        try:
            # Find all markdown files in the posts directory
            markdown_files = list(self.posts_dir.glob("**/*.md"))
            logger.info(f"Found {len(markdown_files)} markdown files to parse")

            # Regular expression to find markdown links
            # Matches both [text](url) and <url> formats
            link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)|<([^>]+)>")

            for file_path in markdown_files:
                try:
                    content = file_path.read_text(encoding="utf-8")
                    matches = link_pattern.finditer(content)

                    for match in matches:
                        if match.group(2):  # [text](url) format
                            url = match.group(2)
                            title = match.group(1)
                        else:  # <url> format
                            url = match.group(3)
                            title = None

                        # Clean the URL
                        cleaned_url = clean_url(url)
                        if cleaned_url:
                            entry = LinkEntry(
                                url=cleaned_url,
                                original_url=url,
                                post_file=str(file_path),
                                added_date=datetime.now().isoformat(),  # Use current time as we don't know when it was added
                                title=title,
                            )
                            self.registry[cleaned_url] = entry

                except Exception as e:
                    logger.error(f"Error parsing file {file_path}: {e}")
                    continue

            logger.info(f"Parsed {len(self.registry)} links from existing posts")

        except Exception as e:
            logger.error(f"Error parsing existing posts: {e}")
            self.registry = {}

    def is_duplicate(self, url: str) -> bool:
        """
        Check if a URL is already in the registry.

        Args:
            url (str): The URL to check

        Returns:
            bool: True if the URL is a duplicate, False otherwise
        """
        return url in self.registry

    def get_duplicate_info(self, url: str) -> Optional[LinkEntry]:
        """
        Get information about a duplicate URL if it exists.

        Args:
            url (str): The URL to check

        Returns:
            Optional[LinkEntry]: LinkEntry if the URL is a duplicate, None otherwise
        """
        return self.registry.get(url)

    def add_link(
        self,
        url: str,
        original_url: str,
        post_file: str,
        title: Optional[str] = None,
    ) -> None:
        """
        Add a new link to the registry.

        Args:
            url (str): The cleaned URL
            original_url (str): The original URL before cleaning
            post_file (str): The blog post file where the link was added
            title (Optional[str]): The title of the content (if available)
        """
        entry = LinkEntry(
            url=url,
            original_url=original_url,
            post_file=post_file,
            added_date=datetime.now().isoformat(),
            title=title,
        )
        self.registry[url] = entry
        logger.debug(f"Added link to registry: {url}")

    def get_all_links(self) -> List[LinkEntry]:
        """
        Get all links in the registry.

        Returns:
            List[LinkEntry]: List of all LinkEntry objects
        """
        return list(self.registry.values())

    def get_links_by_post(self, post_file: str) -> List[LinkEntry]:
        """
        Get all links from a specific blog post.

        Args:
            post_file (str): The blog post file to get links from

        Returns:
            List[LinkEntry]: List of LinkEntry objects from the specified post
        """
        return [
            entry for entry in self.registry.values() if entry.post_file == post_file
        ]
