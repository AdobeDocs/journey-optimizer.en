---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Journey Optimizer ships with built-in roles — from Campaign Administrator to Orchestrated Campaign Viewer — each bundling a ready-made permission set, so administrators can quickly grant users a level of access that matches their responsibilities without building a role from scratch.

**Intents:**

* Identify which built-in role best fits a user's job responsibilities
* Understand what each built-in role can and cannot do (including publish rights)
* Compare roles across journey, campaign, and orchestrated campaign domains
* Assign a ready-made role instead of creating a custom one
* Understand which roles include AI Assistant access

**Glossary:**

* **Built-in role**: A pre-defined set of permissions and resource rights ready to assign to users without custom configuration *(product-specific)*
* **Journey Administrator**: Built-in role enabling management and publication of Journeys and Decision management, including channel configuration and data governance permissions *(product-specific)*
* **Campaign Administrator**: Built-in role enabling management and publication of Campaigns and Decision management, including channel configurations *(product-specific)*
* **Decisioning manager**: Built-in role providing access exclusively to the Decision management menu; can manage, view, and publish decisions *(product-specific)*
* **Content Library Manager**: Built-in role providing access only to the Content templates menu; cannot access journeys or campaigns *(product-specific)*
* **Test mode**: A journey execution mode referenced in Manage journeys and Publish journeys permissions (Journey Administrator can stop journeys in test mode; Publish journeys permission includes starting test mode) *(product-specific)*
* **Dry run**: A journey execution mode referenced in Manage journeys and Publish journeys permissions alongside test mode *(product-specific)*

**Terminology:**

* Canonical name: Built-in roles — variants: out-of-the-box roles, OOTB roles, product profiles
* Do not confuse: "Campaign Approver" (can approve and publish campaigns) ≠ "Campaign Manager" (can create and edit campaigns but cannot publish them)
* Do not confuse: "Journey Approver" (can approve and publish journeys) ≠ "Journey Manager" (can create and edit journeys but cannot publish them)
* Do not confuse: "Journey Viewer" (read-only access to journeys and decision management) ≠ "Campaign Viewer" (read-only access to campaigns and decision management)
* Do not confuse: "Orchestrated Campaign Administrator" (manages orchestrated campaigns, includes AI Assistant and data ingestion/management) ≠ "Campaign Administrator" (manages standard campaigns; does not include orchestrated campaign permissions)
* Do not confuse: "Test mode" (referenced as a journey execution state that can be stopped or started via Manage journeys / Publish journeys) ≠ "Dry run" (a separate journey execution mode also referenced in those same permissions)

**FAQ:**

* **Q: Which built-in roles can publish journeys?** — Journey Administrator and Journey Approver can publish journeys.
* **Q: Can a Journey Manager publish journeys?** — No; Journey Manager can create and edit journeys but the Publish journeys permission is not included in that role.
* **Q: Which role grants access only to the Decision management menu?** — Decisioning manager.
* **Q: Which role provides access only to content templates?** — Content Library Manager.
* **Q: Which built-in roles include the Enable AI Assistant permission?** — Orchestrated Campaign Administrator, Orchestrated Campaign Approver, Orchestrated Campaign Manager, and Orchestrated Campaign Viewer.

+++
<!-- ai-accordion-version: 1 | source-hash: b9740765 -->
