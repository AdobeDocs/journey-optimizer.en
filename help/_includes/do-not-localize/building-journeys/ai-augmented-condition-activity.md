---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes the Condition activity in Journey Optimizer, covering the five available condition types — Data Source, Time, Percentage Split, Date, and Profile Cap — and how to route profiles to different journey paths based on rules, data, or audience membership.

**Intents:**
* Add a Condition activity to a journey and create multiple branching paths
* Configure a Data Source condition using the expression editor to evaluate profile or event attributes
* Set up a Time condition to route profiles based on time of day or day of week
* Use a Percentage Split to randomly distribute profiles across paths
* Apply a Profile Cap to limit the number of profiles taking a specific journey path
* Use an audience membership check as a condition in a journey path

**Glossary:**
* **Condition activity**: A journey activity that evaluates rules and routes profiles to different paths based on the result *(product-specific)*
* **Data Source condition**: A condition type that evaluates fields from data sources or journey events using the expression editor *(product-specific)*
* **Time condition**: A condition type that filters profiles based on the hour of day, day of week, or a combination of both *(product-specific)*
* **Percentage split**: A condition type that randomly distributes profiles across paths using a statistical Java random mechanism *(product-specific)*
* **Profile cap**: A condition type that limits the number of profiles that can take a specific path; additional profiles are routed to an alternate path *(product-specific)*
* **Alternative path**: A fallback path activated when an error, timeout, or profile cap limit is reached *(product-specific)*

**Guardrails:**
* Condition evaluation fails for profiles with more than two cross-device identities in the Profile Store
* Schema fields with no ingested data are interpreted as null; isEmpty() and isNull() evaluate to true for such fields, which can cause unexpected behavior
* Time zone is defined at the journey level, not at the individual condition level
* The "Show path for other cases" option is not available in Percentage Split conditions
* Profile cap default is 1,000; counter resets when the journey is duplicated or a new version is created, but not between recurrences of a recurring journey
* For a cap above 10,000, inject at least 1.3x the cap number of profiles; for a cap below 10,000, inject at least 1,000 plus the cap
* Profile cap is not applied in test mode
* Time series queries (e.g., list of purchases, past clicks) are not supported in the simple expression editor; the advanced editor must be used

**Terminology:**
* Canonical name: Condition activity — Acronym: none — variants: condition node, condition step
* Synonyms: "Data Source condition" = "expression-based condition" ; "Percentage split" = "random split"
* Do not confuse: "Percentage split" ≠ "Profile cap" (percentage split randomly distributes all profiles; profile cap stops routing to a path once a count threshold is reached)

**FAQ:**
* **Q: What happens when multiple paths are defined and a profile meets more than one condition?** — Only the first eligible path (top to bottom on the canvas) is executed; path order determines priority.
* **Q: Can I add a fallback path for profiles that don't match any condition?** — Yes, enable "Show path for other cases than the one(s) above" — except in Percentage Split conditions, where all profiles always enter one of the split paths.
* **Q: Why does my isEmpty() condition evaluate to true for a field I expect to have data?** — If the schema field exists but no data has been ingested for it, Journey Optimizer and Real-Time Customer Profile interpret it as null, so isEmpty() and isNull() return true.
* **Q: Does the profile cap counter reset on a recurring journey?** — No, the counter does not reset between recurrences; it only resets when the journey is duplicated or a new version is created.
* **Q: How does the Percentage Split work in test mode?** — In test mode, the top branch is always chosen regardless of the configured split percentages.

+++
