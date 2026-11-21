"""
Lesson 5 — Conditions and loops together

The loop visits each item. The if decides what that item means.
Run: py -3 05_conditions_and_loops.py
"""

actual_titles = ["Welcome", "Login", "Welcome", "Error"]
expected_title = "Welcome"
passed = 0

for title in actual_titles:
    if title == expected_title:
        passed += 1

tries = ["wrong", "python"]
attempt = 0
found = False

while attempt < len(tries) and not found:
    answer = tries[attempt]
    attempt += 1
    if answer == "python":
        found = True

print(passed, "of", len(actual_titles))
print(found, attempt)
