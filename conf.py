# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = "DynamoJinz's Blog"
WWW_ROOT = 'http://dynamojinz.com/'

AUTHOR = 'dynamojinz'
EMAIL = 'jinzan5766@gmail.com'

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    '/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/page/:num'},

    '/:year/:slug/': {'view': 'entry'},

    '/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/tag/:name/:num'},

    # per tag Atom or RSS feed. Just uncomment to generate them.

    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    '/articles/': {'view': 'articles'},

    '/sitemap.xml': {'view': 'sitemap'},

    # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    # '/:slug/': {'view': 'page'}

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'}
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

CONTENT_EXTENSION = '.md'
DISQUS_SHORTNAME = 'dynamojinz'
# Tuples are (name, link)
BLOGROLL = [
    ('Acrylamid', 'http://posativ.org/acrylamid/'),
]

DEPLOYMENT = {
    "ls": "ls $OUTPUT_DIR",
    "echo": "echo $OUTPUT_DIR",
    "default": "rsync -avz --delete $OUTPUT_DIR ec2-user@dynamojinz.com:/var/www/dynamojinz.com/",
}
