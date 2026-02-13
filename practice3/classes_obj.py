#1
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # instance variable
        self.model = model

name=input()
brands=input()
my_car = Car(name,brands)

print(f"My car is a {my_car.brand} {my_car.model}")
"""
#2
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Create object
s,s1=map(str, input().split())
car1 = Car(s,s1)
print("Car full name:", car1.full_name())
"""
#3
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s=input("Enter name: ")
n=int(input("enter age: "))
person = Person(s, n)
print("Before:", person.name, person.age)
person.age = n+1
print("After birthday:", person.name, person.age)

del person.age
# print(person.age)  # would cause AttributeError
print("Property 'age' deleted")
"""
#4
"""

class Book:
    library_name = "Central Library" 
    def __init__(self, title, author, pages, read=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = read

    def mark_read(self):
        self.read = True

    def update_pages(self, new_pages):
        self.pages = new_pages

    def display_info(self):
        info = f"'{self.title}'"
        info += f" by {self.author}" if hasattr(self, "author") else " by N/A"
        info += f" - {self.pages} pages"
        info += f" - {'Read' if self.read else 'Not read'}"
        info += f" - Library: {self.library_name}"
        print(info)
books = []  
n = int(input("How many books do you want to add? "))
for i in range(n):
    print(f"\nEnter details for book {i+1}:")
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))
    read = False

    book = Book(title, author, pages, read)
    books.append(book)

print("\nAll books in the library:")
for b in books:
    b.display_info()
"""
"""  
new_library = input("\nEnter new library name (or leave blank to skip): ")
if new_library:
    Book.library_name = new_library
    print("\nLibrary name updated for all books:")
    for b in books:
        b.display_info()
Enter details for book 1:
Title: 1984
Author: George Orwell
Pages: 328

Enter details for book 2:
Title: Python Basics
Author: John Doe
Pages: 250
   
"""
