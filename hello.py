from flask import Flask 
app = Flask(__name__)

@app.route('/username/<name>/<int:number>')
def index(name, number):
	return f'<h1 style="text-align: center"> Hello there mr. {name}, you are {number} years old</h1>' \
			'<p>A beautiful gif<p>' \
			'<img src="https://media.giphy.com/media/l3V0lsGtTMSB5YNgc/giphy.gif" width="300">'

# @app.route('/')
# def myhtml():
# 	return '<h1 style="text-align: center"> Hello world</h1>'


if __name__=='__main__':
	app.run(debug=True)