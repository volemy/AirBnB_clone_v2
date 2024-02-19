#!/usr/bin/python3
"""
Script that starts a Flask web application
Route: /states: display a HTML page, /states/<id>: display a HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """List all states"""
    states = storage.all("State")
    return render_template('9-states.html', states=states, mode="all")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """List all states"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=state, mode='id')
        return render_template("9-states.html", states=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
