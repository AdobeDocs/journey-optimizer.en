---
title: AI Knowledge Reference
---

# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents five Adobe CX Enterprise Coworker skills for Adobe Journey Optimizer journeys — Journey Create, Channel Content Create, Journey Analyze, Trace Journey Profile, and Journey Simulation — plus the Compare journey versions tool, with their use cases, scope, prompting guidance, and limitations.

**Intents**

* Build and configure journeys from natural language prompts or uploaded images using Journey Create.
* Generate, edit, and refine channel-specific content for journeys using Channel Content Create.
* Run a Quick Simulation to exercise journey paths, then review step-by-step traversal and branch outcomes using Journey Simulation.
* Analyze journey fallout, audience overlap, schedule conflicts, custom action errors, anomalies, performance, and journey inventory hygiene using Journey Analyze.
* Trace profiles through a published journey (node and branch counts, errored profiles, single-profile traces) using Trace Journey Profile.
* Compare journey versions with Journey Version Comparison and review a structured diff of nodes, connections, and journey-level properties.
* Learn each skill's permissions, scope, and limitations.

**Glossary**

* **Journey Create** *(product-specific)*: CX Coworker skill that builds and configures marketing journeys through natural language prompts.
* **Channel Content Create** *(product-specific)*: CX Coworker skill that generates, edits, and manages channel-specific content (email, push, SMS) for journeys using AI-powered content generation.
* **Journey Analyze** *(product-specific)*: CX Coworker skill that analyzes and optimizes journeys, covering fallout analysis, audience overlap analysis, schedule overlap analysis, operational insights, custom action error analysis, anomaly detection, business performance analysis, and journey hygiene analysis.
* **Trace Journey Profile** *(product-specific)*: CX Coworker skill that returns read-only, profile-level execution data for a published journey, based on journey step events.
* **Journey Simulation** *(product-specific)*: CX Coworker skill that uses Quick Simulation in chat to generate simulated test data, run or manage a simulation, and review results.
* **Quick Simulation**: The simulation flow available in Coworker for a fast, automated sanity check of journey logic.
* **Journey Fallout Analysis**: identifies where and why customers drop off during a journey.
* **Journey Audience Overlap Analysis**: analyzes audience overlap across multiple journeys to prevent fatigue from over-targeting.
* **Journey Schedule Overlap Analysis**: detects timing conflicts between scheduled journeys targeting the same audience.
* **Analyze Journey Anomalies**: detects unexpected spikes, drops, or flatlines in a journey's entry, exit, or send counts compared to historical baselines, confirms whether a flagged change is a genuine anomaly, and runs read-only diagnostics to identify a likely root cause.
* **Business Performance Analysis**: evaluates journey performance, highlights trends and bottlenecks, and recommends concrete optimizations to improve engagement and conversion.
* **Journey Hygiene Analysis**: identifies journeys with missing or generic names; stale draft journeys more than 30 days old that have never been published and have not been modified; stale live journeys more than 90 days old; oversized journeys with 50 or more nodes; long-existing closed journeys more than 90 days old; and similar action and event names. It provides recommendations to clean up and stabilize the journey inventory. A sample prompt is "Audit my journeys configuration."
* **Node and branch counts**: Trace Journey Profile query that shows how many profiles entered a node, how many stopped there, and how they split across branches, as counts and percentages.
* **Errored-profile lookup**: Trace Journey Profile query that shows which profiles errored over a period such as the last 7 days, at which node, and why.
* **Single-profile trace**: Trace Journey Profile query that shows a profile's node-by-node path with timestamps, the attribute value evaluated at each condition node, and the exit point and reason.
* **Journey Version Comparison**: Coworker tool that compares two journey versions and returns a structured diff of added, removed, modified, and moved nodes, changed connections, journey-level property changes, and roll-up counts.

**Guardrails**

* Journey Create requires the following permissions to be fully used: **Manage Journeys**, **View Journey Events, Data Sources and Actions**, **View Segments**, and **Manage Segments**.
* Channel Content Create is available for all customers in Limited Availability; contact your Adobe representative to gain access.
* Journey Analyze is available for all customers who have access to Coworker; full use requires the **View Journeys**, **Manage Journeys**, **View Segments**, and **Manage Segments** permissions.
* Trace Journey Profile is read-only and works on published journeys only. It does not support journeys that were never published (draft-only), B2B journeys, list export, or journey edits, and it does not cover fallout analysis, volume anomalies, custom action error trends, or Read Audience batch timelines; use Journey Analyze for fallout, anomalies, and custom action errors.
* Journey Simulation currently supports only the Quick Simulation flow and does not fully replace the manual simulation experience. Users cannot use chat to choose an existing saved simulated user or edit one before rerunning, create, browse, update, or delete persistent simulated users, or target a specific path or custom test case.

**Terminology**

* Synonyms: "Journey Analyze" = "Journey Skills" — the page introduces the Journey Analyze section using the term "Journey Skills" to refer to the same capability.
* Do not confuse: "Journey Create" (builds new journeys) is not the same skill as "Journey Analyze" (analyzes and optimizes existing journeys), "Trace Journey Profile" (traces profiles through a published journey), or "Channel Content Create" (generates channel content for journeys) — each is a distinct Coworker skill on this page.
* Do not confuse: "Trace Journey Profile" is its own skill, not a use case of "Journey Analyze". Fallout analysis, anomalies, and custom action errors belong to Journey Analyze.
* Do not confuse: Quick Simulation is a fast, automated sanity check; it does not replace the manual simulation experience for granular control over simulated users and scenarios.

**FAQ**

* **What permissions do I need to fully use Journey Create?** Manage Journeys, View Journey Events, Data Sources and Actions, View Segments, and Manage Segments.
* **Is Channel Content Create generally available?** It is available for all customers in Limited Availability; contact your Adobe representative to gain access.
* **What does Journey Analyze detect?** Journey fallout, audience overlap, schedule conflicts, custom action errors, anomalies in a journey's entry, exit, or send counts, business performance trends and optimization opportunities, and journey inventory hygiene issues such as missing or generic names, stale or oversized journeys, and similar action and event names.
* **What does Trace Journey Profile do?** It is a read-only skill that answers three types of queries on a published journey: node and branch counts (how many profiles entered a node, how many stopped there, and how they split across branches), errored-profile lookup (which profiles errored, at which node, and why), and single-profile trace (a profile's node-by-node path with timestamps, the attribute value evaluated at each condition node, and the exit point and reason).
* **What does Journey Version Comparison show?** A structured diff between two journey versions, including node changes with field-level details, changed connections, journey-level property changes, and roll-up counts.
* **Does Quick Simulation replace manual simulation?** No. It provides a fast, automated sanity check; use the manual simulation experience for granular control over simulated users and scenarios.
* **Does Journey Create support cross-journey orchestration?** No. Journey Create does not support cross-journey orchestration.

+++

<!-- ai-section-version: 6 | source-hash: 695594e5 -->
