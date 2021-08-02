#!/usr/bin/env bash

# see README for more details

qsub -I -n 1 -t 30 -A ATPESC2021 -q training

export OMP_NUM_THREADS=1

# testHODLR
mpiexec -n 1 ./build/testHODLR 5000
mpiexec -n 1 ./build/testHODLR 5000 --help
mpiexec -n 1 ./build/testHODLR 5000 --structured_rel_tol 1e-4 --structured_leaf_size 16
mpiexec -n 1 ./build/testHODLR 5000 --structured_rel_tol 1e-4 --structured_leaf_size 128
mpiexec -n 12 ./build/testHODLR 5000 --structured_rel_tol 1e-8 --structured_leaf_size 16
mpiexec -n 12 ./build/testHODLR 5000 --structured_rel_tol 1e-8 --structured_leaf_size 128

# testMMdouble and testMMdoubleMPIDist
mpiexec -n 1 ./build/testMMdouble pde900.mtx --sp_disable_gpu
#mpiexec -n 1 ./build/testMMdouble pde900.mtx --sp_enable_gpu
mpiexec -n 12 ./build/testMMdoubleMPIDist pde900.mtx --sp_disable_gpu

# testPoisson3d and testPoisson3dMPIDist
mpiexec -n 1 ./build/testPoisson3d 40 --help --sp_disable_gpu
mpiexec -n 1 ./build/testPoisson3d 40 --sp_compression BLR --sp_disable_gpu
mpiexec -n 1 ./build/testPoisson3d 40 --sp_compression BLR --blr_rel_tol 1e-2 --sp_disable_gpu
mpiexec -n 1 ./build/testPoisson3d 40 --sp_compression BLR --blr_rel_tol 1e-4 --sp_disable_gpu
mpiexec -n 1 ./build/testPoisson3d 40 --sp_compression BLR --blr_leaf_size 128 --sp_disable_gpu
mpiexec -n 1 ./build/testPoisson3d 40 --sp_compression BLR --blr_leaf_size 256 --sp_disable_gpu

mpiexec -n 12 ./build/testPoisson3dMPIDist 40 --sp_disable_gpu
mpiexec -n 12 ./build/testPoisson3dMPIDist 40 --sp_compression HSS \
   --sp_compression_min_sep_size 1000 --hss_rel_tol 1e-2 --sp_disable_gpu
mpiexec -n 12 ./build/testPoisson3dMPIDist 40 --sp_compression HODLR \
   --sp_compression_min_sep_size 1000 --hodlr_leaf_size 128 --sp_disable_gpu


