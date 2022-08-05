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
qsub -I -q single-gpu -n 1 -t 60 -A ATPESC2022
```
  * **Note 1:** `single-gpu` queue provides  a single GPU and 16 cores - for (max) 60 minutes, we would need to rerun qsub as needed.
  * **Note 2:** One *cannot* (compile or) run the binaries on the frontends theta, thetagpusn1 or thetagpusn2. Use the allocated node for such usage.
  * **Note 3:** ThetaGPU job scheduling policies [document](https://www.alcf.anl.gov/support-center/theta-gpu-nodes/gpu-node-queue-and-policy)
  * **Note 4:** To enable X windows for visualization on the compute node, you can open a new terminal and login to the allocated compute node by doing `ssh -Y thetagpuXY` (`thetagpuXY` is your compute node id)
1. Load the required MPI, blas, lapack modules
```
$ module load openmpi/openmpi-4.1.4_ucx-1.12.1_gcc-9.4.0 aocl/blis/blis-3.2 aocl/libflame/libflame-3.2
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

## Visualization Tool Setup

By far, where visualization tools are concerned, the easiest thing to do is to install the
tools on your local laptop/desktop and then using them in *client/server* mode to connect
to and display data from Cooley.

### Local Installations

Results from various applications we use today may involve visualization with
[VisIt][visit], [ParaView][paraview] or other visualization tools. By far, the simplest and
most reliable way to setup any of these tools is to create a local installation on your laptop
and then transfer data files from Theta or Cooley (they mount the same filesystem) to visualize them locally. In track 4, you will
have alread learned how to do this. Nonetheless, for your convenience links to instructions for
installing these tools locally are provided here...
* For [VisIt][visit], go [here](https://wci.llnl.gov/simulation/computer-codes/visit/executables) to
  find a suitable bundled executable installation for your system and then download and install it.
* For [ParaView][paraview], go [here](https://www.paraview.org/download/)  to
  find a suitable bundled executable installation for your system and then download and install it.

Once you have installed these tools, you can run them in client/server mode to connect to cooley
and visualize here data there or you may manually transfer data between Cooley and your
desktop/laptop system. These two modes of use are described briefly in the remaining two sections.

#### Using Local Installations in Client-Server Mode
A benefit from installing these tools locally is that once you have them installed locally, you
can also configure them to run _client-server_ where you run an instance locally but use that
instance to log into a remote resource, such as cooley, and visualize data there without having
to manually transfer it locally. To setup these tools for client-server operation...
* Follow [these instructions](https://www.alcf.anl.gov/user-guides/visit-cooley) to setup and run [VisIt][visit] client-server to Cooley.
  * **Note:** VisIt versions 3.0, 3.1 and 3.2 are also installed even though the above instructions don't mention that.
* Follow [these instructions](https://www.alcf.anl.gov/user-guides/paraview-cooley) to setup and run [ParaView][paraview] client-server to Cooley.

#### Using Local Installations and Manually Moving Data

Manually logging in to move data files each time you need to
can become combersome. You can use a single `scp` command to copy many files using either
file [globbing](https://en.wikipedia.org/wiki/Glob_(programming)) or the `-r` recursive
command-line option to copy whole directory trees as for example...
```
scp "cooley:/tmp/imag00*.png" .
```
or
```
scp -r cooley:/foo/bar/tree .
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

