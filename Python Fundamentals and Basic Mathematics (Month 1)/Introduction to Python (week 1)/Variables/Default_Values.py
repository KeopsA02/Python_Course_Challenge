""" Functions can have parameters with default values. """

def function_with_default(param="default value"):
    return param

print(f"Without parameter: {function_with_default()}")
print(f"With parameter: {function_with_default('custom')}")