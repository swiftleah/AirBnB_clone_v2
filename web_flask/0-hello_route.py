#!/usr/bin/python3
""" script starts a Flask web application listening on 0.0.0.0
	port 5000, Route '/' displaying 'Hello HBNB!' """
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	""" message that says 'Hello HBNB!' """
	return ("Hello HBNB!")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
