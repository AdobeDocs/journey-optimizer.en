---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the default Loyalty Challenges roles, available permissions for custom roles, role capabilities, sandbox scope, how to assign roles to users, and how to troubleshoot access issues.

**Intents:**

* Identify the three default Loyalty roles and what each one permits.
* Compare role capabilities across Challenges, primary organization configuration, reward configuration, event configuration, product catalog, and insights.
* Understand that default roles are scoped to the Prod sandbox and create a custom role for other sandboxes.
* Select permissions when building a custom role for a non-Prod sandbox.
* Assign roles to users directly or through user groups.
* Troubleshoot why a user cannot access Loyalty Challenges or a related feature.

**Glossary:**

* **Loyalty Administrator**: role providing full administrative access to all Loyalty features: challenges, configuration, product catalog, and insights *(product-specific)*
* **Loyalty Practitioner**: role for business owners who manage the full challenge lifecycle and edit primary configuration; reward configuration, event configuration, and product catalog access are read-only; deletion and advanced configuration writes are not permitted *(product-specific)*
* **Loyalty Analyst**: role providing read-only access to challenges, product catalog, and insights, for reporting and audit purposes *(product-specific)*
* **Manage Loyalty Advanced Configuration**: permission to manage reward endpoints and event transformation settings, including read/write access to sensitive credential values *(product-specific)*
* **Develop Loyalty Challenges**: custom-role permission to create and edit challenges via API; delete and lifecycle actions are not permitted *(product-specific)*

**Guardrails:**

* Role assignment is required before users can perform Loyalty operations.
* Users without an assigned role are denied access to Loyalty service endpoints.
* Default Loyalty roles (Loyalty Administrator, Loyalty Practitioner, Loyalty Analyst) are scoped to the Prod sandbox only.
* Primary organization configuration deletion is permitted for Loyalty Administrator only, not for Loyalty Practitioner.
* Reward configuration write access or access to sensitive values, and event configuration write access, are permitted for Loyalty Administrator only.
* Product catalog import or edit, and insights write or KPI configuration update, are permitted for Loyalty Administrator only.
* Loyalty Analyst has no create, edit, delete, publish, unpublish, archive, or journey-generation-trigger access to Challenges.

**Prerequisites and permissions:**

* To grant users access to a non-Prod sandbox (such as staging or development), create a custom role for that sandbox and assign the same permissions as the corresponding default role.
* Only Product administrators and System administrators can manage users, groups, and roles.

**Terminology:**

* Canonical names: Loyalty Administrator, Loyalty Practitioner, Loyalty Analyst — the three default Loyalty roles.
* Do not confuse: "Manage Loyalty Primary Configuration" (create, edit, and delete) ≠ "Configure Loyalty Primary Configuration" (create and edit; deletion is not permitted).
* Do not confuse: "Manage Loyalty Challenges" (full challenge operations including delete, publish, unpublish, archive, and trigger journey generation) ≠ "Develop Loyalty Challenges" (create and edit via API only; delete and lifecycle actions are not permitted) ≠ "View Loyalty Challenges" (view only).
* Do not confuse: "Manage Loyalty Insights" (view, update KPI configuration, trigger the insights pipeline) ≠ "Develop Loyalty Insights" (view insights data and update insight cards) ≠ "View Loyalty Insights" (view AI-generated insight cards, health vitals, and challenge performance data only).

**FAQ:**

* **Q: What are the three default Loyalty roles?** — Loyalty Administrator, Loyalty Practitioner, and Loyalty Analyst.
* **Q: What sandbox are default Loyalty roles scoped to?** — The Prod sandbox only.
* **Q: How do I give a user access to a non-Prod sandbox?** — Create a custom role for that sandbox and assign the same permissions as the corresponding default role.
* **Q: Can a Loyalty Practitioner delete primary organization configuration?** — No, deletion is not permitted for Loyalty Practitioner.
* **Q: Who can manage users, groups, and roles?** — Only Product administrators and System administrators.
* **Q: What access does a Loyalty Analyst have?** — Read-only access to challenges, product catalog, and insights, for reporting and audit purposes.

**Troubleshooting:**

* Symptom: user cannot access Loyalty Challenges or a related feature. Checks: the user is assigned to a Loyalty role; the role includes the sandbox where Loyalty Challenges is enabled; the role includes the permission required for the action; for non-Prod sandboxes, a custom role has been created for that sandbox; the organization and sandbox are enabled for Loyalty Challenges. If issues persist after permissions are updated, contact your Adobe representative.

**Best practices:**

* Assign users directly to a role for small teams or one-off assignments.
* Use user groups to manage access by department or function at scale.

**Related pages:**

* For step-by-step instructions on managing roles, groups, and users: Manage users and roles (administration/permissions.md)
* For step-by-step instructions on managing roles, groups, and users: Built-in permissions (administration/ootb-permissions.md)

**Personas:**

* **admin:** Can assign a role to users directly, or create a user group and assign both users and a role to the group. Can create a custom role for a non-Prod sandbox and assign it the same permissions as the corresponding default role. The page states that default Loyalty roles are scoped to the Prod sandbox only. Where: "Assign roles to users".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Assign an appropriate role to each user who will use the service.
* **Success check:** The assigned user can perform Loyalty operations and is not denied access to Loyalty service endpoints.
* **Next:** For step-by-step instructions for managing roles, groups, and users: Manage users and roles (administration/permissions.md); For built-in permissions details for managing roles, groups, and users: Built-in Roles (administration/ootb-permissions.md)

+++

<!-- ai-section-version: 1 | source-hash: 6efb20b5 -->
