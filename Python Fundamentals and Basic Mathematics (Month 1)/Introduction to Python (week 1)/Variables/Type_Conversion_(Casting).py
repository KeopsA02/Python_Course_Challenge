""" Converting between different data types using constructor functions like int(), float(), str(). """

integer = 42
float_num = 3.14
string = "Hello Python"
boolean = True
null = None

number_str = "123"
number_int = int(number_str)
number_float = float(number_str)
print(f"String: '{number_str}' -> Integer: {number_int}")
print(f"String: '{number_str}' -> Float: {number_float}")

# Other conversions
integer_to_float = float(integer)
float_to_integer = int(float_num)
number_to_string = str(integer)
print(f"Integer to float: {integer} -> {integer_to_float}")
print(f"Float to integer: {float_num} -> {float_to_integer}")
print(f"Integer to string: {integer} -> '{number_to_string}'")