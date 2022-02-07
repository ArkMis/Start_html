from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def start():
    return f'Witamy...'

@app.route('/hello')
def hello():
    name = "John Ark Mis"
    return f'Hello, {name}!'

@app.route("/me")
def me():
    return render_template("me.html")
#   return f'to jest o mnie'

@app.route('/contact')
def contact():
    return render_template("contact.html")
