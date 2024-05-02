from flask import current_app
from flask_login import current_user
import secrets, os
from PIL import Image

def save_picture(form_picture, img_size):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/images/", picture_fn)
    output_size = img_size
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

# def calculate_average_spend(user_id):
#     total_spend = db.session.query(func.sum(Transaction.transaction_amount)).filter_by(user_id=user_id).scalar()
#     num_transactions = db.session.query(func.count(Transaction.id)).filter_by(user_id=user_id).scalar()
#     if num_transactions > 0:
#         return total_spend / num_transactions, total_spend, num_transactions
#     else:
#         return 0, 0, 0

def get_agegroup_encoding():
    if int(current_user.age) > 13 and int(current_user.age) <= 17:
        return 0
    elif int(current_user.age) >= 18 and int(current_user.age) <= 34:
        return 1
    elif int(current_user.age) >= 35:
        return 2
    
def get_gender_encoding():
    if current_user.gender == "M":
        return 1
    elif current_user.gender == "F":
        return 2
    else:
        return 0