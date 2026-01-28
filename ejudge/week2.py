#2.1
"""
year=int(input())
if year%4==0 and year%10!=0 or year%400==0:
    print("YES")
else:
    print("NO")
"""
#2.2
"""
num=int(input())
sum=0
for i in range(0,num+1):
    sum+=i
print(sum)"""
#2.3
"""
a=int(input())
arr=list(map(int, input().split()))
print(sum(arr))
"""
#2.4
"""
a=int(input())
arr=list(map(int, input().split()))
positive=0
for i in range(0,a):
    if arr[i]>0:
        positive+=1
print(positive)
"""
#2.5
"""
n=int(input())
power=1
b=False
while power <= n:
    if power==n:
        b=True
        break
    power*=2
if b:
    print("YES")
else:
    print("NO")
"""
#2.6
"""
a=int(input())
arr=list(map(int, input().split()))
print(max(arr))
"""
#2.7
"""
a=int(input())
arr=list(map(int, input().split()))
b=max(arr)
pos=0
for i in range (0,a):
    if b==arr[i]:
        pos=i+1
print(pos)
"""
#2.8
"""
a=int(input())
power=1
for i in range (0,a+1):
    if power<=a:
        print(power,end=' ')
    else:
        break
    power*=2
"""
#2.9
"""
a=int (input())
arr=list(map(int , input().split()))
min_num=min(arr)
max_num=max(arr)
for i in range(0,a):
    if arr[i]==max_num:
        arr[i]=min_num
for i in range(0,a):
    print(arr[i],end=' ')
"""
#2.10
"""
a=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr.reverse()
for i in range(0, a):
    print(arr[i],end=' ')
"""
#2.11
"""
n, l, r = map(int, input().split())
arr=list(map(int,input().split()))
arr1=arr[l-1:r]
arr[l-1:r]=[]
arr1=arr1[::-1]
arr[l-1:l-1]=arr1
for i in range ( 0, n):
    print(arr[i],end=' ')
"""
#2.12
"""
a=int(input())
arr=list(map(int,input().split()))
for i in range(0,a):
    print(arr[i]**2,end=' ')
"""
#2.13
"""
a=int(input())
b=False
if a>1:
    for i in range(2,a//2+1):
        if a%i==0:
            b=True
            break
    if b:
        print("No")
    else:
        print("Yes")
else:
    print("No")
"""
#2.15
"""
a=int (input())
surn={}
count=0
for i in range(0,a):
    x=input()
    if x in surn:
        surn[x] += 1
    else:
        surn[x] = 1
for sname,fr in surn.items():
    count+=1
print(count)
"""
#2.16
"""
a=int (input())
arr=list(map(int,input().split()))
nums=[]
for i in range(0,a):
    x=arr[i]
    if x in nums:
        print("NO")
    else:
        print("YES")
    nums.append(x)
"""
#2.17
"""
a=int (input())
surn={}
count=0
for i in range(0,a):
    x=input()
    if x in surn:
        surn[x] += 1
    else:
        surn[x] = 1
for sname,fr in surn.items():
    if fr%3==0:
        count+=1
print(count)
"""
#2.18
"""
a=int (input())
surn={}
for i in range(0,a):
    x=input()
    if x not in surn:
        surn[x] = i+1    
for key in sorted(surn.keys()):
    print(key, surn[key])
"""
#2.19
"""
n = int(input())
doramas = {}
for _ in range(n):
    s, k = input().split()
    k = int(k)
    
    if s in doramas:
        doramas[s] += k
    else:
        doramas[s] = k
for name in sorted(doramas.keys()):
    print(name, doramas[name])
"""
#2.20
"""
import sys
n = int(sys.stdin.readline())
document = {}
output_lines = []
for _ in range(n):
    line = sys.stdin.readline().split()
    cmd = line[0]
    if cmd == "set":
        document[line[1]] = line[2]
    else:  # get
        key = line[1]
        if key in document:
            output_lines.append(document[key])
        else:
            output_lines.append(f"KE: no key {key} found in the document")
print("\n".join(output_lines))
"""
#2.14
"""
n = int(input())
numbers = list(map(int, input().split()))
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
max_freq = max(freq.values())
res = float('inf') 
for num, count in freq.items():
    if count == max_freq and num < res:
        res = num
print(res)
"""

