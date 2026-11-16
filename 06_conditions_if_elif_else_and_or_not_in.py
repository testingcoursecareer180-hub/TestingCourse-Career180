"""
Lesson 6 — Conditions

if / elif / else choose one path.
and / or / not combine comparisons.
in checks whether a value is inside a collection or a string.

Run:
    py -3 06_conditions_if_elif_else_and_or_not_in.py
"""

print("=" * 56)
print("1. if")
print("=" * 56)

temperature = 31
if temperature >= 30:
    print(temperature, "C is hot")

print()
print("=" * 56)
print("2. if / else — one of two paths")
print("=" * 56)

score = 58
if score >= 60:
    print(score, "-> pass")
else:
    print(score, "-> fail")

print()
print("=" * 56)
print("3. if / elif / else — first true branch wins")
print("=" * 56)

for points in (95, 82, 74, 61, 40):
    if points >= 90:
        grade = "A"
    elif points >= 80:
        grade = "B"
    elif points >= 70:
        grade = "C"
    elif points >= 60:
        grade = "D"
    else:
        grade = "F"
    print(points, "->", grade)

print()
print("=" * 56)
print("4. and — both sides must be true")
print("=" * 56)

age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("Welcome in")
else:
    print("Cannot enter")

has_ticket = False
if age >= 18 and has_ticket:
    print("Welcome in")
else:
    print("Need a ticket, even if you are old enough")

print()
print("=" * 56)
print("5. or — at least one side must be true")
print("=" * 56)

is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No class today")
else:
    print("Class today")

print()
print("=" * 56)
print("6. not — flips True and False")
print("=" * 56)

is_logged_in = False
if not is_logged_in:
    print("Please log in")

print("not True ->", not True)
print("not False ->", not False)

print()
print("=" * 56)
print("7. in / not in — membership")
print("=" * 56)

colors = ["red", "green", "blue"]
print("'green' in colors ->", "green" in colors)
print("'pink' not in colors ->", "pink" not in colors)
print("'Py' in 'Python' ->", "Py" in "Python")
print("'age' in student dict ->", "age" in {"name": "Sam", "age": 16})

print()
print("=" * 56)
print("8. Combining them")
print("=" * 56)

role = "editor"
allowed = ["admin", "editor"]
active = True

if active and role in allowed:
    print(role, "may edit")
elif not active:
    print("Account is inactive")
else:
    print(role, "may only read")

# and is checked before or, unless you add parentheses.
# True or False and False  ==  True or (False and False)  ==  True
print("True or False and False ->", True or False and False)
print("(True or False) and False ->", (True or False) and False)
