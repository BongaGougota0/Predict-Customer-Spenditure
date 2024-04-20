# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:09:06 2024

@author: gmvn
"""

import pandas as pd

data = pd.read_csv("bank_transactions.csv")

data.head()
data.info()

data.isna().sum()
data['CustAccountBalance'].fillna(0, inplace=True)
data.isna().sum()
data.head()

locations=data['CustLocation'].value_counts()

print()