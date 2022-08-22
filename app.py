import random #import random library for spinner function
from flask import Flask, render_template, request, redirect, url_for

# Initialize instance of Flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():
    return render_template("index.html")

#package randint into a function called spin
def spin(): 
    return random.randint(1,100) #returns a random integer from 1 to 100, inclusive

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)
