""" Handling text in various languages and special characters. """

spanish_text = "ñandú café"
print(f"Spanish text: {spanish_text}")

# Convert to bytes for storage/transmission
bytes_data = spanish_text.encode('utf-8')
print(f"Bytes: {bytes_data}")

# Convert back to text
text_again = bytes_data.decode('utf-8')
print(f"Back to text: {text_again}")