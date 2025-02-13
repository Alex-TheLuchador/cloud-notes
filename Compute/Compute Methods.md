# Compute Methods - Bare Metal, Virtual Machines, and Containers

When comparing compute methods, it helps to first understand bare metal due to it being the starting point for computing.

## Bare Metal

A bare metal server is one that is a single machine, running a single tenant (i.e. one host OS). This was essentially the starting point for servers before virtualization and containerization.

Bare metal allows hardware and software to be tightly integrated, which can provide a significant performance boost and is especially useful for applications that require high performance.

Bare metal servers are isolated from each other due to them being single machines running single tenants. This provides a few key benefits:

1. Bare metal machines are not affected by the noisy neighbor problem.
    - The issues of one bare metal host do not have any effect on a bare metal host that is close to it. Issues like high resource usage for one machine do not cause problems for the neighboring machine.
2. Isolation also provides an extra layer of security.
    - In things like virtual machines, certain kinds of side-channel attacks can be used to steal information from neighboring VMs. This is not possible with bare metal machines because it is a separate physical entity.

Bare metal is an expensive solution. It is expensive to purchase, maintain, manage, upgrade, and scale the hardware.

## Virtual Machines

Virtualization is the emulation of physical computer hardware, often for the goal of running multiple operating systems on one host machine. This is achieved by placing a piece of software (called the hypervisor) on the OS, which allows us to create and manage virtual machines.

You can picture the stack like this:

1. Base layer: hardware
    - This is the phyiscal computer that runs everything.
2. Host OS
    - Your operating system of choice on which everything will run.
3. Hypervisor
    - This is the management software that you will use to create and maintain your virtual machines.
4. Virtual Machines
    - On top of the hypervisor, you run your VMs.
    - Each VM will have its own OS running its own applications.

Bare metal hypervisors exist to give complete hardware control over to the hypervisor, which provides a performance boost in your VMs. This means the hypervisor does not rely on a host operating system.

Virtual machines are cheaper to run and maintain when compared to bare metal, and they provide much easier methods of scaling vertically and horizontally.

The downsides of VMs include their susceptibility to the noisy neighbor issue, where one VM's resource usage can have adverse affects on their neighbor's performance. Side-channel attacks are also an issue for VMs.

## Containers

Containers are a bundled version of an application that contain all the dependencies necessary to run that application. You can then run multiple instances of that application on one host or one instance of an operating system, and each application instance is isolated from the others. 

On the host OS, you have a container engine, which is special software that allows resource provisioning and management of containers. This also virtualizes an operating system, rather than virtualizing hardware like a virtual machine.

Containers are highly scalable and portable, and they require fewer resources when compared to virtual machines. However, containers are potentially less secure because all instances of a container rely on one OS. Running containers within virtual machines can mitigate some of this risk by reducing the attack surfaces.