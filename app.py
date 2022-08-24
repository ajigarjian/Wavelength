import random #import random library for spinner function
from flask import Flask, render_template, request, redirect, url_for
from math import pi

# Initialize instance of Flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():

    myDict = {}

    #preliminary dictionary of clues
    myDict = {'Hot':'Cold', 'Weak':'Strong', 'Cool':'Uncool','Underrated':'Overrated','Good':'Bad','Normal':'Weird','Soft':'Hard'}

    #assign two variables by calling random on the dictionary
    clue1, clue2 = random.choice(list(myDict.items()))

    #assign the random percentile to a new variable
    user_percentile = random.randint(1,100)

    #initialize center line degree
    winning_degree = 0

    #translate the user_percentile to the center degree
    if user_percentile <= 50:
        winning_degree = -90 * (1-(user_percentile/50))
    else:
        winning_degree = 90 * (-1+(user_percentile/50))

    #creating variables for the 2 and 3 point lines
    degree_3L = winning_degree - 3
    degree_3R = winning_degree + 3

    degree_2L = winning_degree - 6
    degree_2R = winning_degree + 6

    #render the main html template and port the user percentile variable into the html template
    return render_template("index.html", user_percentile = user_percentile, clue1 = clue1, clue2 = clue2, winning_degree = winning_degree, degree_3R = degree_3R, degree_3L = degree_3L, degree_2R = degree_2R, degree_2L = degree_2L)

@app.route("/guessing", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if not request.form.get("percentile_guess"):
                return render_template("apology.html")

        guess_percentile = 0

        guess_percentile = request.form.get("percentile_guess")

        #translate the user_percentile to the center degree
        if guess_percentile <= 50:
            guess_percentile = -90 * (1-(guess_percentile/50))
        else:
            guess_percentile = 90 * (-1+(guess_percentile/50))

        return render_template("guessing.html", guess_percentile = guess_percentile)

    else:
        return render_template("guessing.html", guess_percentile = 0)

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)
