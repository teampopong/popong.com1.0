#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re

import meinheld
from flask import Flask, render_template, redirect, request, url_for
from flask.ext.assets import Environment as Asset

import members
from settings import BABEL_SETTINGS, DIRLINKS, SERVER_SETTINGS
from utils.i18n import PopongBabel


app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']


Asset(app)
PopongBabel(app, **BABEL_SETTINGS)


@app.route('/')
def home():
    return render_template('main.html', dirlinks=DIRLINKS)

@app.route('/team')
def team():
    return render_template('about.html',
            YB=members.YB, CONTRIBUTORS=members.CONTRIBUTORS, partners=members.PARTNERS,
            dirlinks=DIRLINKS)

@app.route('/blog/<locale>')
def blog(locale):
    return redirect('http://blog.popong.com/%s' % locale)

@app.route('/data')
def data():
    return redirect('http://data.popong.com/')

@app.route('/faq')
def faq():
    return render_template('faq.html', dirlinks=DIRLINKS)

@app.route('/sources')
def sources():
    return render_template('sources.html', dirlinks=DIRLINKS)

@app.route('/philosophy')
def philosophy():
    return render_template('philosophy.html', dirlinks=DIRLINKS)

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
    if SERVER_SETTINGS['type']=='flask':
        app.run(SERVER_SETTINGS['host'], SERVER_SETTINGS['port'])
    elif SERVER_SETTINGS['type']=='meinheld':
        print 'On http://%s:%s/' % (SERVER_SETTINGS['host'], SERVER_SETTINGS['port'])
        meinheld.listen((SERVER_SETTINGS['host'], SERVER_SETTINGS['port']))
        meinheld.run(app)



if __name__ == '__main__':
    main()
