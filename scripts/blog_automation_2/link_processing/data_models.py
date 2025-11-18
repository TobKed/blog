"""
Pydantic models for the blog automation tool.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class PageSummary(BaseModel):
    title: str = Field(..., description="Title of the page.")
    summary: str = Field(..., description="Summary of the page.")
    brief_summary: str = Field(..., description="Brief summary of the page.")
    keywords: list = Field(..., description="Keywords assigned to the page.")
    section: str = Field(..., description="Section of the page.")


class PageAnalysisOutout(PageSummary):
    og_title: Optional[str] = Field(..., description="Original title of the page.")
    og_description: Optional[str] = Field(
        ..., description="Original description of the page."
    )
