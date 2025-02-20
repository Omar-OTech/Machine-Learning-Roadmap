import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2
def f(x):
    return x**2

# Analytical derivative of f(x) = x^2 is 2x
def analytical_derivative(x):
    return 2 * x

# Numerical derivative using finite differences
def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Test at a specific point, e.g., x = 3
x_point = 3
analytical_value = analytical_derivative(x_point)
numerical_value = numerical_derivative(f, x_point)

print(f"At x = {x_point}:")
print("Analytical derivative:", analytical_value)
print("Numerical derivative:", numerical_value)