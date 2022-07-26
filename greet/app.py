from flask import Flask

app = Flask (__name__)

@app.route ("/")
def start_page():
    return "Hello :)"

@app.route ("/welcome")
def say_hello():
    return "welcome"

@app.route ("/welcome/home")
def welcome_home():
    return "welcome home"

@app.route ("/welcome/back")
def welcome_back():
    return "welcome back"