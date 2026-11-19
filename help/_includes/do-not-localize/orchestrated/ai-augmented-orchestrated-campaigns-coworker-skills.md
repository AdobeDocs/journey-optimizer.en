---
title: AI Knowledge Reference
---

# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents two Adobe CX Enterprise Coworker skills for Orchestrated campaigns in Adobe Journey Optimizer — Orchestrated Campaign List, a read-only skill to list, browse, filter, search, and count campaigns, and Orchestrated Campaign Get, a read-only skill to retrieve the details, lifecycle history, execution history, and activity graph of a single campaign — with their use cases and limitations.

**Intents**

* List, browse, filter, search, count, and get an overview of Orchestrated campaigns using Orchestrated Campaign List.
* Get an overview of Orchestrated campaigns as a dashboard with metric cards, charts, and a campaign table.
* Retrieve the details, status, and metadata of a specific Orchestrated campaign using Orchestrated Campaign Get.
* Review the lifecycle history and execution history of a campaign, and check whether a campaign failed.
* Visualize the activities of a campaign and their connections as a graph.

**Glossary**

* **Orchestrated Campaign List** (`orchestrated-campaign-list`) *(product-specific)*: CX Coworker skill that lists, browses, filters, searches, and counts Adobe Journey Optimizer Orchestrated campaigns, and presents the results as a dashboard. It is read-only.
* **Orchestrated Campaign Get** (`orchestrated-campaign-get`) *(product-specific)*: CX Coworker skill that retrieves the details, status, metadata, lifecycle history, execution history, and activity graph of a single Orchestrated campaign identified by name or ID. It is read-only.
* **Orchestrated campaign**: A campaign built in Adobe Journey Optimizer as a canvas of connected activities that target, orchestrate, and deliver messages across channels.

**Guardrails**

* Both skills are read-only. Creating or editing Orchestrated campaigns is not supported by the current toolset.
* Orchestrated campaign analytics and performance reporting are not supported.
* Orchestrated Campaign Get works on a single campaign; use Orchestrated Campaign List to work with several campaigns.

**Terminology**

* Do not confuse: "Orchestrated Campaign List" (finds and counts multiple campaigns) is not the same skill as "Orchestrated Campaign Get" (retrieves everything about one campaign); each is a distinct Coworker skill on this page.

**FAQ**

* **Can Coworker create or edit an Orchestrated campaign?** No. The Orchestrated campaign skills are read-only.
* **How do I see the graph of a campaign?** Ask Coworker to draw or visualize the graph of a named campaign, using Orchestrated Campaign Get.
* **How do I find which campaigns are live?** Ask Coworker to show the LIVE Orchestrated campaigns, using Orchestrated Campaign List.
* **Can I get performance reporting for a campaign?** No. Orchestrated campaign analytics and performance reporting are not supported by these skills.

+++

<!-- ai-section-version: 1 | source-hash: 00000000 -->
