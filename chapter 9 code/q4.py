# 4. Apply k-means clustering on a 2D dataset. Experiment with different values of K.
# Visualize clusters and centroids. Explain how K affects clustering.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Create a 2D dataset
X, _ = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.2,
    random_state=42
)

# Apply K-Means for different K values
for K in [2, 3, 4]:
    kmeans = KMeans(n_clusters=K, random_state=42)
    labels = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_

    # Plot clusters and centroids
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200)
    plt.title(f"K-Means Clustering (K = {K})")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()
