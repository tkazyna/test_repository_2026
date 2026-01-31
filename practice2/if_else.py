#1
"""
a = 33
b = 200
if b > a:
  print("b is greater than a")
"""
#2
"""
number = 15
if number > 0:
  print("The number is positive")
"""
#3
"""
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
"""
#4
"""
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
"""
#5
"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
"""
#6
"""
score=76
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  """
#7
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
"""
#8
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
"""
#9
"""
username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
"""
#10
#One-line if/else that prints a value:
"""
a = 2
b = 330
print("A") if a > b else print("B")
"""
#11
#One line, three outcomes:
"""
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
"""
#12
"""
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
"""
#13
#Test if a is greater than b, AND if c is greater than a:
"""
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
"""
#14
"""
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  """
#15
"""
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  """
#16
"""
username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
  """
#17
#You can have if statements inside if statements. This is called nested if statements.
"""
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    """
#18
#Checking multiple conditions with nesting:
"""
age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
  """
#19
"""
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
  """
#20
"""
age = 16
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")
#21
score = 85
if score > 90:
  pass # This is excellent
print("Score processed")"""
#22
"""
score = 85
if score > 90:
  pass # This is excellent
print("Score processed")
"""
#23
"""
def calculate_discount(price):
  pass # TODO: Implement discount logic
# Function exists but doesn't do anything yet
"""

