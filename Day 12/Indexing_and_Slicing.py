import numpy as np

# Accessing and modifying elements
# 1D array indexing and slicing
matrix = np.array([[1, 2, 3], [4, 5, 6]])
a = np.array([10, 20, 30, 40, 50])
print("Element at index 2:", a[2])  # 30
print("Slice from index 1 to 4:", a[1:4])  # [20 30 40]

# 2D array indexing
print("Element at row 1, col 2:", matrix[1, 2])
print("Element at row 0, col 0:", matrix[0, 0])
print("Element at row 1, col 1:", matrix[1, 1])
print("Element at row 0, col 1:", matrix[0, 1])
print("First row:", matrix[0, :])
print("First row:", matrix[1, :])
print("First row:", matrix[1, 1:])
print("First column:", matrix[:, 0])
print("First column:", matrix[:, 1])