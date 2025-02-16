import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# sns.pairplot: Creates a grid of plots (scatter plots for pairwise relationships and histograms on the diagonal) colored by species.
# hue: Differentiates the species with distinct colors.
# markers and palette: Customize markers and color themes.

# Load a sample dataset from Seaborn (Iris dataset)
iris = sns.load_dataset('iris')

# Create a pair plot to visualize relationships between features
sns.pairplot(iris, hue="species", markers=["o", "s", "D"], palette="Set2")
plt.suptitle("Pair Plot of the Iris Dataset", y=1.02)
plt.show()