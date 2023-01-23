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
    car = my_car

    session["test"] = "Testing!"
    # session["car"] = my_car.to_json()
    if request.form.get("wheels") :
        session["wheels"] = request.form.get("wheels")
    if session.get("car"):
        car = Car.from_json(session["car"])
    print(session)

    return render_template("about.html", car_info=car.present_car(),
        info=session.get("test", "Empty"), alt=session.get("wheels", 0),
        owners=", ".join(session.get("owner", [])),
        services=", ".join(session.get("service", [])), car=car)

@app.route("/owner", methods=["POST", "GET"])
def owner():
    """ Adding owner information """
    service_list = ["Insurance", "Roadside assistance"]

    if request.method == "POST":
        if request.form["firstname"] != "":
            my_owners = session.get("owner", [])
            my_owners.append(request.form["firstname"])
            session["owner"] = my_owners
        if (request.form["model"] != "") & (request.form["price"] != ""):
            session["car"] = Car(request.form["model"], request.form["price"]).to_json()
        session["service"] = []
        if request.form.get("service"):
            session["service"] = [service_list[int(s)] for s in request.form.getlist("service")]
    print(session)

    return redirect(url_for('about'))

@app.route("/reset")
def reset():
    """ Route for reset session """
    # session.pop("test")
    # session.pop("wheels")
    _ = [session.pop(key) for key in list(session.keys())]

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
