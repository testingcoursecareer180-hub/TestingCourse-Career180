"""
Lesson 3 — Strings

A string is a sequence of characters. In Python, strings are
immutable: methods return a new string, they do not edit the old one.

Run:
    py -3 03_strings.py
"""

print("=" * 56)
print("1. Creating strings")
print("=" * 56)

single = 'Hello'
double = "World"
both = "It's a nice day"          # double quotes so the apostrophe is fine
quote = 'She said "hi"'           # single quotes so the inner quotes are fine
empty = ""
multiline = """Line one
Line two"""

print(single, double)
print(both)
print(quote)
print("empty length:", len(empty))
print(multiline)

print()
print("=" * 56)
print("2. Combining and repeating")
print("=" * 56)

greeting = "Hello" + " " + "Amina"
print(greeting)
print("ha" * 3)

print()
print("=" * 56)
print("3. f-strings — put values inside text")
print("=" * 56)

name = "Sam"
points = 12
print(f"{name} has {points} points")
print(f"Next level needs {points * 2} points")

print()
print("=" * 56)
print("4. Indexing and slicing")
print("=" * 56)

word = "Python"
print("word =", word)
print("first character word[0] =", word[0])
print("last character word[-1] =", word[-1])
print("word[0:3] =", word[0:3])   # start at 0, stop before 3
print("word[2:] =", word[2:])     # from index 2 to the end
print("word[:4] =", word[:4])     # from the start, stop before 4
print("word[::2] =", word[::2])   # every second character
print("length:", len(word))

print()
print("=" * 56)
print("5. Useful methods")
print("=" * 56)

raw = "  Learn Python  "
print("original: [" + raw + "]")
print("strip:    [" + raw.strip() + "]")
print("lower:", raw.lower().strip())
print("upper:", raw.upper().strip())
print("replace:", "I like Java".replace("Java", "Python"))
print("split:", "red,green,blue".split(","))
print("join:", "-".join(["2026", "11", "16"]))
print("startswith Hello:", "Hello there".startswith("Hello"))
print("count of p:", "apple".count("p"))

print()
print("=" * 56)
print("6. Strings do not change in place")
print("=" * 56)

title = "basics"
shouted = title.upper()
print("title is still", title)
print("shouted is a new string:", shouted)

print()
print("=" * 56)
print("7. Characters you cannot type directly")
print("=" * 56)

print("Tab\tbetween")
print("Line one\nLine two")
print("A quote inside: \"yes\"")
print("Backslash: C:\\Users\\NTG")

print()
print("=" * 56)
print("8. Asking whether text contains something")
print("=" * 56)

sentence = "Python basics"
print("'Python' in sentence ->", "Python" in sentence)
print("'java' in sentence ->", "java" in sentence)
print("'java' not in sentence ->", "java" not in sentence)
