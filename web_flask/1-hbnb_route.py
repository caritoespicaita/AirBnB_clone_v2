#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Hello flask. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ HBNB flask. """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
