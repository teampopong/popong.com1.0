#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

SERVER_SETTINGS = {
    'host': '0.0.0.0',
    'port': 8192,
    'debug': True
}

BABEL_SETTINGS = {
    'default_locale': 'ko',
}

LOCALES = ['ko', 'en']

MENUS = [
    ('Home', '/'),
    ('Blog', '/blog'),
    ('About', '/about')
]

DIRLINKS = [
        ('facebook', 'http://facebook.com/teampopong'),
        ('twitter', 'http://twitter.com/teampopong'),
        #('youtube', 'http://youtube.com/user/teampopong'),
        ('vimeo', 'http://vimeo.com/teampopong'),
        ('slideshare', 'http://slideshare.com/teampopong'),
        ('github', 'http://github.com/popong')
]
