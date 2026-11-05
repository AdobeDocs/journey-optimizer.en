---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how administrators create, set conditions for, activate, and manage approval policies that determine which journeys and campaigns require sign-off before they go live.

**Intents:**

* Create an approval policy from **[!UICONTROL Administration]** > **[!UICONTROL Permissions]** > **[!UICONTROL Policies]** and scope it to **[!UICONTROL Journeys]** or **[!UICONTROL Campaigns]**
* Enable **[!UICONTROL Block self-approval]** to prevent creators from approving their own objects
* Define conditions under the **[!UICONTROL If]** menu that determine which object or user triggers an approval request
* Define who validates the request under the **[!UICONTROL Then, send approval request to]** menu, choosing a User Group or an individual User
* Combine multiple conditions using the **[!UICONTROL And]** or **[!UICONTROL Or]** operators
* Activate, edit, deactivate, or duplicate an approval policy

**Glossary:**

* **Approval policy**: A validation process configured by administrators that determines whether a journey or campaign requires approval before activation. *(product-specific)*
* **[!UICONTROL Block self-approval]**: An option that prevents Journey/Campaign creators from approving their own objects. *(product-specific)*
* **Condition**: A rule, built from a **[!UICONTROL Category]**, **[!UICONTROL Matching Rule]**, and **[!UICONTROL Options]**, that defines which object or user triggers an approval request. *(product-specific)*
* **Category**: The type of criterion a condition targets — for example Campaign type, Action, Tags, Object name, Requestor username, or Requestor user group.

**Guardrails:**

* To create approval policies, you must have system or product administrator privileges in Adobe Experience Platform.
* Once activated, policies cannot be edited; to modify conditions, deactivate the policy first (hard limit — page states policies "cannot be edited").
* A policy applies either to Journeys or to Campaigns, selected per policy.

**Terminology:**

* Canonical name: Approval policy — variants: approval policies
* Do not confuse: "[!UICONTROL If]" (condition defining which object or user triggers an approval request) ≠ "[!UICONTROL Then, send approval request to]" (defining who can validate the request)
* Do not confuse: "[!UICONTROL Activate]" (apply a policy) ≠ "[!UICONTROL Deactivate]" (required before editing) ≠ "[!UICONTROL Duplicate]" (copy a policy)
* Do not confuse: "Requestor username" (name and email address of a designated requestor) ≠ "Requestor user group" (name of the user group of designated requestors)

**FAQ:**

* **Q: Where do I create an approval policy?** — From the **[!UICONTROL Administration]** menu, access **[!UICONTROL Permissions]** then **[!UICONTROL Policies]**, click **[!UICONTROL Create]** in the **[!UICONTROL Approval Policy]** tab, choose **[!UICONTROL Approval Policy]**, and confirm.
* **Q: Can I edit a policy after activating it?** — No. Once activated, policies cannot be edited. Deactivate the policy first to modify its conditions.
* **Q: What criteria can target an approval policy?** — Campaign/Journey names, Tags, Channel types, Campaign types, and Requestors.
* **Q: How do I stop users from approving their own work?** — Enable the **[!UICONTROL Block self-approval]** option when creating the policy.

**Personas:**

* **marketer:** Can create an approval policy from Administration, then Permissions, then Policies, scoping it to Journeys or Campaigns. Can enable Block self-approval to prevent Journey or Campaign creators from approving their own objects. Can define conditions under If using Category, Matching Rule, and Options, then set who validates under Then, send approval request to by choosing a User Group or an individual User. The page states that once activated, a policy cannot be edited, and must be deactivated first to modify conditions. Where: "Create approval policies".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** From the Administration menu in Journey Optimizer, access Permissions then Policies.
* **Success check:** You can now activate your approval policy to apply it.

+++

<!-- ai-section-version: 1 | source-hash: c9b3d0da -->
