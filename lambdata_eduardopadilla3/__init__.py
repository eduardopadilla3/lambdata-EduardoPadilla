"""
lambadata - a collection of DS helper functions
"""

import pandas as pd 
import numpy as np 

from lambdata_eduardopadilla3.dataframe_helper import display_settings
from lambdata_eduardopadilla3.dataframe_helper import train_validate_test

TEST = pd.read_csv('https://docs.google.com/spreadsheets/d/1cCFkJqgf1RaaIQ1xj-WFF5551DyZbuomGrVQZXuiPOo/gviz/tq?tqx=out:csv')
TEST2 = pd.DataFrame(np.ones(10))