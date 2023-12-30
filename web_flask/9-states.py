#!/usr/bin/python3
""" starts a flask web application listening on 0.0.0.0,
port 5000 """
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def id_of_states(id=None):
	""" displays list of states on HTML page """
	 all_states = storage.all(State)
	if id:
        	states = all_states.get('State.{}'.format(id))
    	else:
        	states = all_states.values()
	return render_template('9-states.html', states=states)

@app.teardown_appcontext
def remove_SQLalc_session(exception):
	""" closes storage when teardown executed """
	storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
