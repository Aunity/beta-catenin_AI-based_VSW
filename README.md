# AI-Driven Virtual Screening Workflow

This project implements a multi-step AI-based virtual screening pipeline targeting the β-catenin protein. The workflow integrates deep learning, enhanced sampling, Markov state modeling, and structure-based virtual screening to identify promising molecular candidates.

## Project Structure


## Pipeline Overview

### 0. PSICHI-Based Screening

In this step, the PSICHI algorithm is used to perform sequence-based virtual screening on a large compound library. The goal is to narrow down potential candidate molecules efficiently.

- **Directory**: `0.PSICHI_screen`

### 1. RiD Enhanced Sampling

Reinforced Dynamics (RiD), a reinforcement learning-based enhanced sampling method, is used to explore the conformational space of the β-catenin protein, providing diverse structural states for downstream analysis.

- **Directory**: `1.RiD`

### 2. Markov State Modeling (MSM)

Markov State Models are constructed based on the sampled trajectories to capture the metastable states and transition kinetics of β-catenin. Visualizations and model data are included.

- **Directory**: `2.msm`

### 3. Structure-Based Virtual Screening

Two representative structures from MSM clustering are selected. Structure-based virtual screening (SBVS) is performed to further evaluate ligand binding potential.

- **Directory**: `3.vsw`

## Notes

- This pipeline combines AI-driven selection with physics-based modeling for a comprehensive screening strategy.
- For usage details, dependencies, or reproduction instructions, please refer to individual subfolder scripts and configurations.

---

