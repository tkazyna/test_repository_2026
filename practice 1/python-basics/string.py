#Strings
#1
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
#2
a = "Hello"
print(a)
#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#5
#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
#6
for x in "banana":
  print(x) #Loop through the letters in the word "banana":
#7
#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
#8
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
#9
#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#10
#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
#11
#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Python - Slicing Strings
#1
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#2
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
#3
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
#4
#Get the characters:From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])


#Python - Modify Strings
#1
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#2
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#3
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#4
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#5
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#Python - String Concatenation
#1
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
#2
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#String Format
#1
#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#2
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)
#3
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#4
#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)


#Python - Escape Characters
#1
#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
