"""
Lesson 11 — Nested loops

The inner loop finishes completely once for every item of the outer loop.
break stops only the loop that contains it.
Run: py -3 11_nested_loops.py
"""
#By moahmed Farghali

browsers = ["chrome", "firefox"]
tests = ["login", "search"]
runs = []
for browser in browsers:
    for test in tests:
        runs.append((test, browser))

products = []
for left in range(1, 3):
    for right in range(1, 4):
        products.append(left * right)

suites = [
    ["login", "logout"],
    ["search", "filter"],
]
suite_cases = []
for suite_number, cases in enumerate(suites, start=1):
    for case_name in cases:
        suite_cases.append((suite_number, case_name))

ran = []
for browser in browsers:
    for test in ["login", "stop", "search"]:
        if test == "stop":
            break
        ran.append((browser, test))

print(runs)
print(products)
print(suite_cases)
print(ran)
