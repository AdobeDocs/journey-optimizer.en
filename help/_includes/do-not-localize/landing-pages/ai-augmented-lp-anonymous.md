---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create and publish anonymous landing pages, which are public landing pages that anyone can open from a shared URL and use to submit form data stored in a non-profile enabled dataset, without identifying the visitor.

**Intents**

* Publish a landing page on a public URL that anonymous visitors can open without being identified.
* Capture data from anonymous visitors with a form, in a non-profile enabled dataset.
* Check the prerequisites before creating an anonymous landing page.
* Create, test, and publish an anonymous landing page.
* Share the public URL of an anonymous landing page in emails, SMS messages, or on a website.
* Identify the limitations that apply to anonymous landing pages.

**Glossary**

* **Anonymous landing page:** a Data Capture landing page published on a public URL that anyone can open, without being identified. Visitors can fill in a form on the page and submit data.
* **Data Capture landing page:** the only type of landing page that lets you embed a specific form, and therefore the type used for anonymous landing pages.
* **Non-profile enabled dataset:** the only type of dataset in which data submitted through an anonymous landing page can be stored.
* **Require identified users** *(product-specific)*: the option that restricts access to identified profiles when enabled. It must be disabled for the page to be accessible to anonymous visitors.
* **Cloudflare migration:** the migration of a landing page subdomain to Cloudflare, required to use anonymous landing pages when you reuse a landing page subdomain that you already configured.
* **Landing page preset:** the configuration object, linked to a subdomain, from which a landing page is created.
* **Form preset:** the configuration object, linked to a non-profile enabled dataset for anonymous landing pages, from which a form is created and published.

**Guardrails**

* Anonymous landing pages are available in Limited Availability; contact your Adobe representative to request access.
* The landing page subdomain must be migrated to Cloudflare, a landing page preset must exist for that subdomain, and a form linked to a non-profile enabled dataset must be created and published from a form preset.
* Form data can only be stored in non-profile enabled datasets; anonymous landing pages cannot create or enrich profiles.
* Reporting is not supported for anonymous landing pages.
* Managing allowed IPs is not supported for subdomains used for anonymous landing pages.
* Anonymous landing pages cannot be copied to another sandbox using Sandbox tooling.
* Personalization based on profile data should not be used in the content of an anonymous landing page, because visitors are not identified.
* Submitted data can take up to 15 minutes to be processed and available for use.

**Terminology**

* Do not confuse an anonymous landing page with a Data Capture landing page for known profiles: the latter is usually opened from a personalized link so that the visitor's profile can be identified, and the former is opened from a public URL without identification.
* Data submitted through an anonymous landing page is stored in a dataset, not in a profile.

**FAQ**

* **Who can open an anonymous landing page?** Anyone with the URL.
* **Which type of landing page must I select?** Data Capture, as only Data Capture landing pages let you embed a specific form.
* **Where is the data submitted by visitors stored?** In the non-profile enabled dataset defined in the form preset, not in a profile.
* **Do submissions create or enrich profiles?** No.
* **Which option must be disabled so that anonymous visitors can access the page?** The **[!UICONTROL Require identified users]** option.
* **Do I need to migrate my landing page subdomain to Cloudflare?** Yes, when you reuse a landing page subdomain that you already configured.
* **Can I use allowed IPs with an anonymous landing page?** No, managing allowed IPs is not supported for subdomains used for anonymous landing pages.
* **Is reporting available for anonymous landing pages?** No.
* **How long before submitted data is available?** Up to 15 minutes.

+++

<!-- ai-section-version: 1 | source-hash: f50217a3 -->
