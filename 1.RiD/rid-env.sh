
source ~/.bashrc
# source
micromamba activate ridkit

export LIBRARY_PATH=${CONDA_PREFIX}/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=${CONDA_PREFIX}/lib:$LD_LIBRARY_PATH
export PLUMED_KERNEL=${CONDA_PREFIX}/lib/libplumedKernel.@SOEXT@

source ~/software/apps/gmx2022.5/bin/GMXRC.bash
