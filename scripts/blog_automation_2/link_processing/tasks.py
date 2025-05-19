"""
Defines the CrewAI tasks for link processing.
"""

from crewai import Task, Agent
from .agents import LinkAnalysisAgents, load_prompt


class LinkAnalysisTasks:
    """Container for link analysis and categorization tasks."""

    def __init__(self):
        # Load prompts during initialization
        self.analyze_web_content_prompt_template = load_prompt(
            "analyze_content_prompt.txt"
        )
        self.categorize_link_prompt_template = load_prompt("categorize_link_prompt.txt")

    def analyze_web_content_task(self, agent: Agent, url: str) -> Task:
        """
        Task for an agent to fetch, analyze web content from a URL,
        and extract title, description, and keywords.
        """
        return Task(
            description=(
                f"Fetch the content of the web page at the URL: {url}. "
                "After fetching the content, analyze it thoroughly. "
                "Your goal is to determine the page's title, generate a concise summary (1-3 sentences), "
                "and identify 3-5 relevant keywords. "
                "Adhere to the following detailed guidelines for content analysis and JSON output format: "
                f"\n\n{self.analyze_web_content_prompt_template}"
            ),
            expected_output=(
                "A single JSON string adhering to the specified format: "
                '{ "title": "string", "description": "string", "keywords": ["string", ...] }. '
                "Ensure the JSON is valid."
            ),
            agent=agent,
            async_execution=False,
            instructions=self.analyze_web_content_prompt_template,
        )

    def categorize_link_task(
        self,
        agent: Agent,
        title: str,
        description: str,
        keywords: list,
        available_sections: list,
    ) -> Task:
        """
        Task for an agent to categorize a link based on its title, description,
        keywords, and a list of available blog sections.
        """
        # Prepare the dynamic parts of the prompt
        formatted_keywords = (
            ", ".join(f'"{k}"' for k in keywords) if keywords else "N/A"
        )
        # --- FIX: Format available sections as a simple comma-separated list ---
        formatted_sections = (
            ", ".join(available_sections)
            if available_sections
            else "No specific sections provided (use general knowledge or 'Other stuff')."
        )
        # --- End Fix ---

        # Format the prompt template with the actual data
        task_instructions = self.categorize_link_prompt_template.format(
            title=title,
            description=description,
            keywords=formatted_keywords,
            available_blog_sections=formatted_sections,  # Use the simplified format
        )

        return Task(
            description=(
                "Categorize the web link based on its provided title, description, and keywords. "
                "You must choose the single most suitable section from the list of available blog sections. "
                "Your output should be only the name of the chosen section."
                "Adhere to the following detailed guidelines for content analysis and JSON output format: "
                f"\n\n{task_instructions}"
            ),
            expected_output=(
                "The name of the single most appropriate blog section as a plain string (e.g., 'Python', 'AI', 'Other stuff')."
            ),
            agent=agent,
            instructions=task_instructions,  # Pass the fully formatted prompt
            async_execution=False,
        )
