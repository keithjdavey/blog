#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Keith Davey'
SITENAME = 'Keith\'s Website'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ars Technica', 'https://arstechnica.com/'),
     ('Wikipedia', 'https://wikipedia.org'),)

SOCIAL = (('Twitter', 'https://twitter.com/mbdevaney'),
         ('Github', 'https://github.com/yourekittenme'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../output'
THEME = 'theme'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', ]
PLUGINS = ['i18n_subsites', 'ipynb.markup']

IGNORE_FILES = ['.ipynb_checkpoints']

IPYNB_USE_METACELL = True

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'
