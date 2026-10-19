---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create data governance policies that link labels to marketing actions and apply them to journeys, campaigns, and custom actions so restricted fields cannot be shared externally.

**Intents:**

* Create labels and apply them to profile attribute fields through Schemas
* Create marketing actions for each channel and third-party custom action
* Create a data governance policy that links a label to a marketing action
* Apply marketing actions to channel configurations and to custom actions
* Detect and interpret a data governance policy violation

**Glossary:**

* **Data governance policy**: A policy that links a label and a marketing action so that fields carrying that label cannot be used for the associated action *(product-specific)*
* **Label**: A tag applied to fields to restrict their usage, created under Privacy Policies *(product-specific)*
* **Marketing action**: A configurable element created per channel and per third-party custom action that governance policies are attached to *(product-specific)*
* **Required marketing action**: The marketing action defined when configuring a custom action, prefilled from the selected Channel and not editable in the journey *(product-specific)*
* **Additional marketing action**: A marketing action defined when adding a custom action to a journey to set the purpose of the custom action in that particular journey *(product-specific)*
* **Data lineage diagram**: The diagram in the policy violation dialog used to understand what configuration changes are needed before activation *(product-specific)*

**Guardrails:**

* DULE policy enforcement only applies to profile attributes; event-based fields (context attributes) such as journey event fields are not supported, and labels applied to them have no effect.
* Labels can only be applied to profile attribute fields.
* When applying a marketing action to custom actions, Campaign v7/v8 and Campaign Standard journey actions are not supported.
* If the system identifies a restricted field in a journey, campaign, or custom action, an error is displayed that prevents you from publishing it.
* When both are set, the required marketing action and the additional marketing action both apply.

**Terminology:**

* Canonical name: Data governance policy — Acronym: DULE (Data Usage Labelling and Enforcement) — variants: data governance, governance policy
* Synonyms: "labelling fields" = "applying labels to fields"
* Do not confuse: "Required marketing action" (defined on the custom action, read-only in the journey) ≠ "Additional marketing action" (defined per journey to set the purpose of the custom action)
* Do not confuse: "label" (tag on a field) ≠ "marketing action" (element the label is linked to in a policy)

**FAQ:**

* **Q: Why does a label on a journey event field not restrict data usage?** — DULE policy enforcement only applies to profile attributes; labels applied to event-based fields have no effect.
* **Q: How is a data governance policy created?** — From the Browse tab, click Create policy, select Data governance policy, then choose a label and a marketing action to link.
* **Q: Where are marketing actions applied for journeys and campaigns?** — In the Marketing action field of a channel configuration under Channels General settings Channel configurations.
* **Q: Can a marketing action be applied to Campaign v7/v8 or Campaign Standard actions?** — No, those journey actions are not supported when applying a marketing action to custom actions.
* **Q: How is a policy violation detected?** — An error prevents publishing and is visible from the Alerts button; selecting it shows details and a data lineage diagram.

+++

<!-- ai-section-version: 1 | source-hash: dcc19649 -->
