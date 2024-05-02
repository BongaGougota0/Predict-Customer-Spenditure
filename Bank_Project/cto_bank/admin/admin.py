from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from cto_bank.models import Service, Transaction
from cto_bank import db
from cto_bank.utils.utils import save_picture

admin = Blueprint("admin", __name__)

@admin.route("/admin-payments/", methods=["GET", "POST"])
@login_required
def admin_payments():

    return render_template("admin_payments.html")

@admin.route("/admin-services/", methods=["GET", "POST"])
@login_required
def admin_services():
    services = Service.query.all()
    classes = ['class_0', 'class_1', 'class_2']
    return render_template("admin_services.html", services = services, classes = classes)

@admin.route("/admin-add-service", methods=["POST"])
def add_service():
    if request.method == "POST":
        # file = request.files['image']
        service_class = set_service_class(request.form['service_class'])
        description = request.form['description']
        amount = request.form['amount']
        title = request.form['title']
        service = Service(service_class = service_class, service_amount = amount, service_title = title,\
                           service_description = description)
        db.session.add(service)
        db.session.commit()

        flash("Service added!", 'success')
    return redirect(url_for('admin.admin_services'))

def set_service_class(select_class):
    service_class = ""
    if select_class == "class_0":
        service_class = 0
    elif select_class == "class_1":
        service_class = 1
    elif select_class == "class_2":
        service_class = 2
    return service_class

@admin.route("/admin-transactions/", methods=["GET", "POST"])
@login_required
def admin_transactions():
    transactions = Transaction.query.all()
    classes = ['class_0', 'class_1', 'class_2']
    return render_template("admin_transactions.html", transactions = transactions, classes = classes)