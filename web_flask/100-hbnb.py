#!/usr/bin/python3
"""Serves a page with a list of all states"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask
from flask import render_template, send_from_directory


app = Flask(__name__)


@app.teardown_appcontext
def winddown(exception):
    """Closes the storage"""
    storage.close()


@app.route("/static/<path:path>", strict_slashes=False)
def files(path):
    """Serves static files"""
    return (send_from_directory("static", path))


@app.route("/hbnb", strict_slashes=False)
def filters():
    """Serves the hbnb"""
    slist = storage.all(State).values()
    alist = storage.all(Amenity).values()
    plist = storage.all(Place).values()
    return (render_template("100-hbnb.html", states=slist,
                            amenities=alist, places=plist))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
