---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains Journey Dry run, a special publication mode that lets practitioners test a journey using real production data without contacting customers or modifying profiles, and covers how to start, monitor, stop, and filter Dry run step events.

**Intents:**
* Activate Dry run mode on a Draft journey to validate audience reach and branch logic with real production data
* Monitor journey execution metrics in the canvas during a Dry run
* Stop a Dry run manually and return the journey to Draft status
* Filter Dry run step events out of reporting queries using the `inDryRun` flag
* Understand which activities are disabled or simulated during a Dry run

**Glossary:**
* **Dry run**: A special journey publication mode that executes the journey against real production data without sending any communications or updating profile information *(product-specific)*
* **stepEvent**: An automatically generated dataset record capturing every step a profile takes in a journey; Dry run step events carry `inDryRun=true` and a `dryRunID` *(product-specific)*
* **inDryRun flag**: A boolean field on stepEvents that is `true` for Dry run executions and `null` for live or test journeys *(product-specific)*

**Guardrails:**
* Only Draft journeys with no errors can be activated in Dry run mode
* Starting a Dry run requires the **Publish journeys** permission; stopping it requires **Manage journeys**
* Dry run journeys automatically exit Dry run mode and return to Draft status after 14 days. No journey content is lost; only the Dry run session ends.
* Profiles processed during a Dry run are counted towards Engageable Profiles and the live journey quota
* Channel action nodes (Email, SMS, Push) and Custom actions are not executed during Dry run
* Jump actions are not enabled in Dry run
* Reaction nodes are not executed during Dry run; profiles exit successfully, with priority rules for parallel unitary and reaction branches
* Reporting data is only available while the Dry run is active; once stopped, the data is no longer accessible
* Dry run journeys do not impact business rules
* For journeys using a **Read Audience** activity with a scheduled time (daily, weekly, or monthly), the Dry run does not follow the configured journey schedule — the schedule is anchored to the moment Dry run was activated (e.g. journey set to 10 AM, Dry run activated at 8 AM → all reads during Dry run execute at 8 AM)

**Terminology:**
* Canonical name: Journey Dry run — Acronym: none — variants: dry run mode, Dry run publication mode
* Synonyms: "Dry run" = "smoke test" (informally)
* Do not confuse: "Dry run" ≠ "Test mode" ≠ "Simulation" — Dry run uses real production data and counts toward Engageable Profiles and live journey quota; Test mode uses persistent AEP test profiles in a draft journey; Simulation uses temporary simulated users that do not persist in AEP

**FAQ:**
* **Q: Does Dry run actually send emails or push notifications to customers?** — No; all channel action nodes and custom actions are disabled and not executed during a Dry run.
* **Q: How long does a Dry run last before it automatically stops?** — 14 days, after which the journey automatically transitions back to Draft status.
* **Q: How do I exclude Dry run data from my journey analytics queries?** — Filter out step events where `inDryRun` is `true`; include only events where `inDryRun` is `null` or `false`.
* **Q: Are profiles counted against any limits during a Dry run?** — Yes; profiles are counted towards Engageable Profiles and the Dry run journey is counted towards the live journey quota.
* **Q: Can I enable Wait activities and external data source calls during a Dry run?** — Both are disabled by default, but you can choose to enable or disable them when activating the Dry run.
* **Q: Does Dry run respect the scheduled execution time configured in a Read Audience journey?** — No. The Dry run anchors the schedule to the activation time, not the configured journey time. If the journey is set to run at 10 AM but Dry run is activated at 8 AM, all scheduled reads during Dry run execute at 8 AM.

+++
