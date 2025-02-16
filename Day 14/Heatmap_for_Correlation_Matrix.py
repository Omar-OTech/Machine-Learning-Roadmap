# Compute the correlation matrix for the Iris dataset

# sns.heatmap: Visualizes the correlation matrix as a heatmap, with annot=True to display correlation coefficients within each cell.
# cmap: Chooses a color map (coolwarm) that visually distinguishes between positive and negative correlations.


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
# Compute the correlation matrix for the Iris dataset
corr_matrix = iris.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Iris Features")
plt.show()