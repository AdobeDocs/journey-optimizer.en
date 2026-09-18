---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page walks product and system administrators through the three role management tasks in the Permissions product: assigning an existing role to a user, editing a role's permissions, and creating a new custom role with specific permissions and sandboxes.

**Intents:**

- Assign a built-in or custom role to a user in Journey Optimizer
- Edit the permissions of an existing role (adding or removing rights)
- Create a new custom role with specific permissions and sandbox assignments
- Understand who has the authority to perform role and permission management

**Glossary:**

- **Role**: A collection of users sharing the same permissions and sandboxes, used to manage access within an organization *(product-specific)*
- **Permissions product**: The Adobe CX Enterprise interface (accessed via [!DNL Permissions]) where roles, permissions, and sandboxes are configured *(product-specific)*
- **Built-in role**: A pre-existing role with a defined permission set available for immediate assignment without custom configuration *(product-specific)*

**Guardrails:**

- Only Product or System administrators can assign, edit, or create roles (hard prerequisite, as stated in the Important note on the page)
- Changes made to a built-in or custom role affect all users assigned to that role (as stated in the Important note on the page)

**Terminology:**

- Canonical name: Permissions product — variants: Adobe Permissions, Permissions UI, Adobe CX Enterprise Permissions
- Do not confuse: "Assign a role" (adding a user to an existing role) ≠ "Create a role" (defining a new role with its own permissions and sandboxes from scratch)
- Do not confuse: "Edit an existing role" (modifying permissions or sandboxes on an existing role; affects all assigned users) ≠ "Create a new role" (building a new role without affecting any existing role or its users)

**FAQ:**

- **Q: Who can assign roles to users in Journey Optimizer?** — Only Product or System administrators.
- **Q: What happens if I edit a built-in role's permissions?** — Changes affect all users currently assigned to that role.
- **Q: Where do I go in the product to manage roles?** — In the Permissions product, navigate to the Roles tab.
- **Q: After a role is assigned, does the user receive a notification?** — Yes; the user automatically receives an email redirecting them to the instance.

+++
<!-- ai-accordion-version: 1 | source-hash: 09d3612e -->
