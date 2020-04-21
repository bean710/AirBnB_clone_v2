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


@app.route("/states_list", strict_slashes=False)
def get_states():
    """Returns an HTML page with a list of states"""

    def sort_by_name(item):
        """Sorting function"""
        return item.name.upper()

    stateslist = storage.all(State)
    statesimple = [data for name, data in stateslist.items()]
    statesimple.sort(key=sort_by_name)

    return (render_template("7-states_list.html", states=statesimple))


if __name__ == "__main__":
    app.run()
