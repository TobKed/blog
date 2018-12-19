#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "voce"
PLUGIN_PATHS = ["voce/plugins"]
PLUGINS = ["assets"]

AUTHOR = 'Tobiasz Kedzierski'
SITENAME = 'ups and downs'
SITEURL = ''


PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Home','/index.html'),
    ('about me', '/pages/about-me.html'),
    ('tobked.github.io', 'https://tobked.github.io/'),
)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/tobiaszkedzierski/?locale=en_US'),
          ('GitHub', 'https://github.com/TobKed'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# theme settings
DISPLAY_PAGES_ON_MENU = True
USER_LOGO_URL = "images/qr.png"
MANGLE_EMAILS = True
FUZZY_DATES = True
# TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
PAGES_URL = 'pages.html'
