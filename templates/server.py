from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
	a = 3
	b = 4
	return f"<h1>Hello World {a + b}</h1>"


@app.route("/about")
def about():
	return f"<h1>Hello About</h1>"



if __name__ == "__main__":
	app.run(debug=True)