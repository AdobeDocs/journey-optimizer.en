---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure time zone settings in Adobe Journey Optimizer journey properties, choosing between a fixed time zone applied to all profiles or a per-profile time zone sourced from the Real-time Customer Profile.

**Intents:**
* Set a fixed time zone on a journey so that all profiles follow the same time reference for conditions and waits
* Enable per-profile time zone so that Wait and Condition activities use each individual's stored time zone preference
* Understand which journey activities are affected by the journey time zone setting
* Identify the profile field group that stores the individual time zone value

**Glossary:**
* **Fixed time zone**: A single time zone selected in Journey Properties that applies uniformly to every profile entering the journey *(product-specific)*
* **Profile time zone**: The per-individual time zone stored in the `timeZone` field of the Preference Details field group, used when the "Use Profile time zone in waits and conditions" option is enabled *(product-specific)*
* **Preference Details field group**: The XDM field group that contains the `timeZone` attribute used for profile-level time zone resolution

**Guardrails:**
* The "Use Profile time zone in waits and conditions" option is only available when the journey's entry event has a namespace (i.e., the journey can reach the Real-time Customer Profile service)
* The option is not checked by default; the fixed time zone is used unless explicitly enabled
* If the option is enabled but no time zone is defined on the profile, the journey falls back to the fixed time zone defined in journey properties
* Journey start and end dates cannot be linked to a specific time zone; they are automatically associated with the instance's time zone

**Terminology:**
* Canonical name: Time zone management — Acronym: none — variants: timezone configuration, journey time zone
* Synonyms: "fixed time zone" = "same for all individuals"; "profile time zone" = "Use Profile time zone in waits and conditions"
* Do not confuse: "journey time zone" (applies to activities) ≠ "instance time zone" (applies to journey start/end dates, set automatically)

**FAQ:**
* **Q: Where do I set the time zone for a journey?** — In the Journey Properties pane, accessible via the pencil icon in the top-right of the journey canvas.
* **Q: Which activities use the journey time zone?** — Time conditions, date conditions, and custom wait activities.
* **Q: How do I make each profile follow their own local time zone?** — In Journey Properties, enable the "Use Profile time zone in waits and conditions" option. This requires the journey to have a namespace so it can reach the Real-time Customer Profile service.
* **Q: What happens if a profile has no time zone defined and the profile time zone option is enabled?** — The journey falls back to the fixed time zone defined in the time zone field in Journey Properties.
* **Q: Which profile field stores the individual's time zone?** — The `timeZone` field within the Preference Details field group in the profile schema.
* **Q: Can I set the journey's start and end dates to a specific time zone?** — No. Journey start and end dates are automatically associated with the instance's time zone and cannot be linked to a custom time zone.

+++
