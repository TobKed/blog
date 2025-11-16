"""
Tests for markdown_formatter module.
"""

from unittest.mock import Mock

import pytest
from link_processing.markdown_formatter import (
    ArticleMarkdownFormatter,
    YouTubeVideoMarkdownFormatter,
    get_formatter,
)
from link_processing.url_processor import LinkMetadata, LinkType


@pytest.fixture
def mock_analysis_result():
    """Fixture for a mock PageAnalysisOutout object."""
    mock = Mock()
    mock.og_title = "Original Title"
    mock.og_description = "Original Description"
    mock.title = "Page Title"
    mock.summary = "Detailed summary of the page."
    mock.brief_summary = "Brief summary in a paragraph."
    mock.section = "AI"
    return mock


@pytest.fixture
def article_metadata():
    """Fixture for article link metadata."""
    return LinkMetadata(
        original_url="https://example.com/article",
        cleaned_url="https://example.com/article",
        link_type=LinkType.ARTICLE,
    )


@pytest.fixture
def youtube_video_metadata():
    """Fixture for YouTube video link metadata."""
    return LinkMetadata(
        original_url="https://www.youtube.com/watch?v=12345",
        cleaned_url="https://www.youtube.com/watch?v=12345",
        link_type=LinkType.YOUTUBE,
        video_id="12345",
        is_youtube_playlist=False,
    )


@pytest.fixture
def youtube_playlist_metadata():
    """Fixture for YouTube playlist link metadata."""
    return LinkMetadata(
        original_url="https://www.youtube.com/playlist?list=abcde",
        cleaned_url="https://www.youtube.com/playlist?list=abcde",
        link_type=LinkType.YOUTUBE,
        is_youtube_playlist=True,
    )


def test_article_formatter(article_metadata, mock_analysis_result):
    """Test the ArticleMarkdownFormatter."""
    formatter = ArticleMarkdownFormatter()
    markdown, section = formatter.format(article_metadata, mock_analysis_result)

    assert section == "AI"
    assert "### [Original Title](https://example.com/article)" in markdown
    assert "> Original Description" in markdown
    assert "Brief summary in a paragraph" in markdown


def test_youtube_video_formatter(youtube_video_metadata, mock_analysis_result):
    """Test the YouTubeVideoMarkdownFormatter for a single video."""
    formatter = YouTubeVideoMarkdownFormatter()
    markdown, section = formatter.format(youtube_video_metadata, mock_analysis_result)

    assert section == "Videos"
    assert "### [Original Title](https://www.youtube.com/watch?v=12345)" in markdown
    assert 'src="https://www.youtube-nocookie.com/embed/12345"' in markdown
    assert "Brief summary in a paragraph" in markdown


def test_youtube_playlist_formatter(youtube_playlist_metadata, mock_analysis_result):
    """Test the YouTubeVideoMarkdownFormatter for a playlist."""
    formatter = YouTubeVideoMarkdownFormatter()
    markdown, section = formatter.format(
        youtube_playlist_metadata, mock_analysis_result
    )

    assert section == "Videos"
    assert (
        "### [Original Title](https://www.youtube.com/playlist?list=abcde)" in markdown
    )
    assert "> Original Description" in markdown
    assert "iframe" not in markdown  # Should not be an embedded video


def test_get_formatter():
    """Test the get_formatter factory function."""
    assert isinstance(get_formatter(LinkType.ARTICLE), ArticleMarkdownFormatter)
    assert isinstance(get_formatter(LinkType.YOUTUBE), YouTubeVideoMarkdownFormatter)
