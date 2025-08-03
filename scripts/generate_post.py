#!/usr/bin/env python3
"""
Generates a monthly markdown blog post file based on a template,
updating metadata fields for the specified month and year.

Assumes the following project structure:
project_root/
├── scripts/
│   └── generate_post.py  (this script)
└── content/
    └── posts/
        ├── 2025_xx_xx_template_links.md (default template)
        └── ... (other posts and generated output)
"""

import argparse
import calendar
import datetime
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple

# --- Configuration ---
# Default template filename (relative to content/posts)
DEFAULT_TEMPLATE_FILENAME = "2025_xx_xx_template_links.md"
# Default subdirectory within the project for templates and posts
DEFAULT_CONTENT_DIR = Path("content") / "posts"
# Default year (used if --year is not provided). None means use current year.
DEFAULT_YEAR_FALLBACK: Optional[int] = 2025
# Default template year (used for finding/replacing placeholders if different
# from target year - typically should match the year in the template filename)
TEMPLATE_PLACEHOLDER_YEAR: int = 2025
# ---------------------

# --- Type Hint Alias ---
MonthDetails = Tuple[int, int, str, str, int]


# --- Core Functions ---


def get_month_details(
    year: Optional[int], month: Optional[int]
) -> Optional[MonthDetails]:
    """
    Gets details for the specified month and year, or defaults to current.

    Args:
        year: The target year. Defaults to DEFAULT_YEAR_FALLBACK or current year.
        month: The target month (1-12). Defaults to current month.

    Returns:
        A tuple containing (year, month_num, month_name_full,
        month_name_lower, last_day_num), or None if date calculation fails.
    """
    try:
        now = datetime.date.today()
        target_year = (
            year
            if year is not None
            else (DEFAULT_YEAR_FALLBACK if DEFAULT_YEAR_FALLBACK else now.year)
        )
        target_month = month if month is not None else now.month

        # Basic validation (argparse handles choices, but good practice)
        if not 1 <= target_month <= 12:
            print(
                f"Error: Invalid month number '{target_month}'. Must be 1-12.",
                file=sys.stderr,
            )
            return None

        # Create a date object for the first day of the month
        first_day = datetime.date(target_year, target_month, 1)

        month_name_full = first_day.strftime("%B")
        month_name_lower = month_name_full.lower()

        # Calculate the last day of the month
        _, last_day_num = calendar.monthrange(target_year, target_month)

        return (
            target_year,
            target_month,
            month_name_full,
            month_name_lower,
            last_day_num,
        )

    except ValueError as e:
        print(
            f"Error calculating date details (invalid year/month?): {e}",
            file=sys.stderr,
        )
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred in get_month_details: {e}", file=sys.stderr
        )
        return None


def generate_filename(
    year: int, month_num: int, last_day_num: int, month_name_lower: str
) -> str:
    """
    Generates the filename string for the new markdown file.

    Args:
        year: The year.
        month_num: The month number (1-12).
        last_day_num: The last day of the month.
        month_name_lower: The lowercase full name of the month.

    Returns:
        The generated filename string (e.g., "2025_05_31_may_links.md").
    """
    return f"{year}_{month_num:02d}_{last_day_num:02d}_{month_name_lower}_links.md"


def build_replacements(
    year: int,
    month_num: int,
    month_name_full: str,
    month_name_lower: str,
    formatted_date: str,
) -> Dict[str, str]:
    """
    Builds the dictionary of specific text replacements for the template.

    Args:
        year: Target year.
        month_num: Target month number.
        month_name_full: Target full month name (e.g., "May").
        month_name_lower: Target lowercase month name (e.g., "may").
        formatted_date: Target date string (YYYY-MM-DD).

    Returns:
        A dictionary mapping template strings to their replacements.
    """
    tpl_year = TEMPLATE_PLACEHOLDER_YEAR
    # Uses specific patterns from the template to avoid accidental replacements
    return {
        # Metadata
        f"Title: Month summary - {{Month}} {tpl_year}": f"Title: Month summary - {month_name_full} {year}",
        # Using a unique placeholder date in template is safer
        f"Date: {tpl_year}-12-31": f"Date: {formatted_date}",
        f"Slug: {tpl_year}-{{month}}-links": f"Slug: {year}-{month_name_lower}-links",
        # Be specific about the path structure & placeholder year
        f"Header_Cover: /images/posts/{tpl_year}/{tpl_year}_xx_xx.jpg": f"Header_Cover: /images/posts/{year}/{year}_{month_num:02d}_xx.jpg",
        # Content Heading
        f"# {{Month}} {tpl_year}": f"# {month_name_full} {year}",
        # Add other specific replacements here if needed
    }


