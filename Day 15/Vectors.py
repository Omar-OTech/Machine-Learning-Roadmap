import numpy as np

# Create a 1D array
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Vector Addition
vector_sum = v1 + v2

# Scalar Multiplication
scalar_mult = 3 * v1

# Dot Product of v1 and v2
dot_product = np.dot(v1, v2)

# Norm (Magnitude) of v1
norm_v1 = np.linalg.norm(v1)

print("Vector v1:", v1)
print("Vector v2:", v2)
print("Sum (v1 + v2):", vector_sum)
print("Scalar Multiplication (3*v1):", scalar_mult)
print("Dot Product of v1 and v2:", dot_product)
print("Norm (Magnitude) of v1:", norm_v1)