#!/usr/bin/env python3
"""
Resizes images in a specified directory.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image

# --- Configuration ---
DEFAULT_MAX_SIZE = (1024, 1024)
DEFAULT_DPI = (300, 300)
DEFAULT_INPUT_DIR_NAME = "input"
DEFAULT_OUTPUT_DIR_NAME = "output"


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Resize images in a directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Determine default paths based on script location
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent

    default_input = script_dir / DEFAULT_INPUT_DIR_NAME
    default_output = script_dir / DEFAULT_OUTPUT_DIR_NAME

    parser.add_argument(
        "-i",
        "--input-dir",
        type=Path,
        default=default_input,
        help="Directory containing input images.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=default_output,
        help="Directory to save resized images.",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_MAX_SIZE[0],
        help="Maximum width of the resized image.",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=DEFAULT_MAX_SIZE[1],
        help="Maximum height of the resized image.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=DEFAULT_DPI[0],
        help="DPI for the output image.",
    )

    return parser.parse_args()


def resize_images(
    input_dir: Path, output_dir: Path, max_size: tuple[int, int], dpi: tuple[int, int]
):
    """
    Resizes images from input_dir and saves them to output_dir.
    """
    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Processing images from '{input_dir}' to '{output_dir}'...")
    print(f"Max size: {max_size}, DPI: {dpi}")

    count = 0
    for input_img_path in input_dir.iterdir():
        if input_img_path.is_file() and input_img_path.name != ".DS_Store":
            try:
                output_img_path = output_dir / input_img_path.name

                with Image.open(input_img_path) as im:
                    im.thumbnail(max_size)
                    im.save(output_img_path, dpi=dpi)
                    print(f"  Processed: {input_img_path.name}")
                    count += 1
            except Exception as e:
                print(f"  Error processing {input_img_path.name}: {e}", file=sys.stderr)

    print(f"\nDone. Processed {count} images.")


def main():
    args = parse_arguments()

    max_size = (args.width, args.height)
    dpi = (args.dpi, args.dpi)

    resize_images(args.input_dir, args.output_dir, max_size, dpi)


if __name__ == "__main__":
    main()
