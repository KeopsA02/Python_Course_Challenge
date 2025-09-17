# =============================================
# STRING HANDLING IN PYTHON
# =============================================

# String creation
print("=== STRING CREATION ===")

string1 = 'String with single quotes'
string2 = "String with double quotes"
string3 = '''String with
triple single quotes
(multi-line)'''
string4 = """String with
triple double quotes
(multi-line)"""

print(string1)
print(string2)
print(string3)
print(string4)

# Basic string operations
print("\n=== BASIC OPERATIONS ===")
text = "Python"
print(f"Text: {text}")
print(f"Length: {len(text)}")
print(f"Concatenation: {text + ' is awesome'}")
print(f"Repetition: {text * 3}")

# Indexing and slicing
print("\n=== INDEXING AND SLICING ===")
string = "Programming"
print(f"String: {string}")
print(f"First character: {string[0]}")
print(f"Last character: {string[-1]}")
print(f"From index 2 to 5: {string[2:6]}")
print(f"From start to index 4: {string[:5]}")
print(f"From index 7 to end: {string[7:]}")
print(f"All characters: {string[:]}")
print(f"With step 2: {string[::2]}")
print(f"Reversed: {string[::-1]}")

# String methods
print("\n=== STRING METHODS ===")
text = "  hello WORLD of Python  "
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"strip(): '{text.strip()}'")
print(f"replace('Python', 'Java'): '{text.replace('Python', 'Java')}'")
print(f"split(): {text.split()}")
print(f"startswith('hello'): {text.strip().startswith('hello')}")
print(f"endswith('Python'): {text.strip().endswith('Python')}")
print(f"find('WORLD'): {text.find('WORLD')}")
print(f"count('o'): {text.count('o')}")

# String formatting
print("\n=== STRING FORMATTING ===")

# Formatting with % (old style)
name = "Anna"
age = 25
print("Hello %s, you are %d years old" % (name, age))

# Formatting with .format()
print("Hello {}, you are {} years old".format(name, age))
print("Hello {1}, you are {0} years old".format(age, name))
print("Hello {name}, you are {age} years old".format(name=name, age=age))

# f-strings (Python 3.6+)
print(f"Hello {name}, you are {age} years old")
print(f"Operation: {5 + 3} = {5 + 3}")
print(f"Name in uppercase: {name.upper()}")

# Escape characters
print("\n=== ESCAPE CHARACTERS ===")
print("Line break:\nLine 2")
print("Tab:\tTabbed text")
print("Quotes: \"Text in quotes\"")
print("Backslash: \\")
print('Single quote: \'text\'')

# Raw strings (no escape)
print("\n=== RAW STRINGS ===")
path = r"C:\Users\name\file.txt"
print(f"Raw path: {path}")
regex = r"\d+\s\w+"
print(f"Raw regex: {regex}")

# Verification methods
print("\n=== VERIFICATION METHODS ===")
string = "Python123"
print(f"'{string}'.isalpha(): {string.isalpha()}")
print(f"'{string}'.isdigit(): {string.isdigit()}")
print(f"'{string}'.isalnum(): {string.isalnum()}")
print(f"'{string}'.isupper(): {string.isupper()}")
print(f"'{string}'.islower(): {string.islower()}")
print(f"'{string}'.isspace(): {string.isspace()}")

# Joining and partitioning
print("\n=== JOINING AND PARTITIONING ===")
languages = ["Python", "Java", "C++"]
print(f"List: {languages}")
print(f"join: {', '.join(languages)}")

text = "one|two|three"
print(f"Split: {text.split('|')}")
print(f"Partition: {text.partition('|')}")

# Text alignment
print("\n=== TEXT ALIGNMENT ===")
text = "Python"
print(f"center(10): '{text.center(10)}'")
print(f"ljust(10): '{text.ljust(10)}'")
print(f"rjust(10): '{text.rjust(10)}'")
print(f"zfill(10): '{text.zfill(10)}'")

# Encoding and decoding
print("\n=== ENCODING ===")
text = "ñandú"
print(f"Text: {text}")
bytes_text = text.encode('utf-8')
print(f"Bytes (UTF-8): {bytes_text}")
decoded_text = bytes_text.decode('utf-8')
print(f"Decoded: {decoded_text}")

# Advanced methods
print("\n=== ADVANCED METHODS ===")
text = "python is great, python is powerful"
print(f"Original: {text}")
print(f"replace first: {text.replace('python', 'Python', 1)}")
print(f"rsplit: {text.rsplit(' ', 1)}")
print(f"splitlines: {'line1\nline2'.splitlines()}")

# Text templates
print("\n=== TEXT TEMPLATES ===")
from string import Template
template = Template('Hello $name, welcome to $place')
result = template.substitute(name='Carlos', place='Python')
print(f"Template: {result}")

# Advanced f-strings
print("\n=== ADVANCED F-STRINGS ===")
import math
value = 123.456789
print(f"Value: {value:.2f}")
print(f"Percentage: {0.4567:.1%}")
print(f"Hexadecimal: {255:#x}")
print(f"Binary: {10:b}")
print(f"PI: {math.pi:.3f}")

# Character manipulation
print("\n=== CHARACTER MANIPULATION ===")
text = "abcdef"
print(f"Text: {text}")
for i, char in enumerate(text):
    print(f"Character {i}: {char} - ASCII: {ord(char)}")

# Create string from ASCII codes
ascii_codes = [65, 66, 67]
string_from_ascii = ''.join(chr(code) for code in ascii_codes)
print(f"From ASCII: {string_from_ascii}")

# Basic regular expressions
print("\n=== BASIC REGULAR EXPRESSIONS ===")
import re
text = "The phone number is 123-456-7890 and another is 987-654-3210"
pattern = r'\d{3}-\d{3}-\d{4}'
numbers = re.findall(pattern, text)
print(f"Text: {text}")
print(f"Numbers found: {numbers}")

# Simple email validation
email = "user@example.com"
if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print(f"'{email}' looks like a valid email")
else:
    print(f"'{email}' is not a valid email")

# String interpolation with format specifiers
print("\n=== FORMAT SPECIFIERS ===")
price = 49.99
quantity = 3
total = price * quantity
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity:03d}")  # Zero-padded to 3 digits
print(f"Total: ${total:,.2f}")  # With thousands separator

# Multiline f-strings
print("\n=== MULTILINE F-STRINGS ===")
name = "Alice"
score = 95.5
message = f"""
Student Report:
==============
Name: {name}
Score: {score:.1f}%
Status: {'Pass' if score >= 60 else 'Fail'}
"""
print(message)