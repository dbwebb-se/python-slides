#!/usr/bin/env python3
import traceback
from src.account import Account
from src.owner import Owner
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.j2")

@app.route("/show-accounts")
def show_accounts():
    andreas = Owner("Andreas", "933838339", "BTH")
    a1 = Account(100, "räntor", andreas)
    a2 = Account(35, "aktier", andreas)
    a3 = Account(5050, "pension", andreas)
    andreas.accounts.extend([a1, a2, a3])


    return render_template("show_accounts.j2", owner=andreas)



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
    app.run(debug=True)
