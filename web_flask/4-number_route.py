#!/usr/bin/python3
"""This starts a flask web application
    - / : displays "Hello HBNB!"
    - /hbnb : displays "HBNB"
"""


from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ This method displays  "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text=None):
    """This method displays "C" followed by value of text
    replace underscore with space """
    if text:
        return "C " + text.replace("_", " ")
    else:
        return "C"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ This method display "Python" followed by value of text """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This method displays n is a number only if its an integer"""
    return "{} is a number.format(n)"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
