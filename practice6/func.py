from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
res = list(map(lambda x: x * 2, nums))
print("map:", res)

# filter
res = list(filter(lambda x: x % 2 == 0, nums))
print("filter:", res)

# reduce
res = reduce(lambda x, y: x + y, nums)
print("reduce:", res)

# enumerate
for i, val in enumerate(nums):
    print(i, val)

# zip
names = ["A", "B", "C"]
scores = [90, 80, 70]

for n, s in zip(names, scores):
    print(n, s)

# type checking
x = "123"
print(type(x))
print(isinstance(x, str))

# conversion
num = int(x)
print(num, type(num))