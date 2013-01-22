#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request, g
from flaskext.babel import Babel, gettext

import settings, members


app = Flask(__name__)
app.debug = False

babel = Babel(app, **settings.BABEL_SETTINGS)
default_locale = settings.BABEL_SETTINGS['default_locale']

@babel.localeselector
def get_locale():
    locale = request.host.split('.')[0]
    if locale not in settings.LOCALES:
        locale = settings.LOCALES[0]
    return locale

@app.route('/')
def home():
    return render_template('home.html', menus=settings.MENUS,
            dirlinks=settings.DIRLINKS, active_page='Home')

@app.route('/blog')
def blog(locale=default_locale):
    if locale=='ko':
        return redirect('http://blog.popong.com')
    else:
        return redirect('http://en.blog.popong.com')

@app.route('/about')
def about():
    return render_template('about.html', menus=settings.MENUS,
            dirlinks=settings.DIRLINKS, active_page='About',
            YB=members.YB, OB=members.OB, THANKS_TO=members.THANKS_TO)

@app.route('/error')
def error():
    return 'error ;_;'

def main():
    app.run(**settings.SERVER_SETTINGS)

if __name__ == '__main__':
    main()
