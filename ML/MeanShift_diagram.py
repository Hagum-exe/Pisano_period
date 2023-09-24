import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift

df = pd.read_pickle("pisano_line_df.pkl")
#print(df.head())
df.drop(["periods"], 1, inplace=True)

#print(df.head())
df = df.head(500)

X = df

clf = MeanShift()

clf.fit(X)

labels = clf.labels_
n_clusters = len(np.unique(labels))
#print(n_clusters)
df['cluster_group'] = np.nan

for i in range(len(X)):
    df['cluster_group'][i] = labels[i]
    
#print(df.head())

df.to_pickle("only_lines_MeanShift.pkl")

#print(n_clusters)
#print(df[(df['cluster_group']==50)])