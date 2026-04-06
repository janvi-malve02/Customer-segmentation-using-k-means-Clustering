# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# 2. Load Dataset
df = pd.read_csv(
    r"C:\Users\Dell\Desktop\Customer segmentation Using k-means clustering\online_retail_II.csv",
    encoding="ISO-8859-1"
)

print("\nFirst rows\n", df.head())
print("\nInfo\n", df.info())

# Rename columns for easier use
df.rename(columns={"Customer ID": "CustomerID"}, inplace=True)

# Convert date column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 3. Data Cleaning
cleaned_df = df.copy()

# Keep only valid invoices
cleaned_df["Invoice"] = cleaned_df["Invoice"].astype(str)
mask = cleaned_df["Invoice"].str.match("^\d{6}$")
cleaned_df = cleaned_df[mask]

# Keep valid stock codes
cleaned_df["StockCode"] = cleaned_df["StockCode"].astype(str)
mask = (
    cleaned_df["StockCode"].str.match("^\d{5}$") |
    cleaned_df["StockCode"].str.match("^\d{5}[A-Za-z]+$") |
    cleaned_df["StockCode"].str.match("^PADS$")
)
cleaned_df = cleaned_df[mask]

# Remove missing customers
cleaned_df.dropna(subset=["CustomerID"], inplace=True)

# Remove free items
cleaned_df = cleaned_df[cleaned_df["Price"] > 0]

print("\nCleaned Data Shape:", cleaned_df.shape)

# 4. Feature Engineering
cleaned_df["SalesLineTotal"] = cleaned_df["Quantity"] * cleaned_df["Price"]

# RFM Features
aggregated_df = cleaned_df.groupby("CustomerID", as_index=False).agg(
    MonetaryValue=("SalesLineTotal", "sum"),
    Frequency=("Invoice", "nunique"),
    LastInvoiceDate=("InvoiceDate", "max")
)

max_invoice_date = aggregated_df["LastInvoiceDate"].max()
aggregated_df["Recency"] = (max_invoice_date - aggregated_df["LastInvoiceDate"]).dt.days

print("\nRFM Table\n", aggregated_df.head())

# 5. Outlier Detection
M_Q1 = aggregated_df["MonetaryValue"].quantile(0.25)
M_Q3 = aggregated_df["MonetaryValue"].quantile(0.75)
M_IQR = M_Q3 - M_Q1

F_Q1 = aggregated_df["Frequency"].quantile(0.25)
F_Q3 = aggregated_df["Frequency"].quantile(0.75)
F_IQR = F_Q3 - F_Q1

monetary_outliers = aggregated_df[
    aggregated_df["MonetaryValue"] > (M_Q3 + 1.5 * M_IQR)
]

frequency_outliers = aggregated_df[
    aggregated_df["Frequency"] > (F_Q3 + 1.5 * F_IQR)
]

non_outliers = aggregated_df[
    (~aggregated_df.index.isin(monetary_outliers.index)) &
    (~aggregated_df.index.isin(frequency_outliers.index))
]

print("\nNon-outlier customers:", len(non_outliers))

# 6. Feature Scaling
scaler = StandardScaler()

scaled_data = scaler.fit_transform(
    non_outliers[["MonetaryValue", "Frequency", "Recency"]]
)

# 7. Find Best K
max_k = 12
inertia = []
silhouette_scores = []

for k in range(2, max_k + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(scaled_data)

    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, labels))

# Plot Elbow + Silhouette
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(range(2,max_k+1), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")

plt.subplot(1,2,2)
plt.plot(range(2,max_k+1), silhouette_scores, marker="o", color="orange")
plt.title("Silhouette Score")
plt.xlabel("Number of Clusters")
plt.ylabel("Score")

plt.show()

# 8. KMeans Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_data)

non_outliers = non_outliers.copy()
non_outliers["Cluster"] = cluster_labels

print("\nClustered Data\n", non_outliers.head())

# 9. 3D Cluster Plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    non_outliers["MonetaryValue"],
    non_outliers["Frequency"],
    non_outliers["Recency"],
    c=non_outliers["Cluster"],
    cmap="Set1"
)

ax.set_xlabel("MonetaryValue")
ax.set_ylabel("Frequency")
ax.set_zlabel("Recency")

plt.title("Customer Segments (KMeans)")
plt.show()

# 10. Cluster Analysis
plt.figure(figsize=(12,6))

sns.boxplot(x="Cluster", y="MonetaryValue", data=non_outliers)
plt.title("MonetaryValue by Cluster")
plt.show()

sns.boxplot(x="Cluster", y="Frequency", data=non_outliers)
plt.title("Frequency by Cluster")
plt.show()

sns.boxplot(x="Cluster", y="Recency", data=non_outliers)
plt.title("Recency by Cluster")
plt.show()

# 11. Final Output
print("\nFinal clustered dataset\n")
print(non_outliers.head())