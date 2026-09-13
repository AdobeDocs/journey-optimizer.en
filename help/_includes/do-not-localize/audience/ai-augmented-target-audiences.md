---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to target Adobe Experience Platform audiences in Journey Optimizer campaigns and journeys, the activation delays that apply, and the guardrails for different audience types.

**Intents:**

* Target Adobe Experience Platform audiences in campaigns and journeys
* Understand activation delays for ingested, composition, and batch-segmentation audiences
* Use a Read audience, Optimize, or Audience Qualification activity in a journey
* Understand which audience types can be targeted directly and how to wrap unsupported audiences
* Apply guardrails for custom upload and Federated Audience Composition audiences

**Glossary:**

* **Read audience activity**: A journey orchestration activity that makes all individuals in an audience enter the journey and receive its messages *(product-specific)*
* **Audience Qualification event activity**: A journey event activity that makes individuals enter or move forward based on Adobe Experience Platform audience entrances and exits *(product-specific)*
* **Optimize activity**: A journey activity used to build conditions based on audience membership *(product-specific)*
* **Federated Audience Composition**: One of the audience sources that can be targeted in Journey Optimizer *(product-specific)*
* **execution field**: The channel-configuration field (or "execution address" depending on the channel) that can be set to 'identityMap' so the attribute chosen as the identity at audience creation is used for targeting *(product-specific)*

**Guardrails:**

* Preview and proof are not supported for audiences created using CSV custom upload or Federated Audience Composition.
* For custom upload and Federated Audience Composition, when no match is found between a record and a Unified Profile Service profile a new empty profile is created; standard targeting fields (for example personalEmail.address, mobilePhone.number) are empty and cannot be used for targeting unless the execution field is set to 'identityMap'.
* Every record in a custom upload or Federated Audience Composition audience is activated, including duplicates, so the number of activated records may differ from the number of profiles after identity stitching.
* The use of audiences and attributes from audience composition is currently unavailable with Healthcare Shield or Privacy and Security Shield.
* Audiences are ready for use right after ingestion completes, typically within one hour but subject to variability; audiences resulting from compositions should be available 24 hours after publishing.
* For Read-audience journeys scheduled daily, if the segmentation job does not complete within the defined time window, the journey is skipped until its next occurrence.
* You cannot target audiences created using composition workflows, custom upload, or Federated Audience Composition in an Audience Qualification activity; only audiences created using segment definitions can be used there.
* Only audiences generated using segment definition, audience compositions, custom upload (CSV file), and Federated audience composition can be targeted directly in journeys and campaigns; a non-supported audience (such as a Customer Journey Analytics audience) must be wrapped in a new segment definition in the Audience portal.

**Terminology:**

* Canonical name: Read audience activity — Acronym: n/a — variants: Read audience, Read-audience journey
* Synonyms: "custom upload" = "CSV upload"
* Do not confuse: "Read audience activity" (makes all individuals in an audience enter the journey) ≠ "Audience Qualification event activity" (makes individuals enter or move forward based on audience entrances and exits)
* Do not confuse: "segment definition" audiences (usable in an Audience Qualification activity) ≠ "composition workflow / custom upload / Federated Audience Composition" batch audiences (cannot be targeted in an Audience Qualification activity)

**FAQ:**

* **Q: Which audiences can I target in Journey Optimizer campaigns and journeys?** — Audiences generated using segment definitions, custom upload, composition workflows, or Federated Audience Composition.
* **Q: How long after ingestion can I use an audience?** — Right after ingestion completes, typically within one hour but subject to variability; composition audiences should be available 24 hours after publishing.
* **Q: Why can I not preview or proof a custom upload or Federated Audience Composition audience?** — Preview and proof are currently not supported for audiences created using CSV upload or Federated Audience Composition.
* **Q: Can I use a composition or custom upload audience in an Audience Qualification activity?** — No; due to their batch nature only audiences created using segment definitions can be leveraged in that activity.
* **Q: How do I target a non-supported audience such as a Customer Journey Analytics audience?** — Wrap it in a new segment definition in the Audience portal, then wait for the segmentation evaluation to complete before using it.

+++

<!-- ai-section-version: 1 | source-hash: 6075edc3 -->
