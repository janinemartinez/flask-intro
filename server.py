"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return '<!doctype html><html>Hi! This is the home page. Would you like to navigate to the <a href="/hello"> Hello Page!</a></html>'


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Choose a compliment...
            <input type = "radio" name="compliment" value = "awesome">
            <label>Awesome!</label>
            <input type = "radio" name="compliment" value = "terrific">
            <label>Terrific!</label>
            <input type = "radio" name="compliment" value = "fantastic">
            <label>Fantastic!</label>
            <input type = "radio" name="compliment" value = "neato">
            <label>Neato!</label>
            <input type = "radio" name="compliment" value = "fantabulous">
            <label>Fantabulous!</label>
            <input type = "radio" name="compliment" value = "wowza">
            <label>Wowza!</label>
            <input type = "radio" name="compliment" value = "oh-so-not-meh">
            <label>Oh-so-not-meh.</label>
            <input type = "radio" name="compliment" value = "brilliant">
            <label>Brilliant!</label>
            <input type = "radio" name="compliment" value = "ducky">
            <label>Ducky!</label>
            <input type = "radio" name="compliment" value = "coolio">
            <label>Coolio!</label>
            <input type = "radio" name="compliment" value = "incredible">
            <label>Incredible!</label>
            <input type = "radio" name="compliment" value = "wonderful">
            <label>Wonderful!</label>
            <input type = "radio" name="compliment" value = "smashing">
            <label>Smashing!</label>
            <input type = "radio" name="compliment" value = "lovely">
            <label>Lovely!</label>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
