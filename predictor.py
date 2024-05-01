# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:56:46 2024

@author: gmvn
"""
import pickle
import pandas as pd

with open('RandomForestClassifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions on new data
new_data = pd.DataFrame({'Age': [39], 'Gender': [1], 'Location': [922], 'AccountBalance': [199], 'TransactionAmount': [50], 'TransactionFrequency': [5], 'AverageSpend': [540], 'total_transactions': [1], 'age_group': [1]})
prediction = model.predict(new_data)
print(prediction)