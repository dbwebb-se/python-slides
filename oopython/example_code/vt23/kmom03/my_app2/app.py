#!/usr/bin/env python3
import traceback
import os
import re
from src.account import Account
from src.owner import Owner
from flask import Flask, render_template, session, url_for, redirect

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    session["greeting"] = "Välkommen"

    return render_template("index.j2")

@app.route("/show-accounts", methods=["GET"])
def show_accounts():
    greet = session["greeting"]
    andreas = Owner("Andreas", "933838339", "BTH")
    a1 = Account(100, "räntor", andreas)
    a2 = Account(35, "aktier", andreas)
    a3 = Account(5050, "pension", andreas)
    andreas.accounts.extend([a1, a2, a3])

    return render_template("show_accounts.j2", owner=andreas, greet=greet)

@app.route("/reset")
def reset():
    """ Route for reset session """
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
    app.run(debug=True, port=5002)
