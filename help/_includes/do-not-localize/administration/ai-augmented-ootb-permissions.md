---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page lists the built-in permissions available for each capability, which can be assigned to a Role to fine-tune user access to Journey Optimizer.

**Intents:**

- Look up all available permissions for a given capability area (Journeys, Campaigns, Decision management, AI assistant, etc.)
- Identify the permission to assign to a Role
- Distinguish between Manage and View permissions per resource
- Find permissions for AI Assistant, orchestrated campaigns, and experience decisioning
- Identify which permissions mention test mode, dry run, and Simulation in Journeys

**Glossary:**

- **Built-in permissions**: Permissions that can be assigned to a Role to fine-tune user access to Journey Optimizer; high-level permissions encompass low-level permissions *(product-specific)*
- **Capability**: A functional area grouping related permissions (e.g., Journeys, Campaigns, Decision management, AI assistant) *(product-specific)*
- **Test mode**: Named on the page in the Journeys permissions: Publish journeys includes start test mode, and Manage journeys includes stop (live, test mode and dry run) *(product-specific)*
- **Dry run**: Named on the page in the Journeys permissions: Publish journeys includes start dry run, and Manage journeys includes stop (live, test mode and dry run) *(product-specific)*
- **Simulation**: The Simulate Journeys permission covers read, create and edit Simulation in Journeys; the Simulated Users capability covers simulated users used to test journeys in Simulation *(product-specific)*

**Terminology:**

- Canonical name: Built-in permissions
- Do not confuse: "Manage journeys" (read, create, edit, stop (live, test mode and dry run) and delete journeys) ≠ "Publish journeys" (includes publish, start test mode, start dry run, pause, and resume)
- Do not confuse: "Simulate Journeys" (permission to read, create, and edit Simulation in Journeys) ≠ "Simulate content" (access to the Simulate content option for message preview and proof)
- Do not confuse: "Generate content" (access to Generate content menu in Journey Optimizer) ≠ "Enable AI Assistant" (enable or access AI-powered campaign and audience features)
- Do not confuse: "Test mode" and "Dry run" (named in the Publish journeys and Manage journeys permissions) ≠ "Simulation" (named in the Simulate Journeys permission and the Simulated Users capability)
- Do not confuse: "Manage decisions" (read, create, edit, and delete decisioning entities) ≠ "Manage Experience decisioning" (read, create, edit, and delete Experience Decisioning settings, including decision policies and runtime options)

**FAQ:**

- **Q: Which permission gives access to the Generate content menu in Journey Optimizer?** — Generate content (under the AI assistant capability).
- **Q: What permission lets a user export the suppression list?** — Export suppression list (under Channel configurations).
- **Q: Which permission grants read-only access to journeys?** — View journeys (under the Journeys capability).
- **Q: What permission is needed to publish orchestrated campaigns?** — Publish orchestrated campaigns (under Orchestrated campaigns); this permission is also required to trigger an Orchestrated campaign using a signal.
- **Q: What does the Simulate Journeys permission cover?** — Read, create, and edit of Simulation in Journeys.

+++
<!-- ai-accordion-version: 1 | source-hash: e69cffd6 -->
