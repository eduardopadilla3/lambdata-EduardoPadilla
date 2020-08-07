# lambdata-EduardoPadilla

# What is it?
Found in this package are two function:
1. display_settings()
2. train_validate_test()

# Main Features
- Takes user input and prints a Dataframe based on the inputs
- Takes user input and creates train, validation, test, and each of the targets 

# Where to get it?
The source code is currently hosted on GitHub at: https://github.com/eduardopadilla3/lambdata-EduardoPadilla

It can be intalled using: pip install -i https://test.pypi.org/simple/ lambdata-eduardopadilla3

# Examples
from lambdata_eduardopadilla3.dataframe_helper import display_settings, train_validate_test


display_settings(x)

X_train, X_val, X_test, y_train, y_val, y_test = train_validate_test(x)
