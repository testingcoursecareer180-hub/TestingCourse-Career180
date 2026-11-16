"""
Lesson 10 — enumerate, and looping a dict

enumerate pairs each item with its position.
A dict loop can give the field name, the value, or both.
Run: py -3 10_enumerate_and_looping_a_dict.py
"""
#By moahmed Farghali

steps = ["open page", "type email", "click Send"]

numbered_from_zero = []
for index, step in enumerate(steps):
    numbered_from_zero.append((index, step))

numbered_from_one = []
for number, step in enumerate(steps, start=1):
    numbered_from_one.append((number, step))

test_data = {
    "username": "amina",
    "password": "Secret123",
    "expected": "Welcome",
}
fields = []
for field, value in test_data.items():
    fields.append((field, value))

case_names = ["login", "search", "logout"]
durations = {}
for name in case_names:
    durations[name] = len(name)

print(numbered_from_zero)
print(numbered_from_one)
print(fields)
print(durations)
