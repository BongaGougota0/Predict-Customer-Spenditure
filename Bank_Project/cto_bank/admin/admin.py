from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from cto_bank.models import Service, Transaction
from cto_bank import db

admin = Blueprint("admin", __name__)

@admin.route("/admin-payments/", methods=["GET", "POST"])
@login_required
def admin_payments():

    return render_template("admin_payments.html")

@admin.route("/admin-services/", methods=["GET", "POST"])
@login_required
def admin_services():
    services = Service.query.all()
    return render_template("admin_services.html", services = services)

@admin.route("/admin-add-service", methods=["POST"])
def add_service():
    if request.method == "POST":
        print("adding a service")
        description = request.form['description']
        amount = request.form['amount']
        title = request.form['title']
        
        service = Service(service_amount = amount, service_title = title, service_description = description)
        db.session.add(service)
        db.session.commit()

        flash("Service added!", 'success')
    return redirect(url_for('admin.admin_services'))

@admin.route("/admin-transactions/", methods=["GET", "POST"])
@login_required
def admin_transactions():
    transactions = Transaction.query.all()
    return render_template("admin_transactions.html", transactions = transactions)