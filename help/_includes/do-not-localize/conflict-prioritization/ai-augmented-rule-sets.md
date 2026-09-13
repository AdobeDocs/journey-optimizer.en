---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create channel and journey rule sets that group frequency capping, quiet hours, and journey capping rules, how to activate them, and how to apply them to journeys and campaigns.

**Intents:**

* Understand channel rule sets versus journey rule sets and what rules each holds
* Create a rule set, choose its domain, add rules, and activate the rules and the rule set
* Use the pre-created Global Default Rule Set or create custom rule sets
* Apply a rule set to a message or a journey based on its domain
* Access, deactivate, and delete rule sets

**Glossary:**

* **Rule set**: A group of multiple rules applied to the journeys and campaigns of your choice *(product-specific)*
* **Channel rule set**: A rule set that applies frequency capping rules or quiet hours rules to communication channels *(product-specific)*
* **Journey rule set**: A rule set that applies entry and concurrency capping rules to a journey *(product-specific)*
* **Global Default Rule Set**: A default rule set, pre-created and active, whose global rules apply to all selected channels for journeys and campaigns *(product-specific)*
* **[!UICONTROL View Frequency Rules] / [!UICONTROL Manage Frequency Rules]**: Permissions to view, and to create, edit, or delete, business rules *(product-specific)*

**Guardrails:**

* You can create up to 10 rule sets for the channel domain and 10 rule sets for the journey domain, for a total of 20 rule sets (hard limit).
* Working with business rules requires the [!UICONTROL View Frequency Rules] permission (view) and the [!UICONTROL Manage Frequency Rules] permission (create, edit, delete).
* A rule starts with the [!UICONTROL Draft] status and does not impact any message until you activate it and its rule set.
* It can take up to 10 minutes for a rule or rule set to be fully activated; you do not need to modify messages or republish journeys for a rule to take effect.
* Deactivating a rule or rule set sets its status to [!UICONTROL Inactive]; it does not apply to future message executions, does not affect messages currently in execution, and does not affect or reset any counts on individual profiles.

**Terminology:**

* Canonical name: rule set — Acronym: n/a — variants: rule sets, business rules
* Synonyms: none
* Do not confuse: "rule set" (a group of rules) ≠ "rule" (a single rule inside a rule set)
* Do not confuse: "channel rule set" (frequency capping or quiet hours rules) ≠ "journey rule set" (entry and concurrency capping rules)
* Do not confuse: "Global Default Rule Set" (pre-created global rules applying to all selected channels) ≠ custom rule sets (applied to specific journeys or campaigns)

**FAQ:**

* **Q: What are the two types of rule sets?** — Channel rule sets (frequency capping and quiet hours rules) and journey rule sets (entry and concurrency capping rules).
* **Q: How many rule sets can I create?** — Up to 10 for the channel domain and 10 for the journey domain, for a total of 20.
* **Q: What permissions do I need?** — [!UICONTROL View Frequency Rules] to view business rules and [!UICONTROL Manage Frequency Rules] to create, edit, or delete them.
* **Q: How long does activation take?** — Up to 10 minutes for a rule or rule set to be fully activated, without modifying messages or republishing journeys.
* **Q: Does deactivating a rule reset profile counts?** — No, deactivating a rule or rule set does not affect or reset any counts on individual profiles.
* **Q: What is the Global Default Rule Set?** — A pre-created, active rule set whose global rules apply to all selected channels for both journeys and campaigns.

+++

<!-- ai-section-version: 1 | source-hash: ad0b90c8 -->
