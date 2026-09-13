---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Adobe Experience Platform Privacy Service to submit and manage data access and deletion requests for Adobe Journey Optimizer so you can fulfill data subject rights and automate compliance with privacy regulations.

**Intents:**

* Understand how Privacy Service manages data access and deletion requests
* Submit privacy requests through the Privacy Service UI or API
* Identify the product code and upstream services required for delete requests
* Understand the prerequisites and required field values for requests
* Know which privacy regulations can be specified on a request

**Glossary:**

* **Privacy Service**: Adobe Experience Platform service that provides a RESTful API and user interface to manage customer requests to access and delete personal customer data *(product-specific)*
* **Privacy request**: a data access or data deletion request submitted for Adobe Journey Optimizer, created and managed from the [!UICONTROL Requests] menu *(product-specific)*
* **CJM**: the Adobe product code for Adobe Journey Optimizer, used in the API `include` field *(product-specific)*
* **Upstream services**: Profile (`profileService`), AEP Data Lake (`AdobeCloudPlatform`), and Identity (`identity`), to which delete requests must also be submitted to prevent Journey Optimizer from reinjecting the deleted data *(product-specific)*
* **[!UICONTROL Requests]**: the menu from which privacy requests can be created and managed *(product-specific)*

**Guardrails:**

* Privacy Service supports two types of requests: data access and data deletion
* For access requests, specify "Adobe Journey Optimizer" from the UI, or "CJM" as the product code in the API
* For delete requests, in addition to the "Adobe Journey Optimizer" request you must also submit delete requests to three upstream services — Profile (`profileService`), AEP Data Lake (`AdobeCloudPlatform`), and Identity (`identity`) — otherwise the "Adobe Journey Optimizer" request remains in the "processing" state
* For delete requests, if you do not explicitly include the product name and all applicable namespaces, data is not removed from Adobe Journey Optimizer
* Making a privacy request to Adobe Journey Optimizer will not remove data from all these systems; each system must be called individually
* Prerequisites: an Adobe organization ID, and an identity identifier of the person to act on with the corresponding namespace(s)
* The regulation value must be one of: `gdpr`, `ccpa`, `pdpa`, `lgpd_bra`, or `nzpa_nzl`

**Terminology:**

* Canonical name: Privacy request — variants: data access request, data deletion request
* Synonyms: "Adobe Journey Optimizer" (product name in the UI) = "CJM" (product code in the API)
* Do not confuse: "data access" request ≠ "data deletion" request
* Do not confuse: "Adobe Journey Optimizer" request ≠ the three upstream services (Profile, AEP Data Lake, Identity) that delete requests must also target

**FAQ:**

* **Q: What are the two types of privacy requests?** — Data access and data deletion.
* **Q: What product code represents Adobe Journey Optimizer in the API?** — CJM.
* **Q: Why must delete requests also target upstream services?** — To prevent Journey Optimizer from reinjecting the deleted data; otherwise the request remains in the "processing" state.
* **Q: Which upstream services must be included in a delete request?** — Profile (`profileService`), AEP Data Lake (`AdobeCloudPlatform`), and Identity (`identity`).
* **Q: Which regulations can be specified?** — `gdpr`, `ccpa`, `pdpa`, `lgpd_bra`, or `nzpa_nzl`.
* **Q: Does a privacy request to Adobe Journey Optimizer remove data from all systems?** — No, each system must be called individually to make sure the request is handled.

+++

<!-- ai-section-version: 1 | source-hash: 514b7051 -->
