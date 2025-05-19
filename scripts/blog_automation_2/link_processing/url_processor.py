"""
URL processing and metadata handling module.

This module provides functionality for:
- Cleaning URLs (removing tracking parameters, etc.)
- Extracting metadata from URLs
- Determining link types
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Set
from urllib.parse import parse_qs, urlparse, urlunparse

from loguru import logger


class LinkType(Enum):
    """Enum representing different types of links."""

    YOUTUBE = "youtube"
    VIDEO = "video"
    ARTICLE = "article"
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


def is_youtube_url(parsed_url) -> bool:
    """
    Check if the URL is a YouTube URL.

    Args:
        parsed_url: Parsed URL object

    Returns:
        bool: True if the URL is a YouTube URL
    """
    return "youtube.com" in parsed_url.netloc or "youtu.be" in parsed_url.netloc


def get_youtube_essential_params(query_params: dict) -> dict:
    """
    Get essential YouTube parameters (video ID and playlist ID).

    Args:
        query_params (dict): Dictionary of query parameters

    Returns:
        dict: Dictionary containing only essential YouTube parameters
    """
    essential_params = {}

    # Keep video ID
    if "v" in query_params:
        essential_params["v"] = query_params["v"]

    # Keep playlist ID
    if "list" in query_params:
        essential_params["list"] = query_params["list"]

    return essential_params


def clean_url(url: str) -> str:
    """
    Clean a URL by removing all query parameters except for essential YouTube parameters.
    For YouTube URLs, only keeps video ID ('v') and playlist ID ('list') parameters.
    For all other URLs, removes all query parameters.

    Args:
        url (str): The URL to clean

    Returns:
        str: The cleaned URL
    """
    try:
        # Parse the URL
        parsed = urlparse(url)

        # Handle query parameters
        if parsed.query:
            query_params = parse_qs(parsed.query)

            if is_youtube_url(parsed):
                # For YouTube URLs, keep only essential parameters
                cleaned_params = get_youtube_essential_params(query_params)
            else:
                # For all other URLs, remove all query parameters
                cleaned_params = {}

            # Reconstruct query string if there are any parameters to keep
            new_query = (
                "&".join(f"{k}={v[0]}" for k, v in cleaned_params.items())
                if cleaned_params
                else ""
            )

            # Reconstruct URL with cleaned query
            parsed = parsed._replace(query=new_query)

        # Remove trailing slashes
        path = parsed.path.rstrip("/")
        parsed = parsed._replace(path=path)

        # Reconstruct the URL
        cleaned_url = urlunparse(parsed)

        logger.debug(f"Cleaned URL: {url} -> {cleaned_url}")
        return cleaned_url

    except Exception as e:
        logger.warning(f"Error cleaning URL {url}: {e}")
        return url


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

        # YouTube
        if "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc:
            if "youtu.be" in parsed.netloc:
                return parsed.path[1:]  # Remove leading slash
            query_params = parse_qs(parsed.query)
            return query_params.get("v", [None])[0]

        # Add support for other video platforms here
        # Example: Vimeo, Dailymotion, etc.

        return None

    except Exception as e:
        logger.warning(f"Error extracting video ID from {url}: {e}")
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
