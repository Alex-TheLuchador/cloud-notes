# AAzure Virtual Machine Scale Sets

Virtual machine scale sets lets load balanced VMs automatically increase or decrease in quantity depending on demand or schedule.

Managed images allow for up to 600 VM instances, and standard marketplace or custom images allow up to 1000 VMs.

## Orchestration modes
Orchestration modes let you have greater control over how VM instances are managed by the scale set.
The orchestration mode is defined when you create the scale set and cannot be changed later.

### Uniform orchestration
VM scale sets with uniform orchestration are optimized for large-scale stateless workloads that
require identical instances. There is some customizability for individual instances, but mostly
uniform orchestration uses identical instances. Individual instances are not compatible with
Azure IaaS VM API commands, Azure management features such as Azure Resource Manager resource
tagging RBAC permissions, Azure Backup, or Azure Site Recovery. 

As long as you have under 100 instances,
Uniform orchestration provides fault domain high availability and is generally available while supporting
a full range of scale set management and orchestration like metrics-based autoscaling, instance protection,
and automatic OS upgrades.

### Flexible orchestration
Flexible orchestration allows a unified experience with your VMs, and it guarentees high availability for
up to 1000 VMs by spreading them across fault domains in a region or an AZ. 

Flexible orchestration uses standard Azure Virtual Machines instead of scale set child VMs. This means that
you have full control over the lifecycles, NICs and disks of all the VMs in the scale set, in addition to
being able to use all of the Azure VM APIs and commands you would normally use with a regular Azure VM.
This is not true for scale sets with Uniform orchestration, which uses the VM scale set APIs and commands.

Notes for Flexible orchestration:
- By default, Azure will automatically spread instances across fault domains evenly. With a flexible scale
set, you can override this and specify your preferred fault domain.
- VMs in a flexible scale set let you fully control their instance names. When adding a VM to a scale set
via autoscaling, you will provide a prefix and Azure supplies a unique numbered suffix to the name.