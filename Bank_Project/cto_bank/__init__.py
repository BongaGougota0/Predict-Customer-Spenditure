from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "front.login"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'

def create_app():
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from cto_bank.front.routes import front
    app.register_blueprint(front)
    return app

from cto_bank.models import *