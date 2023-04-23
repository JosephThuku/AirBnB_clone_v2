#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Displays a list of all states and cities"""
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
