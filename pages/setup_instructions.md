---
layout: page
show_meta: false
title: "Setup Instructions"
header:
   image_fullwidth: "atpesc-1024x2746.jpg"
permalink: "/setup_instructions/"
---

All handson activity will be on [ThetaGPU](https://www.alcf.anl.gov/support-center/theta-gpu-nodes). Here are instructions that are common
for all the lessons.

## Using ThetaGPU

1. Log into Theta, then ssh from there to one of the GPU service nodes
  * Use secure shell with trusted X11 forwarding enabled
```
ssh -l <username> -Y theta.alcf.anl.gov
ssh -Y thetagpusn1  # or thetagpusn2
```
1. Copy Installed Software
* Once you are logged into ThetaGPU, please execute the following instruction
to create a local, editable copy of numerical package software.
```
cd ~
rsync -a {{site.handson_install_root}}/{{site.handson_root}} .
```
  * **Note 1:** do not include a trailing slash, `/` in the path argument.
  * **Note 2:** You may be asked periodically throughout the day to re-execute
this command to update your local copy if we discover changes are necessary.
1. Schedue a ThetaGPU compute node for compiles and runs
```
qsub -I -q single-gpu -n 1 -t 60 -A ATPESC2023 --attrs filesystems=home,eagle
```
  * **Note 1:** `single-gpu` queue provides  a single GPU and 16 cores - for (max) 60 minutes, we would need to rerun qsub as needed.
  * **Note 2:** One *cannot* (compile or) run the binaries on the frontends theta, thetagpusn1 or thetagpusn2. Use the allocated node for such usage.
  * **Note 3:** ThetaGPU job scheduling policies [document](https://www.alcf.anl.gov/support-center/theta-gpu-nodes/gpu-node-queue-and-policy)
  * **Note 4:** To enable X windows for visualization on the compute node, you can open a new terminal and login to the allocated compute node by doing `ssh -Y thetagpuXY` (`thetagpuXY` is your compute node id)
1. Load the required MPI, blas, lapack modules
```
module load openmpi/openmpi-4.1.4_ucx-1.12.1_gcc-9.4.0 aocl/blis/blis-3.2 aocl/libflame/libflame-3.2
```
1. Confirm you can compile and run an example
```
$ cd track-5-numerical/hand_coded_heat
$ make mpi_test
mpicc mpi_test.c -o mpi_test
mpiexec -n 4 ./mpi_test
Size=4, Rank=0
Size=4, Rank=1
Size=4, Rank=2
Size=4, Rank=3
```

#### Miscellaneous ssh instructions

Usig ssh `control master` feature helps with repeated access to `theta`. For this, one can add (say on your laptop) the following to `~/.ssh/config`
```
Host theta.alcf.anl.gov
    Compression yes
    ForwardX11 yes
    ForwardX11Trusted yes
    ControlMaster auto
    ControlPersist 12h
    ControlPath ~/.ssh/%r@theta.alcf.anl.gov:%p
```
With this setup - the first time you login theta.alcf.anl.gov - you need to provide passwd. But subsequent ssh/scp/sftp will go through this control master - and not ask for passwd

Beyond that, you may also want to have a look at...

* [Setting Up & Using SSH Multiplexing / Control master](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Multiplexing)
* [Using SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
* [Mounting Filesystems Over SSHFS](https://wiki.archlinux.org/index.php/SSHFS)

