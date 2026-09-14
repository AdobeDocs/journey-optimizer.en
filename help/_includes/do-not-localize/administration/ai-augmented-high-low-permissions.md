---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Journey Optimizer roles are built from high-level permissions, each of which bundles the specific low-level API rights users need to read, write, publish, or delete resources across journeys, campaigns, decisions, channel configurations, and more.

**Intents:**

* Understand the distinction between high-level and low-level permissions
* Identify which low-level permissions are granted by each high-level permission
* Configure roles precisely for journeys, campaigns, decision management, channel configurations, and orchestrated campaigns
* Grant Generate content access for content generation
* Understand what the Publish journeys permission allows compared to the Manage journeys permission

**Glossary:**

* **High-level permission**: A named permission assigned to a role (e.g., Manage journeys, Publish journeys) that encompasses one or more low-level permissions *(product-specific)*
* **Low-level permission**: A granular API-level right (e.g., journeys.read, journeys.write) derived from and included within a high-level permission *(product-specific)*
* **Role**: A collection of users sharing the same permissions and sandboxes within the organization *(product-specific)*

**Terminology:**

* Do not confuse: "High-level permission" (named right assignable to a role) ≠ "Low-level permission" (underlying granular API right, not directly assignable)
* Do not confuse: "Manage journeys" (allows create, edit, delete, stop — including live, test mode, and dry run) ≠ "Publish journeys" (allows publish, start test mode, start dry run, pause, and resume journeys)
* Do not confuse: "Manage journeys events, data sources and actions" (full CRUD on events, sources, actions) ≠ "View journeys events, data sources and actions" (read-only access to those objects)
* Do not confuse: "Generate content" (access to AI Assistant in Journey Optimizer) ≠ other journey or campaign permissions
* Do not confuse: "Test mode" (referenced in Publish journeys and Manage journeys as a journey execution mode that can be started or stopped) ≠ "Dry run" (a separate journey execution mode also referenced in those same permissions)

**FAQ:**

* **Q: Does the Manage journeys permission allow a user to publish journeys?** — No; publishing journeys requires the separate Publish journeys high-level permission.
* **Q: What does the Generate content permission grant?** — Access to AI Assistant in Journey Optimizer.
* **Q: Can a user configure journey events without the Manage journeys permission?** — Yes; Manage journeys events, data sources and actions is a separate high-level permission covering event, data source, and action configuration.
* **Q: What low-level permissions are included in View journeys report?** — journeys_report.read and messages_report.read, plus datasets.read, queries.read, queries.write, and queries.delete from Adobe Experience Platform.

+++
<!-- ai-accordion-version: 1 | source-hash: d1d9ebf9 -->
