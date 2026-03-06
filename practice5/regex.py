import re
#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""
pattern = r'ab*' 
strings = ["a", "ab", "abb", "b", "ba"]
for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
"""
#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
"""
pattern = r'ab{2,3}'  
strings = ["ab", "abb", "abbb", "abbbb"]
for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
"""
#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
"""
pattern = r'[a-z]+_[a-z]+'
text = "my_var some_other testVar"
matches = re.findall(pattern, text)
print(matches)
"""
#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
"""
pattern = r'[A-Z][a-z]+'
text = "Hello World Python is Fun"
matches = re.findall(pattern, text)
print(matches)
"""
#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
"""
pattern = r'a.*b'  
strings = ["ab", "acb", "aXYZb", "abc", "b"]
for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
"""
#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""
text = "Hello, world. How are you?"
new_text = re.sub(r'[ ,.]', ':', text)
print(new_text)
"""
#7 Write a python program to convert snake case string to camel case string.
"""
text = "my_variable_name"
camel = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)
print(camel)
"""
#8 Write a Python program to split a string at uppercase letters.
"""
text = "HelloWorldPython"
parts = re.findall(r'[A-Z][a-z]*', text)
print(parts)
"""
#9 Write a Python program to insert spaces between words starting with capital letters.
"""
text = "HelloWorldPythonIsFun"
spaced = re.sub(r'([A-Z])', r' \1', text).strip()
print(spaced)
"""
#10 Write a Python program to convert a given camel case string to snake case.
"""
text = "myVariableName"
snake = re.sub(r'([A-Z])', r'_\1', text).lower()
print(snake)
"""


