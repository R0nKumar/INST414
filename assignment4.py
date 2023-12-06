import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("nba.csv")

# isolate relevant stats
attr = ['pts', 'reb', 'ast']
stats = df[attr]

# calculate inertia for each cluster range to find best fit
inertia = []
cluster_size = [1, 2, 3, 4, 5, 6, 7, 8]
for size in cluster_size:
    km = KMeans(n_clusters=size, init='k-means++', n_init=100)
    cluster_labels = km.fit_predict(stats)
    inertia.append(km.inertia_)

# plot distances to find best k-value (using elbow method)
plt.figure
plt.plot(cluster_size, inertia)
plt.title('Optimal k')
plt.xlabel('Num Clusters')
plt.ylabel('Inertia')  
plt.show()

# set k-value to the elbow point
k = 3

# perform kmeans clustering using optimal k-value
kmeans = KMeans(n_clusters=k, init='k-means++', n_init=100)

# group dataset by cluster
cluster_labels = kmeans.fit_predict(stats)
df['cluster'] = cluster_labels
df = df.groupby('cluster')
df = df['player_name']

# plot players per cluster
plt.figure()
df.apply(len).plot(kind='barh')
plt.title('Players Per Cluster')
plt.xlabel('Num Players')
plt.ylabel('Cluster')
plt.show()