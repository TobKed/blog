"""
Custom exceptions for the blog automation tool.
"""


class BlogAutomationError(Exception):
    """Base exception for all errors in this tool."""

    pass


class DuplicateLinkError(BlogAutomationError):
    """Raised when a link already exists in the registry."""

    pass


class SectionNotFoundError(BlogAutomationError):
    """Raised when a target section is not found in the markdown file."""

    pass


class URLProcessingError(BlogAutomationError):
    """Raised when there is an error processing or analyzing a URL."""

    pass
