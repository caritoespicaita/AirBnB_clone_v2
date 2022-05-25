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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ c flask. """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def phyton_route(text='is cool'):
    """ phyton flask. """
    return 'Phyton {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run()
