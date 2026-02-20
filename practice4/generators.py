#1
# Create a generator that generates the squares of numbers up to some number N.
"""
def square_gen(n):
    for i in range(n + 1):
        yield i ** 2 
a = int(input())
for square in square_gen(a):
    print(square)
"""
#2
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
"""
def even_gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
first = True
for num in even_gen(n):
    if first:
        print(num, end="")
        first = False
    else:
        print("," + str(num), end="")
print() 
"""
#3
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
"""
def even_num(n):
    for i in range(n):
        if i % 3 == 0 and i%4==0 :
            yield i

a = int(input())

first = True
for num in even_num(a+1):
    if first:
        print(num, end=" ")
        first = False
    else:
        print(str(num), end=" ")
print()  
"""
#4
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
"""
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a,b=map(int,input().split())
for val in squares(3, 7):
    print(val)
"""
#5
#Implement a generator that returns all numbers from (n) down to 0.
"""
def countdown(n):
    while(n>=0):
        yield n
        n-=1

a=int(input())
for i in countdown(a):
    print(i)
"""


