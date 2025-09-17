""" Ways to ask Python questions about your text: "Is this all letters?", "Is this all numbers?", etc. """

text = "Python123"
print(f"All letters? {text.isalpha()}")    # False (has numbers too)
print(f"All numbers? {text.isdigit()}")    # False (has letters too)
print(f"Letters+numbers? {text.isalnum()}") # True
print(f"ALL CAPS? {text.isupper()}")       # False
print(f"all lowercase? {text.islower()}")  # False