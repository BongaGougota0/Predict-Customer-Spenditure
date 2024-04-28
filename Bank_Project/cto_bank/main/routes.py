from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from cto_bank import db

from cto_bank.models import Transaction, Service, User

mainbp = Blueprint('mainbp', __name__)

@mainbp.route("/dashboard/")
@login_required
def dashboard():
    services = Service.query.all()
    return render_template("default_board.html", services = services)

@mainbp.route("/transactions/")
@login_required
def transactions():
    transactions = Transaction.query.filter_by( user_id = current_user.id)
    return render_template("transactions.html", transactions = transactions)

@mainbp.route("/bank-services/")
@login_required
def services():
    #get all services suggested for this user.
    services = Service.query.all()
    return render_template("services.html", services = services)

@mainbp.route("/payments/")
@login_required
def payments():
    services = ""
    return render_template("transactions.html", services = services)

@mainbp.route("/settings/")
@login_required
def settings():
    return render_template("transactions.html")

@mainbp.route("/deposit-into-your-account", methods=["POST"])
def deposit():
    if request.method == 'POST':
        #update user account balance
        account_balance = User.query.get(current_user.id)
        top_up_amount = int(request.form['account_top_up'])
        account_balance.account_balance += top_up_amount
        db.session.commit()

        flash('Funds deposited into your account.', 'success')
    if current_user.account_balance == 'None':
        print(f"render on visit: account balance {current_user.account_balance}")
        current_user.account_balance = 0
        db.session.commit()

    return redirect(url_for('mainbp.transactions'))