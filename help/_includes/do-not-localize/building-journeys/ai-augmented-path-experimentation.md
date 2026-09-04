---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and run path experimentation in Adobe Journey Optimizer journeys using A/B or Multi-armed bandit methods, and how to scale the winning treatment automatically or manually.

**Intents:**
* Set up an A/B or Multi-armed bandit path experiment in a journey
* Define success metrics to evaluate experiment performance
* Allocate traffic between treatment paths evenly or by custom percentage
* Add a holdout group to exclude a portion of the audience from all treatments
* Enable auto-scaling to automatically roll out the winning treatment
* Manually scale the winning treatment after reviewing experiment results

**Glossary:**
* **Optimize activity**: A journey canvas activity used to split profiles into different paths for experimentation or targeting *(product-specific)*
* **Treatment**: A single path variant in a path experiment (e.g., Treatment A, Treatment B) *(product-specific)*
* **Success metric**: The KPI used to evaluate which treatment performs best in an experiment *(product-specific)*
* **Multi-armed bandit**: An experiment type where traffic split is adjusted automatically every 7 days based on primary metric performance *(product-specific)*
* **Scale the Winner**: A feature that rolls out the winning treatment to the full remaining audience, either automatically or manually *(product-specific)*
* **Holdout group**: A segment of the audience excluded from all experiment treatments, used as a control group *(product-specific)*

**Guardrails:**
* Scale the Winner is only available for unitary journeys (event-triggered and Audience Qualification); it is not available for Read Audience journeys.
* Auto-scale time must be scheduled before the experiment's end date, or the journey will not publish.
* Once auto-scaling has occurred, manual scaling is no longer available.
* Manual scaling the winner before the scheduled auto-scale time cancels the auto-scale.
* Scaling the treatment may take up to one hour.

**Terminology:**
* Canonical name: Path Experimentation — Acronym: none — variants: journey experimentation, A/B path test
* Synonyms: "Optimize activity" = "experiment activity" = "path split activity"
* Do not confuse: "A/B experiment" ≠ "Multi-armed bandit" (A/B has fixed traffic split; Multi-armed bandit adjusts weights dynamically every 7 days)

**FAQ:**
* **Q: What is the difference between A/B experiment and Multi-armed bandit?** — A/B experiment uses a fixed traffic split defined at the start, while Multi-armed bandit automatically adjusts traffic weights every 7 days based on the primary metric performance.
* **Q: Can I use Scale the Winner in a Read Audience journey?** — No; Scale the Winner is only available for unitary (event-triggered and Audience Qualification) journeys.
* **Q: What happens if no winner is found by the auto-scale time?** — You can configure a fallback: either continue the experiment until its scheduled end, or scale an alternative treatment after a specified time.
* **Q: How is traffic distributed if I do not configure treatment percentages manually?** — You can enable the Distribute evenly toggle to split traffic equally across all treatments.
* **Q: Can I edit a path experiment after the journey is published?** — The journey enters read-only mode after publishing; to make changes, create a new version of the journey.

+++
