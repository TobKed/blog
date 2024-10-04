#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *
from dotenv import load_dotenv

load_dotenv()

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://blog.tobked.dev/"
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
RSS_FEED_SUMMARY_ONLY = False
FEED_MAX_ITEMS = 50
FEED_ALL_RSS = "feeds/all.rss.xml"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
