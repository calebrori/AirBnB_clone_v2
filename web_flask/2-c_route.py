#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Message when called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays Message when called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ displays Message when called """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ listening port """
    app.run(host='0.0.0.0', port=5000)
