---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Update Profile activity to enrich or correct an existing Adobe Experience Platform profile with data from journey events, datasources, or static values as a customer progresses through a journey.

**Intents:**

* Configure the Update Profile activity to modify existing profile attributes during a journey
* Select a profile-enabled dataset dedicated to Update Profile actions
* Map field values from journey events, datasources, or static values to profile attributes
* Update multiple profile attributes (up to five) in a single activity
* Test profile updates in journey test mode

**Glossary:**

* **Update Profile activity**: An action activity that writes new values to existing fields in an Adobe Experience Platform profile in real time as a profile moves through a journey *(product-specific)*
* **Profile Store**: The Adobe Experience Platform store that holds real-time customer profile data, distinct from the Data Lake *(product-specific)*
* **Identity namespace**: A label that distinguishes identity contexts (e.g., email, CRM ID) used to match the profile being updated *(product-specific)*
* **Profile-enabled dataset**: An Adobe Experience Platform dataset configured to contribute records to the unified profile *(product-specific)*

**Guardrails:**

* The Update Profile action can only be used in journeys that have a namespace defined.
* The action only updates existing XDM fields; it cannot create new profile fields.
* Only simple field types are supported (string, number, boolean); enumerations, object arrays, and complex collections are not supported.
* The action cannot generate experience events such as purchases.
* Up to five field/value pairs can be updated in a single Update Profile action.
* Do not share the dedicated dataset with batch or streaming ingestion processes, as other ingestion runs will overwrite Update Profile changes.
* Profile updates may not be immediately available downstream in the same journey execution.
* The activity only updates the Profile Store, not the Data Lake.

**Terminology:**

* Canonical name: Update Profile — Acronym: none — variants: Update Profile activity, Update Profile action
* Synonyms: "Profile Store" = "Real-Time Customer Profile store"
* Do not confuse: "Profile Store" (updated by this activity) ≠ "Data Lake" (not updated by this activity)

**FAQ:**

* **Q: Can the Update Profile activity create new profile fields?** — No, it can only update fields that already exist in the selected XDM Profile schema.
* **Q: Why should I use a dedicated dataset for Update Profile actions?** — Sharing the dataset with batch or streaming ingestion can cause other ingestion runs to overwrite the changes made by the Update Profile activity.
* **Q: Are profile updates immediately visible to downstream activities in the same journey?** — No, updated values may not yet be reflected if an action reads the same field immediately after the Update Profile activity writes it.
* **Q: How many fields can I update in a single Update Profile action?** — Up to five field/value pairs can be configured in a single activity using the "Update another field" button.
* **Q: Do profile updates apply in test mode?** — Yes, in test mode the updates take effect immediately on the test profile and are not simulated.

+++
