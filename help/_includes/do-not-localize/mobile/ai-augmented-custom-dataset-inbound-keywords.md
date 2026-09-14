---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to store inbound SMS keywords in a profile-enabled custom dataset by creating an Adobe Experience Platform Experience Event schema and a dataset from it, then referencing that dataset in the Journey Optimizer SMS API credentials.

**Intents:**

* Create an Experience Event schema enabled for Profile with the required field groups
* Create a dataset from that schema and enable it for Profile
* Reference the custom dataset in the SMS API credentials so inbound keywords are recorded in it
* Understand where inbound keywords are stored when no custom dataset is configured

**Glossary:**

* **Custom dataset for inbound**: A profile-enabled dataset where inbound SMS keywords for a credential are recorded, selected through the Use custom dataset for inbound option in the SMS API credentials *(product-specific)*
* **Schema**: A structure that defines the validation rules applied to ingested data; here an Experience Event schema enabled for Profile *(product-specific)*
* **Dataset**: The storage container for ingested data, associated with exactly one schema *(product-specific)*
* **AJO Email Tracking Dataset**: The system dataset where inbound keywords are stored by default when no custom dataset is configured *(product-specific)*

**Guardrails:**

* The schema must be an Experience Event schema enabled for Profile and include the field groups Adobe CJM ExperienceEvent - Message interaction details, Adobe CJM ExperienceEvent - Message Execution Details, and Adobe CJM ExperienceEvent - Message Profile Details.
* Each dataset is associated with exactly one schema, and records written must conform to that schema.
* The dataset must be enabled for Profile.
* If no custom dataset is configured, inbound keywords are stored in the system AJO Email Tracking Dataset, and a profile must have at least one message sent from Journey Optimizer before incoming messages are captured in it.
* Upon saving API credentials, Journey Optimizer validates that the inbound keyword dataset is configured correctly; if validation fails, an error message indicates the required correction.

**Terminology:**

* Canonical name: Use custom dataset for inbound — Acronym: n/a — variants: custom dataset for inbound keywords, custom inbound dataset
* Do not confuse: "custom dataset for inbound" (a dataset you create and select) ≠ "AJO Email Tracking Dataset" (the default system dataset used when none is configured)

**FAQ:**

* **Q: Where are inbound keywords stored if I do not configure a custom dataset?** — They are stored in the system AJO Email Tracking Dataset by default.
* **Q: Which field groups must the schema include?** — Adobe CJM ExperienceEvent - Message interaction details, Adobe CJM ExperienceEvent - Message Execution Details, and Adobe CJM ExperienceEvent - Message Profile Details.
* **Q: How do I point a credential to the custom dataset?** — In the SMS API credentials, enable the Use custom dataset for inbound option and select the dataset you created.
* **Q: What happens after the credentials are saved?** — Journey Optimizer validates the inbound keyword dataset; outbound and inbound messaging behavior is unchanged and inbound keywords for that credential are recorded in the selected custom dataset.

+++

<!-- ai-section-version: 1 | source-hash: aa7dfc23 -->
