"""
Tests for the core processing logic.
"""

from pathlib import Path
from unittest.mock import Mock

import pytest
from link_processing.core import process_single_link
from link_processing.exceptions import DuplicateLinkError, URLProcessingError
from link_processing.url_processor import LinkMetadata, LinkType


@pytest.fixture
def mock_link_registry(mocker):
    """Fixture for a mock LinkRegistry."""
    mock = Mock()
    mock.is_duplicate.return_value = False
    mocker.patch("link_processing.core.LinkRegistry", return_value=mock)
    return mock


@pytest.fixture
def mock_url_analyser(mocker):
    """Fixture for a mock UrlAnalyser."""
    mock_analysis = Mock()
    mock_analysis.og_title = "Test Title"
    mock_analysis.summary = "Test Summary"
    mock_analysis.brief_summary = "Brief Test Summary"
    mock_analysis.section = "Test Section"

    mock_analyser = Mock()
    mock_analyser.analyze_url.return_value = mock_analysis
    mocker.patch("link_processing.core.UrlAnalyser", return_value=mock_analyser)
    return mock_analyser


@pytest.fixture
def mock_process_urls(mocker):
    """Fixture to mock the process_urls function."""
    mock_metadata = LinkMetadata(
        original_url="https://example.com",
        cleaned_url="https://example.com",
        link_type=LinkType.ARTICLE,
    )
    return mocker.patch(
        "link_processing.core.process_urls", return_value=[mock_metadata]
    )


@pytest.fixture
def temp_markdown_file_for_core(tmp_path: Path) -> Path:
    """Fixture for a temporary markdown file for core tests."""
    content = "## Test Section\n\n"
    file_path = tmp_path / "core_test_post.md"
    file_path.write_text(content)
    return file_path


def test_process_single_link_success(
    mock_process_urls,
    mock_link_registry,
    mock_url_analyser,
    temp_markdown_file_for_core,
):
    """Test the successful processing of a single link."""
    url = "https://example.com"
    cleaned_url = process_single_link(
        url,
        temp_markdown_file_for_core,
        mock_link_registry,
        mock_url_analyser,
    )

    assert cleaned_url == "https://example.com"
    mock_link_registry.add_link.assert_called_once()
    content = temp_markdown_file_for_core.read_text()
    assert "### [Test Title](https://example.com)" in content


def test_process_single_link_duplicate(
    mock_process_urls,
    mock_link_registry,
    mock_url_analyser,
    temp_markdown_file_for_core,
):
    """Test that a DuplicateLinkError is raised for a duplicate link."""
    mock_link_registry.is_duplicate.return_value = True
    mock_link_registry.get_duplicate_info.return_value = Mock(
        post_file="some_file.md", added_date="some_date"
    )

    with pytest.raises(DuplicateLinkError):
        process_single_link(
            "https://example.com",
            temp_markdown_file_for_core,
            mock_link_registry,
            mock_url_analyser,
        )


def test_process_single_link_analysis_fails(
    mock_process_urls,
    mock_link_registry,
    mock_url_analyser,
    temp_markdown_file_for_core,
):
    """Test that a URLProcessingError is raised if analysis fails."""
    mock_url_analyser.analyze_url.return_value = None

    with pytest.raises(URLProcessingError):
        process_single_link(
            "https://example.com",
            temp_markdown_file_for_core,
            mock_link_registry,
            mock_url_analyser,
        )
