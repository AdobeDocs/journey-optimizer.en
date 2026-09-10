---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a comprehensive comparison of the four AJO journey types — Unitary event, Read Audience, Audience Qualification, and Business event — along with a decision guide and feature compatibility matrix to help users choose the right type for their use case.

**Intents:**

* Choose the correct journey type for a given business use case using the decision table
* Compare journey types side by side using the detailed feature compatibility matrix
* Understand when to use Read Audience journeys for scheduled batch communications
* Understand when to use Unitary event journeys for real-time, event-triggered experiences
* Understand when to use Audience Qualification journeys for real-time status-change responses
* Understand when to use Business event journeys for business-condition-driven communications
* Understand throughput limits per journey type when planning high-volume deployments

**Glossary:**

* **Unitary event journey**: A journey triggered by a specific individual customer action (e.g., purchase, login) where profiles enter one at a time in real time. *(product-specific)*
* **Read Audience journey**: A journey that starts with an Adobe Experience Platform audience and sends messages in batch to all profiles simultaneously on a schedule. *(product-specific)*
* **Audience Qualification journey**: A journey that triggers when profiles qualify for or exit a specific audience segment. Requires a streaming-evaluated audience for real-time entry behavior. *(product-specific)*
* **Business event journey**: A journey triggered by a business-level event (e.g., stock update, price change) that affects multiple profiles simultaneously; always paired with an internal Read Audience step for profile ingestion. *(product-specific)*
* **Incremental read**: A Read Audience capability that processes only profiles who joined the audience since the last execution, not the full audience each time. Available for Read Audience journeys only. *(product-specific)*
* **Streaming audience**: An Adobe Experience Platform audience evaluated continuously in real time, as opposed to a batch audience evaluated on a schedule (e.g., daily). Required for Audience Qualification journeys to achieve real-time entry behavior. *(product-specific)*

**Guardrails:**

* Incremental read is only available for Read Audience journeys, not for Unitary event, Audience Qualification, or Business event journeys
* Path experiments (A/B testing) are not supported for Business event journeys
* Profile re-entrance in Read Audience journeys is limited to once per execution by default; use Force reentrance on recurrence on scheduled runs to allow profiles to re-enter on the next execution
* The Read Audience activity is only available as a journey entry in Read Audience and Business event journeys — not in Unitary event or Audience Qualification entry journeys
* Audience Qualification and Read Audience journeys cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey
* Audience Qualification journeys require a streaming-evaluated audience. Starting August 2026, batch-evaluated audiences cannot be used in an Audience Qualification node — see the [migration guide](aq-batch-audiences-migration.md)
* Unitary event and Audience Qualification journeys share a 5,000 TPS throughput limit at the organization level; Read Audience journeys support up to 20,000 TPS per sandbox
* A profile already present in a journey cannot re-enter the same version of that journey, regardless of re-entrance configuration

**Terminology:**

* Canonical name: Unitary event journey — variants: event-triggered journey, unitary journey
* Canonical name: Read Audience journey — variants: batch journey
* Canonical name: Audience Qualification journey — variants: audience qualification event journey
* Canonical name: Business event journey — variants: business event-triggered journey
* Do not confuse: "Read Audience journey" ≠ "Audience Qualification journey" — Read Audience processes all audience members in batch on schedule; Audience Qualification responds to individual membership changes in real time (streaming audiences only for immediate entry)
* Do not confuse: "Unitary event journey" ≠ "Business event journey" — Unitary is triggered by a customer action affecting one profile; Business event is triggered by a business condition and ingests multiple profiles via an internal Read Audience step

**FAQ:**

* **Q: Which journey type should I use for a monthly newsletter?** — Use a Read Audience journey; it is designed for scheduled batch communication to all profiles in an audience segment simultaneously.
* **Q: Which journey type should I use to recover an abandoned cart?** — Use a Unitary event journey; it triggers immediately when the abandonment event occurs and responds to the individual's behavior in real time.
* **Q: Can I run A/B path experiments in a Business event journey?** — No; path experiments are not supported for Business event journeys.
* **Q: What is the difference between a Unitary event journey and an Audience Qualification journey?** — A Unitary event journey is triggered by a specific customer action (e.g., purchase); an Audience Qualification journey triggers when a profile enters or exits an audience segment based on streaming criteria evaluation.
* **Q: Which journey types support incremental read?** — Only Read Audience journeys support incremental read; the other three journey types do not.
* **Q: Can I add a Read Audience activity to a Unitary event journey?** — No; the Read Audience activity is only available as journey entry in Read Audience and Business event journeys.
* **Q: Can I use a Jump activity in a Read Audience journey?** — No; journeys starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity and cannot be the target of a Jump from another journey.
* **Q: Can I welcome new app users with an Audience Qualification journey?** — Yes, if entry is driven by a streaming audience (for example, when a profile joins a new-user segment); a signup unitary event journey is also a common pattern.
* **Q: My Audience Qualification journey is not triggering in real time. Why?** — Audience Qualification journeys require a streaming-evaluated audience. Using a batch-evaluated audience is deprecated and will be blocked from August 2026. [See the migration guide](aq-batch-audiences-migration.md)
* **Q: What is the throughput difference between Unitary event and Read Audience journeys?** — Unitary event journeys share a 5,000 TPS limit with Audience Qualification journeys at the organization level. Read Audience journeys support up to 20,000 TPS per sandbox, making them better suited for large-scale batch campaigns.

+++
