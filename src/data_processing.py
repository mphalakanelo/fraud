import pandas as pd

# Load dataset
df = pd.read_csv("../data/creditcard.csv")

# Basic exploration
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("../data/cleaned_dataset.csv", index=False)

print("Dataset cleaned and saved.")
