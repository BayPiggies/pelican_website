#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bay Area Python Interest Group (BAyPIGgies)'
SITENAME = u'BayPIGgies Bay Area Python Interest Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Python.org', 'http://python.org/'),
         ('Mailing List', 'https://mail.python.org/mailman/listinfo/baypiggies'),
        )

# Social widget
SOCIAL = (('BayPIGgies Meetup Group', 'http://www.meetup.com/BAyPIGgies/'),
          ('Twitter', 'http://twitter.com/baypiggies'),
          ('YouTube', 'https://www.youtube.com/channel/UCBJV1sd5XcVhijm13pWfBCg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']

THEME='pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# SITELOGO='images/baypiggies.png'
# SITELOGO_SIZE='381x88'
BANNER_IMAGE='images/baypiggies.png'

TWITTER_USER='baypiggies'
# TWITTER_WIDGET_ID='598966848630169601'


TAG_FEED_ATOM = "feeds/tag-{slug}.atom.xml"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'pin_to_top',
    'sitemap',
    'i18n_subsites'
    ]

SITEMAP = {
    'format': 'txt',
}


MENUITEMS = [('Videos', '/tag/video.html')]
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_THESE_CATEGORIES = ['Community']
DISPLAY_PAGES_ON_MENU=True
PAGE_PATHS = ['pages']