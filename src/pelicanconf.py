#!/usr/bin/env python

AUTHOR = 'Till Gartner'
SITENAME = 'Filmz2 - Track Your Movie Journey'
SITEURL = ''
SITESUBTITLE = 'Keep track of what you\'ve watched, what you want to see, and share your ratings with friends'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('App Store', '#'),
    ('Support', 'mailto:support@filmz2.app'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/filmz2app'),
    ('GitHub', 'https://github.com/tillg/filmz2'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'theme'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

# Static paths
STATIC_PATHS = ['images', 'extra']

# Page paths
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Extra files to copy
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
}

# Disable some default pages
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Custom menu
MENUITEMS = (
    ('Features', '/features.html'),
    ('Privacy', '/privacy.html'),
    ('Support', '/support.html'),
)

# Current year for copyright
import datetime
CURRENT_YEAR = datetime.datetime.now().year

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Markdown configuration
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}