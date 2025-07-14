import pandas as pd
import pyemma
import numpy as np
dtrajs = pd.read_pickle('./dtrajs.pkl3')
lags = np.arange(0, 10001, 200)
lags[0] = 1
its = pyemma.msm.its(dtrajs, lags=lags, n_jobs=1)
pd.to_pickle(its, 'its.pkl3')
