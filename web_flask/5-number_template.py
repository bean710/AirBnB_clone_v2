#!/usr/bin/python3
"""This module starts a simple flask server"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Sends simple text"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Sends simple text"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def dyn_text(text):
    """Returns dynamic text"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False, defaults={"text": "is_cool"})
def opt_text(text="is_cool"):
    """Returns optional dynamic text"""
    return("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """Returns if n is a number"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_num(n):
    """Returns an HTML template"""
    return (render_template("5-number.html", name=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
