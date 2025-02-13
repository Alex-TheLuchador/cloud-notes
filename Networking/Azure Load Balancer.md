# Azure Load Balancer

Load balancing is when you evenly distribute load across a group of backend resources. 

Azure load balancer operates at layer 4 of the OSI model. As the point of contact for clients,
traffic arrives at the front end of the load balancer and is distributed to the backend based
on rules and metrics.

## Public load balancers
Public load balancers balance traffic from the internet to your VMs or other resources.
This is done by translating private IP addresses to public IPs. The IP address of
your load balancer determines if it's public or private.

## Private/Internal load balancers
Internal load balancers are used when private IP addresses are going to be hitting
the front end of the load balancer. This is so that traffic on your internal network can be evenly
distributed across the backend.

## Backend pool
The backend pool is the group of VMs or instances in VM scale sets that are receiving traffic
from the load balancer. Scaling instances up or down causes the load balancer to automatically
adjust itself without any additional input from you.

## Health probes
When you create a load balancer, you will setup a health probe for that load balancer. The health
probe will let you know what instances are health and unhealthy, which can determine if an instance
will receive traffic.

You can define the parameters for what is health/unhealthy for an instance. When a probe fails,
load balancers stop sending new connections to the unhealthy instances, although this doesn't
affect existing connections. Connections continue until the application ends the flow, times out,
or the VM shuts down. HTTPS probes will mark an instance as down if the server returns anything other
than HTTP 200 OK.

All Load Balancer health probes originate from 168.63.129.16

There are two SKUs for the Load Balancer:
1. Basic
    - TCP and HTTP probes
    - If all probes are down, all TCP flows expire
2. Standard
    - TCP, HTTP, and HTTPS probes
    - If all probes are down, all TCP flows continue


## Inbound and outbound rules
You can specify rules for inbound and outbound traffic flow for your load balancer. Port forwarding and load
balancing can be done for specific TCP and UDP protocols, but not all.

Various notes:
- Backend pools cannot consist of Private Endpoints.
- Outbound traffic from a backend VM cannot go to the frontend of an internal load balancer.
- Load balancers and their backend pools cannot span VNets.
- You cannot forward IP fragments.
- Only 1 public and 1 private load balancer are allowed per availability set.


Sources:
- https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview
- https://learn.microsoft.com/en-us/azure/load-balancer/components