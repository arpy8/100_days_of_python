from random import *
from flask import Flask

app = Flask(__name__)
number = randint(1, 100)


@app.route("/")
def main_page():
    return '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img> <br>' \
           '<h1>Guess a number between 0 and 9</h1>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img> <br><h1>Too high</h1>'
    elif guess < number:
        return '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img> <br><h1>Too low</h1>'
    elif guess == number:
        return '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img> <br><h1>You found me!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
