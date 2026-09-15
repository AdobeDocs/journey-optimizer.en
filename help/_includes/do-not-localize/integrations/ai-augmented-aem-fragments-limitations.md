---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the key considerations and troubleshooting steps for Adobe Experience Manager Content Fragments in Journey Optimizer, covering fragment types, multilingual content, repository access, personalization, updates, caching, and common errors.

**Intents:**

* Understand which Content Fragment types and variations are supported
* Plan multilingual content when there is no automatic language fallback
* Know that Journey Optimizer integrates with the Publish tier only
* Identify which personalization inputs are supported
* Understand update, versioning, caching, and proofing behavior
* Diagnose common errors such as missing tags, undefined variables, and broken images

**Glossary:**

* **Content Fragment variation**: An alternative version of a fragment selected when inserting it; if none is selected, the Main variation is used *(product-specific)*
* **Main variation**: The fragment's primary content in Adobe Experience Manager, used when no variation is selected *(product-specific)*
* **Publish tier**: The Adobe Experience Manager tier Journey Optimizer integrates with, exposing Content Fragments through a public, unauthenticated endpoint *(product-specific)*
* **Access denied (CPES) error**: An error indicating the user role is not authorized to access certain profile or contextual attributes used in personalization *(product-specific)*
* **Proof**: A preview that always reflects the most recently published version of the Content Fragment *(product-specific)*

**Guardrails:**

* Journey Optimizer integrates with the Adobe Experience Manager Publish tier only; Content Fragments are available through a public, unauthenticated endpoint. Author repositories may appear in the selector, but only fragments published to Publish can be used.
* Personalization supports profile attributes, contextual attributes, static strings, and pre-declared variables; derived or computed attributes are not supported.
* There is no automatic language resolution or fallback between variations; each variation must be authored, tagged, and published in Adobe Experience Manager.
* Updates require manual republication from Adobe Experience Manager; there is no automatic version reconciliation.
* After a successful update, changes are typically available within about 5 minutes for unitary journeys and in the next batch for batch use cases.
* Proofs always reflect the most recently published version; you cannot lock a historical version for proofing.
* Only approved and published Content Fragments are displayed in the Journey Optimizer selector.
* The Adobe Experience Manager tag must use the format `ajo-enabled:{OrgId}/{SandboxName}` with the correct Organization ID and Sandbox Name and no spaces or incorrect separators.
* Image fields must use absolute URLs (`https://...`); relative paths from Adobe Experience Manager are not supported.

**Terminology:**

* Canonical name: Content Fragment — Acronym: n/a — variants: AEM Content Fragment, fragment
* Synonyms: "Main" = "Main variation"
* Do not confuse: "Published" (a Content Fragment status Journey Optimizer surfaces) ≠ "Modified" (a status Journey Optimizer also surfaces, still using the latest published version)

**FAQ:**

* **Q: Which Adobe Experience Manager tier does Journey Optimizer use for Content Fragments?** — The Publish tier only; fragments are available through a public, unauthenticated endpoint, and only fragments published to Publish can be used.
* **Q: What personalization is not supported in Content Fragments?** — Derived or computed attributes; supported inputs are profile attributes, contextual attributes, static strings, and pre-declared variables.
* **Q: How long after publishing are changes available?** — Typically within about 5 minutes for unitary journeys and in the next batch for batch use cases, after manual republication in Adobe Experience Manager.
* **Q: Why is my Content Fragment not visible in the selector?** — The tag syntax may not match `ajo-enabled:{OrgId}/{SandboxName}`, or the fragment may be in draft or unpublished state; correct the tag and republish, and ensure the fragment is approved and published.
* **Q: Why does an image in my Content Fragment not render?** — The image URL may be a relative path; use absolute URLs (`https://...`), since relative paths from Adobe Experience Manager are not supported.
* **Q: Can I proof a specific historical version of a fragment?** — No; proofs always reflect the most recently published version and you cannot lock a historical version for proofing.

+++

<!-- ai-section-version: 1 | source-hash: c463328a -->
