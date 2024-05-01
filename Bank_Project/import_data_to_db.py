import pandas as pd
import subprocess
import bcrypt
from cto_bank import db, bcrypt, create_app
from cto_bank.models import *

create_app().app_context().push()
db.create_all()

#create 500 site users and 500 transactions records data from csv
def read_csv_file(path_to_file):
    data = pd.read_csv(path_to_file)

    for _, df in data.iterrows():
        transaction_id = get_digit(df['TransactionID'])
        customer_account_no = df['CustomerID']
        customer_gender = df['CustGender']
        date_ = convert_to_date(df['TransactionDate'])
        time_ = convert_to_datetime(df['TransactionTime'])
        password = generate_password(customer_account_no)

        print(f" user is acc_no: {customer_account_no}, password = {password}, trans_id = {transaction_id}")

        #check user
        add_user = User.query.filter_by(account_number = customer_account_no).first()
        if add_user:
            #skip
            print(f"User already exists {customer_account_no}")
            add_transaction = Transaction.query.filter_by(id = transaction_id).first()
            if add_transaction:
                add_transaction = Transaction(transaction_id=df['TransactionID'], user_id = add_user.id,\
                                            transaction_amount = df['TransactionAmount (R)'], transaction_date = date_,\
                                                transaction_time = time_, transaction_location = df['CustLocation'])
                next
            else:
                add_transaction = Transaction(id=transaction_id, transaction_id=df['TransactionID'], user_id = add_user.id,\
                                            transaction_amount = df['TransactionAmount (R)'], transaction_date = date_,\
                                                transaction_time = time_, transaction_location = df['CustLocation'])
            next
        else:
            add_user = User(name = df['CustomerID'], account_number = customer_account_no,\
                             password = password, gender = customer_gender, age = df['Age'],\
                                  account_balance = df['CustAccountBalance'])
            db.session.add(add_user)
            db.session.commit()
        #Transaction data record
            add_transaction = Transaction.query.filter_by(id = transaction_id).first()
            if add_transaction:
                add_transaction = Transaction(transaction_id=df['TransactionID'], user_id = add_user.id,\
                                            transaction_amount = df['TransactionAmount (R)'], transaction_date = date_,\
                                                transaction_time = time_, transaction_location = df['CustLocation'])
                next
            else:
                add_transaction = Transaction(id=transaction_id, transaction_id=df['TransactionID'], user_id = add_user.id,\
                                            transaction_amount = df['TransactionAmount (R)'], transaction_date = date_,\
                                                transaction_time = time_, transaction_location = df['CustLocation'])        
        db.session.add(add_transaction)
        db.session.commit()
    return 1

def get_digit(csv_id):
    return int(''.join(filter(str.isdigit, csv_id)))

def convert_to_datetime(datetime_string):
    return datetime.strptime(datetime_string[:26], '%Y-%m-%d %H:%M:%S.%f')

def convert_to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')

def generate_password(password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password

if __name__ == '__main__':
    read_csv_file("bank_transactions.csv")
    subprocess.call(["chmod","666", "./instance/database.db"])