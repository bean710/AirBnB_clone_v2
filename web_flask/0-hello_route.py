"""This module starts a simple flask server"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    """Sends simple text"""
    return ("Hello HBNB!\n")

if __name__ == "__main__":
    app.run()
