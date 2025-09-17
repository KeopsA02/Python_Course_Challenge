""" Rules and conventions for naming variables in Python. """

valid_variable = "OK"
_private_variable = "OK"  # By convention, private
VariableInCamelCase = "OK"  # Convention for classes
variable_in_snake_case = "OK"  # Convention for variables/functions

# Invalid names (would cause errors):
# 2variable = "Error"  # Cannot start with number
# variable-with-dash = "Error"  # Cannot have dashes
# class = "Error"  # Cannot be reserved word

import keyword
print(f"Reserved words: {keyword.kwlist}")