#!/usr/bin/python3
""" starts a flask web application listening on 0.0.0.0, port 5000"""
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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbfilters():
	""" filters mtehod """
	states = storage.all(State).values()
    	ameninities = storage.all(Amenity).values()
    	return (render_template('10-hbnb_filters.html', states=states,
                            	amenities=ameninities))

@app.teardown_appcontext
def teardown(exception):
	""" closes storage when teardown executed """
	storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
