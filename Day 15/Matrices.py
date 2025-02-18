import numpy as np
# Define two matrices (2D arrays)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Addition
matrix_sum = A + B

# Matrix Multiplication (Dot Product)
matrix_product = np.dot(A, B)

# Matrix Transpose
A_transpose = A.T

# Determinant of Matrix A
det_A = np.linalg.det(A)

# Inverse of Matrix A (if invertible)
A_inv = np.linalg.inv(A)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Sum (A + B):\n", matrix_sum)
print("Matrix Product (A * B):\n", matrix_product)
print("Transpose of Matrix A:\n", A_transpose)
print("Determinant of Matrix A:", det_A)
print("Inverse of Matrix A:\n", A_inv)