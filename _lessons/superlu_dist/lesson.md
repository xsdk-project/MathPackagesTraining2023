---
layout: page-fullwidth
order: 0
title: "Lesson Template"
subheadline: "Outline of lesson"
teaser: "Set your teaser here..."
permalink: "lessons/lesson_template/"
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

Set to use one OpenMP thread:
```
export OMP_NUM_THREADS=1
```

### Run 1 (test 2D algorithm driver, with GPU)
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
