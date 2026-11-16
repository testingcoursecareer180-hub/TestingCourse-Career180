"""
Lesson 1 — Variables and data types

A variable is a name for a piece of data.
Run: py -3 01_variables_and_data_types.py
"""
#By moahmed Farghali

# A name stores one value. The type comes from that value.
username = "amina"          # str, text
expected_price = 19.99      # float, decimal
item_count = 3              # int, whole number
test_passed = True          # bool, True or False
error_message = None        # None, no value yet

# Text copied from a page is still text until you convert it.
price_on_screen = "19.99"
price_as_number = float(price_on_screen)

# The same name can later hold a new value, even a different type.
actual_price = 19.99
actual_price = 20.50

tester_name = "Radwa"
MAX_RETRIES = 3  # ALL_CAPS marks a value you plan to keep unchanged

print(username, expected_price, item_count, test_passed, error_message)
print(type(username), type(item_count), type(expected_price), type(test_passed), type(error_message))
print(price_on_screen, price_as_number)
print(actual_price, tester_name, MAX_RETRIES)


actual_price = "Test Strings"
print(actual_price)