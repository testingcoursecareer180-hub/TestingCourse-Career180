"""
Lesson 2 — Operators

Symbols that calculate or compare values.
and / or / not / in are in lesson 6.
Run: py -3 02_operators.py
"""

price = 20
quantity = 3

# / is a decimal. // is how many whole times quantity fits in price. % is the leftover.
added = price + 5  
subtracted = price - 5
multiplied = price * quantity
divided = price / quantity
whole_divided = 20 // 3
remainder = 20 % 3
power = 2 ** 3


# == compares. = only stores. * happens before + unless you add parentheses.
expected = 60
actual = 80
equal = actual == expected
greater = actual > expected
without_parentheses = 2 + 3 * 4
with_parentheses = (2 + 3) * 4

# += adds onto the current value.
retry_count = 0
retry_count += 1 #--> retry_count = retry_count + 1
retry_count += 1    

# Use "is" only to ask whether a value is None.
message = "Heeelo World this string is not empty"
message_is_empty = message is not None

print(added, subtracted, multiplied, divided, whole_divided, remainder, power)
print(equal, greater, without_parentheses, with_parentheses)
print(retry_count, message_is_empty)
