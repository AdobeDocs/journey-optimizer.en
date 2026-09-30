---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to monitor inbound data health in Journey Optimizer with the Edge monitoring graphs in Data Management.

**Intents:**

* Access the Edge monitoring graphs from Data Management > Monitoring > Edge
* Review overall inbound throughput in records per second over time
* Review inbound throughput broken down by location
* Analyze inbound request latency in milliseconds by distribution values such as P50 and P90
* Analyze proposition event throughput by time, channel, and event type

**Glossary:**

* **Edge monitoring graphs**: Graphs in Data Management > Monitoring > Edge that show inbound throughput, inbound latency, and proposition event throughput *(product-specific)*
* **Inbound throughput**: Overall inbound throughput measured in records per second over time *(product-specific)*
* **Proposition events**: Tracking signals generated when a user interacts with, views, or triggers personalized offers *(product-specific)*

**Guardrails:**

* Inbound latency is measured in milliseconds.
* The latency graph shows a distribution of values, including P50 and P90.
* Proposition event channel values are CBE, in-app, and content cards.
* Proposition event type values are dismissed, suppressed, displayed, triggered, interacted, and sent.

**Terminology:**

* Canonical name: Edge monitoring graphs — variants: AJO graphs
* Do not confuse: inbound throughput (records per second) ≠ inbound latency (milliseconds)
* Do not confuse: proposition event channel (CBE, in-app, or content cards) ≠ proposition event type (dismissed, suppressed, displayed, triggered, interacted, or sent)

**FAQ:**

* **Q: Where are the inbound data health graphs?** — Open Data Management > Monitoring > Edge.
* **Q: What does AJO Inbound Throughput measure?** — It measures overall inbound throughput in records per second over time.
* **Q: How is inbound latency shown?** — In milliseconds, by distribution values including P50 and P90.
* **Q: Which proposition event channels are available?** — CBE, in-app, and content cards.
* **Q: Which proposition event types are available?** — Dismissed, suppressed, displayed, triggered, interacted, and sent.

+++

<!-- ai-section-version: 1 | source-hash: a5cf3193 -->