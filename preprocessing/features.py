import re
import pandas as pd
import numpy as np
from sklearn import metrics

train = pd.read_csv('/Users/ccc/src/dev/titanic/data/train.csv')
test = pd.read_csv('/Users/ccc/src/dev/titanic/data/test.csv')

def breakup_names(df):
    """Breakup full name into surname, title, first name"""
    df[['surname','given_name']] = df['Name'].str.split(",", expand= True)
    df[['title', 'first_name']] = df['given_name'].str.split(n=1, expand= True)
    df = df.drop(columns=['Name', 'given_name'])
    return df

def predict_age(df1, df2):
    """Predict age via regression since we have so many NaN"""

train = breakup_names(train)
test = breakup_names(test)
