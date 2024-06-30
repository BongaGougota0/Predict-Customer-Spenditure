from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user
from cto_bank import db, bcrypt

from cto_bank.models import Service, User

front = Blueprint('front', __name__)

@front.route("/home/", methods=['GET', 'POST'])
@front.route("/", methods=['GET', 'POST'])
def home():
    services = Service.query.all()
    return render_template('index.html', services = services)

@front.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        acc_number = request.form['account_number']
        acc_password = request.form['password']
        #check user exists
        user = User.query.filter_by(account_number = acc_number).first()
        if user and bcrypt.check_password_hash(user.password, acc_password):
            if user.role == "admin":
                login_user(user, remember = True)
                return redirect( url_for('admin.admin_transactions') )
            login_user(user, remember = True)
            flash('User logged in','success')
            return redirect(url_for('mainbp.dashboard'))
        flash('Please check your account no. or password', 'warning')
    flash("Login with acc. C2548543 & psswd : C2548543 , do deposits and subscribe to services\
           and see service recommendations change for your account. ", "success")
    return render_template('login.html')


@front.route("/about/", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@front.route("/services/", methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@front.route("/logout", methods=["GET"])
def logout():
    logout_user()
    flash('Logged Out!', 'warning')
    return redirect(url_for('front.home'))