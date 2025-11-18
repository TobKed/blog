"""
Tests for the file_updater module.
"""

from pathlib import Path

import pytest
from link_processing.exceptions import SectionNotFoundError
from link_processing.file_updater import (
    get_available_sections,
    insert_link_into_markdown_file,
)


@pytest.fixture
def temp_markdown_file(tmp_path: Path) -> Path:
    """Fixture to create a temporary markdown file."""
    content = """
# My Blog Post

## Section One

Some content here.

## Section Two

More content.
"""
    file_path = tmp_path / "test_post.md"
    file_path.write_text(content)
    return file_path


def test_get_available_sections(temp_markdown_file: Path):
    """Test that get_available_sections correctly extracts section names."""
    sections = get_available_sections(temp_markdown_file)
    assert sections == ["Section One", "Section Two"]


def test_insert_link_into_existing_section(temp_markdown_file: Path):
    """Test inserting a link into an existing section."""
    link_to_insert = "### [New Link](https://example.com)"
    insert_link_into_markdown_file(temp_markdown_file, "Section One", link_to_insert)

    content = temp_markdown_file.read_text()
    expected_content = """
# My Blog Post

## Section One

Some content here.

### [New Link](https://example.com)

## Section Two

More content.
"""
    assert content.strip() == expected_content.strip()


def test_insert_link_into_new_other_stuff_section(temp_markdown_file: Path):
    """Test inserting a link that creates a new 'Other stuff' section."""
    link_to_insert = "### [Other Link](https://other.com)"
    insert_link_into_markdown_file(temp_markdown_file, "Other stuff", link_to_insert)

    content = temp_markdown_file.read_text()
    assert "## Other stuff" in content
    assert "### [Other Link](https://other.com)" in content


def test_insert_link_raises_section_not_found(temp_markdown_file: Path):
    """Test that an exception is raised if the section does not exist."""
    with pytest.raises(SectionNotFoundError):
        insert_link_into_markdown_file(
            temp_markdown_file, "Non-existent Section", "some markdown"
        )
