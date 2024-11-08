#!/usr/bin/env python3

"""Create a get_locale function with the babel.localeselector decorator."""

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)

class Config:
    """ configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTF"

app.config.from_object(Config)

# initializing Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """defining get_locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run()
