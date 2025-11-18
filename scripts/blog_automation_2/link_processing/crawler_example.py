import asyncio
import json
import os
from pprint import pprint as print
from typing import List

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CrawlResult, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel, Field

url = r"https://github.com/unclecode/crawl4ai"


class PageSummary(BaseModel):
    title: str = Field(..., description="Title of the page.")
    summary: str = Field(..., description="Summary of the page.")
    brief_summary: str = Field(..., description="Brief summary of the page.")
    keywords: list = Field(..., description="Keywords assigned to the page.")
    section: str = Field(..., description="Section of the page.")


async def main():
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
        "5. Section of the page. One of the following: Python, Django, AI, Articles, Other"
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
            raw_summaries = json.loads(results.extracted_content)
            page_summaries = [PageSummary(**summary) for summary in raw_summaries]
            print(page_summaries)
            print(f'title:, {results.metadata["title"]}')
            print(f'description:", {results.metadata["description"]}')


if __name__ == "__main__":
    asyncio.run(main())
