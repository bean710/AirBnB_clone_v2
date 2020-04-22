#!/usr/bin/python3
"""Serves a page with a list of all states"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def winddown(exception):
    """Closes the storage"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Returns an HTML page with a list of states"""
    slist = storage.all(State).values()
    return (render_template("9-states.html", states=slist, l=True))


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """Returns an HTML page with info on a single state"""
    slist = storage.all(State)
    sid = "State.{}".format(id)
    if (sid in slist):
        return (render_template("9-states.html", states=slist[sid], l=False))
    else:
        return (render_template("9-states.html", states=0, l=False))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
