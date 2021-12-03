#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

THEME = "pelican-clean-blog"

AUTHOR = 'Tobiasz Kedzierski'
SITENAME = 'ups and downs'
SITEURL = ''


PATH = 'content'
STATIC_PATHS = ['images', 'css']

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Home', '/index.html'),
    ('about me', '/pages/about-me.html'),
    ('tobked.github.io', 'https://tobked.github.io/'),
)

# Social widget
SOCIAL = (
    ('user', 'https://tobked.github.io/'),
    ('LinkedIn', 'https://www.linkedin.com/in/tobiaszkedzierski/?locale=en_US'),
    ('GitHub', 'https://github.com/TobKed'),
)

DEFAULT_PAGINATION = 10

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = 'css/main.css'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# theme settings
HEADER_COVER = 'images/poli_photo_by_julia_kaczorowska_edit.png'
FOOTER_INCLUDE = "my_footer.html"
IGNORE_FILES = [FOOTER_INCLUDE]
EXTRA_TEMPLATES_PATHS = [os.path.join(os.path.dirname(__file__), "content", "html")]
