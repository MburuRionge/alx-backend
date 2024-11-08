#!/usr/bin/env python3

"""instantiate the Babel object in my app"""

from flask import Flask render_template
from flask_babel import Babel


app = Flask(__name__)

class Config:
    """configutation class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

#apply Config to Flask app
app.config.from_object(Config)

#instantiate Babel and store it in a variable
babel = Babel(app)

@app.route('/')
def index():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
