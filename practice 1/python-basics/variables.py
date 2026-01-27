#Creating Variables
#1
x = 5
y = "John"
print(x)
print(y)
#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#4
x = 5
y = "John"
print(type(x))
print(type(y))
#5
x = "John"
# is the same as
x = 'John'
#6
a = 4  #A will not overwrite a
A = "Sally"


#Legal variable names:
#1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Many Values to Multiple Variables:
#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2
x = y = z = "Orange"
print(x)
print(y)
print(z)
#3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Python - Output Variables
#1
x = "Python is awesome"
print(x)
#2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#4
x = 5
y = 10
print(x + y)
#5
x = 5
y = "John"
print(x, y)


#Global Variables
#1
x = "awesome"  #Create a variable outside of a function, and use it inside the function
def myfunc():
  print("Python is " + x)
myfunc()
#2
#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#3
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#4
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)