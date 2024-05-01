import pickle
from flask_login import current_user
import pandas as pd

from cto_bank.models import Service


class ServicePresenter:
    def __init__(self):
        self.model = self.read_model()
        self.user_data = None
    
    def read_model(self):
        with open('RandomForestClassifier.pkl', 'rb') as f:
            model = pickle.load(f)
            return model
    
    def prepare_data(self):
        user_df = pd.DataFrame({'Age' : [23],
                                'Gender' : [34],
                                'Location' : [43],
                                'AccountBalance' : [345],
                                'TransactionAmount' :[456],
                                'TransactionFrequency' : [46],
                                'AverageSpend' : [64],
                                'total_transactions' : [64],
                                'age_group' : [646] })
        self.user_data = user_df

    def predict(self):
        prediction = self.model.predict(self.user_data)
        #clean the digit
        class_id = prediction[0]
        print(f"m: predict() :: check class id f{class_id}")
        return class_id
    
    def get_user_service(self):
        services_to_display = Service.query.filter_by(service_class = self.predict())
        if services_to_display:
            return services_to_display
        return []
