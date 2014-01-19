#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re

import meinheld
from flask import Flask, render_template, redirect, request, url_for
from flask.ext.assets import Environment as Asset
from flask.ext.babel import get_locale, refresh as refresh_babel

import members
from settings import BABEL_SETTINGS, DIRLINKS, SERVER_SETTINGS
from utils.i18n import PopongBabel


app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']


Asset(app)
PopongBabel(app, **BABEL_SETTINGS)


@app.route('/')
def home():
    return render_template('main.html',
            YB=members.YB, OB=members.OB, THANKS_TO=members.THANKS_TO,
            dirlinks=DIRLINKS, active_page='Home')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/sources')
def sources():
    return render_template('sources.html')


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
    meinheld.listen(('0.0.0.0', 8088))
    meinheld.run(app)


if __name__ == '__main__':
    main()
