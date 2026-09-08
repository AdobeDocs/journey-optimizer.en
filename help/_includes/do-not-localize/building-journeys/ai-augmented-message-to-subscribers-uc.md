---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page shows how to build a journey that sends an email to subscribers of a list by overriding the default email address parameter using an expression that reads subscriber addresses from a consent map field.

**Intents:**

* Build a journey that targets subscribers of a specific list using a Read Audience activity
* Override the default email address in an Email action activity using the expression editor
* Use the `entry` and `firstEntryKey` functions to retrieve subscriber email addresses from a consent map
* Reference the Consent and Preference Details field group to access subscription list data

**Glossary:**

* **Email address override (parameter override)**: A journey Email activity setting that replaces the default profile email address with a custom expression, used for special cases such as subscription list targeting. *(product-specific)*
* **Consent and Preference Details field group**: An Adobe Experience Platform schema field group that contains subscription and consent data, including the `subscriptions` map used to store subscriber email addresses. *(product-specific)*
* **`entry` function**: An expression function that refers to a map element by its namespace key — used here to reference a specific subscription list (e.g., `daily-email`). *(product-specific)*
* **`firstEntryKey` function**: An expression function that retrieves the first key of a map — used here to retrieve the first email address from the subscribers map of a subscription list. *(product-specific)*

**Guardrails:**

* Email address override should only be used for specific use cases such as subscription list targeting; in most cases the primary address defined in Execution fields should be used
* The Consent and Preference Details field group must be present in the schema for this use case to work
* The subscription list name used in the expression (e.g., `daily-email`) must match exactly the name configured in the data

**Terminology:**

* Canonical name: Email address override — Acronym: none — variants: parameter override, email parameter override
* Synonyms: "subscription list" = "subscriber list"
* Do not confuse: "email address override" ≠ "primary email address" — The primary email address is the default address used in all journeys; the override is a per-activity expression used only for special cases like subscription list sending

**FAQ:**

* **Q: How do I send an email to a subscription list's subscribers rather than profile email addresses?** — Enable the parameter override on the Address field of the Email activity and enter an expression using `entry` and `firstEntryKey` functions to retrieve addresses from the subscribers map of the target subscription list.
* **Q: What field group is required for this use case?** — The Consent and Preference Details field group from Adobe Experience Platform, which contains the `subscriptions` map structure used to store subscriber email addresses.
* **Q: Should I always use email address override when targeting subscribers?** — No; email address override is for specific use cases only. In most journeys, the primary address defined in Execution fields should be used.
* **Q: What does the `firstEntryKey` function do in this context?** — It retrieves the first email address key from the `subscribers` map associated with a specific subscription list, enabling the journey to address individual subscribers.

+++
