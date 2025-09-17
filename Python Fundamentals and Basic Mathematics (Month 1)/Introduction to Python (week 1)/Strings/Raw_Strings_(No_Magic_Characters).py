""" When you want Python to treat EVERY character literally (useful for file paths and patterns). """

# Normal string might cause problems:
# path = "C:\Users\name"  # \n becomes new line!

# Raw string treats everything literally:
path = r"C:\Users\name\file.txt"
print(f"File path: {path}")