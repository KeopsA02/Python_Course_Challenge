""" Searching for specific patterns in text (like phone numbers or emails). """

import re

text = "Call me at 123-456-7890 or 987-654-3210"
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Phones found: {phones}")  # ['123-456-7890', '987-654-3210']

# Simple email check
email = "test@example.com"
if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print("Valid email format")
else:
    print("Invalid email format")