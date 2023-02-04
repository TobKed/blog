#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

THEME = "pelican-clean-blog"

AUTHOR = "Tobiasz Kedzierski"
SITENAME = "ups and downs"
SITEURL = ""


PATH = "content"
STATIC_PATHS = [
    "images",
    "css",
    "extra/robots.txt",
]

EXTRA_PATH_METADATA = {"extra/robots.txt": {"path": "./robots.txt"}}

TIMEZONE = "Europe/Warsaw"

DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%d.%m.%Y"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Home", "/index"),
    ("about me", "/pages/about-me"),
    ("tobked.dev", "https://tobked.dev/"),
)

# Social widget
SOCIAL = (
    ("user", "https://tobked.dev"),
    ("LinkedIn", "https://www.linkedin.com/in/tobiaszkedzierski/?locale=en_US"),
    ("GitHub", "https://github.com/TobKed"),
    ("RSS", "https://blog.tobked.dev/feeds/all.rss.xml"),
)

DEFAULT_PAGINATION = 10

COLOR_SCHEME_CSS = "github.css"

CSS_OVERRIDE = "css/main.css"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# theme settings
HEADER_COVER = "images/poli_photo_by_julia_kaczorowska_edit.png"
FOOTER_INCLUDE = "my_footer.html"
IGNORE_FILES = [FOOTER_INCLUDE]
THEME_TEMPLATES_OVERRIDES = [os.path.join(os.path.dirname(__file__), "content", "html")]

# other
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.6, "indexes": 0.5, "pages": 0.4},
    "changefreqs": {"articles": "weekly", "indexes": "weekly", "pages": "monthly"},
}

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of contents:"},
    },
    "output_format": "html5",
}

ARTICLE_URL = "{slug}"
ARTICLE_ORDER_BY = "reversed-date"
ARTICLE_LANG_URL = "{slug}-{lang}"
DRAFT_URL = "drafts/{slug}"
DRAFT_LANG_URL = "drafts/{slug}-{lang}"
PAGE_URL = "pages/{slug}"
PAGE_LANG_URL = "pages/{slug}-{lang}"
DRAFT_PAGE_URL = "drafts/pages/{slug}"
DRAFT_PAGE_LANG_URL = "drafts/pages/{slug}-{lang}"
CATEGORY_URL = "category/{slug}"
TAG_URL = "tag/{slug}"
AUTHOR_URL = "author/{slug}"

PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}", "{base_name}/page/{number}{extension}"),
    (-1, "{base_name}/last/", "{base_name}/last/index.html"),
)
