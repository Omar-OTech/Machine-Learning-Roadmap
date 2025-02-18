import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)
colors = np.random.rand(50)  # Random colors for each point
sizes = 1000 * np.random.rand(50)  # Random sizes for each point

plt.figure(figsize=(8, 4))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title("Random Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()  # Show color scale
plt.grid(True)
plt.show()