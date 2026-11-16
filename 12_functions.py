"""
Lesson 12 — Functions

A function is a named block of code you can run whenever you call it.
Use one when the same steps would otherwise be copied, or when a
chunk of work deserves its own name.

Run:
    py -3 12_functions.py
"""

print("=" * 56)
print("1. Define, then call")
print("=" * 56)


def greet():
    print("Hello from a function")


greet()
greet()

print()
print("=" * 56)
print("2. Parameters — values the function receives")
print("=" * 56)


def greet_person(name):
    print(f"Hello, {name}")


greet_person("Amina")
greet_person("Sam")

print()
print("=" * 56)
print("3. return — send a value back to the caller")
print("=" * 56)


def add(a, b):
    return a + b


total = add(4, 6)
print("add(4, 6) =", total)
print("add(total, 1) =", add(total, 1))

print()
print("=" * 56)
print("4. A function with no return gives None")
print("=" * 56)


def say_hi():
    print("hi")


result = say_hi()
print("result of say_hi():", result)

print()
print("=" * 56)
print("5. Default parameter values")
print("=" * 56)


def power(base, exponent=2):
    return base ** exponent


print("power(5) =", power(5))
print("power(5, 3) =", power(5, 3))

print()
print("=" * 56)
print("6. Keyword arguments — name the parameter at the call")
print("=" * 56)


def describe(name, language):
    return f"{name} is learning {language}"


print(describe(language="Python", name="Lee"))

print()
print("=" * 56)
print("7. Return more than one value (it is a tuple)")
print("=" * 56)


def min_and_max(numbers):
    return min(numbers), max(numbers)


low, high = min_and_max([4, 9, 1, 7])
print("low =", low, " high =", high)

print()
print("=" * 56)
print("8. Functions can use conditions and loops")
print("=" * 56)


def count_passing(scores, passing=60):
    """Return how many scores are greater than or equal to passing."""
    count = 0
    for score in scores:
        if score >= passing:
            count += 1
    return count


print("passing scores:", count_passing([55, 70, 90, 40]))
print("passing at 80:", count_passing([55, 70, 90, 40], passing=80))

print()
print("=" * 56)
print("9. Names inside a function stay inside it")
print("=" * 56)

message = "outside"


def show_local():
    message = "inside"
    print("inside the function:", message)


show_local()
print("outside the function:", message)

print()
print("=" * 56)
print("10. Put the script's starting point in main")
print("=" * 56)


def main():
    print("Program started.")
    print("3 squared is", power(3))


if __name__ == "__main__":
    main()
