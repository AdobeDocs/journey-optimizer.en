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
* **stepEvent**: Journey step events; Journey Dry run generates stepEvents that have a specific flag, `inDryRun`, and a Dry run ID, `dryRunID` *(product-specific)*
* **inDryRun flag**: A flag on stepEvents that is `true` for Dry run executions and `null` for live or test journeys *(product-specific)*

**Guardrails:**
* The Dry run capability can be used in any Draft journey with no error
* Starting a Dry run requires the **Publish journeys** permission; stopping it requires **Manage journeys**
* Dry run journeys automatically exit Dry run mode and return to Draft status after 14 days.
* Profiles in Dry run mode are counted towards Engageable Profiles; journeys in Dry run mode are counted towards the live journey quota
* Channel action nodes (Email, SMS, Push) are not executed during Dry run; Custom actions are disabled and their responses are set to null
* Data sources (including external data sources) and Wait activities are disabled by default during Dry run; this behavior can be changed when activating the Dry run mode
* Jump actions are not enabled in Dry run
* Reaction nodes are not executed during Dry run; profiles exit successfully, with priority rules for parallel unitary and reaction branches
* Reporting data is only available while the Dry run is active; once stopped, the data is no longer accessible
* Dry run journeys do not impact business rules
* For journeys using a **Read Audience** activity with a scheduled time (daily, weekly, or monthly), the Dry run does not follow the configured journey schedule — the schedule is anchored to the moment Dry run was activated (e.g. journey set to 10 AM, Dry run activated at 8 AM → all reads during Dry run execute at 8 AM)

**Terminology:**
* Canonical name: Journey Dry run — Acronym: none — variants: Dry run mode, Dry run publication
* Do not confuse: "Dry run" mode ≠ "Draft" status — a journey enters Dry run mode from a Draft journey and transitions to Draft status after 14 days or when stopped manually
* Do not confuse: "Dry run" ≠ "Journey Simulation" ≠ "Journey Test mode" — the page states that, unlike Journey Simulation and Journey Test mode, Dry run uses the real production audience without contacting anyone; the page links to a comparison of all three validation options
* Do not confuse: "inDryRun" ≠ "dryRunID" — `inDryRun` is the flag that is `true` for Dry run executions; `dryRunID` is the ID of the Dry run instance

**FAQ:**
* **Q: Does Dry run actually send emails or push notifications to customers?** — No; channel action nodes (Email, SMS, Push) are not executed, and custom actions are disabled with their responses set to null.
* **Q: How long does a Dry run last before it automatically stops?** — 14 days, after which the journey automatically transitions back to Draft status.
* **Q: How do I exclude Dry run data from my journey reporting metrics?** — When analyzing journey reporting metrics with Query service, exclude step events where `inDryRun` is `true`; include only events where `inDryRun` is `null` or `false`.
* **Q: Do Dry run profiles and journeys count towards quotas?** — Yes; profiles in Dry run mode are counted towards Engageable Profiles, and journeys in Dry run mode are counted towards the live journey quota.
* **Q: Can I enable Wait activities and external data source calls during a Dry run?** — Both are disabled by default, but you can choose to enable or disable them when activating the Dry run.
* **Q: Does Dry run respect the scheduled execution time configured in a Read Audience journey?** — No. The Dry run anchors the schedule to the activation time, not the configured journey time. If the journey is set to run at 10 AM but Dry run is activated at 8 AM, all scheduled reads during Dry run execute at 8 AM.

+++

<!-- ai-section-version: 2 | source-hash: 8c8ab63f -->
