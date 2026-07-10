---
solution: Journey Optimizer
product: journey optimizer
title: User management overview
description: Learn how to define and manage permissions
feature: Access Management
topic: Administration
role: Admin, Developer
level: Intermediate
keywords: permissions, rights, restrictions, access, sandbox
exl-id: b8e266b1-d8eb-4c77-9341-9761b82609b0
TQID: https://experienceleague.adobe.com/VRUXM-o41h44PxMAKyafwqSHKmduyt48j4sr11Gh-EQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: b856530c-d60b-42d8-a19d-df2dfd7fe62a
    internal-label: Access control
subfeature_v2:
  - id: b856530c-d60b-42d8-a19d-df2dfd7fe62a
    internal-label: Access control
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Get started with access control {#permissions-overview}

>[!BEGINSHADEBOX]

**On this page:** Get familiar with the core access control concepts in Journey Optimizer, including roles, permissions, sandboxes, and object- and attribute-based access control, so you can plan how to grant users the right access.

>[!ENDSHADEBOX]

[!DNL Journey Optimizer] allows you to define and manage the permissions assigned to different users. Permissions are a set of rights and restrictions that authorize or deny access to in-product features and capabilities. 

Access control for [!DNL Journey Optimizer] is provided through **Permissions** in [!DNL Adobe CX Enterprise]. This functionality leverages roles and policies, which link users with permissions and sandboxes.

In order to configure access control for Journey Optimizer, you must have system or product administrator privileges for your organization. The minimum role that can grant or withdraw permissions is a product administrator. Other administrator roles that can manage permissions are system administrators (no restrictions). See the [Adobe Help Center article](https://helpx.adobe.com/enterprise/using/admin-roles.html){target="_blank"} on administrative roles for more information.

<!--
 A high-level workflow for gaining and assigning access permissions can be summarized as follows:

* After licensing [!DNL Journey Optimizer], an email is sent to the administrator specified during licensing.
* The administrator logs in to Adobe Admin Console and selects [!DNL Journey Optimizer] from the list of products on the overview page.
* To grant access to [!DNL Journey Optimizer], it is recommended that the administrator add users to the default product profile
* In Experience Platform Permissions, the administrator can create new roles or edit the permissions and users for any existing roles.
* When creating or editing a role, the administrator adds users to the role using the users tab, and grants permissions to these users (such as "Read Datasets" or "Manage Schemas") by editing the role's permissions. Similarly, the administrator can assign access to sandboxes using the same editing option.
* When users log in to the Journey Optimizer user interface, their access to capabilities is driven by the permissions that have been granted to them from the previous step. For example, if a user does not have the View Datasets permission, the Datasets tab in the side menu will not be visible to that user.
-->


User management in [!DNL Journey Optimizer] is based on these key concepts:

* **[!UICONTROL Roles]**: Roles refer to a collection of users who share the same permissions and sandboxes. These roles allow you to easily manage access and permissions for different groups of users within your organization. A role comes with a set of unitary rights (permissions) which allows users access to certain functionalities or objects in the interface. 
    With [!DNL Journey Optimizer], you can choose from a range of pre-existing **[!UICONTROL Roles]**, each with varying levels of permissions, to assign to your users. Learn more about the available **Built-in roles** on [this page](ootb-product-profiles.md).

* **[!UICONTROL Permissions]**: Permissions are unitary rights which allow you to define the authorizations assigned to **[!UICONTROL Roles]**. Each permission is gathered under resources, e.g. Journey or Offers, which represents the different functionalities or objects in [!DNL Journey Optimizer]. Learn more in the [Permission levels](high-low-permissions.md) section.
    
     ![](assets/do-not-localize/permissions_2.png)

* **[!UICONTROL Sandboxes]**: Virtual sandboxes partition instances into separate, isolated virtual environments. Sandboxes are assigned through roles in Permissions. Learn more about [using sandboxes](sandboxes.md). 

* **Object-based access control**: Labels to limit the access to an object. This approach protects sensitive digital assets from unauthorized users and ensures further protection of personal data. Learn more about [Object-based access management](object-based-access.md).

* **Attribute-based access control**: Authorizations to manage data access for specific teams or groups of users. Attribute-based access control enables administrators to control access to specific objects and/or capabilities based on attributes. Attributes can be metadata added to an object, such as a label added to a schema field or segment. An administrator defines access policies that include attributes to manage user access permissions. Learn more about [Attribute-based access management](attribute-based-access.md).


## Let's dive deeper

Now that you have an understanding of access control concepts in **[!DNL Journey Optimizer]**, it's time to dive deeper into these documentation sections to start configuring permissions.


<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="permissions.md">
<img alt="Permissions" src="assets/do-not-localize/role.jpg">
</a>
<div>
<a href="permissions.md"><strong>Grant access</strong></a>
</div>
<p>
</td>
<td>
<a href="ootb-permissions.md">
<img alt="Built-in permissions" src="assets/do-not-localize/select.jpg">
</a>
<div>
<a href="ootb-permissions.md"><strong>Built-in permissions</strong></a>
</div>
<p>
</td>
<td>
<a href="sandboxes.md">
<img alt="manage sandboxes" src="assets/do-not-localize/sandboxes.jpg">
</a>
<div>
<a href="sandboxes.md"><strong>Manage sandboxes</strong></a>
</div>
<p></td>
<td>
<a href="attribute-based-access.md">
<img alt="Attribute-based access control" src="assets/do-not-localize/data-access.jpeg">
</a>
<div>
<a href="attribute-based-access.md"><strong>Attribute-based access control</strong></a>
</div>
<p>
</td>
</tr></table>

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Access control in Journey Optimizer is built on roles, permissions, and sandboxes managed through Adobe CX Enterprise Permissions, with additional layers of object-based access control (OLAC) and attribute-based access control (ABAC) for fine-grained data protection.

**Intents:**

* Understand the five core access control concepts: roles, permissions, sandboxes, object-based access control, and attribute-based access control
* Know who can configure access control (system or product administrator)
* Navigate to the right documentation section for each access control topic
* Plan an access control strategy for the organization

**Glossary:**

* **Roles**: Collections of users sharing the same permissions and sandboxes; pre-existing built-in roles are available, and custom roles can be created *(product-specific)*
* **Permissions**: Unitary rights defining the authorizations assigned to Roles, grouped under resources such as Journey or Offers *(product-specific)*
* **Sandboxes**: Virtual environments partitioning the Journey Optimizer instance into separate, isolated virtual workspaces; assigned through roles in Permissions *(product-specific)*
* **Object-based access control**: Labels applied to specific Journey Optimizer objects (journeys, campaigns, offers) to restrict access to authorized users *(product-specific)*
* **Attribute-based access control**: Policies controlling access to objects or capabilities based on attributes such as labels added to schema fields or segments *(product-specific)*

**Guardrails:**

* Configuring access control requires system or product administrator privileges (prerequisite)
* The minimum role that can grant or withdraw permissions is a product administrator (as stated on the page)

**Terminology:**

* Canonical name: Attribute-based access control — Acronym: ABAC — variants: attribute-based access management
* Canonical name: Object-based access control — Acronym: OLAC — variants: object-level access control, object-based access management
* Do not confuse: "Object-based access control" (restricts access to specific AJO objects like journeys, campaigns, and offers using labels) ≠ "Attribute-based access control" (restricts access to data attributes like schema fields and segments based on label policies)
* Do not confuse: "Roles" (a collection of users with shared permissions and sandboxes) ≠ "Permissions" (the unitary rights grouped under resources that are assigned to roles)

**FAQ:**

* **Q: Who can configure access control in Journey Optimizer?** — Users with system administrator or product administrator privileges.
* **Q: What is the minimum administrator level required to grant or withdraw permissions?** — Product administrator.
* **Q: Are sandboxes managed independently of roles?** — No; sandboxes are assigned through roles in the Permissions product.
* **Q: Where is access control for Journey Optimizer managed?** — Through Permissions in Adobe CX Enterprise, which links users with permissions and sandboxes via roles and policies.

+++
<!-- ai-accordion-version: 1 | source-hash: 14be1dc6 -->