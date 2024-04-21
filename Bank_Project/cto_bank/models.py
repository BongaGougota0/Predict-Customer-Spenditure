from datetime import datetime
from flask import current_app
from cto_bank import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active = db.Column(db.String(5), nullable=False)
    role = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f""

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_amount = db.Column(db.Integer, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transaction_location = db.Column(db.String(200), nullable=False)
    
    # One-to-one relationship with Service
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), unique=True)
    service = db.relationship('Service', backref='transaction', uselist=False)

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id},\
         transaction_amount={self.transaction_amount}, transaction_date={self.transaction_date},\
          transaction_location={self.transaction_location})"

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_amount = db.Column(db.Integer, nullable=False)
    service_title = db.Column(db.String(100), nullable=False)
    service_description = db.Column(db.String(400), nullable=False)
    service_image = db.Column(db.String(200), default="service.jpg")

    def __repr__(self):
        return f"Service(service_amount={self.service_amount}, service_title={self.service_title},\
         service_description={self.service_description}, service_image={self.service_image})"

