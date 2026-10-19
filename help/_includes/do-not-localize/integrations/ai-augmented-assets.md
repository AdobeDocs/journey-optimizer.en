---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Adobe Experience Manager Assets integration in Journey Optimizer to store, manage, discover, and insert digital assets into email content, with either an Assets Essentials or Assets as a Cloud Service repository.

**Intents:**

* Access Assets Essentials or Assets as a Cloud Service from the Journey Optimizer left menu
* Upload assets to a folder and insert them into email content with the Asset picker in the Email Designer
* Switch between Assets repositories using the repository selector
* Edit assets with Adobe Photoshop Express Edit mode
* Use Dynamic Media URLs when authoring emails
* Troubleshoot and resolve broken images caused by asset expiration

**Glossary:**

* **Assets as a Cloud Service**: A cloud solution for Digital Asset Management and Dynamic Media operations, accessible from Journey Optimizer *(product-specific)*
* **Assets Essentials**: The Assets as a Cloud Service lightweight solution for unified asset management and collaboration *(product-specific)*
* **Content Advisor**: An AI-powered, unified interface that is replacing the Asset Selector and Content Fragment selector for discovering and selecting Assets, Content Fragments, and Dynamic Media within AJO authoring workflows *(product-specific)*
* **Asset picker**: The menu in the left pane of the Email Designer used to browse Assets folders and drag assets into email content *(product-specific)*
* **Time-To-Live (TTL)**: An asset lifecycle policy period after which assets may be removed from CDN storage *(product-specific)*

**Guardrails:**

* Updates made in Assets as a Cloud Service do not automatically propagate to live email campaigns; changes must be manually re-selected in the Email Designer.
* The asset TTL is set to 730 days for all Journey Optimizer organizations; it is managed by AJO backend services and is not currently configurable by customers.
* After the TTL period expires, assets may be removed from the CDN, which can result in broken images in emails that reference those assets.
* Using Assets Essentials requires adding users to the Assets Essentials Consumer Users and/or Assets Essentials Users Product profiles; using Assets as a Cloud Service requires adding users to Assets Cloud Services.
* For Journey Optimizer products obtained before January 6, 2022, Assets Essentials must be deployed for the organization.
* A Journey Optimizer user can edit the Assets as a Cloud Service repository only if entitled as a standard user and holding the Edit permission on the repository.
* Republishing requirements to restore expired assets apply to all environments (production, stage, development).

**Terminology:**

* Canonical name: Adobe Experience Manager Assets — Acronym: n/a — variants: Assets Essentials, Assets as a Cloud Service
* Do not confuse: "Assets Essentials" ≠ "Assets as a Cloud Service" (separate, not-in-sync repositories)
* Do not confuse: "Asset Selector" and "Content Fragment selector" (being replaced) ≠ "Content Advisor" (the replacement experience)

**FAQ:**

* **Q: Are changes in Assets as a Cloud Service reflected automatically in Journey Optimizer?** — No; updates do not automatically propagate to live email campaigns, and any change must be manually re-selected in the Email Designer.
* **Q: Can I use Dynamic Media URLs while authoring emails?** — Yes; paste the URLs instead of selecting from the Asset Selector.
* **Q: Why do images sometimes fail to load in sent emails?** — Assets managed via Experience Manager are subject to a TTL; after it expires (currently 730 days) they may be removed from the CDN, causing broken images.
* **Q: How do I fix broken images caused by asset expiration?** — Republish the affected assets in Experience Manager, update content references (create a draft or clone of the content fragment, re-add or re-select the asset, publish), and proactively review and republish assets used in active campaigns.
* **Q: Can I switch between repositories?** — Yes; select the Account icon in the upper right and click Select Repository.

+++

<!-- ai-section-version: 1 | source-hash: 2cf1f993 -->
