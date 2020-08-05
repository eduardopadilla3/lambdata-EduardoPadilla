"""
some function to help cleaning and handling dataframes

"""

import pandas as pd
import numpy as np


def display_settings(df):
    print('Size of dataframe is:', df.shape)
    y = int(input("Enter rows: "))
    z = int(input("Enter columns: "))
    return print(df.iloc[:y, :z])


def train_validate_test(df):
    s = input("Enter target col:")
    X_train, X_val, X_test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
    y_train = X_train.pop(s)
    y_val = X_val.pop(s)
    y_test = X_test.pop(s)
    return (X_train, X_val, X_test, y_train, y_val, y_test)
