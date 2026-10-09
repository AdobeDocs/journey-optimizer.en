---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Object level access control (OLAC) lets you apply access labels to specific Journey Optimizer objects — such as journeys, campaigns, and offers — so that, to access an object, users must have the specific Label included in their Roles.

**Intents:**

* Create a custom access label directly in Journey Optimizer or via the Permissions product
* Assign access labels to Journey Optimizer objects (journeys, campaigns, offers, etc.)
* Restrict sensitive content to authorized users only
* Understand which permissions are required to create and assign labels

**Glossary:**

* **OLAC (Object level access control)**: A capability to define authorizations to manage data access for a selection of specific Journey Optimizer objects *(product-specific)*
* **Label**: Labels categorize datasets and fields according to usage policies; in OLAC, a Label assigned to an object limits access to users whose Roles include that Label *(product-specific)*
* **Manage access**: The button on an Adobe Journey Optimizer object (and the window it opens) used to create labels and to select labels that manage access to the object *(product-specific)*
* **Core data usage labels**: The page says you can assign custom or core data usage labels, and links to Adobe Experience Platform documentation for more information on core data usage labels *(product-specific)*

**Guardrails:**

* Creating labels requires the **Manage usage labels** permission (prerequisite)
* Assigning labels requires belonging to a role with a **Manage** permission, i.e., Manage journeys, Manage Campaigns, or Manage decisions; without it, the **Manage access** button is greyed out (prerequisite)
* Supported objects for OLAC labels: Journey, Campaign, Template, Fragment, Landing page, Offer, Static offer collection, Offer decision, Channel configuration, IP warmup plan

**Terminology:**

* Canonical name: Object level access control — Acronym: OLAC
* Do not confuse: "core data usage labels" ≠ "custom labels" (the page names both as labels you can select to manage access to an object)

**FAQ:**

* **Q: Can I create a label directly in Journey Optimizer without going to the Permissions product?** — Yes; the page states you can also create Labels directly in Journey Optimizer: from an Adobe Journey Optimizer object, such as a newly created Campaign, click the Manage access button, then click Create label.
* **Q: Which object types support OLAC labels?** — Journey, Campaign, Template, Fragment, Landing page, Offer, Static offer collection, Offer decision, Channel configuration, and IP warmup plan.
* **Q: What permission is needed to assign a label to a journey?** — A role with a Manage permission, i.e., Manage journeys, Manage Campaigns, or Manage decisions; without this permission, the Manage access button is greyed out.
* **Q: If a user has only the C1 label in their role, which objects can they access?** — Only C1-labeled or unlabeled objects.

+++
<!-- ai-accordion-version: 1 | source-hash: 5ae3809d -->
