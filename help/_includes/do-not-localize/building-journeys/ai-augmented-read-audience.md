---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use the Read Audience activity in Adobe Journey Optimizer to add profiles from an Adobe Experience Platform audience into a journey, either once or on a recurring schedule, with guidance on scheduling, throughput, troubleshooting, and best practices.

**Intents:**
* Configure a Read Audience entry point with an Adobe Experience Platform audience and identity namespace
* Set the reading rate to control how many profiles enter per second
* Schedule a journey to run once or on a recurring schedule
* Enable Incremental read to process only new audience members on recurring runs
* Troubleshoot audience count mismatches, zero-profile runs, and delayed entries
* Decide between Read Audience and Audience Qualification based on batch vs. real-time needs

**Glossary:**
* **Read Audience activity**: The journey entry-point activity that reads all qualified profiles from a selected Adobe Experience Platform audience and adds them to the journey *(product-specific)*
* **Reading rate**: The maximum number of profiles that can enter per second through this activity (500–20,000; default 5,000 profiles per second) *(product-specific)*
* **Incremental read**: A recurring journey option that selects newly added audience profiles after the first run; it is not functionally supported for custom upload and other external audiences *(product-specific)*
* **Force reentrance on recurrence**: A scheduling option that removes all active journey participants before each new run so profiles can re-enter fresh *(product-specific)*
* **Trigger after batch audience evaluation**: For daily journeys targeting batch audiences, an option that waits for fresh batch audience data within a configured window of up to 6 hours; if no fresher batch is found, that occurrence is skipped *(product-specific)*
* **Supplemental identifier**: A secondary identifier (e.g., order ID) that allows the same profile to enter the journey multiple times when the identifier differs *(product-specific)*

**Guardrails:**
* Configuration validation must pass before activating test mode. Publication requires successful tests and current, passed validation; changes after validation require **[!UICONTROL Validate]** again and resolution of errors before continuing.
* Only one Read Audience activity is allowed per journey, and it must be the first activity.
* Only one audience can be selected per Read Audience activity.
* Up to five concurrent Read Audience runs per organization.
* Maximum reading rate is 20,000 profiles per second per sandbox (hard limit; sum of all concurrent Read Audience activities).
* Reading rate is limited to 500 profiles per second per journey instance (hard limit) when a supplemental identifier is used.
* Only profiles with Realized audience participation status enter the journey.
* Only people-based identity namespaces are available; profiles without the selected namespace cannot enter.
* Read Audience has a 12-hour job timeout.
* Retries for export job creation failures occur every 10 minutes for up to 1 hour (hard limit).
* For custom upload and other external audiences, including Federated Audience Composition, the entire audience is processed on every recurrence regardless of the Incremental read setting.
* Force reentrance on recurrence clears active participation but does not disable Incremental read or automatically make removed profiles new audience members.

**Terminology:**
* Canonical name: Read Audience. Variants in APIs and technical references: segment-trigger, audience-based journey entry.
* Do not confuse: audience-triggered journeys can start with Read Audience or Business Event; the term is not a synonym for the Read Audience activity alone.
* Do not confuse: "Read Audience" ≠ "Audience Qualification" (Read Audience is batch/scheduled; Audience Qualification is real-time streaming)

**FAQ:**
* **Q: When should I use Read Audience instead of Audience Qualification?** — Use Read Audience for batch, scheduled use cases (e.g., weekly newsletters, re-engagement campaigns). Use Audience Qualification when profiles must enter the journey immediately as they qualify in real time.
* **Q: Why are fewer profiles entering the journey than the audience size?** — Common causes include profiles not having the selected namespace, incomplete batch segmentation or snapshot updates, or profiles not being in Realized status. For daily journeys targeting batch audiences, consider "Trigger after batch audience evaluation" and check namespace configuration.
* **Q: What does Incremental read do on the first run?** — On the first execution, all audience profiles enter. On subsequent runs, only newly added profiles are selected, with a default look-back of 24 hours from the last audience evaluation job. With Trigger after batch audience evaluation, the look-back extends to the last successful journey execution. Custom upload and other external audiences are processed in full on every recurrence instead.
* **Q: What happens if export job creation fails?** — The system retries every 10 minutes for up to 1 hour (hard limit). Failures are reported in Alerts. After 1 hour without success, the run is considered failed.
* **Q: Can the same profile enter a Read Audience journey multiple times?** — A supplemental identifier allows multiple entrances when its value differs. Force reentrance on recurrence removes active participants before the next run, but does not make them newly added audience members for Incremental read.
* **Q: How long does a one-shot Read Audience journey remain live?** — It auto-stops to Stopped when the last profile exits, unless the journey includes Wait, Reaction, or event-triggered transitions — in which case the 91-day global timeout applies. It does not remain Live until Finished at 91 days by default.

+++

<!-- ai-section-version: 1 | source-hash: 8d2a404e -->
