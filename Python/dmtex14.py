from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate synthetic data (you can replace this with your dataset)
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Apply k-means clustering with k=4 (number of clusters)
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Get cluster labels and cluster centers
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Visualize the clustered data
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', s=50, alpha=0.7, edgecolors='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, marker='*', label='Centroids')
plt.legend()
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
