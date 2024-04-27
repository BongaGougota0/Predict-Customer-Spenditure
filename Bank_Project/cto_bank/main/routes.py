from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

from cto_bank.models import Transaction

mainbp = Blueprint('mainbp', __name__)

@mainbp.route("/dashboard/")
@login_required
def dashboard():
    services = ["service 1", "service 2", "service 3"]
    return render_template("default_board.html", services = services)

@mainbp.route("/transactions/")
@login_required
def transactions():
    transactions = Transaction.query.filter_by( user_id = current_user.id)
    return render_template("transactions.html", transactions = transactions)

@mainbp.route("/bank-services/")
@login_required
def services():
    services = ["service 1", "service 2", "service 3"]
    #get all services suggested for this user.
    return render_template("transactions.html", services = services)

@mainbp.route("/payments/")
@login_required
def payments():
    services = ["service 1", "service 2", "service 3"]
    return render_template("transactions.html", services = services)

@mainbp.route("/settings/")
@login_required
def settings():
    return render_template("transactions.html")