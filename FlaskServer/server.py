from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html') 

@app.route('/about.html')
def about():
	return render_template('about.html') 

@app.route('/favicon.ico')
def favicon():
	return send_from_directory('favicon.ico','favicon.ico', mimetype='image/vnd.microsoft.icon')