---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure conditions within the Optimize activity in Journey Optimizer, covering five condition types — Data Source, Time, Percentage Split, Date, and Profile Cap — that route profiles to different journey paths based on rules, time, or audience membership.

**Intents:**
* Add a condition to a journey using the Optimize activity and select a condition method
* Create multiple branching paths and manage their priority order in the journey canvas
* Configure a Data Source condition using the expression editor to evaluate profile or event attributes
* Set up a Time condition to route profiles based on hour of day or day of week
* Apply a Profile Cap to limit the number of profiles routed down a specific path
* Use an audience membership check as a condition in a journey path

**Glossary:**
* **Optimize activity**: The current journey activity that replaces the former Condition activity; all conditional branching logic is now configured through its Method drop-down *(product-specific)*
* **Data source condition**: A condition method that evaluates fields from data sources or journey events using the expression editor *(product-specific)*
* **Percentage split**: A condition method that randomly distributes profiles across paths using a statistical Java random mechanism *(product-specific)*
* **Profile cap**: A condition method that routes profiles to an alternate path once a defined maximum count is reached on the nominal path *(product-specific)*
* **Nominal path**: The primary journey path associated with a Profile Cap condition; it always has priority over the alternate path *(product-specific)*

**Guardrails:**
* Condition evaluation fails for profiles with more than two cross-device identities in the Profile Store
* Schema fields with no ingested data are interpreted as null; isEmpty() and isNull() evaluate to true for such fields
* Time zone is defined at the journey level, not at the individual condition level
* The "Show path for other cases" option is not available in Percentage Split conditions
* Profile cap default is 1,000; counter resets on journey duplication or new version creation, but not between recurrences
* For caps above 10,000, inject at least 1.3x the cap; for caps below 10,000, inject at least 1,000 plus the cap
* Profile cap is not applied in test mode; in test mode, the top branch is always chosen for Percentage Split

**Terminology:**
* Canonical name: Conditions — Acronym: none — variants: condition activity, condition method, conditional branching
* Synonyms: "Optimize activity (Condition method)" = "former Condition activity"
* Do not confuse: "Percentage split" ≠ "Profile cap" (percentage split distributes all profiles statistically; profile cap stops routing to the nominal path after a count threshold)

**FAQ:**
* **Q: The Condition activity is gone from my UI — what replaced it?** — The Condition activity has been replaced by the Optimize activity. Select "Condition" from the Method drop-down to get the same behavior. Existing journeys with Condition activities continue to work and now display with an Optimize icon.
* **Q: When multiple paths are eligible for a profile, which path is taken?** — Only the first eligible path (highest on the canvas) is executed; you can reprioritize by reordering paths vertically.
* **Q: Why does my isEmpty() condition unexpectedly evaluate to true?** — If the schema field exists but no data has been ingested for it, Journey Optimizer interprets it as null, causing isEmpty() and isNull() to return true.
* **Q: Does the profile cap counter reset on a recurring journey?** — No, the counter does not reset between recurrences; it only resets when the journey is duplicated or a new version is created.
* **Q: Can I use an Adobe Experience Platform audience as a condition?** — Yes, drop an Optimize activity, select "Data source condition," add a path, and drag the audience from the Audiences node in the expression editor.

+++
