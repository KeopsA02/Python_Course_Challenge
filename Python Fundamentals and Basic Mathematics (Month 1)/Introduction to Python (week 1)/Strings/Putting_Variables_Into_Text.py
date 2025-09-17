""" Different ways to insert variables into your text (like personalizing a message with someone's name). """

name = "Anna"
age = 25

# Method 1: Old style (%)
print("Hello %s, you are %d years old" % (name, age))

# Method 2: .format()
print("Hello {}, you are {} years old".format(name, age))

# Method 3: f-strings (easiest!)
print(f"Hello {name}, you are {age} years old")
print(f"Math result: {5 + 3} = {5 + 3}")