---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use the Audience Qualification event activity in Journey Optimizer to trigger or advance profiles in a journey when they enter or exit an Adobe Experience Platform audience.

**Intents:**
* Configure an Audience Qualification event activity to trigger journey entry on audience membership changes
* Select the correct behavior (entrance, exit, or both) for an Audience Qualification activity
* Apply best practices to avoid overloading systems when using batch or streaming audiences
* Understand why some qualified profiles may not enter the journey and how to mitigate this
* Use the AudienceQualification node payload in downstream conditions and actions

**Glossary:**
* **Audience Qualification event**: A journey event activity that listens for profile entrances into or exits from an Adobe Experience Platform audience and triggers journey progression *(product-specific)*
* **Behaviour (Enter/Exit)**: The setting that controls whether the journey reacts to profiles joining ("Realized"), leaving ("Exited"), or both states of an audience *(product-specific)*
* **Streaming audience**: An audience evaluated continuously in real time using the High Frequency Audiences option; recommended for Audience Qualification activities *(product-specific)*
* **Batch audience**: An audience recalculated once per day; introduces a daily peak of profile entries and requires a 2-hour readiness window after segmentation job completion *(product-specific)*
* **AudienceQualification node**: The context node available in the expression editor after an Audience Qualification activity, exposing last qualification time and status *(product-specific)*
* **Edge-to-Hub propagation**: The process by which a streaming segment membership evaluated at the Edge is synced to Hub before the journey can act on it; typically takes 15–30 minutes *(product-specific)*

**Guardrails:**
* A new Audience Qualification journey takes up to 10 minutes to become active after publishing
* Batch or streaming audiences using batch-ingested attributes become ready approximately 2 hours after the segmentation job completes
* Only audiences created using segment definitions can be used; composition workflow or custom upload audiences are not supported
* Experience event field groups cannot be used in journeys starting with Audience Qualification
* Only people-based identity namespaces are available for the namespace field; lookup table namespaces are not supported
* Profiles already in the audience before journey publication will not retroactively enter the journey
* Edge-to-Hub propagation for streaming segments typically takes 15–30 minutes

**Terminology:**
* Canonical name: Audience Qualification event — Acronym: none — variants: segment qualification, audience qualification activity
* Synonyms: "Enter" = "Realized" ; "Exit" = "Exited"
* Do not confuse: "Audience Qualification" ≠ "Read Audience" (Audience Qualification reacts to real-time membership changes; Read Audience processes all members at a scheduled time)

**FAQ:**
* **Q: When does a newly published Audience Qualification journey start processing entries?** — It takes up to 10 minutes after publication for the activity to become active and start listening for profile entries and exits.
* **Q: Why are profiles not entering my Audience Qualification journey?** — Common causes include: profiles were already in the audience before publishing, the 10-minute activation window has not elapsed, or the Edge-to-Hub propagation (15–30 min) for streaming segments has not completed yet.
* **Q: Can I use a batch audience in an Audience Qualification activity?** — Yes, but it is not recommended. Batch audiences generate a daily entry peak and are not suited for real-time use cases; use a Read Audience activity instead for batch scenarios.
* **Q: What data is available in the AudienceQualification payload?** — The payload includes the behavior (entrance or exit), the timestamp of qualification, and the audience ID.
* **Q: Can I use audiences created from composition workflows in an Audience Qualification activity?** — No, only audiences created using segment definitions are supported in this activity.

+++
