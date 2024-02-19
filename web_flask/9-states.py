#!/usr/bin/python3
"""
Script that starts a Flask web application
Route: /states: display a HTML page, /states/<id>: display a HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

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
def state(state_id):
    state = storage.get(State, state_id)
    if state:
        return render_template('9-state.html', state=state,
                cities=sorted(state.cities, key=lambda x: x.name))
    else:
        return "Not found!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
