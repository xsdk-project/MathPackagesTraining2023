---
layout: page
show_meta: false
title: "Setup Instructions"
subheadline: "Instructions to complete prior to August 10th."
header:
   image_fullwidth: "atpesc-1024x2746.jpg"
permalink: "/setup_instructions/"
---

In the introductory talk on Tuesday, August 10th, we will provide additional details
about this web site and Zoom rooms and Slack channels for our parallel sessions.
Here, now, we provide instructions for setting up your Cooley login enviornment,
reserving one node for the day for hands-on lessons and setting up visualization
tools.

Instructions here are divided into _required_ and _optional_ steps.
We expect everyone to, minimally, complete all _required_ steps here.
The _optional_ steps are likely to improve your experience by simplifying
or improving performance of certain operations.

## Required Steps

Please complete the following _required_ steps prior to the beginning of the session
on Tuesday, August 10th.

1. Log Into Cooley
  * Use secure shell with compression, and trusted X forwarding enabled
```
ssh -l <username> -C -Y cooley.alcf.anl.gov
```
1. Copy Installed Software
* Once you are logged into Cooley, please execute the following instruction
to create a local, editable copy of numerical package software.
```
cd ~
rsync -a {{site.handson_install_root}}/{{site.handson_root}} .
```
  * **Note 1:** do not include a trailing slash, `/` in the path argument.
  * **Note 2:** You may be asked periodically throughout the day to re-execute
this command to update your local copy if we discover changes are necessary.
1. Setup to use appropriate MPI and GCC
  * The above software is built with gcc-8.2 and corresponding MPI. Please update your `~/.soft.cooley to have
```
+gcc-8.2.0
+cuda-10.2
PATH+=/grand/ATPESC2022/usr/MathPackages/openmpi-4.1.1-gcc82-cuda102/bin
+ffmpeg
@default
```
  * And run
```
resoft
```
  * Confirm correct mpiexec is in PATH
```
$ which mpiexec
/grand/ATPESC2022/usr/MathPackages/openmpi-4.1.1-gcc82-cuda102/bin/mpiexec
```

1. Confirm you can compile and run an example
```
$ qsub -I -n 1 -t 5 -A ATPESC2022 -q training
$ cd track-5-numerical/hand_coded_heat
$ make mpi_test
mpicc mpi_test.c -o mpi_test
mpiexec -n 4 ./mpi_test
Size=4, Rank=0
Size=4, Rank=1
Size=4, Rank=2
Size=4, Rank=3
$ exit
```
  * The `qsub` command reserves a cooley node for interactive work for 5 minutes.
    You may have to wait a moment for the interactive prompt on the reserved node to return.
  * The above commands produce the `mpi_test` binary and execution output.
1. As soon after 9:30am, Tuesday , August 10th as possible, allocate an interactive node on
   cooley. The following command allocates a single Cooley node (`-n 1`) for 300 minutes
   (`-t 300`) using the ATPESC2022 allocation (`-A ATPESC2022`) and the queue reservation (`-q training`):
```
qsub -I -n 1 -t 300 -A ATPESC2022 -q training
```
The command blocks until the node is ready.  Until the allocation expires (300 minutes in this example), all commands executed in the returned session will run on the allocated compute node; `mpiexec` can be used directly instead of going through `qsub`.
  * **Note 1:** Please **DO NOT** run MPI jobs on the login nodes. Instead, run them on an allocated compute node.
  * **Note 2:** Be aware, however, that any running job will be terminated when your allocation expires.
  * **Note 3:** Cooley job scheduling policies [document](https://www.alcf.anl.gov/support-center/cooley/job-scheduling-policies-cooley)
  * **Note 4:** To enable X windows for visualization on the compute node, you can open a new terminal and login to the allocated compute node by doing `ssh -Y cc0xx` (`cc0xx` is your compute node id)

## Visualization Tool Setup

By far, where visualization tools are concerned, the easiest thing to do is to install the
tools on your local laptop/desktop and then using them in *client/server* mode to connect
to and display data from Cooley.

### Local Installations

Results from various applications we use today may involve visualization with
[VisIt][visit], [ParaView][paraview] or other visualization tools. By far, the simplest and
most reliable way to setup any of these tools is to create a local installation on your laptop
and then transfer data files from cooley to visualize them locally. In track 4, you will
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

Beyond that, you may also want to have a look at...

* [Setting Up & Using SSH Multiplexing / Control master](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Multiplexing)
* [Using SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
* [Mounting Filesystems Over SSHFS](https://wiki.archlinux.org/index.php/SSHFS)

to simplify the process of manually moving data over many iterations of examples and tests. For ex: to easily login to cooley - one can do:

* add the following to ~/.ssh/config
```
Host cooley.alcf.anl.gov
    Compression yes
    ForwardX11 yes
    ForwardX11Trusted yes
    ControlMaster auto
    ControlPersist 12h
    ControlPath ~/.ssh/%r@cooley.alcf.anl.gov:%p
```
With this - the first time you login cooley.alcf.anl.gov - you need to provide passwd. But subsequent ssh/scp/sftp will go through this control master - and not ask for passwd

