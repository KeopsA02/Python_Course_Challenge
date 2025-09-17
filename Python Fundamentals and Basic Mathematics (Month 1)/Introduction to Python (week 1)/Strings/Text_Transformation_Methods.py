""" These are like magic buttons that change how your text looks - making it ALL CAPS, lowercase, or cleaning up spaces. """

text = "  hello WORLD of Python  "
print(f"Original: '{text}'")
print(f"UPPERCASE: '{text.upper()}'")
print(f"lowercase: '{text.lower()}'")
print(f"Title Case: '{text.title()}'")
print(f"Clean spaces: '{text.strip()}'")
print(f"Replace words: '{text.replace('Python', 'Java')}'")