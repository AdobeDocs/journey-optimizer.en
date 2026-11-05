---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create reusable loyalty tasks, configure Purchase, Spend, and Custom event activities, and define task attributes, eligibility, and completion requirements.

**Intents:**

* Create a task from the Tasks inventory or from within a challenge.
* Choose a customer activity type (Purchase, Spend, or Custom event) for a task.
* Configure activity-specific attributes, such as quantity, amount, or custom event values.
* Define eligible items and exclusions for Purchase and Spend tasks.
* Use Bring your own data to resolve task eligibility at runtime from external data instead of selecting items in Journey Optimizer.
* Define task properties, including the task name and description.

**Glossary:**

* **Task**: a reusable component representing a measurable action or milestone that customers must complete toward challenge completion *(product-specific)*
* **Purchase activity**: an activity type that requires customers to purchase one or more items to complete a task *(product-specific)*
* **Spend activity**: an activity type that requires customers to spend a specified amount to complete a task *(product-specific)*
* **Custom event activity**: an activity type based on an Adobe Experience Platform experience event that is already captured in Experience Platform and mapped through an event mapping in the Loyalty configurations menu *(product-specific)*
* **Tasks inventory**: the Tasks tab where tasks are saved and available for reuse across multiple challenges *(product-specific)*
* **Eligible items & exclusions**: the Purchase and Spend attribute that defines which items or groups count toward task completion and which are excluded *(product-specific)*
* **Bring your own data**: the option that resolves eligibility per participant at runtime from data synchronized with the Loyalty Challenges environment, instead of a list of item IDs *(product-specific)*

**Guardrails:**

* Custom event tasks do not use eligible items and exclusions; completion is driven by the Custom event values configured for the task.
* Custom event values entered for a task must match event mappings configured in the Loyalty configurations menu.
* Items from the global exclusions list are automatically added as exclusions.
* Exclusions take priority over inclusions: items listed as excluded do not count, even if they are also part of an included group.
* If no eligible items or groups are selected for a Purchase or Spend task, purchases are not limited to a specific inventory set, unless exclusions are configured.
* For Spend activities, the Maximum number of transactions attribute must be activated from the parameters icon.
* When assigning a task configured with Bring your own data to a challenge, select Standard as the challenge type; Bring your own data at the challenge level is reserved for fully data-driven challenges where the entire structure, including tasks and rewards, is supplied externally.

**Applicability:**

* Bring your own data (task-level eligibility for Purchase and Spend activities): applies only to a restricted set of organizations currently; will be made available more broadly in a future release.

**Terminology:**

* Canonical name: Adobe Experience Platform — Acronym: AEP — variants: Experience Platform
* Canonical name: Task — variants: none
* Synonyms: none
* Do not confuse: task-level "Bring your own data" (eligibility resolved at runtime from external data instead of item IDs) ≠ challenge-level "Bring your own data" (reserved for fully data-driven challenges where the entire structure, including tasks and rewards, is supplied externally)
* Do not confuse: "Eligible items & exclusions" (selecting items and groups within Journey Optimizer, for Purchase and Spend only) ≠ "Bring your own data" (eligibility resolved at runtime from synchronized external data)

**FAQ:**

* **Q: What are the three activity types for a task?** — Purchase, Spend, and Custom event.
* **Q: Where can I create a task?** — From the Tasks inventory (Tasks tab, Create Task) or from within a challenge (Add task, New); tasks created within a challenge are also saved to the Tasks inventory.
* **Q: Do Custom event tasks use eligible items and exclusions?** — No; completion for Custom event tasks is driven by the Custom event values configured for the task.
* **Q: What happens if an item is both included and excluded?** — Exclusions take priority over inclusions; excluded items do not count even if part of an included group.
* **Q: What happens if no eligible items or groups are selected for a Purchase or Spend task?** — Purchases are not limited to a specific inventory set, unless exclusions are configured.
* **Q: What challenge type should I use with a task configured for Bring your own data?** — Select Standard as the challenge type; Bring your own data at the challenge level is reserved for fully data-driven challenges where the entire structure, including tasks and rewards, is supplied externally.

**Examples:**

* Eligible items & exclusions (Purchase and Spend): limiting a task to specific product categories, or excluding gift cards or promotional items from counting toward task completion.
* Custom event activity: events such as a hotel check-in, mobile app action, or review submission, represented by an Adobe Experience Platform experience event.

**Related pages:**

* To configure the Custom event event mappings referenced by this page: Learn how to configure event mappings (loyalty-challenges/loyalty-admin.md)
* To configure the product inventory used for eligible items: Learn how to configure product inventory (loyalty-challenges/loyalty-admin.md)
* To configure organization-wide exclusions applied automatically to tasks: exclusions (loyalty-challenges/loyalty-admin.md)

**Personas:**

* **marketer:** Can create a task from the Tasks inventory by selecting Create Task, or from within a challenge by selecting Add task and New. Can choose a Purchase, Spend, or Custom event activity, then configure attributes such as Quantity, Amount, or Custom event values. Can define eligible items and exclusions for Purchase and Spend tasks, and set the task name and description. The page states that Custom event tasks do not use eligible items and exclusions. Where: "Create a task".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Select the Tasks tab and select Create Task.
* **Success check:** The task is saved to your Tasks inventory and, if created from within a challenge, is automatically added to that challenge.
* **Previous:** Configure event mappings, product inventory, or exclusions used when building tasks: Configure loyalty challenges (loyalty-challenges/loyalty-admin.md)

+++

<!-- ai-section-version: 1 | source-hash: 807cc8df -->
