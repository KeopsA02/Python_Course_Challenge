""" Making numbers look pretty in your text. """

price = 49.99
quantity = 3
total = price * quantity

print(f"Price: ${price:.2f}")           # $49.99
print(f"Quantity: {quantity:03d}")      # 003 (3 digits with zeros)
print(f"Total: ${total:,.2f}")          # $149.97 (with comma)