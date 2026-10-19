---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build conditional rules from profile attributes, contextual events, and audiences in the personalization editor, and how to save them to the library for reuse across message content.

**Intents:**

* Access the conditional rule builder from the personalization editor or Email Designer
* Build a conditional rule by combining profile attributes, audience membership, and contextual journey fields
* Add a conditional rule to a message to create dynamic content
* Save a conditional rule to the conditions library for reuse across the organization
* Edit or delete a saved conditional rule

**Glossary:**

* **Conditional rule**: A set of rules that defines which content should be displayed in messages, based on criteria such as profile attributes, audience membership, or contextual events. *(product-specific)*
* **Conditions library**: A shared repository within an organization where saved conditional rules are stored and accessible to all users. *(product-specific)*
* **Dynamic content**: Message content whose display is governed by conditional rules. *(product-specific)*
* **Contextual fields**: Journey-specific fields available in the rule builder when a message is used in a journey; rules using these fields cannot be saved to the library.
* **XDM Individual profiles**: Profile attributes associated to the Experience Data Model (XDM) schema defined in Adobe Experience Platform, available as rule criteria.

**Guardrails:**

* Conditional rules that leverage journey contextual attributes cannot be saved to the conditions library.
* Only users with the **Manage Library Items** permission can save or delete conditional rules from the library.
* Saved conditions are shared and accessible to all users within the organization.
* Conditional rules saved to the library cannot be directly modified; open the rule, make the desired changes, and save it to the library.
* Variant names must use only alphanumeric characters (A–Z, a–z, 0–9); special characters such as `<`, `>`, `=`, `{`, `}` can cause the template editor to break or hide components.

**Terminology:**

* **Canonical name:** conditional rule — variants: condition, conditions, conditional content rule
* **Synonyms:** "conditional rule" = "condition" (as labeled in the UI)
* **Do not confuse:** "Profile" tab (contains both Audiences attributes and XDM Individual profiles sub-sections) ≠ "Audiences" tab (lists all audiences generated from segment definitions in AEP Segmentation service)
* **Do not confuse:** "save a condition" (storing a rule to the shared library) ≠ "create a condition" (building a new rule in the editor)

**FAQ:**

* **Q: What criteria can I use to build a conditional rule?** — Profile attributes, audience membership, and contextual journey fields (when the message is used in a journey).
* **Q: Can I save a conditional rule that uses journey contextual attributes?** — No. Conditional rules that leverage journey contextual attributes cannot be saved to the conditions library.
* **Q: Who can save or delete conditional rules in the library?** — Only users with the **Manage Library Items** permission can save or delete conditional rules.
* **Q: Can I modify a conditional rule that is already saved to the library?** — Conditional rules saved to the library cannot be directly modified. You can open a saved rule, make the desired changes, and save it to the library.
* **Q: Are there restrictions on naming conditional content variants?** — Yes. Variant names must contain only alphanumeric characters (A–Z, a–z, 0–9). Special characters such as `<`, `>`, `=`, `{`, `}` can cause the template editor to break or hide components.

+++

<!-- ai-section-version: 1 | source-hash: f375658d -->
