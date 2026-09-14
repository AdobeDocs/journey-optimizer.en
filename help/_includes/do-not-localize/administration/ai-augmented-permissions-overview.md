---
title: AI Knowledge Reference
---
# AI Knowledge Reference

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
