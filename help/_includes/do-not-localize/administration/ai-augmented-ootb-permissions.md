---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page is a comprehensive reference of every built-in permission in Journey Optimizer, grouped by capability area, so administrators can identify exactly which rights to include when building or auditing a role.

**Intents:**

- Look up all available permissions for a given capability area (Journeys, Campaigns, Decision management, AI assistant, etc.)
- Identify the correct permission to add to a custom or built-in role
- Distinguish between Manage and View permissions per resource
- Find permissions for AI Assistant, orchestrated campaigns, and experience decisioning
- Identify which permissions cover journey execution modes (test mode, dry run, simulation)

**Glossary:**

- **Built-in permissions**: Pre-defined unitary rights assignable to a role to control access to features and objects in Journey Optimizer; high-level permissions encompass low-level permissions *(product-specific)*
- **Capability**: A functional area grouping related permissions (e.g., Journeys, Campaigns, Decision management, AI assistant) *(product-specific)*
- **Test mode**: A journey execution mode; the Publish journeys permission includes the ability to start test mode *(product-specific)*
- **Dry run**: A journey execution mode; the Publish journeys permission includes the ability to start dry run *(product-specific)*
- **Simulation**: A separate journey capability; the Simulate Journeys permission covers read, create, and edit of Simulation in Journeys *(product-specific)*

**Terminology:**

- Canonical name: Built-in permissions — variants: out-of-the-box permissions, OOTB permissions
- Do not confuse: "Manage journeys" (includes stop in live, test mode, and dry run) ≠ "Publish journeys" (includes publish, start test mode, start dry run, pause, and resume)
- Do not confuse: "Simulate Journeys" (permission to read, create, and edit Simulation in Journeys) ≠ "Simulate content" (access to the Simulate content option for message preview and proof)
- Do not confuse: "Generate content" (AI Assistant access in Journey Optimizer) ≠ "Enable AI Assistant" (enable or access AI-powered campaign and audience features)
- Do not confuse: "Test mode" (journey execution mode controlled via Publish journeys permission) ≠ "Dry run" (separate journey execution mode also controlled via Publish journeys permission) ≠ "Simulation" (separate capability via Simulate Journeys permission)
- Do not confuse: "Manage decisions" (CRUD on decisioning entities) ≠ "Manage Experience decisioning" (CRUD on Experience Decisioning settings and decision policies)

**FAQ:**

- **Q: Which permission is required to use AI Assistant for content generation?** — Generate content (under the AI assistant capability).
- **Q: What permission lets a user export the suppression list?** — Export suppression list (under Channel configurations).
- **Q: Which permission grants read-only access to journeys?** — View journeys (under the Journeys capability).
- **Q: What permission is needed to publish orchestrated campaigns?** — Publish orchestrated campaigns (under Orchestrated campaigns); this permission is also required to trigger an Orchestrated campaign using a signal.
- **Q: What does the Simulate Journeys permission cover?** — Read, create, and edit of Simulation in Journeys.

+++
<!-- ai-accordion-version: 1 | source-hash: 1374a5c2 -->
