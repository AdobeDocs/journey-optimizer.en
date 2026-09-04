---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use the Read Audience activity in Adobe Journey Optimizer to add profiles from an Adobe Experience Platform audience into a journey, either once or on a recurring schedule, with guidance on scheduling, throughput, troubleshooting, and best practices.

**Intents:**
* Configure a Read Audience activity as the entry point of a journey
* Select an Adobe Experience Platform audience and identity namespace for the journey
* Set the reading rate to control how many profiles enter per second
* Schedule a journey to run once, daily, weekly, or on a custom recurrence
* Enable Incremental read to process only new audience members on recurring runs
* Troubleshoot audience count mismatches, zero-profile runs, and delayed entries
* Decide between Read Audience and Audience Qualification based on batch vs. real-time needs

**Glossary:**
* **Read Audience activity**: The journey entry-point activity that reads all qualified profiles from a selected Adobe Experience Platform audience and adds them to the journey *(product-specific)*
* **Reading rate**: The maximum number of profiles that can enter the journey per second (500–20,000; default 5,000) *(product-specific)*
* **Incremental read**: A recurring journey option that processes only profiles newly added to the audience since the last journey execution *(product-specific)*
* **Force reentrance on recurrence**: A scheduling option that removes all active journey participants before each new run so profiles can re-enter fresh *(product-specific)*
* **Trigger after batch audience evaluation**: A scheduling option that delays journey execution until a fresh batch audience snapshot is available (up to 6 hours) *(product-specific)*
* **Supplemental identifier**: A secondary identifier (e.g., order ID) that allows the same profile to enter the journey multiple times when the identifier differs *(product-specific)*

**Guardrails:**
* Only one Read Audience activity is allowed per journey, and it must be the first activity.
* Only one audience can be selected per Read Audience activity.
* Up to five concurrent Read Audience runs per organization.
* Maximum reading rate is 20,000 profiles per second per sandbox (sum of all concurrent Read Audience activities).
* Reading rate is limited to 500 profiles per second when a supplemental identifier is used.
* Only profiles with Realized audience participation status enter the journey.
* Only people-based identity namespaces are available; profiles without the selected namespace cannot enter.
* The 12-hour job timeout applies to Read Audience export jobs.
* Retries for failed export jobs occur every 10 minutes for up to 1 hour.
* For custom upload audiences with Incremental read enabled, profiles are only retrieved on the first recurrence (these audiences are fixed).
* Scale the Winner is not available for Read Audience journeys (path experimentation).

**Terminology:**
* Canonical name: Read Audience — Acronym: none — variants: segment-trigger, audience-based journey entry, Read Segment (legacy API name)
* Synonyms: "Read Audience" = "segment trigger" = "audience-triggered journey"
* Do not confuse: "Read Audience" ≠ "Audience Qualification" (Read Audience is batch/scheduled; Audience Qualification is real-time streaming)

**FAQ:**
* **Q: When should I use Read Audience instead of Audience Qualification?** — Use Read Audience for batch, scheduled use cases (e.g., weekly newsletters, re-engagement campaigns). Use Audience Qualification when profiles must enter the journey immediately as they qualify in real time.
* **Q: Why are fewer profiles entering the journey than the audience size?** — Common causes include profiles not having the selected namespace, batch segmentation jobs not yet completed before the journey ran, or profiles not being in Realized status. Enable "Trigger after batch audience evaluation" and check namespace configuration.
* **Q: What does Incremental read do on the first run?** — On the first execution, all audience profiles enter. On subsequent runs, only profiles newly added to the audience since the last execution are processed.
* **Q: What happens if the export job fails?** — The system retries every 10 minutes for up to 1 hour. Failures are reported in Alerts. After 1 hour without success, the run is considered failed.
* **Q: Can the same profile enter a Read Audience journey multiple times?** — Yes, if a supplemental identifier is configured and differs between entries, or if Force reentrance on recurrence is enabled. Without these, a profile cannot be present multiple times at the same time.
* **Q: How long does a one-shot Read Audience journey remain live?** — It auto-stops to Stopped when the last profile exits, unless the journey includes Wait, Reaction, or event-triggered transitions — in which case the 91-day global timeout applies. It does not remain Live until Finished at 91 days by default.

+++
