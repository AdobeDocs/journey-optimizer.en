---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Access control in Journey Optimizer is built on roles, permissions, and sandboxes managed through Adobe CX Enterprise Permissions, with object-based access control and attribute-based access control also listed as key concepts.

**Intents:**

* Understand the five core access control concepts: roles, permissions, sandboxes, object-based access control, and attribute-based access control
* Know who can configure access control (system or product administrator)
* Navigate to the right documentation section for each access control topic
* Plan how to grant users the right access by learning the core access control concepts

**Glossary:**

* **Roles**: A collection of users who share the same permissions and sandboxes; with Journey Optimizer, you can choose from a range of pre-existing Roles, each with varying levels of permissions *(product-specific)*
* **Permissions**: Unitary rights defining the authorizations assigned to Roles, grouped under resources such as Journey or Offers *(product-specific)*
* **Sandboxes**: Virtual sandboxes partition instances into separate, isolated virtual environments; Sandboxes are assigned through roles in Permissions *(product-specific)*
* **Object-based access control**: Labels to limit the access to an object; this approach protects sensitive digital assets from unauthorized users and ensures further protection of personal data *(product-specific)*
* **Attribute-based access control**: Authorizations to manage data access for specific teams or groups of users; it enables administrators to control access to specific objects and/or capabilities based on attributes, which can be metadata added to an object, such as a label added to a schema field or segment *(product-specific)*

**Guardrails:**

* Configuring access control requires system or product administrator privileges (prerequisite); system administrators have no restrictions
* The minimum role that can grant or withdraw permissions is a product administrator (as stated on the page)

**Terminology:**

* Canonical name: Attribute-based access control — variants: Attribute-based access management (link text on the page)
* Canonical name: Object-based access control — variants: Object-based access management (link text on the page)
* Do not confuse: "Object-based access control" (labels to limit the access to an object) ≠ "Attribute-based access control" (access based on attributes, which can be metadata added to an object, such as a label added to a schema field or segment)
* Do not confuse: "Roles" (a collection of users with shared permissions and sandboxes) ≠ "Permissions" (the unitary rights grouped under resources that are assigned to roles)

**FAQ:**

* **Q: Who can configure access control in Journey Optimizer?** — Users with system administrator or product administrator privileges.
* **Q: What is the minimum administrator level required to grant or withdraw permissions?** — Product administrator.
* **Q: Are sandboxes managed independently of roles?** — The page states that Sandboxes are assigned through roles in Permissions.
* **Q: Where is access control for Journey Optimizer managed?** — Through Permissions in Adobe CX Enterprise; this functionality leverages roles and policies, which link users with permissions and sandboxes.

+++
<!-- ai-accordion-version: 1 | source-hash: d4984095 -->
