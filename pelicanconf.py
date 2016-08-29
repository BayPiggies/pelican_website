#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'William Deegan'
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
	# ('Meetup', 'https://www.meetup.com/BAyPIGgies/'),
         ('Python.org', 'http://python.org/'),
         ('Mailing List', 'https://mail.python.org/mailman/listinfo/baypiggies'),
         # ('You can modify those links in your config file', '#')
        )

# Social widget
SOCIAL = (('BayPIGgies Meetup Group', 'http://www.meetup.com/BAyPIGgies/'),
          ('Twitter', 'http://twitter.com/baypiggies'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']

THEME='../pelican-themes/pelican-bootstrap3'
# SITELOGO='images/baypiggies.png'
# SITELOGO_SIZE='381x88'
BANNER_IMAGE='images/baypiggies.png'

TWITTER_USER='baypiggies'
# TWITTER_WIDGET_ID='598966848630169601'

