from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Welcome to this Flask app!</p>'

@app.route('/about')
def about():
	return '<p>This flask app runs on Flask web framework</p><p><a href="https://flask.palletsprojects.com/">Flask website</a></p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
