"""
Lesson 7 — Types of loops

Python has two loops:

- for   : repeat once for each item in a collection, or each number in a range
- while : repeat as long as a condition stays true

Use for when you know the sequence. Use while when you stop
because something changes (a counter, user input, a flag).

Run:
    py -3 07_types_of_loops.py
"""

print("=" * 56)
print("1. for — once per item")
print("=" * 56)

for fruit in ["apple", "banana", "cherry"]:
    print("fruit:", fruit)

print()
print("=" * 56)
print("2. for with range — a count you control")
print("=" * 56)

print("range(5) -> 0, 1, 2, 3, 4")
for n in range(5):
    print("n =", n)

print("range(1, 4) -> 1, 2, 3  (stop is not included)")
for n in range(1, 4):
    print("n =", n)

print("range(0, 10, 2) -> 0, 2, 4, 6, 8  (step of 2)")
for n in range(0, 10, 2):
    print("n =", n)

print()
print("=" * 56)
print("3. while — keep going while the test is true")
print("=" * 56)

count = 3
while count > 0:
    print("count =", count)
    count -= 1
print("done, count =", count)

print()
print("=" * 56)
print("4. The same countdown, written both ways")
print("=" * 56)

print("for version:")
for n in range(3, 0, -1):
    print(" ", n)

print("while version:")
n = 3
while n > 0:
    print(" ", n)
    n -= 1

print()
print("=" * 56)
print("5. A while loop needs a change that can make it stop")
print("=" * 56)

# Without count += 1 this loop would never end.
# Always make the condition able to become False.
total = 0
count = 1
while count <= 4:
    total += count
    count += 1
print("1 + 2 + 3 + 4 =", total)

print()
print("=" * 56)
print("6. Choosing")
print("=" * 56)

print("for   — files in a folder, names in a list, range(10)")
print("while — 'keep asking until the answer is valid'")
