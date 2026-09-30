---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents four CX Coworker skills for Adobe Journey Optimizer journeys — Journey Create, Channel Content Create, Journey Analyze, and Journey Simulation — plus the Journey Version Comparison tool, with their use cases, scope, prompting guidance, and limitations.

**Intents**

* Build and configure journeys from natural language prompts or uploaded images using Journey Create.
* Generate, edit, and refine channel-specific content for journeys using Channel Content Create.
* Run a Quick Simulation to exercise journey paths, then review step-by-step traversal and branch outcomes using Journey Simulation.
* Analyze journey fallout, audience overlap, schedule conflicts, custom action errors, anomalies, and performance using Journey Analyze.
* Compare journey versions with Journey Version Comparison and review a structured diff of nodes, connections, and journey-level properties.
* Learn each skill's permissions, scope, and limitations.

**Glossary**

* **Journey Create** *(product-specific)*: CX Coworker skill that builds and configures marketing journeys through natural language prompts.
* **Channel Content Create** *(product-specific)*: CX Coworker skill that generates, edits, and manages channel-specific content (email, push, SMS) for journeys using AI-powered content generation.
* **Journey Analyze** *(product-specific)*: CX Coworker skill that analyzes and optimizes journeys, covering fallout analysis, audience overlap analysis, schedule overlap analysis, operational insights, custom action error analysis, anomaly detection, and business performance analysis.
* **Journey Simulation** *(product-specific)*: CX Coworker skill that uses Quick Simulation in chat to generate simulated test data, run or manage a simulation, and review results.
* **Quick Simulation**: The simulation flow available in Coworker for a fast, automated sanity check of journey logic.
* **Journey Fallout Analysis**: identifies where and why customers drop off during a journey.
* **Journey Audience Overlap Analysis**: analyzes audience overlap across multiple journeys to prevent fatigue from over-targeting.
* **Journey Schedule Overlap Analysis**: detects timing conflicts between scheduled journeys targeting the same audience.
* **Analyze Journey Anomalies**: detects unexpected spikes, drops, or flatlines in a journey's entry, exit, or send counts compared to historical baselines, confirms whether a flagged change is a genuine anomaly, and runs read-only diagnostics to identify a likely root cause.
* **Business Performance Analysis**: evaluates journey performance, highlights trends and bottlenecks, and recommends concrete optimizations to improve engagement and conversion.
* **Journey Version Comparison**: Coworker tool that compares two journey versions and returns a structured diff of added, removed, modified, and moved nodes, changed connections, journey-level property changes, and roll-up counts.

**Guardrails**

* Journey Create requires the following permissions to be fully used: **Manage Journeys**, **View Journey Events, Data Sources and Actions**, **View Segments**, and **Manage Segments**.
* Channel Content Create is available for all customers in Limited Availability; contact your Adobe representative to gain access.
* Journey Analyze is available for all customers who have access to CX Coworker; full use requires the **View Journeys**, **Manage Journeys**, **View Segments**, and **Manage Segments** permissions.
* Journey Simulation currently supports only the Quick Simulation flow and does not fully replace the manual simulation experience. Users cannot use chat to choose an existing saved simulated user or edit one before rerunning, create, browse, update, or delete persistent simulated users, or target a specific path or custom test case.

**Terminology**

* Synonyms: "Journey Analyze" = "Journey Skills" — the page introduces the Journey Analyze section using the term "Journey Skills" to refer to the same capability.
* Do not confuse: "Journey Create" (builds new journeys) is not the same skill as "Journey Analyze" (analyzes and optimizes existing journeys) or "Channel Content Create" (generates channel content for journeys) — each is a distinct CX Coworker skill on this page.
* Do not confuse: Quick Simulation is a fast, automated sanity check; it does not replace the manual simulation experience for granular control over simulated users and scenarios.

**FAQ**

* **What permissions do I need to fully use Journey Create?** Manage Journeys, View Journey Events/Data Sources and Actions, View Segments, and Manage Segments.
* **Is Channel Content Create generally available?** It is available for all customers in Limited Availability; contact your Adobe representative to gain access.
* **What does Journey Analyze detect?** Journey fallout, audience overlap, schedule conflicts, custom action errors, anomalies in a journey's entry, exit, or send counts, and business performance trends and optimization opportunities.
* **What does Journey Version Comparison show?** A structured diff between two journey versions, including node changes with field-level details, changed connections, journey-level property changes, and roll-up counts.
* **Does Quick Simulation replace manual simulation?** No. It provides a fast, automated sanity check; use the manual simulation experience for granular control over simulated users and scenarios.
* **What are Journey Create and Channel Content Create not designed to do?** Journey Create does not support cross-journey orchestration, and Channel Content Create does not support brand alignment or content quality checks.

+++

<!-- ai-section-version: 4 | source-hash: 9581b35e -->
