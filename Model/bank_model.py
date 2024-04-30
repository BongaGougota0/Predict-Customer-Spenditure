# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:09:06 2024

@author: gmvn
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import pandas as pd

df = pd.read_csv('data_for_lr_model.csv')
# feature columns
X = df[['Age', 'Gender', 'Location', 'AccountBalance',
       'TransactionAmount', 'TransactionFrequency', 'AverageSpend',
       'total_transactions', 'age_group']]
y = df['Class'] # target column
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# logistic regression model
model = LogisticRegression(max_iter=10000)
# training data
model.fit(X_train, y_train)
# testing data
y_pred = model.predict(X_test)
# model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

with open('logistic_regression_model.pkl', 'wb') as f:
    pickle.dump(model, f)