def create_markdown_file(
    template_path: Path, output_path: Path, replacements: Dict[str, str]
) -> bool:
    """
    Reads the template, applies replacements, and writes the new file.

    Args:
        template_path: Path object for the template markdown file.
        output_path: Path object where the new markdown file will be saved.
        replacements: A dictionary of {pattern_to_find: replacement_text}.

    Returns:
        True if successful, False otherwise.
    """
    try:
        # Ensure parent directory exists before writing
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Read template content
        content = template_path.read_text(encoding="utf-8")

        # Apply replacements
        for pattern, replacement in replacements.items():
            content = content.replace(pattern, replacement)

        # Write the new file
        output_path.write_text(content, encoding="utf-8")
        return True

    except FileNotFoundError:
        print(f"Error: Template file not found at '{template_path}'", file=sys.stderr)
        return False
    except IsADirectoryError:
        print(
            f"Error: Expected a file but found a directory at '{template_path}'",
            file=sys.stderr,
        )
        return False
    except IOError as e:
        print(
            f"Error reading template or writing output file '{output_path}': {e}",
            file=sys.stderr,
        )
        return False
    except OSError as e:
        print(f"Error creating directory for '{output_path}': {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(
            f"An unexpected error occurred during file creation: {e}", file=sys.stderr
        )
        return False


# --- Argument Parsing ---


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a monthly markdown blog post from a template.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-m",
        "--month",
        type=int,
        choices=range(1, 13),
        metavar="{1-12}",
        help="Month number to generate the post for (default: current month).",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        metavar="YYYY",
        help=f"Year to generate the post for (default: {DEFAULT_YEAR_FALLBACK or 'current year'}).",
    )
    parser.add_argument(
        "-t",
        "--template",
        default=DEFAULT_TEMPLATE_FILENAME,
        metavar="FILENAME",
        help=f"Filename of the template within '{DEFAULT_CONTENT_DIR}'.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        metavar="DIRECTORY",
        help=f"Output directory relative to project root "
        f"(default: '{DEFAULT_CONTENT_DIR}').",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists without asking.",
    )
    return parser.parse_args()


# --- Main Execution ---


def main():
    """Main function to orchestrate the markdown file generation."""
    args = parse_arguments()
    print("Starting monthly markdown generation...")

    # --- Determine Project Root and Paths ---
    try:
        # Assumes script is in project_root/scripts/
        script_path = Path(__file__).resolve()
        project_root = script_path.parent.parent
    except NameError:
        # Fallback for environments where __file__ might not be defined (e.g. interactive)
        project_root = Path.cwd()
        print(
            "Warning: Could not determine script location automatically, using current working directory as project root.",
            file=sys.stderr,
        )

    print(f"-> Project Root detected as: '{project_root}'")

    # Template path is within content/posts relative to project root
    template_path = project_root / DEFAULT_CONTENT_DIR / args.template

    # Determine output directory relative to project root
    if args.output_dir:
        # Treat output_dir relative to project root unless it's absolute
        output_dir_path = Path(args.output_dir)
        if not output_dir_path.is_absolute():
            output_dir_path = project_root / output_dir_path
        print(f"-> Using specified output directory: '{output_dir_path}'")
    else:
        # Default output is content/posts relative to project root
        output_dir_path = project_root / DEFAULT_CONTENT_DIR
        print(f"-> Using default output directory: '{output_dir_path}'")

    # --- Determine Target Date ---
    month_details = get_month_details(args.year, args.month)
    if not month_details:
        sys.exit(1)  # Exit if date calculation failed

    year, month_num, month_name_full, month_name_lower, last_day_num = month_details
    formatted_last_day = f"{year}-{month_num:02d}-{last_day_num:02d}"
    print(f"-> Generating post for: {month_name_full} {year}")

    # --- Prepare Output File Path ---
    output_filename = generate_filename(year, month_num, last_day_num, month_name_lower)
    output_path = output_dir_path / output_filename

    # --- Safety Checks ---
    if not template_path.is_file():
        print(
            f"\nError: Template file '{args.template}' not found or is not a file "
            f"at the expected location '{template_path}'",
            file=sys.stderr,
        )
        sys.exit(1)

    if output_path.exists():
        if not args.force:
            try:
                overwrite = input(
                    f"\nWarning: Output file '{output_path}' already exists. Overwrite? (y/N): "
                )
                if overwrite.lower() != "y":
                    print("Operation cancelled by user.")
                    sys.exit(0)
            except EOFError:  # Handle non-interactive environments
                print(
                    "\nWarning: Output file exists and cannot prompt for confirmation. Use --force to overwrite.",
                    file=sys.stderr,
                )
                sys.exit(1)
        print(f"-> Overwriting existing file: '{output_path}'")

    # --- Build Replacements & Create File ---
    replacements = build_replacements(
        year, month_num, month_name_full, month_name_lower, formatted_last_day
    )

    print(f"-> Reading template from: '{template_path}'")
    print(f"-> Preparing to write new file to: '{output_path}'")

    if create_markdown_file(template_path, output_path, replacements):
        print(f"\nSuccessfully created '{output_filename}' at '{output_path.parent}'!")
    else:
        print("\nFailed to create monthly post.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
