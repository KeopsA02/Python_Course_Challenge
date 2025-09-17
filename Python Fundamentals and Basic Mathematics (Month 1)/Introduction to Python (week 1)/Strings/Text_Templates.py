""" Creating reusable text patterns with placeholders. """

from string import Template
greeting = Template('Hello $name, welcome to $city')
result = greeting.substitute(name='Maria', city='Madrid')
print(f"Template: {result}")  # "Hello Maria, welcome to Madrid"