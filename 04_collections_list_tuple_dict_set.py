"""
Lesson 4 — list, tuple, dict, and set

list  : ordered, and you can change it
tuple : ordered, and it stays fixed
dict  : look up a value by a name
set   : each value is stored once
Run: py -3 04_collections_list_tuple_dict_set.py
"""
#By moahmed Farghali

steps = ["open login page", "type username", "click Login"]
steps.append("check welcome message")
first_step = steps[0]
step_count = len(steps)

# A tuple is unpacked into separate names. You read it; you do not replace its items.
screen_size = (1920, 1080)
width, height = screen_size

# A missing dict key can return a backup value through .get.
test_data = {
    "username": "amina",
    "password": "Secret123",
    "expected": "Welcome",
}
test_data["browser"] = "chrome"
role = test_data.get("role", "not set")

# The second "chrome" is dropped. A set does not promise an order.
browsers = {"chrome", "firefox", "chrome"}
browsers.add("edge")

print(steps, first_step, step_count)
print(width, height)
print(test_data["username"], test_data["browser"], role)
print(browsers)
