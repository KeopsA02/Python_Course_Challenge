""" You can pick out individual letters or parts of text using their position (like finding the 3rd letter in a word). """

word = "Programming"
print(f"First letter: {word[0]}")      # P (position 0)
print(f"Last letter: {word[-1]}")      # g (last position)
print(f"Letters 2-5: {word[2:6]}")     # "ogra" (positions 2 to 5)
print(f"Every other letter: {word[::2]}") # "Pormig" (step by 2)
print(f"Backwards: {word[::-1]}")      # "gnimmargorP" (reversed)