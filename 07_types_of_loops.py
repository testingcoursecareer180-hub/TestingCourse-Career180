"""
Lesson 7 — for and while

for repeats once for each item, or each number in a range.
while repeats while a condition stays true. Change something inside it, or it never stops.
Run: py -3 07_types_of_loops.py
"""
#By moahmed Farghali

browsers_run = []
for browser in ["chrome", "firefox", "edge"]:
    browsers_run.append(browser)

# range(3) is 0, 1, 2. It stops before 3.
retries = []
for number in range(3):
    retries.append(number)

retries_left = 3
while retries_left > 0:
    retries_left -= 1

countdown = []
for n in range(3, 0, -1):
    countdown.append(n)

print(browsers_run)
print(retries)
print(retries_left)
print(countdown)
