"""
Lesson 8 — for loop: go through a collection

for name in collection:
    ...

The loop variable (name) takes the next item on every pass.
This works for list, tuple, str, set, dict, and range.

Run:
    py -3 08_for_loop_go_through_a_collection.py
"""

print("=" * 56)
print("1. list")
print("=" * 56)

names = ["Amina", "Sam", "Lee"]
for name in names:
    print("Hello,", name)

print()
print("=" * 56)
print("2. tuple")
print("=" * 56)

point = (4, 7, 2)
for coordinate in point:
    print("coordinate:", coordinate)

print()
print("=" * 56)
print("3. string — one character at a time")
print("=" * 56)

word = "code"
for character in word:
    print(character)

print()
print("=" * 56)
print("4. set — each unique item once")
print("=" * 56)

# A set does not promise an order, so this print order can vary.
languages = {"Python", "Go", "Python", "Rust"}
print("unique languages:", languages)
for language in languages:
    print("language:", language)

print()
print("=" * 56)
print("5. Build a new list while looping")
print("=" * 56)

prices = [10, 20, 5]
with_tax = []
for price in prices:
    with_tax.append(price * 1.1)
print("prices:", prices)
print("with 10% tax:", with_tax)

print()
print("=" * 56)
print("6. Loop a list of tuples")
print("=" * 56)

students = [("Amina", 90), ("Sam", 76), ("Lee", 88)]
for name, score in students:
    print(f"{name} scored {score}")

print()
print("=" * 56)
print("7. Do not change the list size while you loop it")
print("=" * 56)

# Removing or inserting items in the list you are looping can skip items.
# Collect what you want in a new list instead.
numbers = [1, 2, 3, 4, 5]
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print("evens:", evens)
