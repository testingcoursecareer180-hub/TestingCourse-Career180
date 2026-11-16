"""
Lesson 3 — Strings

Text from a page is a string. Methods return a new string.
Run: py -3 03_strings.py
"""
#By moahmed Farghali

page_title = "Login"
message = "It's the wrong password"
full_name = "Amina" + " " + "Hassan"

user = "Sam"
attempts = 2
report_line = f"{user} failed the login {attempts} time(s)"

# Counting starts at 0. The end index is not included.
word = "Python"
first_letter = word[0]
last_letter = word[-1]
first_three = word[0:3]

# strip removes end spaces. lower makes comparison easier. The original stays unchanged.
raw_title = "  Welcome Back  "
clean_title = raw_title.strip().lower()
status = "fail"
status_upper = status.upper()

banner = "Error: password is required"
has_password = "password" in banner
parts = "amina,pass,login".split(",")

print(full_name)
print(report_line)
print(first_letter, last_letter, first_three, len(word))
print(clean_title, status, status_upper)
print(has_password, parts)
