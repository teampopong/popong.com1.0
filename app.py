#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from flask import Flask, render_template, redirect, request, url_for
from flask.ext.babel import get_locale, refresh as refresh_babel

import members
from settings import BABEL_SETTINGS, DIRLINKS, SERVER_SETTINGS
from utils.i18n import PopongBabel
from utils.glossary import load as load_glossary


app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']


terms = load_glossary('static/data/glossary/glossary.csv')
PopongBabel(app, **BABEL_SETTINGS)


@app.route('/')
def home():
    return render_template('home.html',
            dirlinks=DIRLINKS, active_page='Home')

@app.route('/blog')
def blog():
    if str(get_locale()) == 'ko':
        return redirect('http://blog.popong.com/ko')
    else:
        return redirect('http://blog.popong.com/en')

@app.route('/about')
def about():
    return render_template('about.html',
            dirlinks=DIRLINKS, active_page='About',
            YB=members.YB, OB=members.OB, THANKS_TO=members.THANKS_TO)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')


@app.route('/glossary')
def glossary():
    return render_template('glossary.html', terms=terms)

@app.route('/error')
def error():
    return render_template('404.html')


@app.context_processor
def inject_menus():
    return dict(menus=[
            ('Home', url_for('home')),
            ('Blog', url_for('blog')),
            ('About', url_for('about'))
        ])


def cmd_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-l', dest='locale',
            choices=app.LOCALES + ['auto'],
            default='auto')
    args = parser.parse_args()
    return args


def main():
    args = cmd_args()
    if args.locale and args.locale != 'auto':
        app.babel.locale_selector_func = lambda: args.locale
    app.run(**SERVER_SETTINGS)


if __name__ == '__main__':
    main()
