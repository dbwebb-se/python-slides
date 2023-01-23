#!/usr/bin/env python3
"""
My first Flask app.
Minimal Flask application, including useful error handlers.
"""
# Import relevant modules
import os
import re
import traceback
from flask import Flask, render_template, session, request, redirect, url_for
from car import Car

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about", methods=["POST", "GET"])
def about():
    """ About route """
    my_car = Car("BMW", 90000)
    my_name = "Marie Grahn"
    my_course = "OOPython"

    print(session)
    if session.get("test"):
        session["test"] = "No testing!"
    else:
        session["test"] = "Testing!"
    if request.form.get("wheels") :
        session["wheels"] = request.form.get("wheels")
    print(session)

    return render_template("about.html", name=my_name, course=my_course,
        car_info=my_car.present_car(), alt=session.get("wheels", 0))

@app.route("/owner", methods=["POST", "GET"])
def owner():
    """ Company route """
    if request.method == "POST":
        my_owners = session.get("owner", [])

        my_owners.append(request.form["firstname"] + " " + request.form["lastname"])
        session["owner"] = my_owners
    print(session)

    return redirect(url_for('about'))

@app.route("/reset")
def reset():
    """ Route for reset session """
    session.pop("test")
    session.pop("wheels")
    session.pop("owner")

    return redirect(url_for('about'))

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)