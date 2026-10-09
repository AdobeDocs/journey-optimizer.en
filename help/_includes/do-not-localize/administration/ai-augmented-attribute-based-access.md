---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Protect sensitive data fields in Journey Optimizer by applying governance labels to schema fields and assigning matching labels to roles, so unauthorized users cannot view, edit, test, or publish journeys that use those restricted fields.

**Intents:**

* Create a role and assign a governance label to restrict access to specific schema fields
* Apply a label to a schema field in Adobe Experience Platform to enforce access restrictions
* Use a labeled schema field in a Journey Optimizer journey
* Understand how users without the required label experience access restrictions in journeys
* Know that Roles, Policies, and Products can also be accessed with the attribute-based access control API

**Glossary:**

* **ABAC (Attribute-based access control)**: A capability that allows you to define authorizations to manage data access for specific teams or groups of users, protecting sensitive digital assets from unauthorized users *(product-specific)*
* **Role**: A set of users sharing the same permissions, labels, and sandboxes within an organization *(product-specific)*
* **Label**: A label (for example, C2 - Data cannot be exported to a third-party) assigned to a schema field and granted to a Role; the page also states that a Label can be added to Schema, Datasets, and Audiences *(product-specific)*
* **Policy**: A policy must be created before managing permissions for a role *(product-specific)*
* **XDM schema**: Experience Data Model schema; the page says attribute-based access control can grant specific access to XDM schemas *(product-specific)*

**Guardrails:**

* A policy must be created before managing permissions for a role (prerequisite, as stated in the Important note on the page)
* Incorrect label usage can break access for people and trigger policy violations (as stated in the Warning on the page)
* Users without a label matching a restricted field cannot: view the restricted field name, edit expressions referencing it in advanced mode, test the journey, or publish the journey

**Terminology:**

* Canonical name: Attribute-based access control
* Canonical name: Experience Data Model — Acronym: XDM — variants: XDM schema, XDM schemas
* Synonyms: "Label" = "governance label" (the page uses the **Edit governance labels** option for labels)
* Do not confuse: "Role" (a set of users that share the same permissions, labels, and sandboxes) ≠ "Policy" (the page only states that a policy must be created before managing permissions for a role)

**FAQ:**

* **Q: Can labels be added to built-in roles?** — Yes, you can also add a Label to built-in roles, and you can create your own Roles.
* **Q: What happens to a user who lacks the label for a restricted field in a journey?** — The restricted field name is not visible to them, they cannot edit the expression with it in advanced mode (the error `The expression is invalid. Field is no longer available or you do not have enough permission to see it` appears), they cannot test the journey, and they cannot publish the journey. They can delete the expression.
* **Q: Can labels be applied to objects other than schema fields?** — Yes; the page states you can also add a Label to Schema, Datasets, and Audiences.
* **Q: Is there an API for managing roles, policies, and products with ABAC?** — Yes; Roles, Policies, and Products can be accessed via the attribute-based access control API.

+++
<!-- ai-accordion-version: 1 | source-hash: 49ef3ad5 -->
