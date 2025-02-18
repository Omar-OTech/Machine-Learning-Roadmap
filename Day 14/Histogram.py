import matplotlib.pyplot as plt
import numpy as np

# plt.hist: Creates a histogram of the data with 30 bins. The edgecolor parameter enhances visual separation between bins.

# Generate random data following a normal distribution
data = np.random.randn(1000)

# Create a histogram with 30 bins
plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()