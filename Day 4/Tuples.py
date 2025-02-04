# Creating a tuple of strings
colors = ('red', 'green', 'blue')
print("Tuples of colors:", colors)

# Accessing tuple elements
print("First Element:", colors[0])
print("Last Element:", colors[-1])

# Tuples are immutable, so the following line would cause an error because tuples cannot be modified:
# colors[1] = "yellow"  # Uncommenting this line will raise a TypeError

# Tuple unpacking
(r, g, b) = colors
print("Unpacked Tuple:", r, g, b)