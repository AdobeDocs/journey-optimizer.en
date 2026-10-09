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
* **Read Audience journey**: A journey that starts with an Adobe Experience Platform audience and sends messages in batch to its profiles *(product-specific)*
* **Audience Qualification journey**: A journey triggered when profiles qualify for or exit a specific audience segment; streaming audiences are recommended and batch audiences have delayed qualification detection *(product-specific)*
* **Journey capping**: A configuration that limits how many times a profile can enter journeys within a time window or how many journeys a profile can be in simultaneously *(product-specific)*
* **Journey Fragment**: A reusable, static set of journey nodes built once and inserted into multiple journeys at design time *(product-specific)*
* **Send-Time Optimization (STO)**: An AI-driven feature that predicts the optimal send time for each individual profile to maximize engagement *(product-specific)*
* **Supplemental identifier**: An additional identifier that lets a profile enter the same journey multiple times for different entities (e.g., separate orders) *(product-specific)*

**Guardrails:**
* Configuration validation must pass before testing; errors in the Alerts panel must be resolved and validation rerun before continuing. Edits require revalidation before testing or publishing, including for a new journey version.
* Maximum of 50 activities per journey (hard limit).
* The page gives 91 days as an example of maximum journey duration.
* Upload audiences and Federated Audience Composition audiences are not supported in Audience Qualification journeys
* Reaction events must be placed immediately after a channel action, without a Wait activity in between
* Jump activities are not allowed inside a Journey Fragment
* A Journey Fragment supports a maximum of 20 nodes (hard limit); a sandbox supports a maximum of 200 active fragments (hard limit).
* Profiles already in a streaming audience before publication may not enter an Audience Qualification journey; entry can also be delayed while the journey completes its activation period, up to 10 minutes after publishing.

**Terminology:**
* Canonical name: journey. Journey types: Unitary, Read Audience, Audience Qualification, Business event.
* Do not confuse: "Journey" ≠ "Campaign" — journeys are multi-step orchestrations reacting to events or targeting audiences; campaign types include Action campaigns, API-triggered campaigns, and multi-step Orchestrated campaigns.
* Do not confuse: "Journey Simulation" ≠ "Test mode" ≠ "Dry run mode" — Journey Simulation uses temporary simulated users; Test mode uses real, designated test profiles; Dry run mode uses real production data without contacting customers or updating profile information.

**FAQ:**
* **Q: What is the maximum number of activities in a journey?** — 50 activities (hard limit); keeping journeys simpler improves maintainability and performance.
* **Q: Why did a profile not enter my journey?** — Common causes include the triggering event not being received, audience criteria not met, re-entrance rules blocking re-entry, the journey being unpublished, or a namespace mismatch.
* **Q: Can I modify a live journey's structure?** — No; structural changes require creating a new journey version. Message content can be updated without a new version.
* **Q: What is the difference between Pause, Close to new entrances, and Stop?** — Pause temporarily halts the journey so it can be resumed later. Close to new entrances stops new entries but lets existing profiles finish. Stop immediately exits all profiles.
* **Q: When should I use Journey Fragments instead of the Jump activity?** — Use fragments to reuse common node logic at design time (copy-paste behavior). Use Jump to redirect profiles to another live journey at runtime.
* **Q: How do I prevent message fatigue across journeys?** — Apply journey capping rules: entry capping limits entries within a specified time period, and concurrency capping limits how many journeys a profile can be in simultaneously.

+++

<!-- ai-section-version: 1 | source-hash: f3faf5b6 -->
