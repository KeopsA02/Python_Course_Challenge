""" Making your text look neat by aligning it or adding spaces. """

text = "Python"
print(f"Centered: '{text.center(10)}'")   # '  Python  '
print(f"Left: '{text.ljust(10)}'")        # 'Python    '
print(f"Right: '{text.rjust(10)}'")       # '    Python'
print(f"Zero-filled: '{text.zfill(10)}'") # '0000Python'