---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create and publish public landing pages, which are public landing pages that anyone can open from a shared URL and use to submit form data stored in a non-profile enabled dataset, without identifying the visitor.

**Intents**

* Publish a landing page on a public URL that anonymous visitors can open without being identified.
* Capture data from anonymous visitors with a form, in a non-profile enabled dataset.
* Check the prerequisites before creating a public landing page.
* Create, test, and publish a public landing page.
* Share the public URL of a public landing page in emails, SMS messages, or on a website.
* Identify the limitations that apply to public landing pages.

**Glossary**

* **Public landing page:** a Data Capture landing page published on a public URL that anyone can open, without being identified. Visitors can fill in a form on the page and submit data.
* **Data Capture landing page:** the only type of landing page that lets you embed a specific form, and therefore the type used for public landing pages.
* **Non-profile enabled dataset:** the type of dataset that is strongly recommended to store data submitted through a public landing page. With a profile-enabled dataset, many lead profiles might be created unnecessarily and existing profiles might be corrupted.
* **Require identified users** *(product-specific)*: the option that restricts access to identified profiles when enabled. It must be disabled for the page to be accessible to anonymous visitors.
* **Cloudflare migration:** the migration of a landing page subdomain to Cloudflare, required to use public landing pages when you reuse a landing page subdomain that you already configured.
* **Landing page preset:** the configuration object, linked to a subdomain, from which a landing page is created.
* **Form preset:** the configuration object, linked to a non-profile enabled dataset for public landing pages, from which a form is created and published.

**Guardrails**

* Public landing pages are available in Limited Availability; contact your Adobe representative to request access.
* The landing page subdomain must be migrated to Cloudflare, a landing page preset must exist for that subdomain, and a form, preferably linked to a non-profile enabled dataset, must be created and published from a form preset.
* Form data should be stored in non-profile enabled datasets; public landing pages are not meant to create or enrich profiles, which can happen with a profile-enabled dataset.
* Reporting is not supported for public landing pages.
* Managing allowed IPs is not supported for subdomains used for public landing pages.
* Public landing pages cannot be copied to another sandbox using Sandbox tooling.
* Personalization based on profile data should not be used in the content of a public landing page, because visitors are not identified.
* Submitted data can take up to 15 minutes to be processed and available for use.

**Terminology**

* Do not confuse a public landing page with a Data Capture landing page for known profiles: the latter is usually opened from a personalized link so that the visitor's profile can be identified, and the former is opened from a public URL without identification.
* Data submitted through a public landing page is stored in a dataset, not in a profile.

**FAQ**

* **Who can open a public landing page?** Anyone with the URL.
* **Which type of landing page must I select?** Data Capture, as only Data Capture landing pages let you embed a specific form.
* **Where is the data submitted by visitors stored?** In the non-profile enabled dataset defined in the form preset, not in a profile.
* **Do submissions create or enrich profiles?** Not with a non-profile enabled dataset, which is strongly recommended. With a profile-enabled dataset, lead profiles might be created unnecessarily and existing profiles might be corrupted.
* **Which option must be disabled so that anonymous visitors can access the page?** The **[!UICONTROL Require identified users]** option.
* **Do I need to migrate my landing page subdomain to Cloudflare?** Yes, when you reuse a landing page subdomain that you already configured.
* **Can I use allowed IPs with a public landing page?** No, managing allowed IPs is not supported for subdomains used for public landing pages.
* **Is reporting available for public landing pages?** No.
* **How long before submitted data is available?** Up to 15 minutes.

+++

<!-- ai-section-version: 1 | source-hash: f50217a3 -->
