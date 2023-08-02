# MathPackagesTraining
A gh-pages site to host SWC style training materials for various HPC math packages


# Website

The public site for this repo is https://xsdk-project.github.io/MathPackagesTraining2023/.
After pushing to the Repo, changes should be visible within minutes.

## To Render Locally

install Jekyll, see http://jekyllrb.com/

install Ruby dependencies:
```
bundle install
```

Clone or move to the MathPackagesTraining2023 directory and start the Jekyll server:

```
git clone https://github.com/xsdk-project/MathPackagesTraining2023.git
bundle exec jekyll serve
```

Then point your web broswer at http://localhost:4000/MathPackagesTraining2023/


# ThetaGPU

## Accounts

If you have an active ACLF account and are a member of atpesc_instructors, then
you can access ThetaGPU node now. **Anyone who will be participating as an
instructor and does not have an ALCF account or does not have access to the
atpesc_instructors project should request access to those ASAP**.

## Quick Start

To connect:

```
ssh theta.alcf.anl.gov
```
To work on ThetaGPU resources, login to a Theta login node, and then
hop on to one of the GPU service nodes:

```
ssh thetagpusn1  # or thetagpusn2
```

The OS/compilers on the `thetagpusn1` and `thetagpusn2` are different
then the compute nodes.
Therefore, you will likely want to immediately move to the GPU node
to build.

To request an interactive session:
```
qsub -I -q single-gpu -t 60 -n 1 -A ATPESC_Instructors --attrs filesystems=home,eagle
```

The admin recommends using a newer OpenMPI module:

```
module load openmpi/openmpi-4.1.4_ucx-1.12.1_gcc-9.4.0
```

For CMake:

```
module load cmake-3.20.3-gcc-9.3.0-57eqw4f
```

For blas, lapack the recommendation is to use blis, libflame (from aocl) - i.e:

```
module load aocl/blis/blis-3.2 aocl/libflame/libflame-3.2
gcc -lflame -lblis
```

## CUDA options

The A100 GPU has `CUDA Capability: 8.0`  i.e the corresponding compile options are:

```
nvcc -gencode arch=compute_80,code=sm_80
```

With cmake - the likely option is: `-DCMAKE_CUDA_ARCHITECTURES=80`

## Install software

Install software at `/eagle/projects/ATPESC2023/usr/MathPackages` - for ex: `/eagle/projects/ATPESC2023/usr/MathPackages/petsc-3.19.4`

And then copy over needed tutorial binaries, datafiles etc. over to `/eagle/projects/ATPESC2023/EXAMPLES/track-5-numerical` into appropriate folders - for ex: (from last year)

```
balay@thetagpu06:~$ ls -l /eagle/projects/ATPESC2023/EXAMPLES/track-5-numerical
total 40
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 amrex
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 hand_coded_heat
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 krylov_amg_hypre
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 krylov_amg_muelu
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 mfem-pumi-lesson
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:33 nonlinear_solvers_petsc
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:21 numerical_optimization_tao
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 rank_structured_strumpack
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 superlu
drwxrwsr-x 2 balay ATPESC_Instructors 4096 Aug  2 12:13 time_integrators_sundials
```

## Getting Started Guide

The "getting started" guide for ThetaGPU can be found at
https://www.alcf.anl.gov/support-center/theta-gpu-nodes/getting-started-thetagpu.



