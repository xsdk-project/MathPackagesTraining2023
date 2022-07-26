# MathPackagesTraining
A gh-pages site to host SWC style training materials for various HPC math packages


# Website

The public site for this repo is https://xsdk-project.github.io/MathPackagesTraining2022/.
After pushing to the Repo, changes should be visible within minutes.

## To Render Locally

install Jekyll, see http://jekyllrb.com/

install Ruby dependencies:
```
bundle install
```

Clone or move to the MathPackagesTraining2022 directory and start the Jekyll server:

```
git clone https://github.com/xsdk-project/MathPackagesTraining2022.git
bundle exec jekyll serve
```

Then point your web broswer at http://localhost:4000/MathPackagesTraining2022/


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
qsub -I -q single-gpu -t 60 -n 1 -A ATPESC_Instructors
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
gcc -llibflame -lblis
```

## Install software

Install software at `/grand/ATPESC2022/usr/MathPackages` - for ex: `/grand/ATPESC2022/usr/MathPackages/petsc`

And then copy over needed tutorial binaries, datafiles etc. over to `/grand/ATPESC2022/EXAMPLES/track-5-numerical` into appropriate folders - for ex: (from last year)

```
balay@thetalogin5:~> ls /grand/ATPESC2021/EXAMPLES/track-5-numerical
amrex  hand_coded_heat  krylov_amg_hypre  krylov_amg_muelu  mfem-pumi-lesson  nonlinear_solvers_petsc  numerical_optimization_tao  rank_structured_strumpack  superlu  time_integrators_sundials
```

## Getting Started Guide

The "getting started" guide for ThetaGPU can be found at
https://www.alcf.anl.gov/support-center/theta-gpu-nodes/getting-started-thetagpu.



