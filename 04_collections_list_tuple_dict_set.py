"""
Lesson 4 — Collections: list, tuple, dict, set

- list  : ordered, changeable, allows duplicates
- tuple : ordered, not changeable
- dict  : key -> value pairs, keys are unique
- set   : unique items, no guaranteed order

Run:
    py -3 04_collections_list_tuple_dict_set.py
"""

print("=" * 56)
print("1. list")
print("=" * 56)

colors = ["red", "green", "blue"]
print("colors =", colors)
print("first:", colors[0])
print("last:", colors[-1])
print("slice [0:2]:", colors[0:2])

colors.append("yellow")          # add at the end
colors.insert(1, "orange")       # insert at index 1
print("after append and insert:", colors)

removed = colors.pop()           # remove and return the last item
print("popped:", removed)
print("now:", colors)

colors[0] = "crimson"            # replace by index
print("after change:", colors)
print("length:", len(colors))
print("'green' in colors ->", "green" in colors)

numbers = [3, 1, 3, 2]
print("duplicates are allowed:", numbers)
print("sorted copy:", sorted(numbers))
print("original list is unchanged:", numbers)

print()
print("=" * 56)
print("2. tuple")
print("=" * 56)

point = (10, 20)
print("point =", point)
print("x =", point[0], " y =", point[1])

x, y = point  # unpacking
print("unpacked x =", x, " y =", y)

rgb = (255, 128, 0)
print("a tuple can hold several fixed values:", rgb)

single = (5,)  # a one-item tuple needs the comma
print("one-item tuple:", single, type(single))
print("without the comma, (5) is just the number 5:", type((5)))

# point[0] = 99  would raise TypeError — tuples cannot be changed

print()
print("=" * 56)
print("3. dict")
print("=" * 56)

student = {
    "name": "Amina",
    "age": 16,
    "city": "Cairo",
}
print("student =", student)
print("name:", student["name"])

student["age"] = 17              # update
student["course"] = "Python"     # add a new key
print("after updates:", student)

print("grade with .get (missing key):", student.get("grade", "not set"))
print("keys:", list(student.keys()))
print("values:", list(student.values()))

del student["city"]
print("after delete city:", student)
print("'name' in student ->", "name" in student)

print()
print("=" * 56)
print("4. set")
print("=" * 56)

tags = {"python", "basics", "python"}  # the second "python" is dropped
print("tags (duplicates removed):", tags)

tags.add("loops")
tags.discard("missing")  # discard does nothing if the item is absent
print("after add:", tags)
print("count of unique tags:", len(tags))

beginner = {"variables", "strings", "lists"}
intermediate = {"lists", "dicts", "functions"}
print("in both:", beginner & intermediate)       # intersection
print("in either:", beginner | intermediate)     # union
print("only in beginner:", beginner - intermediate)

print()
print("=" * 56)
print("5. Which one to pick")
print("=" * 56)

print("list  — a row of items you may add, remove, or reorder")
print("tuple — a fixed group, like a coordinate or an RGB color")
print("dict  — look up a value by a name (a key)")
print("set   — keep only unique items, or compare groups")
