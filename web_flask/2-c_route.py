#!/usr/bin/python3
"""This module starts a simple flask server"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Sends simple text"""
    return ("Hello HBNB!\n")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Sends simple text"""
    return ("HBNB\n")


@app.route("/c/<text>", strict_slashes=False)
def dyn_text(text):
    """Returns dynamic text"""
    return ("C {}\n".format(text.replace("_", " ")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
