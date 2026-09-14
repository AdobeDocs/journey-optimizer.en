---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure, use, and undelegate the subdomains used to build landing page URLs, either by reusing a subdomain already delegated to Adobe or by delegating a new one.

**Intents**

* Reuse a subdomain already delegated to Adobe for landing pages.
* Configure a new subdomain for landing pages by generating a matching DNS record.
* Identify which subdomain prefixes are reserved or restricted before submitting a configuration.
* Check the delegation status of a landing page subdomain.
* Configure a WAF IP allowlist for a delegated landing page subdomain.
* Undelegate a landing page subdomain that is no longer needed.

**Glossary**

* **Landing page subdomain:** the subdomain used to build a landing page URL, either reused from an existing Adobe delegation or newly delegated for that purpose.
* **Prefix:** the alphanumeric and hyphen string entered by the user that displays in the landing page URL, combined with the selected subdomain.
* **Delegated subdomain** *(product-specific)*: a subdomain already delegated to Adobe that can be reused as a landing page subdomain.
* **Landing page preset:** the configuration object that requires a landing page subdomain to be set up beforehand, from which its subdomain name is picked.

**Guardrails**

* The **[!UICONTROL Manage Landing Page Subdomains]** permission on the production sandbox is required to access and edit landing page subdomains.
* Landing page subdomain configuration is common to all environments; any modification to a landing page subdomain also impacts the production sandboxes.
* Only alphanumeric characters and hyphens are allowed in the prefix.
* The `cdn` and `data` prefixes cannot be used, as they are reserved for internal use.
* The `dmarc` and `spf` prefixes should also be avoided (recommended).
* A subdomain that is already used as a landing page subdomain cannot be selected again.
* Multiple delegated subdomains of the same parent domain cannot be used for landing pages; however, multi-level subdomains of an already-used parent domain are supported.
* Capital letters are not allowed in subdomains.
* After submission, required checks can take up to 4 hours before the subdomain is ready for use.

**Terminology**

* **[!UICONTROL Processing]**, **[!UICONTROL Success]**, and **[!UICONTROL Failed]** are the statuses a landing page subdomain can display during and after delegation.
* Do not confuse "delegating a subdomain" (making it available for use) with "undelegating a subdomain" (removing it from use).

**FAQ**

* **Can I reuse a subdomain already delegated to Adobe for landing pages?** Yes, as long as it is not already used as a landing page subdomain.
* **What prefixes cannot be used?** The `cdn` and `data` prefixes cannot be used, as they are reserved for internal use; the `dmarc` and `spf` prefixes should also be avoided.
* **How long does subdomain validation take?** Required checks can take up to 4 hours after submission.
* **Can I use multiple delegated subdomains of the same parent domain?** No, but multi-level subdomains of an already-used parent domain are supported.
* **What happens if I fail to create the validation record on my hosting solution?** The subdomain is marked as **[!UICONTROL Failed]**.
* **How do I undelegate a landing page subdomain?** Unpublish the associated landing pages, optionally delete the CNAME DNS record without deleting an original email subdomain, then reach out to your Adobe representative.

+++

<!-- ai-section-version: 1 | source-hash: 84514bb0 -->
