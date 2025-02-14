import pandas as pd

# Create a Series from a list
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series:\n", s)
print("Series Index:", s.index)
print("Series Values:", s.values)
