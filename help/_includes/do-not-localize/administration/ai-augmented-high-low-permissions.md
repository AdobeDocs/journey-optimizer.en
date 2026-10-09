---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Journey Optimizer roles are built from high-level permissions, each of which encompasses low-level permissions, with the page listing them per resource (journey, rules, campaign, decision management, channel configurations, AI assistance, and orchestrated campaign).

**Intents:**

* Understand the distinction between high-level and low-level permissions
* Identify which low-level permissions are granted by each high-level permission
* Configure roles precisely for journeys, campaigns, decision management, channel configurations, and orchestrated campaigns
* Identify the Generate content high-level permission, which allows users to access the Generate content menu in Journey Optimizer
* Understand what the Publish journeys permission allows compared to the Manage journeys permission

**Glossary:**

* **High-level permission**: A permission that can be assigned to a Role, such as Publish journeys and Manage subdomains delegation; high-level permissions encompass low-level permissions *(product-specific)*
* **Low-level permission**: A permission that comes from the high-level permission (for example, journeys.read, journeys.write) *(product-specific)*
* **Role**: Each role is composed of permissions allowing users to access the different features *(product-specific)*

**Terminology:**

* Do not confuse: "High-level permission" (can be assigned to a Role) ≠ "Low-level permission" (comes from the high-level permission)
* Do not confuse: "Manage journeys" (allows users to create new and edit/delete/stop/pause existing Journeys, and to access the objects used in the journey canvas) ≠ "Publish journeys" (allows users to publish journeys)
* Do not confuse: "Manage journeys events, data sources and actions" (allows users to configure event and data configurations) ≠ "View journeys events, data sources and actions" (allows users to use event and data in the journey flow)

**FAQ:**

* **Q: Does the Manage journeys permission allow a user to publish journeys?** — The page states that the Publish journeys high-level permission allows users to publish journeys, and its low-level permissions include journeys.publish; the low-level permissions listed for Manage journeys do not include journeys.publish.
* **Q: What does the Generate content permission grant?** — It allows users to access the Generate content menu in Journey Optimizer (low-level permission ai-assistant-generated-content.generate).
* **Q: Can a user configure journey events without the Manage journeys permission?** — Manage journeys events, data sources and actions is a separate high-level permission that allows users to configure event and data configurations; its low-level permissions include journeys_events.read, journeys_events.write, and journeys_events.delete.
* **Q: What low-level permissions are included in View journeys report?** — journeys_report.read and messages_report.read, plus datasets.read, queries.read, queries.write, and queries.delete from Adobe Experience Platform.

+++
<!-- ai-accordion-version: 1 | source-hash: e0430508 -->
