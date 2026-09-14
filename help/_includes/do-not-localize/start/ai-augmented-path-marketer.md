---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is the Marketer getting-started path, covering how to create audiences, design content, add offers and decisioning, test and validate, build journeys, launch orchestrated campaigns, and monitor and optimize.

**Intents:**

* Create audiences through segment definitions, CSV upload, or audience composition
* Design and personalize content across channels and use AI content generation
* Add offers and decisioning to personalize content
* Test and validate content with test profiles, sample data, and experiments before sending
* Build customer journeys on the journey canvas, including with Journey Agent
* Launch orchestrated campaigns and monitor and optimize performance

**Glossary:**

* **Journey Agent**: A capability in AI Assistant that creates journeys from natural language prompts *(product-specific)*
* **Action activity**: The unified activity used for all channel actions in a journey, such as email, push, and SMS *(product-specific)*
* **Content decision activity**: A journey activity that integrates personalized offers directly into the journey flow *(product-specific)*
* **Content card**: Persistent, non-intrusive content delivered within mobile apps and websites that remains visible until dismissed, unlike push notifications *(product-specific)*
* **Wave sending**: Delivering messages in controlled batches (Limited Availability for journeys) *(product-specific)*
* **Orchestrated campaign**: A complex, multi-step batch campaign built on a visual canvas where all profiles progress together through the workflow in batch mode *(product-specific)*

**Guardrails:**

* You can start working once the System Administrator and the Data Engineer have granted you access and prepared your environment.
* Wave sending is in Limited Availability for journeys.
* Approval workflows for campaigns and journeys require an additional license.
* Multi-armed bandit experimentation automatically allocates more traffic to winning variations in real time.

**Terminology:**

* Canonical name: Marketer — variants: Business Practitioner, Journey Practitioner
* Implementation order: Administrator → Data Engineer → Developer → Marketer
* Journey triggers: events (customer actions) and audiences (batch sends)
* Do not confuse: "journeys" (real-time, one-to-one experiences) ≠ "orchestrated campaigns" (batch, one-to-many, where all profiles progress together)
* Do not confuse: "content cards" (persistent until dismissed) ≠ "push notifications"

**FAQ:**

* **Q: How can I create audiences?** — Through segment definitions, by uploading CSV files, or by using audience composition.
* **Q: How can I test and validate content before sending?** — Use test profiles to preview personalization and check rendering, test with sample data from CSV or JSON files, preview email rendering across popular email clients, and run A/B tests and experiments.
* **Q: How do I validate journey logic before activating?** — Test in draft mode and validate journey logic with dry run before activating.
* **Q: What triggers a journey?** — Events, which are customer actions, or audiences, which are batch sends.
* **Q: When should I use an orchestrated campaign instead of a journey?** — Use orchestrated campaigns for complex, multi-step batch campaigns at scale where all profiles progress together in batch mode, and journeys for real-time, one-to-one experiences.

+++

<!-- ai-section-version: 1 | source-hash: 24f0585b -->
