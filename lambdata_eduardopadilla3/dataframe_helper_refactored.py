import pandas as pd 
import numpy as np


class df_helper:
    def __init__(self, df):
        self.df = df

    def display_settings(self):
        print('Size of dataframe is:', self.df.shape)
        self.y = int(input("Enter rows: "))
        self.z = int(input("Enter columns: "))
        return print(self.df.iloc[:self.y, :self.z])

    def train_validate_test(self):
        self.s = input("Enter target col:")
        self.X_train, self.X_val, self.X_test = np.split(self.df.sample(frac=1), [int(.6*len(self.df)), int(.8*len(self.df))])
        self.y_train = self.X_train.pop(self.s)
        self.y_val = self.X_val.pop(self.s)
        self.y_test = self.X_test.pop(self.s)
        return (self.X_train, self.X_val, self.X_test, self.y_train, self.y_val, self.y_test)