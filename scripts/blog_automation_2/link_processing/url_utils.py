"""
URL processing utilities for the blog automation tool.

This module provides functions for cleaning and processing URLs.
"""

from typing import Optional
from urllib.parse import parse_qs, urlencode, urlparse

from loguru import logger


def clean_url(url: str) -> Optional[str]:
    """
    Clean a URL by removing tracking parameters and normalizing it.

    Args:
        url (str): The URL to clean

    Returns:
        Optional[str]: The cleaned URL or None if invalid
    """
    try:
        # Parse the URL
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return None

        # Parse query parameters
        query_params = parse_qs(parsed.query)

        # Remove tracking parameters
        tracking_params = {
            "utm_source",
            "utm_medium",
            "utm_campaign",
            "utm_term",
            "utm_content",
            "ref",
            "source",
            "fbclid",
            "gclid",
            "msclkid",
        }

        # Filter out tracking parameters
        filtered_params = {
            k: v[0] for k, v in query_params.items() if k.lower() not in tracking_params
        }

        # Reconstruct the URL without tracking parameters
        cleaned = parsed._replace(
            query=urlencode(filtered_params) if filtered_params else "",
            fragment="",  # Remove fragments
        ).geturl()

        return cleaned

    except Exception as e:
        logger.error(f"Error cleaning URL {url}: {e}")
        return None
