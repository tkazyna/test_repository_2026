#3.1
"""
n=int(input())
a=True
while n>0:
    b=n%10
    if b%2!=0:
        a=False 
        break
    n//=10
if a:
    print("Valid")
else:
    print("Not valid")
"""
#3.2
"""
def isUsual(num: int)->bool:
    for p in (2, 3, 5):
        while num % p == 0:
            num //= p
    return num == 1
n=int(input())
if isUsual(n):
    print("Yes")
else:
    print("No")
"""
#3.3
"""
s=input()
toDigit={
    "ZER": '0',
    "ONE": '1',
    "TWO": '2',
    "THR": '3',
    "FOU": '4',
    "FIV": '5',
    "SIX": '6',
    "SEV": '7',
    "EIG": '8',
    "NIN": '9'
}

toStr = {v: k for k, v in toDigit.items()}

n=0
if s.find('+')!=-1:
    n=s.find('+')
    op = '+'
elif s.find('-')!=-1:
    n=s.find('-')
    op = '-'
else:
    n=s.find('*')
    op = '*'

left=s[:n]
right=s[n+1:]

num1=""
num2=""

for i in range(0,len(left),3):
    num1=num1+toDigit[left[i:i+3]]
for i in range(0,len(right),3):
    num2=num2+toDigit[right[i:i+3]]

if op == '+':
    res = int(num1) + int(num2)
elif op == '-':
    res = int(num1) - int(num2)
else:
    res = int(num1) * int(num2)

res_str = str(res)
result=""

for ch in res_str:
    result += toStr[ch]

print(result)
"""
#3.4
"""
s=input()
print(s.upper())
"""
#3.5
"""
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
n = int(input())
sq = Square(n)
print(sq.area())
"""
#3.6
"""
class Shape:
    def area(self):
        pass  # пустой метод

# наследуем Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # переопределяем метод area
    def area(self):
        return self.length * self.width

# ввод
a, b = map(int, input().split())

# создаём объект
rect = Rectangle(a, b)

# выводим результат
print(rect.area())
"""
#3.7
"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 +(self.y - other_point.y) ** 2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

p1 = Point(x1, y1)
p1.show()
p1.move(x2, y2)
p1.show()
p2 = Point(x3, y3)
distance = p1.dist(p2)
print(f"{distance:.2f}")
"""
#3.8
"""
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance
    
initial_balance, withdraw_amount = map(int, input().split())
account = Account("User", initial_balance)
result = account.withdraw(withdraw_amount)
print(result)
"""
#3.9
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (self.radius**2)*3.14159
n=int(input())
cir = Circle(n)
res=cir.area()
print(f"{res:.2f}")
"""
#3.10
"""
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)  
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

name, gpa = input().split()
gpa = float(gpa)

student = Student(name, gpa)
student.display()
"""
#3.11
"""
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)

a1, b1, a2, b2 = map(int, input().split())

p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

result = p1.add(p2)

print(f"Result: {result.a} {result.b}")
"""
#3.12
"""
data = input().split()

role = data[0]
name = data[1]
base_salary = int(data[2])

if role == "Manager":
    bonus_percent = int(data[3])
    total = base_salary * (1 + bonus_percent / 100)

elif role == "Developer":
    completed_projects = int(data[3])
    total = base_salary + completed_projects * 500

elif role == "Intern":
    total = base_salary

print(f"Name: {name}, Total: {total:.2f}")
"""
#3.13
"""
arr=list(map(int, input().split()))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
primes = list(filter(is_prime, arr))

if primes:
    print(*primes)
else:
    print("No primes")
"""
#3.14
"""
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    operation = input().split()
    
    if operation[0] == "add":
        x = int(operation[1])
        func = lambda a, x=x: a + x
        
    elif operation[0] == "multiply":
        x = int(operation[1])
        func = lambda a, x=x: a * x
        
    elif operation[0] == "power":
        x = int(operation[1])
        func = lambda a, x=x: a ** x
        
    elif operation[0] == "abs":
        func = lambda a: abs(a)
    
    arr = list(map(func, arr))

print(*arr)
"""


