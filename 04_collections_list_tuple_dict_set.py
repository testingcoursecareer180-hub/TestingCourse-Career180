"""
Lesson 4 — list, tuple, dict, and set

list  : ordered, and you can change it
tuple : ordered, and it stays fixed
dict  : look up a value by a name
set   : each value is stored once
Run: py -3 04_collections_list_tuple_dict_set.py
"""
#By moahmed Farghali

# List Format: name = [item1, item2, item3] (square brackets).
steps = ["open login page", "type username", "click Login"]
steps.append("check welcome message")
first_step = steps[0]
step_count = len(steps)

#Tuple : Form: name = (item1, item2) (round brackets). 
screen_size = (1920, 1080)
width, height = screen_size

#Dictionary : Form: name = {"key": value} (curly brackets, a colon between key and value).
test_data = {
    "username": "amina",
    "password": "Secret123",
    "expected": "Welcome",
}
test_data["browser"] = "chrome"
role = test_data.get("role", "not set")
print(test_data["username"], test_data["browser"], role)


#Set : Form: name = {item1, item2} (curly brackets).
browsers = {"chrome", "firefox", "chrome"}
browsers.add("edge")
print(browsers)