#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Barton'
SITENAME = u'Dodcott-cum-Wilkesley'
SITEURL = 'http://dodcott.org'

THEME = "../../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

TIMEZONE = 'Europe/London'
MARKUP = (('rst', 'md', 'yml'))
DEFAULT_LANG = 'en'


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_SIDEBAR = True



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/dodcottfibre'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = "/home/ian/Dropbox/src/pelican-plugins"
PLUGINS = ['yaml_importer', 'summary']

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

GOOGLE_ANALYTICS = "UA-46964007-1"
