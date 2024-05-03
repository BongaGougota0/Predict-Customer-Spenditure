from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from cto_bank.utils.service_presenter import ServicePresenter

service_presenter = ServicePresenter()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "front.login"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = 'secret_key_for_flask_session'
migrate = Migrate(app, db)

def create_app():
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from cto_bank.front.routes import front
    from cto_bank.main.routes import mainbp
    from cto_bank.admin.admin import admin
    app.register_blueprint(mainbp)
    app.register_blueprint(front)
    app.register_blueprint(admin)
    return app