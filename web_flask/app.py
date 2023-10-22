#!/usr/bin/python3
"""Hello HBNB from Flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"
