---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** Sandboxes partition your Journey Optimizer instance into isolated virtual workspaces for development, testing, and production; they are assigned to users through roles in the Permissions product, and content access is configured via shared folders in Admin Console.

**Intents:**

- Switch between sandboxes in the Journey Optimizer interface using the sandbox switcher
- Assign one or more sandboxes to a role in the Permissions product
- Remove sandbox access from a role
- Configure content access (shared folders) for a sandbox
- Understand how sandboxes relate to roles and permissions

**Glossary:**

- **Sandbox**: A virtual environment partitioning the Journey Optimizer instance into separate, isolated workspaces for development, testing, or production use *(product-specific)*
- **Sandbox switcher**: The control at the top-right of the Journey Optimizer interface, next to the organization name, used to switch between sandboxes *(product-specific)*
- **Shared folder**: A storage folder configured in Admin Console for a sandbox that enables content access; its name must match the sandbox name for content to sync correctly *(product-specific)*

**Guardrails:**

- Sandbox management can only be carried out by a Product or System administrator (hard prerequisite, as stated in the Important note on the page)
- Shared folder names must follow the same syntax as the sandbox name for content to sync to the correct sandbox (as stated on the page)

**Terminology:**

- Do not confuse: "Using a sandbox" (switching to it in the UI using the sandbox switcher) ≠ "Assigning a sandbox" (adding a sandbox to a role in the Permissions product) ≠ "Creating a sandbox" (done in Adobe Experience Platform, not in Journey Optimizer)
- Synonyms: "sandbox" = "virtual environment" in the context of this page
- Do not confuse: "Assign sandboxes" (adding sandboxes to a role in Permissions) ≠ "Manage sandboxes" (creating, resetting, or deleting sandboxes — done in Adobe Experience Platform)

**FAQ:**

- **Q: How do I switch between sandboxes in Journey Optimizer?** — Use the sandbox switcher at the top-right of the screen, next to your organization's name; click the active sandbox and select another from the drop-down list.
- **Q: Who can assign sandboxes to roles?** — Only Product or System administrators.
- **Q: How are sandboxes made available to users?** — Sandboxes are assigned through roles in the Permissions product.
- **Q: What naming convention must shared folders follow?** — The shared folder must have the same name as the sandbox it is associated with (e.g., if the sandbox is called "development," the shared folder must also be called "development").

+++
<!-- ai-accordion-version: 1 | source-hash: 0a5ada9b -->
