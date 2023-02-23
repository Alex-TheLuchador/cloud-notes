# Units of Management in Azure

Azure AD is the identity provider for our cloud environments. It can be thought of as the top-level identity and governance construct. Azure AD has a few different units of management, and each is capable of having policies, role-based access controls (RBAC), and budgets applied to them.

Applying a policy/RBAC/budget to a unit of management will apply to all the children of that group/unit of management.

## Management Groups

There is always a root management group in the Azure AD tenant, but you can also have a heirarchy of management groups that goes up to 6 levels deep (not including the root management group).

## Subscriptions

A subscription in Azure is simply a unit of management that is defined by a payment method. For example, a credit card belonging to a company's IT department could be one subscription, and a credit card belonging to the Accounting department would be another subscription.

Subscriptions can also have policies, RBAC, and budgets applied to them.

## Resource Groups

A resource group holds resources. Isn't that surprising...

Resources in resource groups are not restricted to communicating within their group - resources can communicate outside their own resource group.