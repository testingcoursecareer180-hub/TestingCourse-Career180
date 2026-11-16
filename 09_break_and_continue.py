"""
Lesson 9 — break and continue

break leaves the loop immediately.
continue skips the rest of this pass and starts the next item.
Run: py -3 09_break_and_continue.py
"""
#By moahmed Farghali

results = ["pass", "pass", "fail", "pass"]
checked = []
for result in results:
    checked.append(result)
    if result == "fail":
        break

rows = ["login", "", "checkout", ""]
kept = []
for row in rows:
    if row == "":
        continue
    kept.append(row)

# break stops only the inner loop. The outer loop continues.
groups = [["a", "b"], ["c", "stop", "d"]]
kept_items = []
for group in groups:
    for item in group:
        if item == "stop":
            break
        kept_items.append(item)

print(checked)
print(kept)
print(kept_items)
