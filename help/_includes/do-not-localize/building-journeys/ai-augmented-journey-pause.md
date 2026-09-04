---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to pause and resume a live journey in Adobe Journey Optimizer, including profile hold or discard behavior during the pause, how to apply profile attribute exit criteria while paused, and how to troubleshoot profile discards using Query Service.

**Intents:**
* Pause a live journey to prevent new profile entries and hold or discard in-flight profiles at the next action node
* Resume a paused journey manually or understand when it auto-resumes after the maximum pause period
* Apply a profile attribute exit criteria to exclude specific profiles (e.g., by country) when a journey is paused
* Bulk-pause or bulk-resume multiple live journeys from the journey inventory list
* Troubleshoot profile discards in a paused journey using Adobe Experience Platform Query Service step event queries
* View the audit trail of who paused or resumed a journey and when

**Glossary:**
* **Pause (journey)**: A state that temporarily suspends a live journey, preventing new entrances and halting profile progress at the next action node; no communications are sent while paused *(product-specific)*
* **Hold mode**: A pause option that keeps in-flight profiles waiting at the next action node until the journey resumes *(product-specific)*
* **Discard mode**: A pause option that exits in-flight profiles from the journey when they reach the next action node *(product-specific)*
* **Profile Attribute-based exit criteria**: A filter applied to a paused journey that excludes profiles matching a defined expression at the next action node upon resume *(product-specific)*
* **Bulk pause / Bulk resume**: The ability to pause or resume multiple live or paused journeys simultaneously from the journey inventory list *(product-specific)*

**Guardrails:**
* Only users with the **Publish journeys** permission can pause and resume journeys; stopping a paused journey requires **Manage journeys** (and **Campaigns > Publish Campaigns** if inline campaigns or messaging nodes are present)
* Pause duration is configurable from 1 to 14 days; after that the journey auto-resumes
* Profiles held during pause resume at up to 5,000 TPS; the journey remains in Resuming until all held profiles have resumed
* Maximum of 10 million profiles can be held across all paused journeys in an organisation; excess profiles are automatically discarded
* Only one Profile Attribute-based exit criteria can be set per journey
* Profile Attribute-based exit criteria can only be created, updated, or deleted while the journey is paused
* Paused journeys count towards the live journey quota
* Journey global timeout (91 days) still applies during a pause
* Inbound activity communications already triggered before the pause continue to be delivered; to stop them, the journey must be stopped entirely
* Alerts for batch segment do not fire in paused journeys
* Fresh entrances are always discarded when a journey is paused, regardless of Hold or Discard mode

**Terminology:**
* Canonical name: Pause a journey — Acronym: none — variants: journey pause, pause/resume
* Synonyms: "Hold" = "park profiles"; "Discard" = "exit profiles"
* Do not confuse: "Pause" ≠ "Stop" — Pause is temporary and allows resume; Stop immediately exits all profiles and cannot be undone to a live state
* Do not confuse: "Pause" ≠ "Close to new entrances" — Close to new entrances lets existing profiles finish but does not suspend them; Pause suspends all in-flight profiles at the next action node

**FAQ:**
* **Q: What happens to profiles already in a journey when it is paused?** — Depending on the option chosen at pause time, profiles are either held (waiting at the next action node) or discarded (exited from the journey at the next action node).
* **Q: How long can a journey remain paused?** — Between 1 and 14 days (chosen at pause time); after that it automatically resumes.
* **Q: Can I exclude certain profiles while a journey is paused?** — Yes; apply a Profile Attribute-based exit criteria (one per journey) while the journey is paused to exclude matching profiles at the next action node upon resume.
* **Q: Does pausing a journey stop in-app or web messages already triggered?** — No; inbound communications already triggered before the pause continue to be delivered. To stop all inbound communications, you must stop the journey entirely.
* **Q: How do I find out which profiles were discarded during a pause?** — Query the `journey_step_events` dataset in Adobe Experience Platform Query Service using the `PAUSED_JOURNEY_VERSION` or `JOURNEY_IN_PAUSED_STATE` event type filters with the journey version ID.

+++
