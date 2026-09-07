---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a comprehensive FAQ covering journey orchestration concepts, building journeys, testing and publishing, execution monitoring, advanced features, and best practices in Adobe Journey Optimizer.

**Intents:**
* Understand the four journey types (unitary, Read Audience, Audience Qualification, business event) and when to use each
* Decide between a journey and a campaign for a given use case
* Configure re-entrance settings to control how often a profile can enter the same journey
* Troubleshoot why a profile did not enter or why messages were not sent
* Apply journey capping rules to prevent message fatigue across multiple journeys
* Use Journey Fragments to reuse common node sequences across journeys

**Glossary:**
* **Unitary journey**: A journey triggered one profile at a time by a real-time event such as a purchase or sign-up *(product-specific)*
* **Read Audience journey**: A journey that processes all profiles in a batch audience at once or on a schedule *(product-specific)*
* **Audience Qualification journey**: A journey triggered when a profile enters or exits a streaming audience segment *(product-specific)*
* **Journey capping**: A configuration that limits how many times a profile can enter journeys within a time window or how many journeys a profile can be in simultaneously *(product-specific)*
* **Journey Fragment**: A reusable, static set of journey nodes built once and inserted into multiple journeys at design time *(product-specific)*
* **Send-Time Optimization (STO)**: An AI-driven feature that predicts the optimal send time for each individual profile to maximize engagement *(product-specific)*
* **Supplemental identifier**: An additional identifier that lets a profile enter the same journey multiple times for different entities (e.g., separate orders) *(product-specific)*

**Guardrails:**
* Maximum of 50 activities per journey
* Maximum journey duration is 91 days (global timeout)
* Upload audiences and Federated Audience Composition audiences are not supported in Audience Qualification journeys
* Reaction events must be placed immediately after a channel action, without a Wait activity in between
* Jump activities are not allowed inside a Journey Fragment
* A Journey Fragment supports a maximum of 20 nodes; a sandbox supports a maximum of 200 active fragments
* Streaming audience qualification may be delayed up to 10 minutes after journey publication for profiles already in the audience

**Terminology:**
* Canonical name: Journey — Acronym: none — variants: customer journey, orchestration, flow
* Synonyms: "Close to new entrances" = "graceful stop"; "Stop" = "immediate stop"
* Do not confuse: "Journey" ≠ "Campaign" — journeys support multi-step event-triggered orchestration; campaigns are one-time or scheduled audience-based sends
* Do not confuse: "Simulation" ≠ "Test mode" ≠ "Dry run" — Simulation uses temporary simulated users; Test mode uses persistent AEP test profiles; Dry run uses real production data without contacting customers or updating profiles

**FAQ:**
* **Q: What is the maximum number of activities in a journey?** — 50 activities; keeping journeys simpler improves maintainability and performance.
* **Q: Why did a profile not enter my journey?** — Common causes include the triggering event not being received, audience criteria not met, re-entrance rules blocking re-entry, the journey being unpublished, or a namespace mismatch.
* **Q: Can I modify a live journey's structure?** — No; structural changes require creating a new journey version. Message content can be updated without a new version.
* **Q: What is the difference between Pause, Close to new entrances, and Stop?** — Pause temporarily suspends the journey while holding or discarding in-flight profiles. Close to new entrances stops new entries but lets existing profiles finish. Stop immediately exits all profiles.
* **Q: When should I use Journey Fragments instead of the Jump activity?** — Use fragments to reuse common node logic at design time (copy-paste behavior). Use Jump to redirect profiles to another live journey at runtime.
* **Q: How do I prevent sending too many messages to the same customer?** — Apply journey capping rules (entry capping or concurrency capping) and use frequency capping business rules on individual channel actions.

+++
