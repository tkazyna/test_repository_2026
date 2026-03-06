#5.1
"""
import re
text = input()
if re.match(r"Hello", text):
    print("Yes")
else:
    print("No")
"""
#5.2
"""
import re
main_string = input()
substring = input()
if re.search(substring, main_string):
    print("Yes")
else:
    print("No")
"""
#5.3
"""
import re
main_string = input()
pattern = input()
matches = re.findall(re.escape(pattern), main_string)
print(len(matches))
"""
#5.4
"""
import re
text = input()
digits = re.findall(r"\d", text)
print(" ".join(digits))
"""
#5.5
"""
import re
text = input()
if re.match(r"^[A-Za-z].*[0-9]$", text):
    print("Yes")
else:
    print("No")
"""
#5.6
"""
import re
text = input()
pattern = r"\S+@\S+\.\S+"
match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print("No email")
"""
#5.7
"""
import re
main_string = input()
pattern = input()
replacement = input()
result = re.sub(re.escape(pattern), replacement, main_string)
print(result)
"""
#5.8
"""
import re
text = input()
delimiter_pattern = input()
parts = re.split(delimiter_pattern, text)
print(",".join(parts))
"""
#5.9
"""
import re
text = input()
matches = re.findall(r'\b\w{3}\b', text)
print(len(matches))
"""
#5.10
"""
import re
text = input()
if re.search(r"cat|dog", text):
    print("Yes")
else:
    print("No")
"""
#5.11
"""
import re
text = input()
upper_l = re.findall(r'[A-Z]', text)
print(len(upper_l))
"""
#5.12
"""
import re
text = input()
digit_seq = re.findall(r'\d{2,}', text)
print(" ".join(digit_seq))
"""
#5.13
"""
import re
text = input()
words = re.findall(r'\w+', text)
print(len(words))
"""
#5.14
"""
import re
text = input()
pattern = re.compile(r'^\d+$')
if pattern.match(text):
    print("Match")
else:
    print("No match")
"""
#5.15
"""
import re
text = input()
def double_digit(match):
    digit = match.group()
    return digit * 2
result = re.sub(r'\d', double_digit, text)
print(result)
"""
#5.16
"""
import re
text = input()
pattern = r'Name: (.+), Age: (.+)'
match = re.search(pattern, text)
if match:
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")
"""
#5.17
"""
import re
text = input()
pattern = r'\d{2}/\d{2}/\d{4}'
dates = re.findall(pattern, text)
print(len(dates))
"""
#5.18
"""
import re
text = input()
pattern = input()
matches = re.findall(re.escape(pattern), text)
print(len(matches))
"""
#5.19
"""
import re
text = input()
pattern = re.compile(r'\b\w+\b')
words = pattern.findall(text)
print(len(words))
"""


