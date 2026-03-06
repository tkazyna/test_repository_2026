#4.1
"""
def squares(num,n):
    for i in range(num,n):
        yield i * i

a=int(input())
for num in squares(1,a+1):
    print(num)
"""
#4.2
"""
def even_num(n):
    for i in range(n):
        if i % 2 == 0:
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
#4.3
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
#4.4
"""
def squares(num,n):
    for i in range(num,n):
        yield i * i

a,b=map(int,input().split())

for num in squares(a,b+1):
    print(num)
"""
#4.5
"""
def countdown(n):
    while(n>=0):
        yield n
        n-=1

a=int(input())
for i in countdown(a):
    print(i)
"""
#4.6
"""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

count = int(input())

if count > 0:
    first = True
    for num in fibonacci(count):
        if first:
            print(num, end="")
            first = False
        else:
            print("," + str(num), end="")
    print() 
"""
#4.7
"""
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration  
        self.index -= 1
        return self.data[self.index]

s = input()
for char in Reverse(s):
    print(char, end='')
"""
#4.8
"""
def primes(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

n = int(input())
for p in primes(n):
    print(p, end=' ')
"""
#4.9
"""
def Two(n):
    for num in range(n + 1):
        yield 2**num

n = int(input())
for p in Two(n):
    print(p, end=' ')
"""
#4.10
"""
def Cycle(n,lst):
    for i in range(n):
        for item in lst:
            yield item


arr=list(input().split())
n=int(input())
for p in Cycle(n,arr):
    print(p, end=' ')
"""
#4.11
"""
import json
def apply_patch(source, patch):
    for key in patch:
        if patch[key] is None:
            if key in source:
                del source[key]
        elif (key in source and
              isinstance(source[key], dict) and
              isinstance(patch[key], dict)):
            apply_patch(source[key], patch[key])
        else:
            source[key] = patch[key]
    return source

source = json.loads(input())
patch = json.loads(input())
result = apply_patch(source, patch)
print(json.dumps(result, sort_keys=True, separators=(',', ':')))
"""
#4.12






