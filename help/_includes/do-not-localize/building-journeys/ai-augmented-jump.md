---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the Jump activity, which pushes profiles from one journey to another to simplify complex journey designs through reusable sub-journey patterns.

**Intents:**

* Use the Jump activity to transfer profiles from an origin journey to a target journey
* Decompose a complex journey into smaller, manageable sub-journeys connected by Jump activities
* Configure the Jump activity by selecting a target journey and mapping action parameters
* Understand profile behavior when a Jump is executed (profile active in both journeys simultaneously)
* Troubleshoot Jump configuration errors and runtime failures
* Avoid loop patterns when chaining multiple journeys with Jump activities

**Glossary:**

* **Jump activity**: An action activity that sends an internal event to the first event of a target journey, causing the profile to begin flowing through that journey. *(product-specific)*
* **Origin journey**: The journey that contains the Jump activity and initiates the transfer of a profile to another journey. *(product-specific)*
* **Target journey**: The journey that receives the profile via the Jump activity's internal event trigger. *(product-specific)*
* **Silent skip**: The behavior when a profile is already active in the target journey at the time of a Jump — the Jump is skipped without an error, and the origin journey continues normally. *(product-specific)*

**Guardrails:**

* Jump activity is only available in journeys that use a namespace; origin and target journeys must share the same namespace
* Cannot jump to a journey starting with an Audience Qualification event or Read Audience
* Cannot use a Jump activity and an Audience Qualification event or Read Audience in the same journey
* Loop patterns (circular journey chains) are not supported and are prevented by the configuration UI
* At runtime, the latest live version of the target journey is triggered
* A profile can only be present once in the same journey at a time; if already active in the target journey, the Jump is silently skipped
* If the target journey is draft, closed, stopped, deleted, or its first event mapping is broken, the Jump results in a configuration error

**Terminology:**

* Canonical name: Jump activity — Acronym: none — variants: Jump action, journey jump
* Synonyms: "origin journey" = "source journey"; "target journey" = "destination journey"
* Do not confuse: "silent skip" ≠ "runtime failure" — A silent skip occurs when the profile is already in the target journey (no error raised); a runtime failure occurs when the target journey is unreachable or non-reentrant (treated as a failed action)

**FAQ:**

* **Q: What happens to a profile in the origin journey after a Jump?** — The profile continues progressing through any remaining steps in the origin journey after the Jump step while simultaneously entering the target journey; it is active in both journeys at the same time.
* **Q: Can I jump to a Read Audience journey?** — No; you cannot jump to a journey that starts with a Read Audience or Audience Qualification event.
* **Q: What triggers the target journey when a Jump is executed?** — An internal event is sent to the first event of the target journey by the Jump activity; the profile then flows through the target journey from that first event.
* **Q: How do I prevent infinite loops when chaining journeys with Jump?** — Loop patterns are blocked by the Jump activity configuration UI, which filters out target journeys that would create a circular chain.
* **Q: What version of the target journey is triggered by a Jump?** — The latest live (or test mode) version of the target journey is triggered at runtime.

+++
