"""
Lesson 12 — Functions

def creates a named block. The block runs when you call that name.
return sends a value back. A function with no return gives None.
Run: py -3 12_functions.py
"""
#By moahmed Farghali


def add(a, b):
    return a + b


def retry(case_name, times=1):
    # times uses 1 when the caller does not pass it.
    return f"{case_name} x{times}"


def count_passes(results):
    count = 0
    for result in results:
        if result == "pass":
            count += 1
    return count


def show_local_status():
    # This status exists only inside the function.
    status = "inside"
    return status


status = "outside"
total = add(4, 6)
one_try = retry("login")
three_tries = retry("login", times=3)
passes = count_passes(["pass", "fail", "pass"])
inside = show_local_status()


def main():
    print(total, one_try, three_tries, passes, inside, status)


if __name__ == "__main__":
    main()
