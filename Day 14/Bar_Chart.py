# Scatter Plot: Demonstrates how to use random data to create a scatter plot with varying point sizes and colors. The alpha parameter adjusts transparency, and cmap defines the color map.
# Bar Chart: Simple bar chart illustrating categorical data with corresponding values.

import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 12]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()