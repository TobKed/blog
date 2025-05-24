import asyncio
import json
import os
from abc import ABC, abstractmethod
from pprint import pprint as print
from typing import List, Optional

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CrawlResult, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel, Field


class PageSummary(BaseModel):
    title: str = Field(..., description="Title of the page.")
    summary: str = Field(..., description="Summary of the page.")
    brief_summary: str = Field(..., description="Brief summary of the page.")
    keywords: list = Field(..., description="Keywords assigned to the page.")
    section: str = Field(..., description="Section of the page.")


class PageAnalysisOutout(PageSummary):
    og_title: str = Field(..., description="Original title of the page.")
    og_description: Optional[str] = Field(
        ..., description="Original description of the page."
    )


class UrlAnalyserBase(ABC):
    @abstractmethod
    def analyze_url(
        self, url: str, available_sections: List[str]
    ) -> Optional[PageAnalysisOutout]:
        pass


class UrlAnalyser(UrlAnalyserBase):
    def analyze_url(
        self, url: str, available_sections: List[str]
    ) -> Optional[PageAnalysisOutout]:
        """
        Analyze a URL and return a PageSummary object containing extracted information.

        Args:
            url (str): The URL to analyze
            available_sections (List[str]): List of available sections to categorize the page

        Returns:
            Optional[PageSummary]: A PageSummary object if successful, None if analysis fails
        """

        async def _analyze_url_async() -> Optional[PageSummary]:
            llm_strategy = LLMExtractionStrategy(
                llm_config=LLMConfig(
                    provider="openai/gpt-4o", api_token=os.getenv("OPENAI_API_KEY")
                ),
                schema=PageSummary.model_json_schema(),
                extraction_type="schema",
                verbose=True,
                instruction="From the crawled content, extract the following details: "
                "1. Title of the page "
                "2. Summary of the page, which is a detailed summary "
                "3. Brief summary of the page, which is a paragraph text "
                "4. Keywords assigned to the page, which is a list of keywords. "
                f"5. Section of the page. One of the following: {available_sections}"
                "The extracted JSON format should look like this: "
                '{ "title": "Page Title", "summary": "Detailed summary of the page.", "brief_summary": "Brief summary in a paragraph.", "keywords": ["keyword1", "keyword2", "keyword3"], section="Section name" }',
            )

            config = CrawlerRunConfig(
                exclude_external_links=True,
                exclude_internal_links=True,
                exclude_external_images=True,
                exclude_social_media_links=True,
                word_count_threshold=20,
                extraction_strategy=llm_strategy,
            )

            async with AsyncWebCrawler() as crawler:
                results: List[CrawlResult] = await crawler.arun(url=url, config=config)
                if results:
                    raw_summaries = json.loads(results[0].extracted_content)
                    og_title = results[0].metadata["title"]
                    og_description = results[0].metadata["description"]
                    page_summaries = [
                        PageAnalysisOutout(
                            **summary, og_title=og_title, og_description=og_description
                        )
                        for summary in raw_summaries
                    ]
                    if page_summaries:
                        return page_summaries[0]
            return None

        try:
            return asyncio.run(_analyze_url_async())
        except Exception as e:
            print(f"Error analyzing URL: {e}")
            return None
