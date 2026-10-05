import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# ============================================
# OPTION 1: LOAD FROM CSV FILE
# ============================================
# Save the data as 'house_data.csv' first, then load it
# df = pd.read_csv('house_data.csv')

# ============================================
# OPTION 2: MANUALLY CREATE THE DATASET (No CSV file needed)
# ============================================
data = {
    'Size': [5400, 4500, 3400, 1200, 3300, 9000,7600, 4546, 2245, 7542, 2300, 4224],
    'SqFt': [5400, 4500, 3400, 1200, 3300, 9000,7600, 4546, 2245, 7542, 2300, 4224],
    'Bedrooms': [3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7],
    'Bathrooms': [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],
    'Age': [5, 10, 8, 3, 1, 2, 6, 4, 7, 9, 12, 15],
    'Price': [250000, 280000, 320000, 350000, 400000, 450000, 
              480000, 520000, 560000, 600000, 620000, 650000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=" * 60)
print("HOUSE PRICE DATA - FIRST 5 ROWS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("DATA SUMMARY STATISTICS")
print("=" * 60)

# Compute mean and standard deviation for each numeric column
numeric_cols = ['Size', 'SqFt', 'Bedrooms', 'Bathrooms', 'Age', 'Price']

print("\n{:<12} {:<12} {:<12} {:<12}".format('Feature', 'Mean', 'Std Dev', 'Count'))
print("-" * 50)

for col in numeric_cols:
    mean_val = np.mean(df[col])
    sd_val = np.std(df[col])
    count = len(df[col])
    print("{:<12} {:<12.2f} {:<12.2f} {:<12}".format(col, mean_val, sd_val, count))

# ============================================
# VISUALIZE DISTRIBUTIONS
# ============================================
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    axes[i].hist(df[col], bins=10, color='#3b82f6', alpha=0.7, edgecolor='black')
    mean_val = np.mean(df[col])
    sd_val = np.std(df[col])
    axes[i].axvline(mean_val, color='red', linestyle='dashed', linewidth=2, 
                    label=f'mean = {mean_val:.1f}')
    axes[i].axvline(mean_val + sd_val, color='orange', linestyle='dotted', linewidth=1.5, 
                    alpha=0.7, label=f'+1σ = {mean_val+sd_val:.1f}')
    axes[i].axvline(mean_val - sd_val, color='orange', linestyle='dotted', linewidth=1.5, 
                    alpha=0.7, label=f'-1σ = {mean_val-sd_val:.1f}')
    axes[i].set_title(f'{col}\nmean = {mean_val:.2f}, SD = {sd_val:.2f}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frequency')
    axes[i].legend(fontsize=8)
    axes[i].grid(alpha=0.2)

plt.suptitle('House Dataset - Feature Distributions', fontsize=14)
plt.tight_layout()
plt.show()

# ============================================
# CORRELATION HEATMAP
# ============================================
plt.figure(figsize=(8, 6))
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=0.5)
plt.title('Correlation Between Features\n(Strong positive correlation between SqFt and Price)')
plt.tight_layout()
plt.show()

# ============================================
# STANDARDIZATION (Z-SCORE)
# ============================================
print("\n" + "=" * 60)
print("STANDARDIZATION (Z-SCORE) EXAMPLE")
print("=" * 60)

# Standardize SqFt and Price
sqft_mean = np.mean(df['SqFt'])
sqft_sd = np.std(df['SqFt'])
price_mean = np.mean(df['Price'])
price_sd = np.std(df['Price'])

df['SqFt_standardized'] = (df['SqFt'] - sqft_mean) / sqft_sd
df['Price_standardized'] = (df['Price'] - price_mean) / price_sd

print("\nAfter standardization:")
print(f"SqFt  → mean = {np.mean(df['SqFt_standardized']):.2f}, SD = {np.std(df['SqFt_standardized']):.2f}")
print(f"Price → mean = {np.mean(df['Price_standardized']):.2f}, SD = {np.std(df['Price_standardized']):.2f}")

# Show the standardized values
print("\nFirst 5 rows with standardized values:")
print(df[['SqFt', 'Price', 'SqFt_standardized', 'Price_standardized']].head())

# ============================================
# OUTLIER DETECTION
# ============================================
print("\n" + "=" * 60)
print("OUTLIER DETECTION (Using Z-Score)")
print("=" * 60)

# Find houses with Price > 2 standard deviations from mean
price_z_scores = (df['Price'] - price_mean) / price_sd
outliers = df[abs(price_z_scores) > 2]

if len(outliers) > 0:
    print(f"Found {len(outliers)} potential outlier(s):")
    print(outliers[['Size', 'SqFt', 'Price']])
else:
    print("No outliers detected in Price (all within ±2σ)")

# ============================================
# 68-95-99.7 RULE (Bell Curve)
# ============================================
print("\n" + "=" * 60)
print("68-95-99.7 RULE (Empirical Rule)")
print("=" * 60)

# Check what percentage of SqFt falls within 1, 2, and 3 SDs
sqft_z = (df['SqFt'] - sqft_mean) / sqft_sd

within_1 = np.sum(abs(sqft_z) <= 1) / len(df) * 100
within_2 = np.sum(abs(sqft_z) <= 2) / len(df) * 100
within_3 = np.sum(abs(sqft_z) <= 3) / len(df) * 100

print(f"SqFt within ±1σ: {within_1:.1f}% (Expected: 68%)")
print(f"SqFt within ±2σ: {within_2:.1f}% (Expected: 95%)")
print(f"SqFt within ±3σ: {within_3:.1f}% (Expected: 99.7%)")

# Plot the bell curve
x = np.linspace(-4, 4, 500)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 5))
plt.plot(x, y, color='black', linewidth=2.5, label='Standard Normal Distribution')

colors = ['#b3d9ff', '#a3e4a3', '#f7b3b3']
labels = ['68% within ±1σ', '95% within ±2σ', '99.7% within ±3σ']
for k, color in zip([1, 2, 3], colors):
    x_fill = np.linspace(-k, k, 300)
    y_fill = norm.pdf(x_fill, 0, 1)
    plt.fill_between(x_fill, y_fill, color=color, alpha=0.5, label=labels[k-1])

plt.xticks([-3, -2, -1, 0, 1, 2, 3], ['-3σ', '-2σ', '-1σ', 'μ', '+1σ', '+2σ', '+3σ'])
plt.title('The 68-95-99.7 Rule (Empirical Rule)')
plt.xlabel('Standard deviations from the mean')
plt.ylabel('Probability density')
plt.legend()
plt.grid(alpha=0.15)
plt.show()

print("\n✅ Key Takeaways:")
print("1. Mean gives us the 'center' of each feature (e.g., average house price).")
print("2. Standard deviation tells us how spread out the values are.")
print("3. Standardization transforms features to have mean=0, SD=1.")
print("4. This is essential for ML algorithms like SVM, PCA, and neural networks!")