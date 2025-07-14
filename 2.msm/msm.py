import pyemma
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dtrajs = pd.read_pickle('./dtrajs.pkl3')
lag = 3000
msm = pyemma.msm.bayesian_markov_model(dtrajs, lag=lag)
pd.to_pickle(msm, 'msm.pkl3')


ics = pd.read_pickle('../../02.ticas/ics.pkl3')
txx = np.concatenate(ics)
msm = pd.read_pickle('msm.pkl3')

fig, ax = plt.subplots()
pyemma.plots.plot_free_energy(txx[:,0], txx[:,1], weights=np.concatenate(msm.trajectory_weights()), ax=ax)

ax.set_ylabel('IC 2')

fig.tight_layout()

fig.savefig('IC_msm.png', dpi=200)

fig, ax = plt.subplots()
pyemma.plots.plot_free_energy(txx[:,0], txx[:,1], ax=ax)

ax.set_xlabel('IC 1')
ax.set_ylabel('IC 2')

fig.tight_layout()

fig.savefig('IC_ori.png', dpi=200)
