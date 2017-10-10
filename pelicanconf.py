#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import os.path

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
	# ('Meetup', 'https://www.meetup.com/BAyPIGgies/'),
         ('Python.org', 'http://python.org/'),
         ('Mailing List', 'https://mail.python.org/mailman/listinfo/baypiggies'),
         # ('You can modify those links in your config file', '#')
        )

# Social widget
SOCIAL = (('BayPIGgies Meetup Group', 'http://www.meetup.com/BAyPIGgies/'),
          ('Twitter', 'http://twitter.com/baypiggies'),
          ('YouTube', 'https://www.youtube.com/channel/UCBJV1sd5XcVhijm13pWfBCg'),)

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

# The index.html page will be rendered from the featured.html template
# in this directory.
# TEMPLATE_PAGES = {os.path.join(os.path.dirname(__file__), 'featured.html'): 'index.html'}
# The title of the article to be featured on the home page
# FEATURED_ARTICLE = 'Thursday, November 17th, 2016 Meeting'

TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"
MENUITEMS = [('Videos', '/tag/video.html')]

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'pin_to_top',
    'sitemap',
    ]

SITEMAP = {
    'format': 'txt',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
}

