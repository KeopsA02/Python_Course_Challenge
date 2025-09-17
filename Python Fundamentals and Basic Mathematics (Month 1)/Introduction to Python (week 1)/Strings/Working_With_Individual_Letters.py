""" Examining and working with each character separately. """

word = "hello"
for position, letter in enumerate(word):
    print(f"Position {position}: {letter} - ASCII: {ord(letter)}")

# Convert numbers back to letters
numbers = [72, 101, 108, 108, 111]
message = ''.join(chr(num) for num in numbers)
print(f"From numbers: {message}")  # "Hello"