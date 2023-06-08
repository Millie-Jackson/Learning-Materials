import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)


# Data Exploration
df.info()
df.describe()

# Number of columns and rows
df.shape()

# Drop NULL Values
null_count = df.isnull().sum()
df.droppna(inplace=True)

# Fill na with something else
df.fillan(df.mean, inplace=True)

# Find all unique values
df("sepal length (cm)").unique()
value_counts = df("sepal length (cm)").value_counts()
count = value_counts[5.0]

# Filtering
mask = df["sepal length (cm)"] > 5
filtered_df = df[mask]