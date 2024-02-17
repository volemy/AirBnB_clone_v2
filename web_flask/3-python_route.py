#!/usr/bin/python3
"""This starts a flask web application
    - / : displays "Hello HBNB!"
    - /hbnb : displays "HBNB"
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ This method displays  "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "Returns HBNB"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text=None):
    """This method displays "C" followed by value of text
    replace underscore with space """
    if text:
        return "C " + text.replace("_", " ")
    else:
        return "C"


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ This method display python followed by value of text """
    if text:
        return "python " + text.replace("_", " ")
    else:
        return "python"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
