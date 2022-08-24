"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


MADLIB_TEMPLATES = [
    "madlib1.html", 
    "madlib2.html", 
    "madlib3.html"
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


# Why does game.html and goodbye.html both load on /game?
@app.route("/game")
def show_madlib_form():
    """Play a game."""

    game_answer = request.args.get("play-game")
    
    if game_answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")
   


@app.route("/madlib")
def show_madlib():
    """Shows to madlib"""

    person = request.args.get("person-game")
    color = request.args.get("color-game")
    noun = request.args.get("noun-game")
    adjective = request.args.get("adjective-game")

    madlib_template = choice(MADLIB_TEMPLATES)
    
    return render_template(madlib_template, person = person, color = color, noun = noun, adjective = adjective)







if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
