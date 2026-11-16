"""
Lesson 5 — Conditions and loops together

A condition decides whether a block of code runs.
A loop repeats a block of code.

Real programs use both: the loop walks through data, and the
condition decides what to do with each item.

The next lessons split this apart:
  06  if / elif / else, and / or / not / in
  07  types of loops
  08  for loop over a collection
  09  break and continue
  10  enumerate and looping a dict
  11  nested loops

Run:
    py -3 05_conditions_and_loops.py
"""

print("=" * 56)
print("1. A loop walks the data; if labels each item")
print("=" * 56)

temperatures = [18, 22, 31, 15, 27]
hot_days = 0

for temp in temperatures:
    if temp >= 30:
        label = "hot"
        hot_days += 1
    elif temp >= 20:
        label = "warm"
    else:
        label = "cool"
    print(temp, "C ->", label)

print("Hot days:", hot_days)

print()
print("=" * 56)
print("2. A while loop can stop when a condition becomes false")
print("=" * 56)

password = ""
attempts = ["no", "python"]
index = 0

while password != "python" and index < len(attempts):
    password = attempts[index]
    index += 1
    if password == "python":
        print("Access granted on try", index)
    else:
        print("Rejected:", password)

print()
print("=" * 56)
print("3. Count items that match a condition")
print("=" * 56)

scores = [55, 70, 90, 61, 40, 88]
passed = 0

for score in scores:
    if score >= 60:
        passed += 1

print("scores:", scores)
print("passed:", passed, "of", len(scores))
print("Detail lives in lessons 06 through 11.")
