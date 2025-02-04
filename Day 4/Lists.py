# Creating a list of integers
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing elements (indexing starts at 0)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing a list (getting a subset)
print("Slice (2nd to 4th elements):", numbers[1:4])

# Modifying a list (lists are mutable)
numbers.append(60)
print("After Appending 60:", numbers)

numbers.insert(1, 15) # Inserts 15 at index 1
print("After Inserting 15 at index 1:", numbers)

# Removing elements
numbers.remove(30) # Removes the first occurrence of 30
print("After Removing 30:", numbers)
del numbers[0] # Removes the first element
print("After Deleting the First Element:", numbers)
numbers.pop() # Removes the last element
print("After Popping the Last Element:", numbers)