"""
Created on 2026-04-18
@author: Andrey

Description
-----------
This file preprocesses the data.
"""

#%% IMPORTS

import pandas as pd

#%% LOAD & PREPROCESS DATA

# Load data & create a 'clean' copy
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df_clean = df.copy()

# Rename columns keeping the pattern
df_clean.rename(columns={
    'customerID':'CustomerID',
    'gender': 'Gender',
    'tenure': 'Tenure'
}, inplace=True)

# Adapt data type - from string to numbers
df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')

# Drop missing values from the transformation above
df_clean = df_clean.dropna()
"""
Obs: 1.All missing values come from empty strings in 'TotalCharges'.
     2.All of them have 'No' for Churn, which is the most common value.
"""



