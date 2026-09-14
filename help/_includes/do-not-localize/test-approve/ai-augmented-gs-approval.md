---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the embedded approval process in Journey Optimizer, covering the permissions it requires, the end-to-end policy-to-publish workflow, and how to monitor requests so stakeholders sign off before journeys and campaigns go live.

**Intents:**

* Understand the embedded approval process that keeps journeys and campaigns locked during review
* Assign the **Approve & publish Campaigns** and **Approve & publish Journeys** permissions
* Follow the workflow from approval policy setup to submission, review, and activation
* Monitor approval and change requests using the **[!UICONTROL Show Audit Trail]** icon
* Understand which policy applies when several active policies could match

**Glossary:**

* **Approval policy**: A policy that defines the conditions under which a journey or campaign requires approval before it can go live. *(product-specific)*
* **In Review**: The locked state a campaign or journey enters after submission, during which no edits can be made unless the request is canceled. *(product-specific)*
* **[!UICONTROL Show Audit Trail]**: An icon on the journey canvas or campaign review screen used to monitor the approval and change requests submitted for an object. *(product-specific)*
* **Approve & publish Campaigns / Approve & publish Journeys**: The permissions required to approve and publish campaigns and journeys respectively. *(product-specific)*

**Guardrails:**

* To approve and publish journeys and campaigns, users need the **Approve & publish Campaigns** and **Approve & publish Journeys** permissions.
* Campaigns and journeys only need to be submitted for approval if an approval policy is in place; if no policy applies, the creator can publish directly.
* During review, campaigns and journeys remain in a locked state so that no changes or unintended activations occur before all approvals are in place.
* When several active approval policies could apply to the same object, the policy activated most recently takes precedence.

**Terminology:**

* Canonical name: approval process — variants: approval workflow
* Do not confuse: "Draft" (editable state, and the state an object returns to when a request is canceled or changes are requested) ≠ "In Review" (locked state during approval)
* Do not confuse: "Approve & publish Campaigns" (requires the Campaigns resource) ≠ "Approve & publish Journeys" (requires the Journeys resource)

**FAQ:**

* **Q: Do I need an approval policy for every campaign or journey?** — No. Policies are conditional; create one only to enforce review for a specific set. If no policy applies, the creator can publish directly.
* **Q: What happens if the approver is unavailable?** — The request stays In Review until an approver acts. You can cancel it, returning the item to Draft, and resubmit, or an admin can add additional approvers to the policy.
* **Q: Can I edit a campaign or journey while it is pending approval?** — No. It is in a locked In Review state; the creator or an approver must cancel the request first, which returns it to Draft.
* **Q: Which policy applies when more than one could match?** — The policy activated most recently takes precedence, and its approver user groups are the ones notified and governing the request.
* **Q: If a requestor belongs to multiple user groups, can they choose which group receives the request?** — No. The user groups specified in the applicable policy are notified automatically.

+++

<!-- ai-section-version: 1 | source-hash: a2207ec5 -->
