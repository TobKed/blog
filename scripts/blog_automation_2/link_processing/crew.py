"""
Defines the CrewAI crew for processing links.
Orchestrates agents and tasks for analysis and categorization.
"""

import json
import traceback  # Added for better error logging
from crewai import Crew, Process

# Import CrewOutput if you need to explicitly check its type
# from crewai.outputs import CrewOutput
from .agents import LinkAnalysisAgents
from .tasks import LinkAnalysisTasks
from typing import Optional, Union


class LinkProcessingCrew:
    """
    Manages the crew of agents and tasks for analyzing and categorizing URLs.
    """

    def __init__(
        self,
        llm_provider: str = "openai",
        model_name: Optional[str] = None,
        verbose_level: int = 0,
    ):
        """
        Initializes agents and tasks providers.

        Args:
            llm_provider (str): The LLM provider (e.g., "openai").
            model_name (Optional[str]): Specific model name for the LLM.
            verbose_level (int): Verbosity level for the crew (0=silent, >0=verbose).
                                 Used to set boolean flags for CrewAI components.
        """
        self.crew_verbose_bool = verbose_level > 0
        self.agents_provider = LinkAnalysisAgents(
            llm_provider=llm_provider,
            model_name=model_name,
            verbose=self.crew_verbose_bool,
        )
        self.tasks_provider = LinkAnalysisTasks()

    def _format_markdown(self, title: str, url: str, description: str) -> str:
        """Formats the extracted information into a markdown link string."""
        safe_title = title.replace("[", "(").replace("]", ")")
        safe_description = description.replace("\n", " ").strip()
        return f"### [{safe_title}]({url})\n\n> {safe_description}"

    def process_url(self, url: str, available_blog_sections: list) -> Optional[dict]:
        """
        Processes a single URL to analyze its content, categorize it,
        and prepare markdown.

        Args:
            url (str): The URL to process.
            available_blog_sections (list): A list of section names available in the blog.

        Returns:
            A dictionary containing processed data (url, title, description,
            keywords, category, markdown_string), or None if processing fails.
        """
        try:
            analyzer_agent = self.agents_provider.content_analyzer_agent()
            categorizer_agent = self.agents_provider.link_categorizer_agent()

            # Task 1: Analyze Web Content
            analyze_task = self.tasks_provider.analyze_web_content_task(
                analyzer_agent, url
            )

            analysis_crew = Crew(
                agents=[analyzer_agent],
                tasks=[analyze_task],
                process=Process.sequential,
                verbose=self.crew_verbose_bool,
            )

            print(f"  [Crew] Kicking off analysis for URL: {url}")
            analysis_result_object = None  # Renamed to reflect it's an object
            try:
                # kickoff returns a CrewOutput object (or similar based on version)
                analysis_result_object = analysis_crew.kickoff(inputs={"url": url})
            except Exception as e:
                print(f"  [Crew] Error during analysis task execution for {url}:")
                traceback.print_exc()
                return None

            if not analysis_result_object:
                print(f"  [Crew] Analysis task for {url} returned no result.")
                return None

            # --- FIX: Extract raw string from CrewOutput object ---
            # Convert the result object to string or access its raw attribute
            # Using str() is generally safer as it relies on the object's __str__ method
            analysis_result_raw_str = str(analysis_result_object)
            # Alternatively, if CrewOutput has a .raw attribute:
            # analysis_result_raw_str = analysis_result_object.raw
            # --- End Fix ---

            print(
                f"  [Crew] Analysis raw output: {analysis_result_raw_str[:200]}..."
            )  # Now slicing the string

            # Post-process analysis result (using the extracted raw string)
            analysis_data = None
            title = None
            description = None
            keywords = []
            try:
                # Basic cleaning attempt on the raw string:
                cleaned_json_str = analysis_result_raw_str  # Start with the raw string
                if isinstance(cleaned_json_str, str):
                    if "```json" in cleaned_json_str:
                        cleaned_json_str = (
                            cleaned_json_str.split("```json")[1].split("```")[0].strip()
                        )
                    elif (
                        "```" in cleaned_json_str
                        and not cleaned_json_str.strip().startswith("{")
                    ):
                        cleaned_json_str = cleaned_json_str.split("```")[1].strip()
                    analysis_data = json.loads(cleaned_json_str)
                # If the object itself somehow held a dict (less likely now, but keep check)
                elif isinstance(analysis_result_object, dict):
                    analysis_data = analysis_result_object  # Should not happen if kickoff returns CrewOutput
                else:
                    print(
                        f"  [Crew] Error: Unexpected analysis result type after conversion: {type(cleaned_json_str)}"
                    )
                    return None

                title = analysis_data.get("title")
                description = analysis_data.get("description")
                keywords = analysis_data.get("keywords", [])

                if not title or not description:
                    print(
                        f"  [Crew] Error: Could not extract required fields (title, description) "
                        f"from analysis for {url}. Parsed Data: {analysis_data}"
                    )
                    return None
                print(
                    f"  [Crew] Parsed analysis - Title: {title}, Desc: {description[:50]}..."
                )

            except json.JSONDecodeError as e:
                print(
                    f"  [Crew] Error: Could not parse JSON from analysis result for {url}. "
                    f"Detail: {e}. Raw output used for parsing: '{cleaned_json_str}'"
                )
                return None
            except Exception as e:
                print(
                    f"  [Crew] Error processing parsed analysis result for {url}: {e}. Data: '{cleaned_json_str}'"
                )
                traceback.print_exc()
                return None

            # Task 2: Categorize the Link
            categorize_task = self.tasks_provider.categorize_link_task(
                agent=categorizer_agent,
                title=title,
                description=description,
                keywords=keywords,
                available_sections=available_blog_sections,
            )

            categorization_crew = Crew(
                agents=[categorizer_agent],
                tasks=[categorize_task],
                process=Process.sequential,
                verbose=self.crew_verbose_bool,
            )

            print(f"  [Crew] Kicking off categorization for: {title}")
            category_result_object = None  # Renamed
            try:
                category_result_object = categorization_crew.kickoff()
            except Exception as e:
                print(f"  [Crew] Error during categorization task execution for {url}:")
                traceback.print_exc()
                category_result_object = "Other stuff"  # Fallback

            # --- FIX: Extract raw string from result object ---
            category_result_raw_str = (
                str(category_result_object) if category_result_object else None
            )
            # --- End Fix ---

            if not category_result_raw_str:
                print(
                    f"  [Crew] Categorization task for {url} returned no result. Defaulting to 'Other stuff'."
                )
                final_category = "Other stuff"
            else:
                # Clean the extracted string
                final_category = (
                    category_result_raw_str.strip().replace("'", "").replace('"', "")
                )
                print(
                    f"  [Crew] Categorization raw output: {category_result_raw_str}, Cleaned: {final_category}"
                )

                if (
                    available_blog_sections
                    and final_category not in available_blog_sections
                    and final_category != "Other stuff"
                ):
                    print(
                        f"  [Crew] Warning: LLM chose category '{final_category}' which is not in available sections. "
                        "Consider if 'Other stuff' is more appropriate or if prompt needs adjustment."
                    )

            # Final processing: Format for markdown
            formatted_md = self._format_markdown(title, url, description)

            return {
                "url": url,
                "title": title,
                "description": description,
                "keywords": keywords,
                "category": final_category,
                "markdown_string": formatted_md,
            }
        except Exception as e:
            print(f"  [Crew] Unexpected error during overall processing of URL {url}:")
            traceback.print_exc()
            return None  # Indicate failure for this URL
