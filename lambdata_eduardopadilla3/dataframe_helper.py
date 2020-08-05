"""
some function to help cleaning and handling dataframes

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def display_settings(df):
    print('Size of dataframe is:', df.shape)
    y = int(input("Enter rows: "))
    z = int(input("Enter columns: "))
    return print(df.iloc[:y, :z])


def train_validate_test(df):
    s = input("Enter target col:")
    X = df
    y = X.pop(s)
    X_train, X_test, y_train, y_test =
    train_test_split(X, y, test_size=0.2, random_state=1)
    X_train, X_val, y_train, y_val =
    train_test_split(X_train, y_train, test_size=0.25, random_state=1)
    return (X_train, X_val, X_test, y_train, y_val, y_test)
