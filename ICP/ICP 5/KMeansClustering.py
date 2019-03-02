import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
import seaborn as sns

dataset = pd.read_csv('College.csv')

x_train = dataset.iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
df = x_train

#Preprocessing the data
scaler = preprocessing.StandardScaler()
scaler.fit(x_train)
X_scaled_array = scaler.transform(x_train)
X_scaled = pd.DataFrame(X_scaled_array, columns = x_train.columns)


from sklearn import metrics
wcss = []
##elbow method to know the number of clusters
for i in range(2,12):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x_train)
    wcss.append(kmeans.inertia_)
    score = silhouette_score(x_train, kmeans.labels_, metric='euclidean')
    print("For n_clusters = {}, silhouette score is {})".format(i, score))

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()


sns.FacetGrid(dataset, hue="Private").map(plt.scatter,"F.Undergrad","P.Undergrad")
plt.show()