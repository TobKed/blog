"""
Agents for the link processing crew.

This module defines the agents used in the link processing crew:
- LinkAnalyzerAgent: Analyzes URLs and generates descriptions
- LinkCategorizerAgent: Categorizes links based on their content
"""

import os
from pathlib import Path
from crewai import Agent
from langchain_openai import ChatOpenAI
from loguru import logger

from typing import Optional

from .tools import web_content_fetcher_tool
from .prompts import (
    LINK_ANALYZER_PROMPT,
    LINK_CATEGORIZER_PROMPT,
)


# Helper to load prompts from the 'prompts' directory (sibling to 'link_processing')
def load_prompt(filename: str) -> str:
    """Loads a prompt from the 'prompts' directory."""
    try:
        # Assumes 'prompts' is a sibling directory to 'link_processing'
        # and 'link_processing' is where this 'agents.py' file is.
        # So, Path(__file__).parent gives 'link_processing', .parent gives 'scripts', .parent gives 'project_root'
        # This needs to be relative to the script that *runs* this, or use absolute paths.
        # For simplicity, assuming 'prompts' is at PROJECT_ROOT/scripts/prompts
        # Corrected path based on SCRIPT_DIR from main script:
        # SCRIPT_DIR = project_root/scripts
        prompt_path = Path(__file__).resolve().parent.parent / "prompts" / filename
        if not prompt_path.exists():  # Fallback if structure is slightly different
            script_dir_path = Path(
                os.getenv("SCRIPT_DIR_PATH", Path(__file__).resolve().parent.parent)
            )
            prompt_path = script_dir_path / "prompts" / filename

        return prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}. Check paths.")
    except Exception as e:
        raise Exception(f"Error reading prompt file {prompt_path}: {e}")


class LinkAnalysisAgents:
    """Container for initializing and providing link analysis agents."""

    def __init__(
        self,
        llm_provider: str = "openai",
        model_name: Optional[str] = None,
        verbose: bool = False,
    ):
        """
        Initializes the LLM for the agents.

        Args:
            llm_provider (str): The LLM provider to use (e.g., "openai").
            model_name (Optional[str]): Specific model name. If None, uses provider's default or env var.
            verbose (bool): Whether agents should be verbose.
        """
        self.verbose = verbose
        if llm_provider.lower() == "openai":
            effective_model_name = model_name or os.getenv(
                "OPENAI_MODEL_NAME", "gpt-4o"
            )
            self.llm = ChatOpenAI(
                model_name=effective_model_name,
                temperature=0.2,  # Lower temperature for more deterministic analysis
                # openai_api_key=os.getenv("OPENAI_API_KEY") # Handled by ChatOpenAI if env var is set
            )
            logger.info(f"Using OpenAI model: {effective_model_name}")
        # Example for future extension:
        # elif llm_provider.lower() == "anthropic":
        #     effective_model_name = model_name or os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-opus-20240229")
        #     self.llm = ChatAnthropic(
        #         model=effective_model_name,
        #         temperature=0.2,
        #         # anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
        #     )
        #     print(f"Using Anthropic model: {effective_model_name}")
        else:
            raise ValueError(f"Unsupported LLM provider for agents: {llm_provider}")

    def content_analyzer_agent(self) -> Agent:
        """
        Agent responsible for fetching web content, extracting title,
        generating a summary, and identifying keywords.
        """
        return Agent(
            role="Expert Web Content Analyst",
            goal="Fetch web page content using the provided URL. Then, from the fetched content, "
            "accurately determine the page title, generate a concise and meaningful summary (1-3 sentences), "
            "and identify 3-5 relevant keywords. Output this information in a structured JSON format.",
            backstory=(
                "You are a meticulous analyst with a keen eye for detail and an expert in web content. "
                "You specialize in dissecting web pages to understand their core essence, "
                "providing structured and useful information for content curation and summarization. "
                "You always use your tools to fetch fresh content for analysis."
            ),
            llm=self.llm,
            tools=[
                web_content_fetcher_tool
            ],  # Agent needs this tool to get web content
            verbose=self.verbose,
            allow_delegation=False,  # This agent completes its task independently
            # memory=True # Consider if memory is needed across multiple interactions with the same agent instance
        )

    def link_categorizer_agent(self) -> Agent:
        """
        Agent responsible for categorizing a link based on its analyzed content
        against a list of available blog sections.
        """
        return Agent(
            role="Intelligent Blog Content Categorizer",
            goal="Assign a web link to the most appropriate section of a tech-focused blog. "
            "Base your decision on the link's title, description, and keywords, "
            "selecting from a predefined list of available blog sections. "
            "Output only the chosen section name.",
            backstory=(
                "You are an expert librarian and content curator for a popular tech blog. "
                "You have an uncanny ability to quickly understand the relevance of an article "
                "and slot it into the perfect category to help readers discover relevant information. "
                "You are very precise and only choose from the provided list of sections."
            ),
            llm=self.llm,
            tools=[],  # This agent primarily processes information, doesn't need external tools
            verbose=self.verbose,
            allow_delegation=False,
        )


def create_link_analyzer_agent(
    llm_provider: str,
    model_name: Optional[str] = None,
    verbose: bool = False,
) -> Agent:
    """
    Create a LinkAnalyzerAgent for analyzing URLs and generating descriptions.

    Args:
        llm_provider (str): The LLM provider to use (e.g., 'openai', 'anthropic')
        model_name (Optional[str]): The specific model to use
        verbose (bool): Whether to enable verbose output

    Returns:
        Agent: The configured LinkAnalyzerAgent
    """
    # Determine effective model name based on provider
    effective_model_name = model_name or (
        "gpt-4-turbo-preview" if llm_provider == "openai" else "claude-3-opus-20240229"
    )

    if llm_provider == "openai":
        logger.info(f"Using OpenAI model: {effective_model_name}")
    # elif llm_provider == "anthropic":
    #     logger.info(f"Using Anthropic model: {effective_model_name}")

    return Agent(
        role="Link Analyzer",
        goal="Analyze URLs and generate accurate, concise descriptions",
        backstory="""You are an expert at analyzing web content and creating
        clear, informative descriptions. You have a keen eye for detail and
        can quickly identify the key points of any content.""",
        verbose=verbose,
        llm_provider=llm_provider,
        model_name=effective_model_name,
        allow_delegation=False,
        prompt=LINK_ANALYZER_PROMPT,
    )


def create_link_categorizer_agent(
    llm_provider: str,
    model_name: Optional[str] = None,
    verbose: bool = False,
) -> Agent:
    """
    Create a LinkCategorizerAgent for categorizing links.

    Args:
        llm_provider (str): The LLM provider to use (e.g., 'openai', 'anthropic')
        model_name (Optional[str]): The specific model to use
        verbose (bool): Whether to enable verbose output

    Returns:
        Agent: The configured LinkCategorizerAgent
    """
    # Determine effective model name based on provider
    effective_model_name = model_name or (
        "gpt-4-turbo-preview" if llm_provider == "openai" else "claude-3-opus-20240229"
    )

    return Agent(
        role="Link Categorizer",
        goal="Categorize links into appropriate sections based on their content",
        backstory="""You are an expert at organizing and categorizing content.
        You have a deep understanding of various topics and can quickly determine
        the most appropriate category for any piece of content.""",
        verbose=verbose,
        llm_provider=llm_provider,
        model_name=effective_model_name,
        allow_delegation=False,
        prompt=LINK_CATEGORIZER_PROMPT,
    )
