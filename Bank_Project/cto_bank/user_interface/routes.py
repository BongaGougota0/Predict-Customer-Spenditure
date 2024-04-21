from flask import render_template, url_for, flash, redirect, request, Blueprint

user_board = Blueprint('user_board', __name__)

@user_board.route("/my-bank-board", methods=['GET', 'POST'])
def user_board():
    return render_template("user_board.html")