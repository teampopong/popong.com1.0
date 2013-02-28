#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from flask import Flask, render_template, redirect, request, url_for
from flaskext.babel import Babel
from werkzeug.local import LocalProxy

import settings, members

app = Flask(__name__)
app.debug = False

babel = Babel(app, **settings.BABEL_SETTINGS)
default_locale = settings.BABEL_SETTINGS['default_locale']

@babel.localeselector
def get_locale():
    if getattr(app, 'locale', 'auto') != 'auto':
        return app.locale
    locale = request.host.split('.')[0]
    if locale not in settings.LOCALES:
        locale = default_locale
    return locale

def host(locale=default_locale):
    if locale not in settings.LOCALES:
        locale = default_locale
    return '%s.popong.com' % locale

locale = LocalProxy(get_locale) # 함수를 변수처럼

@app.route('/')
def home():
    return render_template('home.html',
            dirlinks=settings.DIRLINKS, active_page='Home')

@app.route('/blog')
def blog():
    if locale=='ko':
        return redirect('http://blog.popong.com')
    else:
        return redirect('http://en.blog.popong.com')

@app.route('/about')
def about():
    return render_template('about.html',
            dirlinks=settings.DIRLINKS, active_page='About',
            YB=members.YB, OB=members.OB, THANKS_TO=members.THANKS_TO)

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/glossary')
def glossary():
    return render_template('glossary.html', locale=app.locale, terms=load_data('static/data/glossary.csv'))

def load_data(data):
    import csv
    items = []
    with open(data, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            items.append([unicode(cell, 'utf-8') for cell in row])
    return items

@app.route('/error')
def error():
    return 'error ;_;'

@app.context_processor
def inject_menus():
    return dict(menus=[
            ('Home', url_for('home')),
            ('Blog', url_for('blog')),
            ('About', url_for('about'))
        ])

@app.context_processor
def inject_locale():
    locale_links = dict((locale, request.url.replace(request.host, host(locale)))
            for locale in settings.LOCALES)
    return dict(locale_links=locale_links,
            active_lang=locale)

def cmd_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-l', dest='locale',
            choices=settings.LOCALES + ['auto'],
            default='auto')
    args = parser.parse_args()
    return args

def main():
    args = cmd_args()
    app.locale = args.locale
    app.run(**settings.SERVER_SETTINGS)

if __name__ == '__main__':
    main()
