# question2
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
df = pd.read_excel("OnlineRetail (1).xlsx")
df.head(5)
df = df.drop(columns=['StockCode', 'InvoiceNo',
             'InvoiceDate', 'Description', 'Country'], axis=1)
df = df.dropna()
cluster = AgglomerativeClustering(
    n_clusters=1, affinity='euclidean', linkage='ward')
cluster.fit_predict(df)
plt.figure(figsize=(8, 8))
plt.scatter(df['Quantity'], df['UnitPrice'], c=cluster.labels_)
plt.show()

#------------------------------------------------------------------------
# Question1
%matplotlib inline # comment it if you are not using jupyter notebook
df = pd.read_excel("OnlineRetail (1).xlsx")
df.head(5)
df = df.drop(columns=['StockCode', 'InvoiceNo',
             'InvoiceDate', 'Description', 'Country'], axis=1)
df = df.dropna()
kmeans = KMeans(n_clusters=4, max_iter=50)
labels = kmeans.fit(df)
plt.figure(figsize=(8, 8))
plt.scatter(df['Quantity'], df['UnitPrice'], c=kmeans.labels_)
plt.show()
