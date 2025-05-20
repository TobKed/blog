"""
URL processing module for the blog automation tool.

This module provides functionality to:
1. Process and clean URLs
2. Extract metadata from URLs
3. Determine link types
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from urllib.parse import urlparse

from loguru import logger

from .url_utils import clean_url


class LinkType(Enum):
    """Enum for different types of links."""

    ARTICLE = "article"
    YOUTUBE = "youtube"
    VIDEO = "video"
    UNKNOWN = "unknown"


@dataclass
class LinkMetadata:
    """
    Data class for storing link metadata.

    Attributes:
        original_url (str): The original URL before cleaning
        cleaned_url (str): The cleaned URL without tracking parameters
        link_type (LinkType): Type of the link (YouTube, video, article, etc.)
        title (Optional[str]): Title of the content (if available)
        description (Optional[str]): Description of the content (if available)
        video_id (Optional[str]): Video ID for video links (if applicable)
    """

    original_url: str
    cleaned_url: str
    link_type: LinkType
    title: Optional[str] = None
    description: Optional[str] = None
    video_id: Optional[str] = None


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract video ID from various video platform URLs.

    Args:
        url (str): The URL to extract video ID from

    Returns:
        Optional[str]: The video ID if found, None otherwise
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # YouTube
        if "youtube.com" in domain:
            if "v=" in parsed.query:
                return parsed.query.split("v=")[1].split("&")[0]
        elif "youtu.be" in domain:
            return parsed.path.strip("/")

        # Vimeo
        elif "vimeo.com" in domain:
            return parsed.path.strip("/")

        # Other video platforms
        elif domain in {"dailymotion.com", "twitch.tv", "bitchute.com", "odysee.com"}:
            return parsed.path.strip("/")

        return None

    except Exception as e:
        logger.error(f"Error extracting video ID from {url}: {e}")
        return None


def determine_link_type(url: str) -> LinkType:
    """
    Determine the type of link based on the URL.

    Args:
        url (str): The URL to analyze

    Returns:
        LinkType: The determined type of link
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Check for YouTube
        if "youtube.com" in domain or "youtu.be" in domain:
            return LinkType.YOUTUBE

        # Check for other video platforms
        video_domains = {
            "vimeo.com",
            "dailymotion.com",
            "twitch.tv",
            "vimeo.com",
            "dailymotion.com",
            "twitch.tv",
            "bitchute.com",
            "odysee.com",
        }
        if domain in video_domains:
            return LinkType.VIDEO

        # Default to article for other links
        return LinkType.ARTICLE

    except Exception as e:
        logger.warning(f"Error determining link type for {url}: {e}")
        return LinkType.UNKNOWN


def process_url(url: str) -> LinkMetadata:
    """
    Process a URL to extract metadata and clean it.

    Args:
        url (str): The URL to process

    Returns:
        LinkMetadata: Object containing the processed URL and its metadata
    """
    try:
        # Clean the URL
        cleaned_url = clean_url(url)
        if not cleaned_url:
            raise ValueError(f"Invalid URL: {url}")

        # Determine link type
        link_type = determine_link_type(cleaned_url)

        # Extract video ID if applicable
        video_id = None
        if link_type in (LinkType.YOUTUBE, LinkType.VIDEO):
            video_id = extract_video_id(cleaned_url)

        # Create metadata object
        metadata = LinkMetadata(
            original_url=url,
            cleaned_url=cleaned_url,
            link_type=link_type,
            video_id=video_id,
        )

        logger.debug(f"Processed URL: {metadata}")
        return metadata

    except Exception as e:
        logger.exception(f"Error processing URL {url}")
        # Return basic metadata in case of error
        return LinkMetadata(
            original_url=url, cleaned_url=url, link_type=LinkType.UNKNOWN
        )
