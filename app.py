#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from flask import Flask, render_template, redirect, request, url_for
from flask.ext.babel import get_locale, refresh as refresh_babel

import members
from settings import BABEL_SETTINGS, SERVER_SETTINGS
from utils.i18n import PopongBabel

app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']

PopongBabel(app, **BABEL_SETTINGS)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',
            YB=members.YB, OB=members.OB, THANKS_TO=members.THANKS_TO)

@app.route('/blog')
def blog():
    if str(get_locale()) == 'ko':
        return redirect('http://blog.popong.com/ko')
    else:
        return redirect('http://blog.popong.com/en')

@app.route('/developers')
def developers():
    if str(get_locale()) == 'ko':
        return redirect('http://developers.popong.com')
    else:
        return redirect('http://en.developers.popong.com')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/participate')
def participate():
    return render_template('participate.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/favicon.ico')

@app.route('/googlef6e4487896615e46.html')
def google_webmaster_tools():
    return render_template('googlef6e4487896615e46.html')

@app.context_processor
def inject_menus():
    return dict(menus=[
        ('Blog', url_for('blog')),
        ('Projects', url_for('projects')),
        ('Developers', url_for('developers')),
        ('Participate', url_for('participate')),
        ('About', url_for('about'))
    ])

@app.context_processor
def direct_links():
    return dict(dirlinks=[
        ('facebook', 'http://facebook.com/teampopong'),
        ('twitter', 'http://twitter.com/teampopong'),
        #('youtube', 'http://youtube.com/user/teampopong'),
        ('vimeo', 'http://vimeo.com/teampopong'),
        ('slideshare', 'http://slideshare.com/teampopong'),
        ('github', 'http://github.com/teampopong')
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
