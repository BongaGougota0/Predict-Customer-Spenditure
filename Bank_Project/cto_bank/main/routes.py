from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from sqlalchemy import func
from cto_bank import db
from cto_bank import service_presenter
from cto_bank.models import Transaction, Service, User
import secrets

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
    av, t, f = calculate_average_spend(current_user.id)
    service_presenter.prepare_data(av, t, f)
    suggested_services = service_presenter.predict()
    # print(f"m mainbp.services :: see suggested services by model {suggested_services}")
    services = Service.query.filter_by(service_class = int(suggested_services)).all()
    # print(f" found services are {services}")
    return render_template("services.html", services = services)

def calculate_average_spend(user_id):
    total_spend = db.session.query(func.sum(Transaction.transaction_amount)).filter_by(user_id=user_id).scalar()
    num_transactions = db.session.query(func.count(Transaction.id)).filter_by(user_id=user_id).scalar()
    if num_transactions > 0:
        return total_spend / num_transactions, total_spend, num_transactions
    else:
        return 0, 0, 0

@mainbp.route("/payments/")
@login_required
def payments():
    services = ""
    return render_template("transactions.html", services = services)

@mainbp.route("/settings/", methods = ["POST", "GET"])
@login_required
def settings():
    if request.method == 'POST':
        #update user account balance
        
        gender = request.form['gender'] # Gender is encoded in the model (1 or 0)
        age = int(request.form['age']) # make it a double
        current_user.age = age
        current_user.gender = gender
        db.session.commit()

        flash('User details updated!', 'success')
        return redirect( url_for('mainbp.settings') )

    return render_template("settings.html")

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

@mainbp.route("/transact-user/<int:service_id>", methods=['POST','GET'])
def transact(service_id):
    service_charge = Service.query.get(service_id)
    #check user can transact this service
    if int(current_user.account_balance) >= int(service_charge.service_amount):
        current_user.account_balance -= service_charge.service_amount
        new_transaction = Transaction(transaction_id = secrets.token_hex(6), user_id = current_user.id, transaction_amount = service_charge.service_amount, transaction_location = 1, service_id = service_charge.id)
        db.session.add(new_transaction)
        db.session.commit()
        flash('transaction succesfully complete', 'success')
        return redirect(url_for('mainbp.transactions'))
    
    flash('Sorry you have insufficient funds', 'danger')
    return redirect(url_for('mainbp.transactions'))

@mainbp.route("/delete-transaction/<int:transaction_id>")
def delete_transaction(transaction_id):
    to_delete_transaction = Transaction.query.filter_by(id = transaction_id).first()
    db.session.delete(to_delete_transaction)
    db.session.commit()
    flash("tranasction deleted!", "warning")
    return redirect(url_for('mainbp.transactions'))