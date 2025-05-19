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
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from dotenv import load_dotenv
from loguru import logger


@dataclass
class CommandLineArgs:
    """
    Data class representing command line arguments for the blog automation tool.

    Attributes:
        target_markdown_file (str): Path to the target markdown blog post file
        urls (List[str]): List of URLs to process
        llm_provider (str): LLM provider to use (e.g., "openai")
        model_name (str): Model name for the LLM provider
        verbose (bool): Whether to enable verbose output
    """

    target_markdown_file: str
    urls: List[str]
    llm_provider: str
    model_name: str
    verbose: bool


def setup_logging(verbose: bool = False) -> None:
    """
    Configure logging with loguru.

    Args:
        verbose (bool): Whether to enable verbose logging
    """
    # Remove default logger
    logger.remove()

    # Add console logger with appropriate level
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG" if verbose else "INFO",
        colorize=True,
    )


def setup_paths() -> Tuple[Path, Path]:
    """
    Set up and validate the project paths.

    Returns:
        Tuple[Path, Path]: A tuple containing (PROJECT_ROOT, SCRIPT_DIR)
    """
    try:
        script_dir = Path(__file__).resolve().parent
        project_root = script_dir.parent.parent
        sys.path.append(str(project_root))
    except NameError:
        project_root = Path.cwd()
        script_dir = project_root / "scripts" / "blog_automation_2"
        if not (script_dir / "link_processing").exists():
            logger.error(
                "Could not reliably find the 'link_processing' directory. "
                "Please run from the project root or ensure script is in 'scripts/' subdir."
            )
            sys.exit(1)

    logger.debug(f"Project root: {project_root}")
    logger.debug(f"Script directory: {script_dir}")
    return project_root, script_dir


def load_environment(script_dir: Path) -> None:
    """
    Load environment variables from .env file.

    Args:
        script_dir (Path): Directory containing the .env file
    """
    dotenv_path = script_dir / ".env"
    if dotenv_path.exists():
        load_dotenv(dotenv_path)
        logger.debug(f"Loaded environment variables from {dotenv_path}")
    else:
        logger.warning(
            f".env file not found at {dotenv_path}. API keys should be set in environment."
        )


def parse_arguments() -> CommandLineArgs:
    """
    Parse command line arguments.

    Returns:
        CommandLineArgs: Dataclass containing parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Analyzes URLs, generates descriptions and categories, "
        "and inserts them into a markdown blog post.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "target_markdown_file",
        type=str,
        help="Path to the target markdown blog post file (relative to project root, e.g., content/posts/file.md).",
    )
    parser.add_argument(
        "urls",
        type=str,
        nargs="+",
        help="One or more URLs to process.",
    )
    parser.add_argument(
        "--llm-provider",
        choices=["openai"],
        default=os.getenv("DEFAULT_LLM_PROVIDER", "openai"),
        help="Specify the LLM provider to use. Can also be set via DEFAULT_LLM_PROVIDER in .env.",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default=os.getenv("DEFAULT_MODEL_NAME"),
        help="Specify the model name for the LLM provider. Overrides environment variables like OPENAI_MODEL_NAME.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output from the CrewAI tasks.",
    )

    args = parser.parse_args()
    return CommandLineArgs(
        target_markdown_file=args.target_markdown_file,
        urls=args.urls,
        llm_provider=args.llm_provider,
        model_name=args.model_name,
        verbose=args.verbose,
    )


def validate_markdown_file(project_root: Path, target_markdown_file: str) -> Path:
    """
    Validate that the target markdown file exists.

    Args:
        project_root (Path): Root directory of the project
        target_markdown_file (str): Path to the target markdown file

    Returns:
        Path: Resolved path to the markdown file

    Raises:
        SystemExit: If the file is not found
    """
    target_markdown_path = project_root / target_markdown_file
    if not target_markdown_path.is_file():
        logger.error(f"Target markdown file not found: {target_markdown_path}")
        sys.exit(1)
    return target_markdown_path
