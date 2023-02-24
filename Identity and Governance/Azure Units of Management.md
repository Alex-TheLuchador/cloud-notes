# Units of Management in Azure

Azure AD is the identity provider for our cloud environments. It can be thought of as the top-level identity and governance construct. Azure AD has a few different units of management, and each is capable of having policies, role-based access controls (RBAC), and budgets applied to them.

Applying a policy/RBAC/budget to a unit of management will apply to all the children of that group/unit of management. An idea mentioned by [John Savill](https://youtu.be/vq9LuCM4YP4) is useful for understanding how scope works when applying these controls:

- WHO (RBAC)
    - Who can access this unit of management?
- WHAT (Policy)
    - What can a user do in this unit of management?
- HOW MUCH (Budget)
    - How much can be spent on this unit of management?

## Management Groups

There is always a root management group in the Azure AD tenant, but you can also have a heirarchy of management groups that goes up to 6 levels deep (not including the root management group).

## Subscriptions

A subscription in Azure is simply a unit of management that is defined by a payment method. For example, a credit card belonging to a company's IT department could be one subscription, and a credit card belonging to the Accounting department would be another subscription.

Some resources are bound to a specific subscription, like virtual networks. A virtual machine in Subscription A cannot be in a VNet in Subscription B. Resources also have limits within their subscription, so you may need more subscriptions if you begin to hit the limit for some of your resources.

## Resource Groups

A resource group holds resources. Isn't that surprising...

Resources in resource groups are not restricted to communicating within their group; Resources can communicate outside their own resource group.

You should put resources in the same resource group if they share a common lifecycle. This is because you can apply updates or governance controls to the resource group that contains resources performing a specific function, which is where access is typically controlled.

When creating a resource group, you will need to assign the group to a region. This region does not have an effect on the region of the resources within the group, but it is used for the metadata of the resource group to be stored in a particular region. This is useful for organizations that must meet certain compliance standards.

Resources can belong to only one resource group, and resource groups cannot be nested within each other.