""" Python allows assigning values to multiple variables in a single line. """

# Multiple variables
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Value swapping
x, y = 10, 20
print(f"Before: x = {x}, y = {y}")
x, y = y, x  # Swap without temporary variable
print(f"After: x = {x}, y = {y}")

# Same value to multiple variables
value1 = value2 = value3 = "Same value"
print(f"value1: {value1}, value2: {value2}, value3: {value3}")