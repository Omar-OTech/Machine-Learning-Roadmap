import pandas as pd

# Creating a DataFrame
# From a Dictionary and a CSV File:

# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Tom"],
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Saving the DataFrame to a CSV and reading it back
df.to_csv("employees.csv", index=False)
df_from_csv = pd.read_csv('employees.csv')
print("DataFrame read from CSV:\n", df_from_csv)

# Exploring and Analyzing Data
# Display the first few rows
print("Head of dataframe:\n", df.head())

# Display summary statistics
print("Summary Statistics:\n", df.describe())

# Information about DataFrame structure
print("DataFrame Info:")
df.info()

print('-' * 40)

# Data Selection and Filtering
# Accessing Columns, Rows, and Conditional Filtering:

# Selecting a single column
ages = df['Age']
print("Ages:\n", ages)

# Selecting multiple columns
subset = df[['Name', 'Salary']]
print("Subset of DataFrame:\n", subset)

# Filtering rows based on a condition
high_salary = df[df['Salary'] > 60000]
print("Employees with Salary > 60000:\n", high_salary)
