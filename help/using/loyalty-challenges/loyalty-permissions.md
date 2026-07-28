---
solution: Journey Optimizer
product: journey optimizer
title: Loyalty Challenges permissions
description: Learn which permissions are required to access, configure, and use Loyalty Challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Administration
role: Admin
level: Intermediate
exl-id: 7d6d4f18-8c5d-4c9c-9f7d-2d6c5f9a8b31
feature_v2: []
subfeature_v2: []
---
# Loyalty Challenges permissions {#loyalty-permissions}

## Overview {#overview}

[!DNL Adobe Journey Optimizer] Loyalty uses Adobe Admin Console role-based access control (RBAC) to manage user access.

Role assignment is required before users can perform Loyalty operations. Users without an assigned role are denied access to Loyalty service endpoints. Before onboarding users to Loyalty, assign an appropriate role to each user who will use the service.

Roles can be assigned directly to individual users, or through user groups. [Learn how to assign roles to users](#assign-roles).

## Recommended roles {#recommended-roles}

Loyalty provides three default roles pre-configured for the **Prod** sandbox. New customers can use these roles as-is.

### Loyalty Administrator {#loyalty-administrator}

The **Loyalty Administrator** role provides full administrative access to all Loyalty features: challenges, configuration, product catalog, and insights.

| Permission | Description |
| - | - |
| Manage Loyalty Challenges | Create, edit, delete, publish, unpublish, and archive challenges; trigger journey generation |
| Manage Loyalty Primary Configuration | Create, edit, and delete primary organization configuration |
| Manage Loyalty Advanced Configuration | Manage reward endpoints and event transformation settings, including read/write access to sensitive credential values |
| Manage Loyalty Product Catalog | View, import, and edit product catalog entries |
| Manage Loyalty Insights | View insights, update KPI configuration, and trigger the insights pipeline |

### Loyalty Practitioner {#loyalty-practitioner}

The **Loyalty Practitioner** role is designed for business owners who manage the full challenge lifecycle and edit primary configuration. Reward configuration, event configuration, and product catalog access are read-only. Deletion and advanced configuration writes are not permitted.

| Permission | Description |
| - | - |
| Manage Loyalty Challenges | Create, edit, delete, publish, unpublish, and archive challenges; trigger journey generation |
| Configure Loyalty Primary Configuration | Create and edit primary organization configuration. Deletion is not permitted |
| View Loyalty Reward Configuration | View reward configuration, including providers, definitions, and proxies. Sensitive values are excluded |
| View Loyalty Event Configuration | View event definitions and event transformation mappings |
| View Loyalty Product Catalog | View product catalog entries and import job status |
| Develop Loyalty Insights | View insights data and update insight cards |

### Loyalty Analyst {#loyalty-analyst}

The **Loyalty Analyst** role provides read-only access to challenges, product catalog, and insights. Use this role for reporting and audit purposes.

| Permission | Description |
| - | - |
| View Loyalty Challenges | View challenges |
| View Loyalty Product Catalog | View product catalog entries and import job status |
| View Loyalty Insights | View AI-generated insight cards, health vitals, and challenge performance data |

## Role capabilities {#role-capabilities}

| Operation | Administrator | Practitioner | Analyst |
| - | - | - | - |
| Challenges - view | Yes | Yes | Yes |
| Challenges - create or edit | Yes | Yes | No |
| Challenges - delete | Yes | Yes | No |
| Challenges - publish, unpublish, or archive | Yes | Yes | No |
| Challenges - trigger journey generation | Yes | Yes | No |
| Primary organization configuration - view | Yes | Yes | No |
| Primary organization configuration - create or edit | Yes | Yes | No |
| Primary organization configuration - delete | Yes | No | No |
| Reward configuration - view, sensitive values excluded | Yes | Yes | No |
| Reward configuration - write or access sensitive values | Yes | No | No |
| Event configuration - view | Yes | Yes | No |
| Event configuration - write | Yes | No | No |
| Product catalog - view | Yes | Yes | Yes |
| Product catalog - import or edit | Yes | No | No |
| Insights - view | Yes | Yes | Yes |
| Insights - write or update KPI configuration | Yes | No | No |

## Default role scope {#default-role-scope}

>[!IMPORTANT]
>
>Default Loyalty roles are scoped to the **Prod** sandbox only.

To grant users access to a non-Prod sandbox, such as a staging or development sandbox, create a custom role for that sandbox and assign the same permissions as the corresponding default role.

## Available permissions for custom roles {#custom-role-permissions}

When you create a custom role for a non-Prod sandbox, select from the permissions below. To replicate a default role, refer to the permissions listed in the relevant role section above.

| Permission | Description |
| - | - |
| Manage Loyalty Challenges | Full challenge operations: create, edit, delete, publish, unpublish, archive, and trigger journey generation |
| Develop Loyalty Challenges | Create and edit challenges via API. Delete and lifecycle actions are not permitted |
| View Loyalty Challenges | View challenges only |
| Manage Loyalty Primary Configuration | Create, edit, and delete primary organization configuration |
| Configure Loyalty Primary Configuration | Create and edit primary organization configuration. Deletion is not permitted |
| Manage Loyalty Advanced Configuration | Manage reward endpoints and event transformation settings, including read/write access to sensitive credential values |
| View Loyalty Reward Configuration | View reward providers, reward definitions, and reward proxies. Sensitive values are excluded |
| View Loyalty Event Configuration | View event definitions and event transformation mappings |
| Manage Loyalty Product Catalog | View, import from CSV, and edit product catalog entries, including inclusions and exclusions; monitor import job status |
| View Loyalty Product Catalog | View product catalog entries and import job status. Upload and edit actions are not permitted |
| Manage Loyalty Insights | View insights, update KPI configuration, and trigger the insights pipeline |
| Develop Loyalty Insights | View insights data and update insight cards |
| View Loyalty Insights | View AI-generated insight cards, health vitals, and challenge performance data only |

## Assign roles to users {#assign-roles}

>[!IMPORTANT]
>
>Only Product administrators and System administrators can manage users, groups, and roles.

Adobe Admin Console supports two approaches for associating roles with users.

### Assign users directly to a role {#assign-users-directly}

Add individual users directly to a role. This approach is best suited for small teams or one-off assignments.

### Use user groups {#use-user-groups}

Create a user group, then assign both users and a role to the group. This approach is best suited for managing access by department or function at scale.

For step-by-step instructions on managing roles, groups, and users, refer to the Adobe Journey Optimizer access control documentation:

* [Manage users and roles](../administration/permissions.md)
* [Built-in permissions](../administration/ootb-permissions.md)

## Troubleshooting access {#troubleshooting}

If a user cannot access Loyalty Challenges or a related feature, check the following:

* The user is assigned to a Loyalty role.
* The role includes the sandbox where Loyalty Challenges is enabled.
* The role includes the permission required for the action the user is trying to perform.
* For non-Prod sandboxes, a custom role has been created for that sandbox.
* The organization and sandbox are enabled for Loyalty Challenges.

If access issues persist after permissions are updated, contact your Adobe representative.
