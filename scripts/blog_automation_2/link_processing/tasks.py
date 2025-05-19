"""
Tasks for the link processing crew.

This module defines the tasks used in the link processing crew:
- Analysis task: Analyzes URLs and generates descriptions
- Categorization task: Categorizes links based on their content
"""

from typing import List

from crewai import Task
from loguru import logger
from pydantic import BaseModel, Field

from .prompts import (
    LINK_ANALYZER_PROMPT,
    LINK_CATEGORIZER_PROMPT,
)


class AnalysisOutput(BaseModel):
    """Output model for the analysis task."""

    title: str = Field(..., description="A clear, concise title for the content")
    description: str = Field(
        ...,
        description="A detailed description of the content, highlighting key points",
    )
    keywords: List[str] = Field(..., description="A list of relevant keywords")


class CategorizationOutput(BaseModel):
    """Output model for the categorization task."""

    category: str = Field(..., description="The chosen category/section name")


def create_analysis_task(url: str, agent) -> Task:
    """
    Create a task for analyzing a URL and generating a description.

    Args:
        url (str): The URL to analyze
        agent: The agent that will perform the analysis

    Returns:
        Task: The configured analysis task
    """
    return Task(
        description=f"""Analyze the following URL and provide a detailed description:
        URL: {url}

        {LINK_ANALYZER_PROMPT}""",
        agent=agent,
        expected_output="""A JSON object containing:
        - title: A clear, concise title
        - description: A detailed description
        - keywords: A list of relevant keywords""",
        output_pydantic=AnalysisOutput,
    )


def create_categorization_task(url: str, available_sections: List[str], agent) -> Task:
    """
    Create a task for categorizing a URL into an appropriate section.

    Args:
        url (str): The URL to categorize
        available_sections (List[str]): List of available sections for categorization
        agent: The agent that will perform the categorization

    Returns:
        Task: The configured categorization task
    """
    sections_str = "\n".join(f"- {section}" for section in available_sections)

    return Task(
        description=f"""Categorize the following URL into the most appropriate section:
        URL: {url}

        {LINK_CATEGORIZER_PROMPT.format(available_sections=sections_str)}""",
        agent=agent,
        expected_output="A single string containing the chosen section name",
        output_pydantic=CategorizationOutput,
    )
