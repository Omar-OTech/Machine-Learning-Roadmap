import numpy as np

# Performing element-wise operations without loops

# Vectorized arithmetic
b = np.array([1, 2, 3, 4, 5])
c = np.array([10, 20, 30, 40, 50])

sum_arr = b + c   # Element-wise addition
prod_arr = b * c  # Element-wise multiplication

print("Element-wise Sum:", sum_arr)
print("Element-wise Product:", prod_arr)

# Broadcasting: adding a scalar to an array
print("Add scalar 5 to array b:", b + 5)

# Common NumPy Functions
# Aggregations and Linear Algebra:
# Sum, Mean, and Standard Deviation
print('Sum of b', np.sum(b))
print('Mean of b:', np.mean(b))
print('Max of b:', np.max(b))
print('Median of b:', np.median(b))
print('Standard Deviation of b:', np.std(b))

# Dot product of two arrays
dot_product = np.dot(b, c)
print("Dot Product:", dot_product)

# Transpose of a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Matrix:\n", matrix)
print('-' * 40)
print("Transposed Matrix:\n", matrix.T)