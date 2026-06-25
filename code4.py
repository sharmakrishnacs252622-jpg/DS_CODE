# Create a tuple
bike = ("Royal Enfield Classic 350", 101)

# Try to modify an element in the tuple
try:
    bike[1] = 999  # Attempt to change the bike code
except TypeError as e:
    print("Tuple is immutable! Error:", e)
