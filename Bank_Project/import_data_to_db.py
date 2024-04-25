import pandas as pd
import subprocess
from cto_bank import db, bcrypt, create_app
from cto_bank.models import *

create_app().app_context().push()
db.create_all()

#create dummy users, transactions from csv
def read_csv_file(path_to_file):
    data = pd.read_csv(path_to_file)

    for index, df in data.iterrows():
        transaction_id = get_digit(df['TransactionID'])
        customer_account_no = df['CustomerID']
        customer_gender = df['CustGender']
        date_ = convert_to_date(df['TransactionDate'])
        time_ = convert_to_datetime(df['TransactionTime'])

        add_user = User(name = df['CustomerID'], account_number = customer_account_no, password = customer_account_no, gender = customer_gender)
        db.session.add(add_user)
        db.session.commit()
        #Transaction data record
        add_transaction = Transaction(id=transaction_id, transaction_id=df['TransactionID'], user_id = add_user.id,\
                                       transaction_amount = df['TransactionAmount (R)'], transaction_date = date_,\
                                          transaction_time = time_, transaction_location = df['CustLocation'])
        print(add_user)
        
        db.session.add(add_transaction)
        db.session.commit()
    return 1

def get_digit(csv_id):
    return int(''.join(filter(str.isdigit, csv_id)))

def convert_to_datetime(datetime_string):
    return datetime.strptime(datetime_string[:26], '%Y-%m-%d %H:%M:%S.%f')

def convert_to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')

if __name__ == '__main__':
    read_csv_file("bank_transactions.csv")
    subprocess.call(["chmod","666", "./instance/mysite.db"])