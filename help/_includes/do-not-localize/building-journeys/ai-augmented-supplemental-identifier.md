---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use supplemental identifiers in Adobe Journey Optimizer journeys to allow a single profile to have multiple concurrent journey instances, each scoped to a distinct secondary ID such as a booking, subscription, or policy ID.

**Intents:**
* Understand when and why to use a supplemental identifier instead of relying solely on a profile ID
* Configure a supplemental identifier in an event-triggered journey by marking an attribute as an identity in the event schema
* Configure a supplemental identifier in a Read audience journey by enabling the option in the Read audience activity
* Reference supplemental identifier attributes for message personalization and conditional logic using the expression editor
* Apply the correct expression syntax to iterate over object arrays keyed by a supplemental ID
* Identify guardrails and limitations before implementing supplemental identifiers in a journey

**Glossary:**
* **Supplemental identifier**: A secondary identifier (e.g., order ID, booking ID, subscription ID) used alongside the profile ID to scope a journey instance to a specific record, enabling multiple concurrent instances per profile *(product-specific)*
* **Profile ID**: The primary identifier used by default to execute journeys; a profile active in a journey cannot re-enter another journey without a supplemental ID
* **Non-person identifier namespace**: An identity namespace that does not represent a person (required for supplemental IDs); must be distinct from the primary identity namespace
* **joai namespace**: Not applicable to this page (see inbound actions troubleshooting)
* **DULE**: Data Use Labelling and Enforcement — the data governance policy validation framework in Adobe Experience Platform; supplemental IDs are not subject to DULE checks

**Guardrails:**
* Supplemental identifiers are supported only for event-triggered and Read audience journeys; not supported for Audience qualification journeys
* A profile cannot have more than 10 concurrent journey instances
* Each journey instance counts toward frequency capping even when created via supplemental identifiers
* The supplemental identifier must be of type `string`; string arrays and maps are not supported
* The supplemental ID attribute must not be marked as Primary identity in the schema
* The namespace used for the supplemental ID must be a non-person identifier namespace
* After applying the non-person identity namespace to a schema, a new event or field group must be created; existing entities cannot be refreshed
* For Read audience journeys with supplemental IDs: the reading rate is limited to 500 profiles per second per journey instance; only Unified Profile Service audiences are supported; supplemental ID must be a profile field (not an event/context field)
* Downstream events in the same journey must use the same supplemental ID and namespace
* Supplemental ID is disabled for Read audience journeys that use a business event

**Terminology:**
* Canonical name: Supplemental identifier — Acronym: none — variants: supplemental ID, secondary identifier
* Synonyms: "supplemental identifier" = "supplemental ID" (used interchangeably in the UI and documentation)
* Do not confuse: "supplemental identifier" ≠ "primary identity" — the supplemental ID must never be marked as the primary identity in the schema

**FAQ:**
* **Q: What is a supplemental identifier used for?** — It allows a single profile to enter and execute a journey multiple times simultaneously, with each instance scoped to a different secondary record such as a booking, subscription, or policy ID.
* **Q: Which journey types support supplemental identifiers?** — Event-triggered journeys and Read audience journeys. Audience qualification journeys do not support supplemental identifiers.
* **Q: How many concurrent journey instances can a profile have with supplemental identifiers?** — A maximum of 10 concurrent journey instances per profile.
* **Q: Can I use the supplemental ID attributes for message personalization?** — Yes. Reference them via the Contextual attributes menu in the expression editor or personalization editor.
* **Q: Does the supplemental ID need to be marked as a Primary identity in the schema?** — No. It must be marked as an Identity but must not be set as the Primary identity.
* **Q: Are DULE governance policies applied to the supplemental identifier?** — No. DULE validation checks are not performed on the supplemental ID.

+++
