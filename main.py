from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/index.html")
def index():
    
    return render_template('index.html')

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    return render_template('hello_greeting.html', name=username)

