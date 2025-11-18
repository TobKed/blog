"""
Module for formatting link metadata into markdown strings.
"""

from abc import ABC, abstractmethod
from typing import Optional

from .data_models import PageAnalysisOutout
from .url_processor import LinkMetadata, LinkType


class BaseMarkdownFormatter(ABC):
    """Base class for all markdown formatters."""

    @abstractmethod
    def format(
        self,
        metadata: LinkMetadata,
        analysis_result: PageAnalysisOutout,
    ) -> tuple[str, str]:
        """
        Formats the link metadata and analysis result into a markdown string.

        Args:
            metadata (LinkMetadata): The processed link metadata.
            analysis_result (PageAnalysisOutout): The analysis result from the URL.

        Returns:
            tuple[str, str]: A tuple containing the formatted markdown string and the suggested section name.
        """
        pass


class ArticleMarkdownFormatter(BaseMarkdownFormatter):
    """Formats an article link into a markdown string."""

    def format(
        self,
        metadata: LinkMetadata,
        analysis_result: PageAnalysisOutout,
    ) -> tuple[str, str]:
        title = metadata.title or analysis_result.og_title or analysis_result.title
        description = analysis_result.og_description or analysis_result.summary

        markdown_string = (
            f"### [{title}]({metadata.cleaned_url})\n\n"
            f"> {description}\n\n"
            f"#### AI generated summary\n\n"
            f"{analysis_result.brief_summary}"
        )
        return markdown_string, analysis_result.section


class YouTubeVideoMarkdownFormatter(BaseMarkdownFormatter):
    """Formats a YouTube video link into a markdown string."""

    def format(
        self,
        metadata: LinkMetadata,
        analysis_result: PageAnalysisOutout,
    ) -> tuple[str, str]:
        title = analysis_result.og_title or analysis_result.title
        description = analysis_result.og_description or analysis_result.summary

        if metadata.is_youtube_playlist:
            markdown_string = (
                f"### [{title}]({metadata.cleaned_url})\n\n> {description}"
            )
            section = "Videos"
        elif metadata.video_id:
            video_id_to_embed = metadata.video_id
            markdown_string = (
                f"### [{title}](https://www.youtube.com/watch?v={video_id_to_embed})\n\n"
                f'<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">\n'
                f'    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/{video_id_to_embed}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n'
                f"</div>\n\n"
                f"#### AI generated summary\n\n"
                f"{analysis_result.brief_summary}"
            )
            section = "Videos"
        else:
            # Fallback to article format if it's a YouTube link but not a video or playlist
            return ArticleMarkdownFormatter().format(metadata, analysis_result)

        return markdown_string, section


class OtherVideoMarkdownFormatter(BaseMarkdownFormatter):
    """Formats a generic video link (non-YouTube) into a markdown string."""

    def format(
        self,
        metadata: LinkMetadata,
        analysis_result: PageAnalysisOutout,
    ) -> tuple[str, str]:
        # For other video types, we'll treat them like articles for now,
        # as embedding might require specific platform handling.
        return ArticleMarkdownFormatter().format(metadata, analysis_result)


class UnknownMarkdownFormatter(BaseMarkdownFormatter):
    """Formats an unknown link type into a markdown string (fallback to article)."""

    def format(
        self,
        metadata: LinkMetadata,
        analysis_result: PageAnalysisOutout,
    ) -> tuple[str, str]:
        return ArticleMarkdownFormatter().format(metadata, analysis_result)


def get_formatter(link_type: LinkType) -> BaseMarkdownFormatter:
    """
    Returns the appropriate markdown formatter for a given link type.
    """
    if link_type == LinkType.YOUTUBE:
        return YouTubeVideoMarkdownFormatter()
    elif link_type == LinkType.VIDEO:
        return OtherVideoMarkdownFormatter()
    elif link_type == LinkType.ARTICLE:
        return ArticleMarkdownFormatter()
    else:
        return UnknownMarkdownFormatter()
