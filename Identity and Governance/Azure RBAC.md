# Azure Role-Based Access Control (RBAC)

Role-based access control (RBAC) in Azure is how we can manage an identity's access to resources. 

## Parts of RBAC

It may help to think of RBAC as having a few components to it that define how it operates.

- Identity
    - An identity in Azure is anything that can be authenticated.
    - Users, applications, or other servers can be identities.
- Scope
    - RBAC needs a scope at which to operate. This can be a management group, a resource group, or a subscription.
- Role
    - The 'R' in RBAC stands for 'Role', which is like a position that an identity can play in your Azure environment. 
    - This will define what an identity can or cannot do.

A role assignment is a term you may hear that refers to assigning an identity a role at a particular scope.

## Control and Data Actions

RBAC can operate at the 'control plane' which is essentially operation though the Azure Resource Manager (ARM). This is where you manage access to resources, create resources, or update resources. 

RBAC can now also operate at the 'data plane' as well. Things that involve the actual data of a resource are in the data plane. Reading a list of blobs in a container, deleting a message in a queue, and writing a storage blob in a container are examples of data plane actions.