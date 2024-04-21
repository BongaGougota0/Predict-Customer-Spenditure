from flask import render_template, url_for, flash, redirect, request, Blueprint

front = Blueprint('front', __name__)

@front.route("/home/", methods=['GET', 'POST'])
@front.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@front.route("/login/", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@front.route("/about/", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@front.route("/services/", methods=['GET', 'POST'])
def services():
    return render_template('services.html')