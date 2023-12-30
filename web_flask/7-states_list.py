#!/usr/bin/python3
""" starts a Flask web application listening on 0.0.0.0,
    port 5000 """

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app.route('/states_list', strict_slashes=False)
def states_list():
	""" displays list of states on HTML page """
	states = storage.all(classes["State"]).values()
	return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_database(exception):
	""" closes storage when tear down executed """
	storage.close()


if __name__ == "__main__":
	 app.run(host='0.0.0.0', port=5000)
