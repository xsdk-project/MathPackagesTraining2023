---
layout: page-fullwidth
order: 7
title: "Sparse, Direct Solvers with SuperLU"
subheadline: "Linear Solvers"
teaser: "Role and Use of Direct Solvers in Ill-Conditioned Problems"
permalink: "lessons/superlu_dist/"
use_math: true
lesson: true
header:
 image_fullwidth: "matrices.png"
---

## To begin this lesson

- Enter the lesson directory
```
cd {{site.handson_root}}/superlu_dist
```

There are two folders:
```
SRC/ : source code
EXAMPLE/ : example drivers

```

## The Example Source Code

README file explains various example drivers.

## Running the Example

The current directory contains relatively small sparse matrices: g4.rua, g20.rua, and big.rua.

Set the following directory that contains larger matrix files:
```
export matdir=/grand/ATPESC2022/usr/MathPackages/datafiles
```

### Run 1 (test 2D algorithm driver)
```
mpiexec -n 2 pddrive -r 1 -c 2 ${matdir}/torso3.mtx 2>&1 | tee out
```

#### Expected Behavior/Output

### Run 2 (test 3D algorithm driver))
```
mpiexec -n 2 pddrive3d -r 1 -c 1 -d 2  ${matdir}/torso3.mtx 2>&1 | tee out
```

#### Expected Behavior/Output

### Run 3

#### Expected Behavior/Output

### Further Reading

https://github.com/xiaoyeli/superlu_dist
