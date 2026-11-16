"""
Lesson 10 — enumerate, and looping a dict

enumerate pairs each item with its position: (index, item).
A dict can be looped by keys, by values, or by key and value together.

Run:
    py -3 10_enumerate_and_looping_a_dict.py
"""

print("=" * 56)
print("1. enumerate — index and item")
print("=" * 56)

tasks = ["open file", "read lines", "close file"]
for index, task in enumerate(tasks):
    print(index, task)

print()
print("=" * 56)
print("2. Start counting at 1")
print("=" * 56)

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print()
print("=" * 56)
print("3. A dict loop gives the keys")
print("=" * 56)

book = {
    "title": "Python Basics",
    "pages": 120,
    "language": "English",
}

for key in book:
    print(key, "->", book[key])

print()
print("=" * 56)
print("4. .items() — key and value together")
print("=" * 56)

for key, value in book.items():
    print(f"{key}: {value}")

print()
print("=" * 56)
print("5. .keys() and .values()")
print("=" * 56)

print("keys:", list(book.keys()))
print("values:", list(book.values()))

for value in book.values():
    print("value:", value)

print()
print("=" * 56)
print("6. enumerate the pairs when you also want a position")
print("=" * 56)

for index, (key, value) in enumerate(book.items(), start=1):
    print(f"{index}. {key} = {value}")

print()
print("=" * 56)
print("7. Build a dict while looping")
print("=" * 56)

names = ["Amina", "Sam", "Lee"]
name_lengths = {}
for name in names:
    name_lengths[name] = len(name)
print(name_lengths)
