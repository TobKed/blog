"""
Tests for URL utility functions.
"""

import pytest
from link_processing.url_utils import clean_url


@pytest.mark.parametrize(
    "original_url, expected_url",
    [
        (
            "https://example.com/page?utm_source=google&utm_medium=cpc&param=value",
            "https://example.com/page?param=value",
        ),
        (
            "https://example.com/page?fbclid=12345&ref=some_ref",
            "https://example.com/page",
        ),
        ("https://example.com/page#section", "https://example.com/page"),
        (
            "http://example.com/page?a=1&utm_campaign=test&b=2",
            "http://example.com/page?a=1&b=2",
        ),
        ("https://example.com", "https://example.com"),
        ("invalid-url", None),
    ],
)
def test_clean_url(original_url, expected_url):
    """
    Tests that clean_url removes tracking parameters and normalizes URLs correctly.
    """
    assert clean_url(original_url) == expected_url
