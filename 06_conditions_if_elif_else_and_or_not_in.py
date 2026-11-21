"""
Lesson 6 — if, elif, else, and, or, not, in

if / elif / else pick one path. The first true path wins.
and, or, and not combine questions. in asks if a value is inside something.
Run: py -3 06_conditions_if_elif_else_and_or_not_in.py
"""

actual = "Login"
expected = "Welcome"
if actual == expected:
    check = "pass"
else:
    check = "fail"

levels = []
for defects in (0, 2, 8):
    if defects == 0:
        level = "green"
    elif defects <= 3:
        level = "yellow"
    else:
        level = "red"
    levels.append(level)

logged_in = True
on_checkout_page = False
can_pay = logged_in and on_checkout_page

browser = "firefox"
supported = browser == "chrome" or browser == "firefox"

button_visible = False
must_wait = not button_visible

allowed = ["admin", "editor"]
role = "editor"
role_allowed = role in allowed

environment = "staging"
run_admin_test = environment == "staging" and role in allowed

print(check)
print(levels)
print(can_pay, supported, must_wait, role_allowed, run_admin_test)
