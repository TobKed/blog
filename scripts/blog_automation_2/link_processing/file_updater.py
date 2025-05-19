"""
Utility functions for updating the markdown blog post file.
Includes extracting sections and inserting new link content.
"""

import re
from pathlib import Path
from typing import List, Optional


def get_available_sections(markdown_file_path: Path) -> List[str]:
    """
    Extracts H2 level section names from a markdown file.
    Example: "## Section Name" -> "Section Name"
    """
    sections: List[str] = []
    try:
        content = markdown_file_path.read_text(encoding="utf-8")
        # Regex to find lines starting with '## ' followed by the section name
        # It captures the text after '## ' up to the end of the line.
        matches = re.findall(r"^\s*##\s+(.+?)\s*$", content, re.MULTILINE)
        sections = [match.strip() for match in matches if match.strip()]
    except FileNotFoundError:
        print(
            f"Error: Markdown file not found at {markdown_file_path}", file=sys.stderr
        )
    except Exception as e:
        print(
            f"Error reading or parsing sections from {markdown_file_path}: {e}",
            file=sys.stderr,
        )
    return sections


def insert_link_into_markdown_file(
    markdown_file_path: Path, section_name: str, markdown_to_insert: str
) -> bool:
    """
    Inserts a markdown formatted link string under a specific H2 section
    in a markdown file. If the section doesn't exist, and the section_name
    is "Other stuff", it appends a new "## Other stuff" section.

    Args:
        markdown_file_path (Path): Path to the markdown file.
        section_name (str): The name of the H2 section (e.g., "Python").
        markdown_to_insert (str): The full markdown block for the link.

    Returns:
        bool: True if insertion was successful, False otherwise.
    """
    try:
        content = markdown_file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        new_content_lines: List[str] = []
        inserted = False

        # Normalize target section name for robust matching
        normalized_target_section_name = section_name.strip().lower()

        section_line_indices = []
        for i, line in enumerate(lines):
            match = re.match(r"^\s*##\s+(.+?)\s*$", line)
            if match:
                current_section_name = match.group(1).strip().lower()
                section_line_indices.append(
                    {
                        "name": current_section_name,
                        "index": i,
                        "original_name": match.group(1).strip(),
                    }
                )

        target_section_info = next(
            (
                s
                for s in section_line_indices
                if s["name"] == normalized_target_section_name
            ),
            None,
        )

        if target_section_info:
            target_idx = target_section_info["index"]
            # Find where the target section ends (either next H2 or EOF)
            next_section_start_idx = len(lines)  # Default to end of file
            for s_info in section_line_indices:
                if s_info["index"] > target_idx:
                    next_section_start_idx = s_info["index"]
                    break

            # Insert before the next section header, or at the end of the file if it's the last section
            # Add the new link at the end of the content of the target section.
            # This means inserting just before `next_section_start_idx`.
            insertion_point = next_section_start_idx

            # Add lines before the insertion point
            new_content_lines.extend(lines[:insertion_point])
            # Add a blank line if the last line before insertion isn't already blank
            if new_content_lines and new_content_lines[-1].strip() != "":
                new_content_lines.append("")
            new_content_lines.append(markdown_to_insert)
            # Add a blank line after insertion if not immediately followed by another section or EOF
            if insertion_point == len(lines) or (
                insertion_point < len(lines) and lines[insertion_point].strip() != ""
            ):
                new_content_lines.append("")
            # Add remaining lines
            new_content_lines.extend(lines[insertion_point:])
            inserted = True

        elif normalized_target_section_name == "other stuff":
            # If "Other stuff" section doesn't exist, append it
            print(
                f"  Section '{section_name}' not found. Appending as new '## {section_name}' section."
            )
            if (
                lines and lines[-1].strip() != ""
            ):  # Ensure a blank line before new section
                new_content_lines.extend(lines)
                new_content_lines.append("")
            else:
                new_content_lines.extend(lines)

            new_content_lines.append(
                f"## {section_name}"
            )  # Use original casing for new section
            new_content_lines.append("")
            new_content_lines.append(markdown_to_insert)
            new_content_lines.append("")
            inserted = True
        else:
            print(
                f"  Warning: Section '{section_name}' not found. Link not inserted.",
                file=sys.stderr,
            )
            return False

        if inserted:
            markdown_file_path.write_text(
                "\n".join(new_content_lines), encoding="utf-8"
            )
            return True

        return False  # Should not be reached if logic is correct

    except FileNotFoundError:
        print(
            f"Error: Markdown file not found at {markdown_file_path} during update.",
            file=sys.stderr,
        )
        return False
    except Exception as e:
        print(
            f"Error updating markdown file {markdown_file_path}: {e}", file=sys.stderr
        )
        # import traceback
        # traceback.print_exc() # For debugging
        return False
