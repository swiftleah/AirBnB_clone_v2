#!/usr/bin/python3
""" starts a Flask web application listening on 0.0.0.0,
port 5000 """
from flask import Flask, render_template
from models.base_model import BaseModel, Base
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template(
        '7-dump.html', states=sorted_states
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
