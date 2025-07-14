# AI-Driven Virtual Screening Workflow

This project implements a multi-step AI-based virtual screening pipeline targeting the β-catenin protein. The workflow integrates deep learning, enhanced sampling, Markov state modeling, and structure-based virtual screening to identify promising molecular candidates.

## Project Structure


## Pipeline Overview

### 0. PSICHI-Based Screening

In this step, the PSICHI algorithm is used to perform sequence-based virtual screening on a large compound library. The goal is to narrow down potential candidate molecules efficiently.

- **Directory**: `0.PSICHI_screen`

* `config.json`
Configuration file used during fine-tuning of the PSICHI model.

* `final-model/`
The directory containing the fine-tuned PSICHI model, trained specifically on β-catenin-related data.

* `PSICHI_screening-out.csv.gz`
The output file from virtual screening, containing ranked candidate molecules based on predictions from the fine-tuned model.

* `screening.py`
The Python script used to perform virtual screening using the fine-tuned model.


### 1. RiD Enhanced Sampling

Reinforced Dynamics (RiD), a reinforcement learning-based enhanced sampling method, is used to explore the conformational space of the β-catenin protein, providing diverse structural states for downstream analysis.

- **Directory**: `1.RiD`

* `data/`
Contains initial molecular structures and force field topology files required for running molecular dynamics simulations.

* `machine_slurm_local.json`
Specifies machine configuration and resource allocation for running RiD, including SLURM parameters for local or cluster execution.

* `psi-phi.cv`
Collective variables (CVs) used during RiD simulations. These were selected based on the ψ (psi) and φ (phi) backbone dihedral angles of β-catenin.

* `rid-env.sh`
Shell script for setting up the appropriate environment (e.g., conda environments, module loads) for RiD execution.

* `rid_gmx_dih.json`
Main configuration file for RiD, specifying simulation parameters, training schedules, and integration with GROMACS and CVs.

* `top.pdb`
PDB file of the β-catenin protein used as the input structure for the simulations.

* `run.sh`
Script to initiate the full RiD workflow, including simulation, training, and bias updates.


### 2. Markov State Modeling (MSM)

Markov State Models are constructed based on the sampled trajectories to capture the metastable states and transition kinetics of β-catenin. Visualizations and model data are included.

- **Directory**: `2.msm`

* `cluster.py`
Script for clustering trajectory frames into discrete states using dimensionality reduction and clustering algorithms.

* `cluster.pkl3`
Serialized clustering object that stores clustering model results, including centroids and parameters.

* `dtrajs.pkl3`
Discrete trajectories: assigns each conformation in the original trajectory to a cluster/state label.

* `lag1000/`
Contains MSM models built using a lag time of 1000 steps. This lag time was selected based on implied timescale analysis.

* `msm.pkl3`
Symlink to lag1000/msm.pkl3, the MSM model file used for downstream analysis.

* `msm.py`
Python script used to construct the Markov State Model from the discrete trajectories.

* `its.py`
Script used to generate implied timescale (ITS) plots to select an appropriate lag time.

* `its.png`
Visualization of implied timescales as a function of lag time, used to validate the Markovian behavior.

* `IC_ori.png`
Original input conformational distribution (e.g., before MSM clustering or tICA).

* `IC_msm.png`
Conformational distribution reweighted by MSM model, useful for state population comparison.


### 3. Structure-Based Virtual Screening

Two representative structures from MSM clustering are selected. Structure-based virtual screening (SBVS) is performed to further evaluate ligand binding potential.

- **Directory**: `3.vsw`

* `pocket1.pdb`
First representative protein structure used for docking/screening.

* `pocket1_vsw_out.csv`
Virtual screening results (e.g., ranked molecule list, scores) for pocket 1.

* `pocket2.pdb`
Second representative protein structure selected for SBVS.

* `pocket2_vsw_out.csv`
Virtual screening results for pocket 2.

## Notes

- This pipeline combines AI-driven selection with physics-based modeling for a comprehensive screening strategy.
- For usage details, dependencies, or reproduction instructions, please refer to individual subfolder scripts and configurations.

---

