""" Python variables can change type during execution, as types are determined at runtime. """

variable = 100
print(f"Variable as integer: {variable}, type: {type(variable)}")
variable = "Now I'm a string"
print(f"Variable as string: {variable}, type: {type(variable)}")
variable = [1, 2, 3]
print(f"Variable as list: {variable}, type: {type(variable)}")