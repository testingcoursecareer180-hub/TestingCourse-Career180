"""
Lesson 8 — for loop over a collection

for item in collection:
    the name item takes the next value on each pass.
Run: py -3 08_for_loop_go_through_a_collection.py
"""
#By moahmed Farghali

cases = ["login", "logout", "reset password"]
case_names = []
for case_name in cases:
    case_names.append(case_name)

# A string gives one character at a time.
code = "A-19"
characters = []
for character in code:
    characters.append(character)

# A set keeps each value once. Its order is not guaranteed.
seen_bugs = {"BUG-1", "BUG-2", "BUG-1"}

rows = [("login", "pass"), ("checkout", "fail")]
summary = []
for case_name, result in rows:
    summary.append((case_name, result))

numbers = [1, 2, 3, 4, 5]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(case_names)
print(characters)
print(seen_bugs)
print(summary)
print(even_numbers)
