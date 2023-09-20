from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world, from Flask!, for flask"

@app.route("/hello")
def home1():
    return "Hello, this is me .. hehehehe :)"