""" A mechanism to handle errors and exceptions gracefully using try-except blocks. """

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