"""
CrewAI-based system for processing and categorizing links.

This module provides a crew-based system for:
1. Analyzing URLs and generating descriptions
2. Categorizing links based on their content
"""

import json
import traceback
from typing import Dict, List, Optional

from crewai import Crew, CrewOutput, Process
from loguru import logger

from .agents import create_link_analyzer_agent, create_link_categorizer_agent
from .tasks import (
    AnalysisOutput,
    CategorizationOutput,
    create_analysis_task,
    create_categorization_task,
)


class LinkProcessingCrew:
    """
    Crew for processing and categorizing links.

    This crew consists of two agents:
    1. LinkAnalyzerAgent: Analyzes URLs and generates descriptions
    2. LinkCategorizerAgent: Categorizes links based on their content
    """

    def __init__(
        self,
        llm_provider: str = "openai",
        model_name: Optional[str] = None,
        verbose_level: int = 0,
    ):
        """
        Initialize the LinkProcessingCrew.

        Args:
            llm_provider (str): The LLM provider to use (e.g., 'openai', 'anthropic')
            model_name (Optional[str]): The specific model to use
            verbose_level (int): Level of verbosity (0-2)
        """
        self.llm_provider = llm_provider
        self.model_name = model_name
        self.verbose = verbose_level > 0

        # Create agents
        self.analyzer_agent = create_link_analyzer_agent(
            llm_provider=llm_provider,
            model_name=model_name,
            verbose=self.verbose,
        )

        self.categorizer_agent = create_link_categorizer_agent(
            llm_provider=llm_provider,
            model_name=model_name,
            verbose=self.verbose,
        )

    def process_url(self, url: str, available_sections: List[str]) -> Optional[Dict]:
        """
        Process a URL through the crew system.

        Args:
            url (str): The URL to process
            available_sections (List[str]): List of available sections for categorization

        Returns:
            Optional[Dict]: Dictionary containing processed data or None if processing failed
        """
        try:
            # 1. Create tasks with their respective agents
            analysis_task = create_analysis_task(url, self.analyzer_agent)
            categorization_task = create_categorization_task(
                url, available_sections, self.categorizer_agent
            )

            # 2. Create and run the crew
            crew = Crew(
                agents=[self.analyzer_agent, self.categorizer_agent],
                tasks=[analysis_task, categorization_task],
                verbose=self.verbose,
                process=Process.sequential,
            )

            logger.info(f"Starting analysis for URL: {url}")
            result: CrewOutput = crew.kickoff()

            if not result:
                logger.error(f"Analysis task for {url} returned no result.")
                return None

            # 3. Parse the result using Pydantic models
            try:
                # Get the parsed Pydantic models directly from task outputs
                analysis_output: AnalysisOutput = analysis_task.output.pydantic
                categorization_output: CategorizationOutput = (
                    categorization_task.output.pydantic
                )

                logger.debug(f"Analysis output: {analysis_output}")
                logger.debug(f"Categorization output: {categorization_output}")

                # Extract data from the Pydantic models
                title = analysis_output.title
                description = analysis_output.description
                keywords = analysis_output.keywords
                category = categorization_output.category

                # Validate category against available sections
                if category not in available_sections:
                    logger.warning(
                        f"Category '{category}' not in available sections, using 'Other stuff'"
                    )
                    category = "Other stuff"

                # Combine results
                processed_data = {
                    "title": title,
                    "description": description,
                    "category": category,
                    "keywords": keywords,
                    "markdown_string": f"### [{title}]({url})\n\n{description}",
                }

                logger.debug(f"Processed data: {processed_data}")
                return processed_data

            except Exception as e:
                logger.exception(f"Error parsing crew results for {url}")
                return None

        except Exception as e:
            logger.exception(f"Unexpected error during overall processing of URL {url}")
            return None
