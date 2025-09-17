# =============================================
# INTRODUCTION TO PYTHON - BASIC CONCEPTS
# =============================================

# Hello World basic
print("Hello, World!")  # This is a comment

# Basic syntax - Indentation (very important in Python)
def example_function():
    # This 4-space indentation is mandatory
    print("Function executed")
    return True

# Types of comments
# This is a single-line comment

"""
This is a multi-line
comment using triple quotes
"""

'''
You can also use
single quotes for
multi-line comments
'''

# Basic operators
print("\n=== ARITHMETIC OPERATORS ===")
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison operators
print("\n=== COMPARISON OPERATORS ===")
print(f"Equality: {a} == {b} -> {a == b}")
print(f"Inequality: {a} != {b} -> {a != b}")
print(f"Greater than: {a} > {b} -> {a > b}")
print(f"Less than: {a} < {b} -> {a < b}")
print(f"Greater or equal: {a} >= {b} -> {a >= b}")
print(f"Less or equal: {a} <= {b} -> {a <= b}")

# Logical operators
print("\n=== LOGICAL OPERATORS ===")
x = True
y = False
print(f"AND: {x} and {y} -> {x and y}")
print(f"OR: {x} or {y} -> {x or y}")
print(f"NOT: not {x} -> {not x}")

# User input
print("\n=== USER INPUT ===")
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old.")

# Basic control structures
print("\n=== CONTROL STRUCTURES ===")

# If-elif-else
number = 15
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# For loop
print("\nFor loop:")
for i in range(5):  # range(5) generates 0,1,2,3,4
    print(f"Iteration {i}")

# While loop
print("\nWhile loop:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1  # counter = counter + 1

# Basic exception handling
print("\n=== EXCEPTION HANDLING ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Everything went well")
finally:
    print("This always executes")

# Basic data structures
print("\n=== BASIC DATA STRUCTURES ===")
# List
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")

# Tuple (immutable)
colors = ("red", "green", "blue")
print(f"Tuple: {colors}")

# Dictionary
person = {"name": "John", "age": 30}
print(f"Dictionary: {person}")

# Set (unique elements)
unique_numbers = {1, 2, 2, 3, 4}
print(f"Set: {unique_numbers}")