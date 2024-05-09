import pickle
from flask_login import current_user
import pandas as pd

from cto_bank.utils.utils import get_agegroup_encoding, get_gender_encoding


class ServicePresenter(object):
    def __init__(self):
        self.model = self.read_model()
        self.user_data = None
    
    def read_model(self):
        with open('../Model/RandomForestClassifier.pkl', 'rb') as f:
            model = pickle.load(f)
            return model
    
    def prepare_data(self, average, total_transactions_value, frequency_trans):
        # average, total_transactions_value, frequency_trans = calculate_average_spend(current_user.id)
        user_df = pd.DataFrame({'Age' : [current_user.age],
                                'Gender' : [get_gender_encoding()],
                                'Location' : [100],
                                'AccountBalance' : [current_user.account_balance],
                                'TransactionFrequency' : [frequency_trans],
                                'AverageSpend' : [average],
                                'total_transactions' : [total_transactions_value],
                                'age_group' : [get_agegroup_encoding()] })
        print(f"service_presenter refreshed: \n {user_df}")
        self.user_data = user_df

    def predict(self):
        print(f"m: predict() :: making prediction")
        prediction = self.model.predict(self.user_data)
        #clean the digit
        class_id = prediction[0]
        print(f"m: predict() :: class for user is: {class_id}")
        return class_id
    
    # def get_user_services(self):
    #     services_to_display = Service.query.filter_by(service_class = self.predict())
    #     if services_to_display:
    #         return services_to_display
    #     return []
