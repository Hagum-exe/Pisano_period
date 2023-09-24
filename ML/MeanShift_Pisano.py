import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift

df = pd.read_pickle("pisano_df.pkl")
print(df.head())
df.drop(["repetitions"], 1, inplace=True)

X = df

clf = MeanShift()

clf.fit(X)

labels = clf.labels_
n_clusters = len(np.unique(labels))
#print(n_clusters)
df['cluster_group'] = np.nan

for i in range(len(X)):
    df['cluster_group'].iloc[i] = labels[i]
    
print(df[(df['cluster_group']==0)])