import pandas as pd
import pyemma
ics = pd.read_pickle('../../02.ticas/ics.pkl3')
data = []
for ic in ics:
    data.append(ic[:,:2])
cluster = pyemma.coordinates.cluster_kmeans(data=data, k=200, n_jobs=20)
pd.to_pickle(cluster, 'cluster.pkl3')
pd.to_pickle(cluster.dtrajs, 'dtrajs.pkl3')
