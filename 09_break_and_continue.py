"""
Lesson 9 — break and continue

break    — leave the loop immediately
continue — skip the rest of this pass and start the next one

Both work in for and while loops.

Run:
    py -3 09_break_and_continue.py
"""

print("=" * 56)
print("1. break — stop when you find what you need")
print("=" * 56)

names = ["Sam", "Lee", "Amina", "Noah"]
found = False

for name in names:
    print("checking", name)
    if name == "Amina":
        found = True
        break

print("found Amina:", found)

print()
print("=" * 56)
print("2. continue — skip items you do not want")
print("=" * 56)

raw_scores = [80, -1, 95, 0, 70]
print("Ignore scores that are not between 1 and 100")

for score in raw_scores:
    if score < 1 or score > 100:
        print(" skip", score)
        continue
    print(" keep", score)

print()
print("=" * 56)
print("3. continue in a while loop")
print("=" * 56)

n = 0
while n < 6:
    n += 1
    if n % 2 == 0:
        continue
    print("odd:", n)

print()
print("=" * 56)
print("4. break only leaves the loop it is inside")
print("=" * 56)

# The outer loop keeps going. Nested loops are lesson 11.
for group in (["a", "b"], ["c", "stop", "d"]):
    for item in group:
        if item == "stop":
            break
        print("item:", item)
    print("finished a group")

print()
print("=" * 56)
print("5. A search that may fail")
print("=" * 56)

target = "kiwi"
basket = ["apple", "pear", "plum"]
for fruit in basket:
    if fruit == target:
        print("Found", target)
        break
else:
    # This else belongs to the for, not to the if.
    # It runs only when break did not happen.
    print(target, "is not in the basket")
