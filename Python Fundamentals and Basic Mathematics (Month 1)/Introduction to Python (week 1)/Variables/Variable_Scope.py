""" Variables have different scopes - global (accessible everywhere) and local (accessible only within their function). """

global_variable = "I'm global"

def scope_function():
    local_variable = "I'm local"
    global global_variable  # To modify global variable
    global_variable = "Modified from function"
    print(f"Inside function - Local: {local_variable}")
    print(f"Inside function - Global: {global_variable}")

scope_function()
print(f"Outside function - Global: {global_variable}")
# print(local_variable)  # This would error, local_variable not defined