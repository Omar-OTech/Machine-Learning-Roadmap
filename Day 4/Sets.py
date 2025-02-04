# Creating a set of integers (duplicates will be automatically removed)
unique_numbers = {1, 2, 3, 2, 4, 5, 3}
print("Unique Numbers Set:", unique_numbers)

# Adding an element
unique_numbers.add(6)
print("After Adding 6:", unique_numbers)

# Removing an element
unique_numbers.remove(3)
print("After Removing 3:", unique_numbers)

# Set operations: union, intersection, difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))  # Or use the pipe operator: set_a | set_b
print("Intersection:", set_a.intersection(set_b))  # Or use the ampersand operator: set_a & set_b
print("Difference:", set_a.difference(set_b))  # Or use the minus operator: set_a - set_b
print("Difference:", set_b.difference(set_a))  # Or use the minus operator: set_b - set_a