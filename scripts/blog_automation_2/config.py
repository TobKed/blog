#!/usr/bin/env python3
"""
Configuration module for the blog automation tool.

This module handles:
- Path setup and validation
- Environment variable loading
- Command line argument parsing
- Global configuration variables
"""
import argparse
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
from loguru import logger


@dataclass
class CommandLineArgs:
    """
    Command line arguments for the script.

    Attributes:
        markdown_file (str): Path to the target markdown file
        urls (List[str]): List of URLs to process
        verbose (bool): Whether to enable verbose logging
        llm_provider (str): The LLM provider to use
        model_name (Optional[str]): The specific model to use
    """

    markdown_file: str
    urls: List[str]
    verbose: bool
    llm_provider: str
    model_name: Optional[str]


@dataclass
class Paths:
    """
    Paths used by the script.

    Attributes:
        project_root (Path): Root directory of the project
        script_dir (Path): Directory containing the scripts
        data_dir (Path): Directory for storing data files
    """

    project_root: Path
    script_dir: Path
    data_dir: Path


def parse_arguments() -> CommandLineArgs:
    """
    Parse command line arguments.

    Returns:
        CommandLineArgs: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Process URLs and add them to a markdown blog post."
    )
    parser.add_argument(
        "markdown_file",
        help="Path to the target markdown file",
    )
    parser.add_argument(
        "urls",
        nargs="+",
        help="URLs to process",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    parser.add_argument(
        "--llm-provider",
        default="openai",
        choices=["openai", "anthropic"],
        help="LLM provider to use",
    )
    parser.add_argument(
        "--model-name",
        help="Specific model to use (optional)",
    )

    args = parser.parse_args()
    return CommandLineArgs(
        markdown_file=args.markdown_file,
        urls=args.urls,
        verbose=args.verbose,
        llm_provider=args.llm_provider,
        model_name=args.model_name,
    )


def load_environment() -> None:
    """Load environment variables from .env file."""
    # Get the script directory
    script_dir = Path(__file__).parent

    # Load environment variables from .env file
    env_file = script_dir.parent.parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        logger.debug(f"Loaded environment variables from {env_file}")
    else:
        logger.warning(f"No .env file found at {env_file}")


def setup_paths() -> Paths:
    """
    Setup paths used by the script.

    Returns:
        Paths: Paths used by the script
    """
    # Get the project root directory (3 levels up from this file)
    project_root = Path(__file__).parent.parent.parent
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"

    # Create data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)

    paths = Paths(
        project_root=project_root,
        script_dir=script_dir,
        data_dir=data_dir,
    )

    logger.info(f"Paths setup: {paths}")

    return paths


def setup_logging(verbose: bool = False) -> None:
    """
    Setup logging configuration.

    Args:
        verbose (bool): Whether to enable verbose logging
    """
    # Remove default logger
    logger.remove()

    # Add console logger
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG" if verbose else "INFO",
    )

    # Add file logger
    log_file = Path(__file__).parent / "link_processor.log"
    logger.add(
        log_file,
        rotation="1 day",
        retention="7 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG" if verbose else "INFO",
    )


def validate_markdown_file(markdown_file: str | Path) -> Path:
    """
    Validate the target markdown file.

    Args:
        markdown_file (str): Path to the target markdown file

    Returns:
        Path: Path object for the target markdown file

    Raises:
        FileNotFoundError: If the markdown file doesn't exist
    """
    markdown_path = Path(markdown_file)
    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    return markdown_path
