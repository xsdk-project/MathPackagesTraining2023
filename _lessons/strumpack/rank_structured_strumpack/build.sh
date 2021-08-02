#!/usr/bin/env bash

#### system setup: add the following lines, without the leading '#' in
#### ~/.soft.cooley and log in again or run "resoft"
#+gcc-8.2.0
#+cuda-10.2
#PATH+=/grand/ATPESC2021/usr/MathPackages/openmpi-4.1.1-gcc82-cuda102/bin
#@visit
#@paraview
#@default


#### also execute the following to setup spack:
export SPACK_ROOT=/grand/ATPESC2021/usr/MathPackages/spack
. ${SPACK_ROOT}/share/spack/setup-env.sh

module load cmake-3.20.5-gcc-8.2.0-t4l7a67
module load strumpack-master-gcc-8.2.0-jjmbznc
module load butterflypack-1.2.1-gcc-8.2.0-7tinedv
module load metis-5.1.0-gcc-8.2.0-fuzkuyr 
module load parmetis-4.0.3-gcc-8.2.0-idkcsqt 
module load zfp-0.5.5-gcc-8.2.0-uny4psy 
module load netlib-lapack-3.9.1-gcc-8.2.0-wcocx5w 
module load netlib-scalapack-2.1.0-gcc-8.2.0-enyytzp


rm -rf build
mkdir build
cd build
cmake ../ -DCMAKE_BUILD_TYPE=Release
make -j4
