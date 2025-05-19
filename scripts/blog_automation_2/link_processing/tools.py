"""
Custom or pre-configured tools for CrewAI agents.
"""

from crewai_tools import WebsiteSearchTool

# Initialize any tools that your agents will use.
# WebsiteSearchTool is a good general-purpose tool for fetching web content.
# You can configure it further if needed, e.g., with specific headers or a search backend.
# For now, default initialization is fine.
# Ensure that any underlying dependencies for these tools (like duckduckgo-search for WebsiteSearchTool's
# default search functionality if web_search_engine is not specified or if it uses it) are in requirements.txt.
# Alternatively, you can specify a web_search_engine instance.

# Create an instance of the tool to be used by agents
# This tool fetches content from a URL.
web_content_fetcher_tool = WebsiteSearchTool()
