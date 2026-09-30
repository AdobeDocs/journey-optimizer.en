---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure wave sending in Adobe Journey Optimizer to deliver outbound messages in controlled batches over time, improving deliverability and protecting sender reputation. Wave sending is available in read-audience journeys, action campaigns, and orchestrated campaigns.

**Intents:**

* Enable wave sending on a Read Audience journey, an Action campaign, or an Orchestrated campaign channel activity
* Configure equal waves with a fixed interval between each wave
* Define custom wave sizes as percentages or absolute profile counts
* Schedule each wave with a specific start date and time
* Control delivery volume to protect sender reputation or align with operational capacity

**Glossary:**

* **Wave sending**: A delivery mode that splits the audience into batches (waves) and sends messages to each batch at scheduled intervals instead of all at once *(product-specific)*
* **Equal waves**: A configuration where the audience is split into equal-sized portions with a fixed interval between wave starts *(product-specific)*
* **Custom distribution**: A configuration where each wave's size is defined manually as a percentage or absolute number of profiles *(product-specific)*
* **Custom schedule**: A configuration where each wave has a specific start date and time, allowing non-uniform spacing *(product-specific)*

**Contexts where wave sending is available:**

* Read audience journeys ("As soon as possible" or "Once" scheduler only — not for recurring, event-triggered, business-event, test, or dry-run journeys)
* Action campaigns (outbound channel actions only)
* Orchestrated campaigns (outbound channel activities only, configured per channel activity)

**Common guardrails (all contexts):**

* Minimum 2 waves, maximum 10 waves
* Minimum 30 minutes between the start of two consecutive waves
* Wave start cannot be in the past
* Percentage-based custom distribution must total 100%
* Number-based custom distribution does not auto-validate total coverage

**Journey-specific guardrails:**

* Wave start cannot be before journey start
* The last wave must be scheduled within 6 days and 18 hours of the journey start; exceeding this triggers a validation error
* Audience splitting can take up to 1 hour; profiles may be delayed
* Two waves never run simultaneously within the same journey version
* Wave starts can be delayed by platform quota limits or heavy system load

**FAQ:**

* **Q: Does wave sending apply to inbound channels?** — No; outbound only (Email, SMS, Push, Direct mail).
* **Q: Can I assign different content to individual waves?** — No; same audience and content for all waves. Only size and timing can differ.
* **Q: What is the minimum time between two waves?** — 30 minutes between the start of two consecutive waves.
* **Q: What happens if wave sizes exceed or fall short of the audience?** — Excess: first wave sends to full audience, remaining waves do not execute. Shortfall: only profiled in defined waves receive the message; the rest are not retried.
* **Q: Is the audience re-evaluated per wave?** — No; the audience is snapshotted at activation. Profile attributes (personalization, consent) are read at wave processing time.

+++
