"""
Lesson 1 — Variables and data types

A variable is a name that points to a value. Python figures out the
type from the value you store (this is called dynamic typing).

Run:
    py -3 01_variables_and_data_types.py
"""

print("=" * 56)
print("1. Creating variables")
print("=" * 56)

student_name = "Amina"
age = 16
height_m = 1.62
is_enrolled = True
nickname = None  # None means "no value yet"

print("name:", student_name)
print("age:", age)
print("height (m):", height_m)
print("enrolled:", is_enrolled)
print("nickname:", nickname)

print()
print("=" * 56)
print("2. Asking Python for the type")
print("=" * 56)

print(student_name, "->", type(student_name))
print(age, "->", type(age))
print(height_m, "->", type(height_m))
print(is_enrolled, "->", type(is_enrolled))
print(nickname, "->", type(nickname))

print()
print("=" * 56)
print("3. The basic types")
print("=" * 56)

whole_number = 42          # int   — whole numbers, positive or negative
decimal_number = 3.14      # float — numbers with a decimal point
text = "Hello"             # str   — text, in quotes
flag = False               # bool  — only True or False
empty = None               # NoneType — the absence of a value

print(whole_number, decimal_number, text, flag, empty)

print()
print("=" * 56)
print("4. A name can be pointed at a new value")
print("=" * 56)

score = 10
print("score starts at", score, type(score))

score = 10 + 5
print("score is now", score)

score = "ten"  # the same name can later hold a different type
print("score is now", score, type(score))

print()
print("=" * 56)
print("5. Several names at once")
print("=" * 56)

x, y, z = 1, 2, 3
print("x =", x, " y =", y, " z =", z)

a = b = c = 0  # three names, one value
print("a =", a, " b =", b, " c =", c)

print()
print("=" * 56)
print("6. Converting between types")
print("=" * 56)

digits = "42"
print("int('42') =", int(digits), type(int(digits)))
print("float('3.5') =", float("3.5"))
print("str(100) =", str(100), type(str(100)))
print("bool(0) =", bool(0), " bool(1) =", bool(1))
print("bool('') =", bool(""), " bool('hi') =", bool("hi"))

print()
print("=" * 56)
print("7. Names should describe the value")
print("=" * 56)

# Good: letters, digits, underscore. Cannot start with a digit.
lesson_count = 12
MAX_SCORE = 100  # ALL_CAPS is a common style for values you do not plan to change

print("lessons:", lesson_count)
print("max score:", MAX_SCORE)
print("Use lowercase_with_underscores for normal variables.")
