from flask import render_template, url_for, flash, redirect, request, Blueprint

mainbp = Blueprint('mainbp', __name__)

@mainbp.route("/dashboard/")
def dashboard():
    services = ["service 1", "service 2", "service 3"]
    return render_template("default_board.html", services = services)

@mainbp.route("/transactions/")
def transactions():
    services = ["service 1", "service 2", "service 3"]
    return render_template("transactions.html", services = services)

@mainbp.route("/services/")
def services():
    services = ["service 1", "service 2", "service 3"]
    return render_template("transactions.html", services = services)

@mainbp.route("/payments/")
def payments():
    services = ["service 1", "service 2", "service 3"]
    return render_template("transactions.html", services = services)

@mainbp.route("/settings/")
def settings():
    return render_template("transactions.html")