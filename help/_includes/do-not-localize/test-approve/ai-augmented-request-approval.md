---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how creators submit a journey or campaign for approval, how the available action button depends on whether an active approval policy applies, and how to cancel, edit, and resubmit a request while it is in review.

**Intents:**

* Determine which action button appears (**[!UICONTROL Activate]**, **[!UICONTROL Publish]**, or **[!UICONTROL Request Approval]**) based on active approval policies
* Submit a campaign or journey for review with the **[!UICONTROL Request Approval]** button and an optional message to the approvers
* Understand the auto-approval workflow when no policy applies to the selected object
* Cancel an approval request to return the object to the draft stage, then edit and resubmit it
* Respond to requested changes received through an email and a Journey Optimizer alert

**Glossary:**

* **[!UICONTROL Request Approval]**: The button that submits a campaign or journey for review when one or more active approval policies exist for that object type in the sandbox. *(product-specific)*
* **Auto-approval workflow**: The flow triggered when no approval policy applies to the selected object after clicking **[!UICONTROL Request Approval]**; the object is automatically approved and either activated or published. *(product-specific)*
* **In review**: The state of a campaign or journey after a request is sent, during which the request can be canceled. *(product-specific)*
* **[!UICONTROL Cancel request]**: The action that returns the campaign or journey to the draft stage and notifies the reviewers. *(product-specific)*

**Guardrails:**

* If no approval policy is active for the object type in a sandbox, campaigns show the **[!UICONTROL Activate]** button and journeys show the **[!UICONTROL Publish]** button, allowing activation or publishing without approval.
* If one or more active approval policies exist for the object type in a sandbox, all objects of that type display the **[!UICONTROL Request Approval]** button.
* If no policy applies to the selected object when **[!UICONTROL Request Approval]** is clicked, the auto-approval workflow is triggered and the object is automatically approved and either activated or published.
* While an object is In review, you can cancel the request to return it to the draft stage, then make edits and resubmit it for approval.

**Terminology:**

* Canonical name: Request Approval (button) — variants: Request approval (pane)
* Do not confuse: "[!UICONTROL Activate]" (campaigns, no active policy) ≠ "[!UICONTROL Publish]" (journeys, no active policy) ≠ "[!UICONTROL Request Approval]" (submit for review when a policy is active)
* Do not confuse: "[!UICONTROL Cancel request]" (returns the object to draft and notifies reviewers) ≠ an approver requesting changes
* Do not confuse: an applicable approval policy found (object sent for review) ≠ no applicable policy after clicking Request Approval (auto-approval workflow: automatically approved and activated or published)

**FAQ:**

* **Q: Why do I see Request Approval instead of Activate or Publish?** — Because one or more active approval policies exist for that object type in your sandbox.
* **Q: What if I click Request Approval but no policy actually applies?** — The auto-approval workflow triggers and the object is automatically approved and either activated or published.
* **Q: Can I change an object after submitting it?** — Cancel the request with **[!UICONTROL Cancel request]** to return it to the draft stage, make the edits, then resubmit with the **[!UICONTROL Request approval]** button.
* **Q: How am I notified when an approver requests changes?** — Through an email and a Journey Optimizer alert accessible when clicking the bell icon, in the **[!UICONTROL Requests]** tab.

+++

<!-- ai-section-version: 1 | source-hash: 75c6ec13 -->
