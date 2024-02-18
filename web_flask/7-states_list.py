#!/usr/bin/python3
"""
This script starts flask that lists all states in the database
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This method displays a HTML with the list of all states present in
    database from A -> Z"""
    states = storage.all(state).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ Close the SQLAchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
