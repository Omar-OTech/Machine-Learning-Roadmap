import numpy as np

# Create an array from a list
arr = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr)

# Create an array with a range of values
range_arr = np.arange(0, 10, 2)  # start=0, stop=10, step=2
print("Range Array:", range_arr)

# Create an array with linearly spaced elements
linspace_arr = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
print("Linspace Array:", linspace_arr)