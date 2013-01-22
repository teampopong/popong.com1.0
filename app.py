#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

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
    locale = request.host.split('.')[0]
    if locale not in settings.LOCALES:
        locale = default_locale
    return locale

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

def main():
    app.run(**settings.SERVER_SETTINGS)

if __name__ == '__main__':
    main()
