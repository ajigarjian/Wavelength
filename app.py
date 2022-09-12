import random #import random library for spinner function
from flask import Flask, render_template, request, redirect, url_for
from math import pi

# Initialize instance of Flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#preliminary dictionary of clues
myDict = {'Hot':'Cold', 'Weak':'Strong', 'Cool':'Uncool','Underrated':'Overrated','Good':'Bad','Normal':'Weird','Soft':'Hard'}

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():
    return render_template("index.html")

# Returns content from clues.html
@app.route("/clues")
def clues():

    #myDict = {}

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

    #render the main html template and port the user percentile variable into the html template
    return render_template("clues.html", user_percentile = user_percentile, clue1 = clue1, clue2 = clue2, winning_degree = winning_degree)

@app.route("/guessing", methods=["GET", "POST"])
def guess():
    clue1 = request.args.get('clue1', None)
    clue2 = request.args.get('clue2', None)
    winning_degree = request.args.get('winning_degree', type=float)
    
    #User reached route via POST (as by submitting a form via POST)
    
    if request.method == "POST":

        #verify that user submitted guess
        if not request.form.get("percentile_guess"):
                return render_template("apology.html", apology_input = "guess")

        #start the dial all the way to the left
        guess_percentile = -90

        #save the guess as a variable
        guess_percentile = int(request.form.get("percentile_guess"))

        #translate the guess_percentile to the center degree
        if guess_percentile <= 50:
            guess_percentile = -90 * (1-(guess_percentile/50))
        else:
            guess_percentile = 90 * (-1+(guess_percentile/50))

        #render template with dial degree as updated guess
        return render_template("guessing.html", guess_percentile = guess_percentile, clue1 = clue1, clue2 = clue2, winning_degree=winning_degree)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        #default page (no guesses)
        return render_template("guessing.html", guess_percentile = -90, clue1 = clue1, clue2 = clue2, winning_degree=winning_degree)

#TODO: create result.html, which superimposes the guess on the score
@app.route("/result", methods=["GET", "POST"])
def result():

    clue1 = request.args.get('clue1', None)
    clue2 = request.args.get('clue2', None)
    winning_degree = request.args.get('winning_degree', type=float)


    return render_template("result.html", clue1 = clue1, clue2 = clue2, winning_degree=winning_degree)

@app.route("/test")
def test():
    return render_template("test.html")

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)
