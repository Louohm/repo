# AutoInsight Demo: Automated Analysis of CSV Data
import pandas as pd

# Load sample dataset
df = pd.read_csv('sample_data.csv')  # Replace with your dataset

# Basic summary
print("Dataset shape:", df.shape)
print("\nColumn types:")
print(df.dtypes)

# Identify numeric columns
numeric_cols = df.select_dtypes(include='number').columns

# Correlation analysis
corr_matrix = df[numeric_cols].corr()
print("\nCorrelation matrix:")
print(corr_matrix)

# Find strongest correlations (excluding self-correlation)
strong_corrs = [(i, j, corr_matrix.loc[i,j])
                for i in numeric_cols for j in numeric_cols
                if i != j and abs(corr_matrix.loc[i,j]) > 0.7]
if strong_corrs:
    print("\nStrong correlations (>0.7):")
    for i, j, val in strong_corrs:
        print(f"{i} and {j}: {val:.2f}")
else:
    print("\nNo strong correlations found.")

# Generate a quick textual insight
print("\nInsights:")
for col in numeric_cols:
    mean_val = df[col].mean()
    print(f"- The average of {col} is {mean_val:.2f}.")
