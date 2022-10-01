import random #import random library for spinner function
from flask import Flask, render_template, request, redirect, url_for, flash, session
from math import pi

# Initialize instance of Flask application
app = Flask(__name__, template_folder="templates")

#setting secret key for session
app.secret_key = "abc"

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# ---------------------------------------------------

#helper functions for when a new turn is played
def selectClues():

    clue1, clue2 = random.choice(list(myDict.items()))
    return(clue1, clue2)

def selectWinningDegree():    
    #assign the random percentile to a new variable
    user_percentile = random.randint(1,100)

    #translate the user_percentile to the center degree
    if user_percentile <= 50:
        return(-90 * (1-(user_percentile/50)))
    else:
        return(90 * (-1+(user_percentile/50)))

#preliminary dictionary of clues
myDict = {'Hot':'Cold', 'Weak':'Strong', 'Cool':'Uncool','Underrated':'Overrated','Good':'Bad','Normal':'Weird','Soft':'Hard'}

# ---------------------------------------------------

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():
    return render_template("index.html")

# Returns content from clues.html
@app.route("/clues", methods=["GET", "POST"])
def clues():

        if request.method == "POST":

            #upon arriving at clues view via home page view (post method), initiate pair of clues and winning degree via helper functions
            clue1, clue2 = selectClues()
            winning_degree = selectWinningDegree()

            session['clue1'] = clue1
            session['clue2'] = clue2
            session['winning_degree'] = winning_degree

            #store form 'clues' response into variable
            return render_template("clues.html", clue1 = clue1, clue2 = clue2, winning_degree = winning_degree)
        
        # User reached route via GET (as by clicking a link or via redirect, send back to home page)
        else:
            return redirect("/")


@app.route("/guessing", methods=["GET", "POST"])
def guess():
    
    #User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #retrieving clues and winning degree from session as initiated in clues route
        clue1 = session.get('clue1', None)
        clue2 = session.get('clue2', None)
        winning_degree = session.get('winning_degree', None)

        #retrieving the round owner's clue submission for the teams to see 
        user_clue = request.form['clue']

        #verify that user submitted clue (NOT WORKING!)
        if not user_clue:
                flash("Clue is required")

        #render template with dial degree as updated guess
        return render_template("guessing.html", clue1 = clue1, clue2 = clue2, winning_degree=winning_degree, user_clue=user_clue)

    #User reached route via GET (as by clicking a link or via redirect, send back to home page)
    else:
        return redirect("/")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

# ---------------------------------------------------

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)



