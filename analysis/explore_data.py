import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
data_path = os.path.join('data', 'heart.csv')  # adjust path if needed
df = pd.read_csv(data_path)

# Show basic info
print("🔍 Data Overview:")
print(df.head())

print("\n📊 Summary Statistics:")
print(df.describe())

print("\n🧼 Missing Values:")
print(df.isnull().sum())

print("\n📌 Column Names:")
print(df.columns.tolist())

# Plot: Count of heart disease presence
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='target', palette='Set2')
plt.title('Heart Disease Count (1 = Disease, 0 = No Disease)')
plt.xlabel('Target')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Plot: Age distribution by target
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='age', hue='target', kde=True, palette='coolwarm', bins=30)
plt.title('Age Distribution by Heart Disease Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()