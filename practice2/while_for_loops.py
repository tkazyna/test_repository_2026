#1
"""
i = 1
while i < 6:
  print(i)
  i += 1
"""
#2
"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
"""
  #3
"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
"""
#4
"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")"""
#5
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)"""
#6
"""
for x in "banana":
  print(x)
"""
#7
#Exit the loop when x is "banana":
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
"""
#8
#Exit the loop when x is "banana", but this time the break comes before the print:
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
"""
#9
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)"""

#10
"""
for x in range(6):
  print(x)"""
#11
#Using the start parameter:
"""
for x in range(2, 6):
  print(x)"""
#12
#Increment the sequence with 3 (default is 1):
"""
for x in range(2, 30, 3):
  print(x)"""
#13
#Print all numbers from 0 to 5, and print a message when the loop has ended:
"""
for x in range(6):
  print(x)
else:
  print("Finally finished!")"""
#14
#Break the loop when x is 3, and see what happens with the else block:
"""
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")"""
#15
#Print each adjective for every fruit:
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)"""
#16
"""
for x in [0, 1, 2]:
  pass
"""
