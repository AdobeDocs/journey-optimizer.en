---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page shows how to build a journey that sends an email to subscribers of a list by overriding the default email address parameter using an expression that reads subscriber addresses from a consent map field.

**Intents:**

* Build a journey that targets subscribers of a specific list using a Read activity
* Override the default email address in the Email channel of an Action activity using the expression editor
* Use the `entry` and `firstEntryKey` functions to retrieve subscriber email addresses from a consent map
* Reference the Consent and Preference Details field group to access subscription list data

**Glossary:**

* **Email address override (parameter override)**: An Email channel setting of the journey Action activity that replaces the default profile email address with a custom expression, used for special cases such as subscription list targeting. *(product-specific)*
* **Consent and Preference Details field group**: An Adobe Experience Platform schema field group that contains subscription and consent data, including the subscriptions element; subscriber email addresses are defined as keys in the `subscribers` map, which is linked to the subscription list map. *(product-specific)*
* **`entry` function**: An expression function that refers to a map element by its namespace key — used here to reference a specific subscription list (e.g., `daily-email`). *(product-specific)*
* **`firstEntryKey` function**: An expression function that retrieves the first key of a map — used here to retrieve the first email address from the subscribers map of a subscription list. *(product-specific)*

**Guardrails:**

* Email address override should only be used for specific use cases such as subscription list targeting; in most cases the primary address defined in Execution fields should be used
* The example in this use case uses the Consent and Preference Details field group from Adobe Experience Platform
* In the example, the subscription list is named `daily-email`, and email addresses are defined as keys in the `subscribers` map

**Terminology:**

* Canonical name: Email address override — Acronym: none — variants: parameter override
* Do not confuse: "email address override" ≠ "primary email address" — The primary address defined in Execution fields is the one that should be used in most cases; the override replaces the default email address with an expression and is only for specific use cases such as subscription list targeting

**FAQ:**

* **Q: How do I send an email to a subscription list's subscribers rather than profile email addresses?** — Enable the parameter override on the Address field of the Email channel in the Action activity and enter an expression using `entry` and `firstEntryKey` functions to retrieve addresses from the subscribers map of the target subscription list.
* **Q: What field group is required for this use case?** — The example uses the Consent and Preference Details field group from Adobe Experience Platform, which includes the subscriptions element.
* **Q: Should I always use email address override when targeting subscribers?** — No; email address override is for specific use cases only. In most journeys, the primary address defined in Execution fields should be used.
* **Q: What does the `firstEntryKey` function do in this context?** — It retrieves the first email address key from the `subscribers` map associated with a specific subscription list.

+++
