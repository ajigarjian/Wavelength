import random #import random library for spinner function
from flask import Flask, render_template, request, redirect, url_for

# Initialize instance of Flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():
    #assign the random percentile to a new variable
    #user_percentile = random.randint(1,100)
    #rendering the variable isn't working. so tried to simplify by assigning it one number
    user_percentile = 5

    #render the main html template and port the user percentile variable into the html template
    return render_template("index.html", user_percentile = user_percentile )

#package randint into a function called spin
#def spin(): 
#    return random.randint(1,100) #returns a random integer from 1 to 100, inclusive

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)
