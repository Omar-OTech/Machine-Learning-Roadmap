import numpy as np
import matplotlib.pyplot as plt

# Gradient descent to minimize f(x) = x^2
def f(x):
    return x**2

# Analytical derivative of f(x) = x^2 is 2x
def analytical_derivative(x):
    return 2 * x

# Numerical derivative using finite differences
def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Parameters for gradient descent
learning_rate = 0.1
num_iterations = 500

# Initial guess for x
x_current = 10.0
history = [x_current]

for i in range(num_iterations):
    # Compute the gradient (derivative) at the current x
    grad = 2 * x_current
    # Update the value of x
    x_current = x_current - learning_rate * grad
    history.append(x_current)
    print(f"Iteration {i+1}: x = {x_current:.4f}, f(x) = {f(x_current):.4f}")

# Plot the progress of x over iterations
plt.figure(figsize=(8, 4))
plt.plot(history, marker='o')
plt.title("Gradient Descent on f(x) = x^2")
plt.xlabel("Iteration")
plt.ylabel("x value")
plt.grid(True)
plt.show()