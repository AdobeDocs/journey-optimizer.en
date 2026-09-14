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
* Manage Roles, Policies, and Products via the attribute-based access control API

**Glossary:**

* **ABAC (Attribute-based access control)**: A capability to define authorizations to manage data access for specific teams or groups of users based on attributes such as labels *(product-specific)*
* **Role**: A set of users sharing the same permissions, labels, and sandboxes within an organization *(product-specific)*
* **Label**: A governance marker (e.g., C2) applied to schema fields, datasets, or audiences to control which roles can access them *(product-specific)*
* **Policy**: A configuration that must be created before managing permissions for a role — prerequisite for ABAC *(product-specific)*
* **XDM schema**: Experience Data Model schema used to define data structure in Adobe Experience Platform *(product-specific)*

**Guardrails:**

* A policy must be created before managing permissions for a role (prerequisite, as stated in the Important note on the page)
* Incorrect label usage can break access for people and trigger policy violations (as stated in the Warning on the page)
* Users without a label matching a restricted field cannot: view the restricted field name, edit expressions referencing it in advanced mode, test the journey, or publish the journey

**Terminology:**

* Canonical name: Attribute-based access control — Acronym: ABAC — variants: attribute-based access management
* Canonical name: Experience Data Model — Acronym: XDM — variants: XDM schema, XDM schemas
* Synonyms: "Label" = "governance label" = "data governance label"
* Do not confuse: "Role" (a group of users with shared permissions and labels) ≠ "Policy" (rules governing enforcement of data access based on labels)
* Do not confuse: ABAC (controls access to schema fields, datasets, and audiences via label policies at the platform level) ≠ OLAC (controls access to specific Journey Optimizer objects like journeys and campaigns)

**FAQ:**

* **Q: Can labels be added to built-in roles?** — Yes, labels can be added to both custom and built-in roles.
* **Q: What happens to a user who lacks the label for a restricted field in a journey?** — The field is not visible to them; they cannot edit expressions referencing it, test the journey, or publish the journey.
* **Q: Can labels be applied to objects other than schema fields?** — Yes; labels can also be applied to schemas, datasets, and audiences.
* **Q: Is there an API for managing roles, policies, and products with ABAC?** — Yes; Roles, Policies, and Products can be accessed via the attribute-based access control API.

+++
<!-- ai-accordion-version: 1 | source-hash: aa94c226 -->
