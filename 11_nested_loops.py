"""
Lesson 11 — Nested loops

A loop inside another loop. The inner loop runs all the way
through for every single pass of the outer loop.

break and continue affect only the loop that contains them.

Run:
    py -3 11_nested_loops.py
"""

print("=" * 56)
print("1. Rows and seats")
print("=" * 56)

rows = ["A", "B"]
seats = [1, 2, 3]

for row in rows:
    for seat in seats:
        print(f"seat {row}{seat}")

print()
print("=" * 56)
print("2. A small multiplication table")
print("=" * 56)

for left in range(1, 4):
    for right in range(1, 4):
        print(f"{left} x {right} = {left * right}")
    print("---")

print()
print("=" * 56)
print("3. A list of lists")
print("=" * 56)

grid = [
    [1, 2, 3],
    [4, 5, 6],
]

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        print(f"grid[{row_index}][{col_index}] = {value}")

print()
print("=" * 56)
print("4. Pairs of students")
print("=" * 56)

students = ["Amina", "Sam", "Lee"]
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        print(students[i], "and", students[j])

print()
print("=" * 56)
print("5. break stops the inner loop only")
print("=" * 56)

for outer in range(1, 4):
    print("outer", outer)
    for inner in range(1, 6):
        if inner == 3:
            break
        print("  inner", inner)

print()
print("=" * 56)
print("6. continue skips one inner step")
print("=" * 56)

for outer in (1, 2):
    for inner in range(1, 5):
        if inner == 2:
            continue
        print(f"({outer}, {inner})")
