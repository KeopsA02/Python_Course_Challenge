""" Taking pieces of text apart or putting them together. """

# Joining list items into one string
languages = ["Python", "Java", "C++"]
combined = ', '.join(languages)
print(f"Combined: {combined}")  # "Python, Java, C++"

# Splitting one string into pieces
text = "apple,banana,cherry"
fruits = text.split(',')
print(f"Split: {fruits}")  # ['apple', 'banana', 'cherry']