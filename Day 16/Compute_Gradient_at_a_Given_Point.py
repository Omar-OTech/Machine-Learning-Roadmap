import numpy as np
import matplotlib.pyplot as plt

# ∇f(x,y)=(2x,2y)

# Define the multivariable function f(x, y) = x^2 + y^2
def f_multivariable(x, y):
    return x**2 + y**2

# Analytical gradients
def gradient_f(x, y):
    df_dx = 2 * x
    df_dy = 2 * y
    return np.array([df_dx, df_dy])

# Test at a specific point (x, y) = (3, 4)
x_val, y_val = 3, 4
grad = gradient_f(x_val, y_val)
print(f"Gradient of f(x, y) at ({x_val}, {y_val}):", grad)