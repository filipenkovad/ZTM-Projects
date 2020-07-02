from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_page():
	return render_template('index.html') 

@app.route('/index.html')
def my_page0():
	return render_template('index.html') 

@app.route('/about.html')
def my_page1():
	return render_template('about.html') 

@app.route('/contact.html')
def my_page2():
	return render_template('contact.html') 

@app.route('/work.html')
def my_page3():
	return render_template('work.html') 

@app.route('/works.html')
def my_page4():
	return render_template('works.html') 

@app.route('/components.html')
def my_page5():
	return render_template('components.html') 
