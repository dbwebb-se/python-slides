#!/usr/bin/env python3
"""
My second Flask app.
Minimal Flask application with GET, POST and SESSION, including useful error handlers.
"""

import os
import re
import traceback
from flask import Flask, render_template, request, session, redirect, url_for
from handler import Handler

app = Flask(__name__)
handler = Handler()
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """ Main route """
    handler.read_session(session)
    session["no_of_employees"] = len(handler.get_people())
    session["names"] = handler.get_list_of_names()
    print(session)

    return render_template("index.html", people=handler.get_people(),
        quantity = len(handler.get_people()))

#Route with read_session
@app.route("/company", methods=["POST", "GET"])
def company():
    """ Company route """
    if request.method == "POST":
        handler.read_session(session)
        handler.add_employee(request.form)
        handler.write_session(session)
        session["no_of_employees"] = len(handler.get_people())
        session["names"] = handler.get_list_of_names()

    return render_template("company.html", persons=handler.get_people())

@app.route("/reset")
def reset():
    """ Route for reset session """
    handler.people = []
    handler.add_predefined_employees()
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

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
