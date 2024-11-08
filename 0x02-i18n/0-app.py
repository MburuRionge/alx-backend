#!/usr/bin/env python3

"""creating a route with flask"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('0-index.html')
