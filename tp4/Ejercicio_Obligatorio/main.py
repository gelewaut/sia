import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Load the dataset
entry = pd.read_csv("../data/europe.csv").values
countries = entry[:, 0]
data = entry[:, 1:].astype(float)
data = stats.zscore(data, axis=0)

# Select numeric columns
numeric_columns = ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]

# Perform a descriptive analysis of the variables
plt.boxplot(data, labels=numeric_columns)
plt.xticks(rotation=45)
plt.title("Variable Analysis")
plt.show()

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Perform principal component analysis
pca = PCA()
pca.fit(data_scaled)

# Get the explained variances for each principal component
explained_var_ratio = pca.explained_variance_ratio_

# Explained variance plot
plt.bar(range(1, len(explained_var_ratio) + 1), explained_var_ratio)
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance")
plt.title("Explained Variance by Principal Component")
plt.show()

# Biplot of PC1 and PC2
pca_data = pca.transform(data_scaled)[:, :2]

# Print the values of PC1 and PC2 vectors
print("PC1 Vector:", pca.components_[0])
print("PC2 Vector:", pca.components_[1])

# Create a DataFrame with the principal components for plotting
pca_df = pd.DataFrame(data=pca_data, columns=["PC1", "PC2"])

plt.figure(figsize=(8, 6))
plt.scatter(pca_df["PC1"], pca_df["PC2"])
# Add labels to each point
# for i, row in pca_df.iterrows():
    # plt.text(row["PC1"], row["PC2"], countries[i])  # You can replace 'i' with the label you want to add
for i, variable in enumerate(numeric_columns):
    plt.arrow(0, 0, pca.components_[0, i], pca.components_[1, i], color='r', alpha=0.5)
    plt.text(pca.components_[0, i] * 1.5, pca.components_[1, i] * 1.5, variable, color='r')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Biplot of PC1 and PC2")
plt.grid()
plt.show()

# Create an index based on PC1
data = pca_data[:,0]
# Combine the two lists into a list of tuples using zip
combined_list = list(zip(countries, data))
sorted_combined_list = sorted(combined_list, key=lambda x: -x[1])

# Display the index of countries ordered by PC1
print("Index of Countries Ordered by PC1:")
for i in range(0,len(data)):
    print(sorted_combined_list[i])
