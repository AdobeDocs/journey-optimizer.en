---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build a segment definition from attributes and events to create an audience, choose its streaming, batch, or edge evaluation method, and evaluate audiences on demand for targeting in Journey Optimizer.

**Intents:**

* Create an audience with the Build rule method from the Audiences menu
* Use attributes and events (and components from existing audiences) as building blocks of a segment definition
* Choose the streaming, batch, or edge evaluation method for the audience
* Run on-demand (flexible) evaluation of selected audiences before targeting them
* Understand backfilling timing after an audience is first defined

**Glossary:**

* **Segment definition**: A new audience definition created with Adobe Experience Platform Segmentation Service using the Build rule method *(product-specific)*
* **Build rule**: The audience creation method selected from Create audience that opens the segment definition screen *(product-specific)*
* **Attributes**: Building block representing profile characteristics used to define an audience *(product-specific)*
* **Events**: Building block representing profile actions used to define an audience *(product-specific)*
* **Streaming segmentation**: Evaluation method where the audience profile list is kept up to date in real time as new data flows in *(product-specific)*
* **Batch segmentation**: Evaluation method where the audience profile list is evaluated every 24 hours as a snapshot *(product-specific)*
* **Edge segmentation**: Evaluation method that evaluates segments instantaneously on the edge for same-page and next-page personalization *(product-specific)*
* **Flexible audience evaluation**: The Audience Portal ability to run a segmentation job on demand for selected audiences *(product-specific)*

**Guardrails:**

* The `frequencyMap` attribute is not supported for use in segment definitions and cannot be used as part of audience segmentation criteria; for frequency-based targeting, consider frequency capping rules under business rules.
* As of November 1st, 2024, streaming segmentation no longer supports the use of send and open events from Journey Optimizer tracking and feedback datasets; this applies to all customer sandboxes and organizations.
* Send and open events can still be used in batch segments, but if included in a streaming segment they are evaluated in a batch manner; clicks and other tracking events remain available for streaming segmentation.
* Edge segmentation can currently evaluate only select query types.
* Batch segmentation is evaluated every 24 hours; attempts to force an immediate update do not override the daily cycle.
* After an audience is first defined, backfilling the audience from prior data can take up to 24 hours.
* Flexible audience evaluation lets you evaluate up to 20 audiences at a time, and ineligible audiences are automatically excluded.

**Terminology:**

* Canonical name: Segment definition — Acronym: n/a — variants: audience definition, segment
* Synonyms: "Build rule" = "Create a rule"
* Do not confuse: "Streaming segmentation" (real-time updates) ≠ "Batch segmentation" (evaluated every 24 hours) ≠ "Edge segmentation" (instantaneous on the edge)
* Do not confuse: "Attributes" (profile characteristics) ≠ "Events" (profile actions)

**FAQ:**

* **Q: How do I start creating a segment definition?** — From the Audiences menu, click Create audience and select Build rule.
* **Q: Can I use the `frequencyMap` attribute in a segment definition?** — No; it is not supported and cannot be used as segmentation criteria. Consider frequency capping rules under business rules instead.
* **Q: Can I still use send and open events in streaming segmentation?** — No; as of November 1st, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets, though they remain usable in batch segments.
* **Q: How long does backfilling take?** — Backfilling the audience from prior data can take up to 24 hours after the audience is first defined.
* **Q: How many audiences can I evaluate on demand at once?** — You can evaluate up to 20 audiences at a time with flexible audience evaluation, and ineligible audiences are automatically excluded.

+++

<!-- ai-section-version: 1 | source-hash: 0b760cd3 -->
