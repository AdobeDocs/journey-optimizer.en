---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Object level access control (OLAC) lets you apply access labels to specific Journey Optimizer objects — such as journeys, campaigns, and offers — so only users whose role includes the matching label can view or interact with those objects.

**Intents:**

* Create a custom access label directly in Journey Optimizer or via the Permissions product
* Assign access labels to Journey Optimizer objects (journeys, campaigns, offers, etc.)
* Restrict sensitive content to authorized users only
* Understand which permissions are required to create and assign labels

**Glossary:**

* **OLAC (Object level access control)**: A capability to define authorizations to manage data access for a selection of specific Journey Optimizer objects *(product-specific)*
* **Label**: A tag applied to an object to categorize it by usage policy and restrict access based on role membership *(product-specific)*
* **Manage access**: The button or interface available on supported Journey Optimizer objects for creating and assigning access labels *(product-specific)*
* **Core data usage labels**: Pre-defined labels provided by Adobe Experience Platform, as opposed to custom labels created by the organization *(product-specific)*

**Guardrails:**

* Creating labels requires the **Manage usage labels** permission (prerequisite)
* Assigning labels requires a **Manage** permission for the object type (e.g., Manage journeys, Manage Campaigns, or Manage decisions); without it, the **Manage access** button is greyed out (prerequisite)
* Supported objects for OLAC labels: Journey, Campaign, Template, Fragment, Landing page, Offer, Static offer collection, Offer decision, Channel configuration, IP warmup plan

**Terminology:**

* Canonical name: Object level access control — Acronym: OLAC — variants: object-based access control, object-based access management
* Do not confuse: OLAC (restricts access to specific AJO objects like journeys and campaigns using labels) ≠ ABAC (attribute-based, applies label policies to schema fields, datasets, and audiences at the platform level)
* Do not confuse: "core data usage labels" (pre-built labels from Adobe Experience Platform) ≠ "custom labels" (labels created by the organization)

**FAQ:**

* **Q: Can I create a label directly in Journey Optimizer without going to the Permissions product?** — Yes; use the Manage access window on any supported object and click Create label.
* **Q: Which object types support OLAC labels?** — Journey, Campaign, Template, Fragment, Landing page, Offer, Static offer collection, Offer decision, Channel configuration, and IP warmup plan.
* **Q: What permission is needed to assign a label to a journey?** — The Manage journeys permission; without a Manage permission, the Manage access button is greyed out.
* **Q: If a user has only the C1 label in their role, which objects can they access?** — Only C1-labeled or unlabeled objects.

+++
<!-- ai-accordion-version: 1 | source-hash: 4e9b2577 -->
