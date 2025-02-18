# np.linspace: Generates 100 evenly spaced values between 0 and 2π.
# plt.plot: Plots the sine wave with custom styling (dashed line, blue color, 2-pixel width).
# plt.legend, plt.title, plt.xlabel, plt.ylabel: These functions add clarity to the plot by labeling the axes and adding a title and legend.
# plt.grid: Adds grid lines for better readability.

import matplotlib.pyplot as plt
import numpy as np

# Create a sequence of numbers for x-axis
x = np.linspace(0, 2 * np.pi, 100)
# Compute sine values for y-axis
y = np.sin(x)

# Create a figure and axis
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2, linestyle='--')
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()