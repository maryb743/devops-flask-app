from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p>'

@app.route('/about')
def about():
	return '<p>This flask app runs on Flask web framework</p><p><a href="https://flask.palletsprojects.com/">Flask website</a></p>'
