#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "pelican-chunk"


AUTHOR = 'Tobiasz Kedzierski'
SITENAME = 'ups and downs'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
SITESUBTITLE = 'by Tobiasz Kedzierski'
FOOTER_TEXT = 'pelican theme: <a href=\"https://github.com/onlyhavecans/pelican-chunk\">pelican-chunk</a>'
DISPLAY_CATEGORIES_ON_MENU = True
SINGLE_AUTHOR = True
MINT = False

LINKS = (
    ('tobked.github.io', 'https://tobked.github.io/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True