import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

# Load the dataset
df = pd.read_csv('PO_Processing.csv')

# 1. Display First Few Rows
print("1. First Few Rows:")
print(df.head())

# 2. Get Dataset Structure
print("\n2. Dataset Structure:")
print(df.info())

# 3. Summary Statistics
print("\n3. Summary Statistics:")
print(df.describe())

# 4. Average Processing Time
avg_time = df["Processing_Time"].mean()
print("\n4. Average Processing Time:", avg_time)

# 5. Median Processing Time
median_time = df["Processing_Time"].median()
print("\n5. Median Processing Time:", median_time)

# 6. Mode Processing Time
mode_time = df["Processing_Time"].mode().tolist()
print("\n6. Mode Processing Time:", mode_time)

# 7. Standard Deviation of Processing Time
std_time = df["Processing_Time"].std()
print("\n7. Standard Deviation:", std_time)

# 8. Variance of Processing Time
var_time = df["Processing_Time"].var()
print("\n8. Variance:", var_time)

# 9. Minimum Processing Time
min_time = df["Processing_Time"].min()
print("\n9. Minimum Processing Time:", min_time)

# 10. Maximum Processing Time
max_time = df["Processing_Time"].max()
print("\n10. Maximum Processing Time:", max_time)

# 11. Quantiles of Processing Time
quantiles = df["Processing_Time"].quantile([0.25, 0.5, 0.75])
print("\n11. Quantiles of Processing Time:")
print(quantiles)

# 12. Histogram of Processing Times
plt.figure(figsize=(8, 6))
plt.hist(df["Processing_Time"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Processing Times")
plt.xlabel("Processing Time (days)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 13. Boxplot of Processing Times
plt.figure(figsize=(8, 6))
plt.boxplot(df["Processing_Time"], vert=False)
plt.title("Boxplot of Processing Times")
plt.xlabel("Processing Time (days)")
plt.grid(True)
plt.show()

# 14. Detect Outliers in Processing Time
Q1 = df["Processing_Time"].quantile(0.25)
Q3 = df["Processing_Time"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Processing_Time"] < lower_bound) | (df["Processing_Time"] > upper_bound)][["PO_Number", "Processing_Time"]]
print("\n14. Outliers in Processing Time:")
print(outliers)

# 15. Count of Processing Times Above Mean
above_mean = len(df[df["Processing_Time"] > df["Processing_Time"].mean()])
print("\n15. Count of Processing Times Above Mean:", above_mean)

# 16. Count of Processing Times Below Mean
below_mean = len(df[df["Processing_Time"] < df["Processing_Time"].mean()])
print("\n16. Count of Processing Times Below Mean:", below_mean)

# 17. Hypothesis Testing: One-Sample t-test (Mean vs. 45 days)
t_stat, p_value = ttest_1samp(df["Processing_Time"], popmean=45)
print("\n17. One-Sample t-test (H0: Mean Processing Time = 45 days):")
print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")