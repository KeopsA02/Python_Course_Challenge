""" Each object has a unique identifier showing its memory location. """

var1 = "hello"
var2 = "hello"
var3 = "world"
print(f"var1 id: {id(var1)}")
print(f"var2 id: {id(var2)}")
print(f"var3 id: {id(var3)}")
print(f"var1 is var2: {var1 is var2}")  # Same object (string interning)
print(f"var1 is var3: {var1 is var3}")