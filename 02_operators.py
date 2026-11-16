"""
Lesson 2 — Operators

Operators are symbols that do work on values: math, comparison,
and updating a variable.

and / or / not / in are covered in lesson 6, where they are used
inside conditions.

Run:
    py -3 02_operators.py
"""
#By moahmed Farghali

print("=" * 56)
print("1. Arithmetic")
print("=" * 56)

a = 17
b = 5
print("a =", a, " b =", b)
print("a + b =", a + b)    # add
print("a - b =", a - b)    # subtract
print("a * b =", a * b)    # multiply
print("a / b =", a / b)    # divide — always a float in Python 3
print("a // b =", a // b)  # floor division — whole number of times b fits in a
print("a % b =", a % b)    # remainder
print("a ** b =", a ** b)  # power: 17 to the power of 5
print("2 ** 4 =", 2 ** 4)  # a smaller power, easier to check by hand

print()
print("=" * 56)
print("2. Comparison — each result is True or False")
print("=" * 56)

score = 80
passing = 60
print("score =", score, " passing =", passing)
print("score == 80 ->", score == 80)
print("score != 80 ->", score != 80)
print("score > passing ->", score > passing)
print("score < passing ->", score < passing)
print("score >= 80 ->", score >= 80)
print("score <= 79 ->", score <= 79)

print()
print("=" * 56)
print("3. Assignment — store, and update in place")
print("=" * 56)

lives = 3
print("lives =", lives)

lives += 1  # same as lives = lives + 1
print("after += 1 ->", lives)

lives -= 2
print("after -= 2 ->", lives)

lives *= 4
print("after *= 4 ->", lives)

lives //= 3
print("after //= 3 ->", lives)

print()
print("=" * 56)
print("4. Identity — is / is not  (same object, not equal value)")
print("=" * 56)

left = None
right = None
zero = 0
print("left is right ->", left is right)  # both names point at the one None object
print("left is not zero ->", left is not zero)

# Prefer == when you care about the value.
# Prefer is when you care whether something is None.
print("left is None ->", left is None)

print()
print("=" * 56)
print("5. Order of operations")
print("=" * 56)

# Parentheses, then powers, then * / // %, then + -
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("2 ** 3 * 2 =", 2 ** 3 * 2)
