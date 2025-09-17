""" Using isinstance() to check variable types. """

value = 42.5
print(f"Is {value} integer? {isinstance(value, int)}")
print(f"Is {value} float? {isinstance(value, float)}")
print(f"Is {value} numeric? {isinstance(value, (int, float))}")