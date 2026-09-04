---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to personalize email URLs with profile attributes — including complete or base URLs and per-link tracking parameters — while keeping links valid and trackable.

**Intents:**

* Personalize a URL with profile attributes in the Email Designer
* Personalize an entire URL or the base domain of a URL
* Add accepted domains to the allowed list to enable complete or base URL personalization
* Understand the click tracking limitation for dynamically generated URLs
* Personalize URL tracking parameters for an individual link

**Glossary:**

* **Personalized URL**: An email link generated dynamically from profile attributes to deliver contextual experiences (recipient-specific links or appended dynamic parameters) *(product-specific)*
* **Complete/base URL personalization**: Personalizing the entire URL or the base domain of a URL, which requires the domain to be on the allowed list *(product-specific)*
* **Allowed list - domains**: The list of accepted domains that may be used in complete or base URL personalization, to help prevent unsafe redirects *(product-specific)*
* **Per-link URL tracking parameter**: A recipient-specific tracking parameter appended to a single link, personalized with a profile attribute in the Email Designer *(product-specific)*

**Guardrails:**

* Personalization is only available for External link, Unsubscription link, and Opt-Out link types.
* In the personalization editor, helper functions and audiences membership are disabled for security reasons; spaces are not supported in the personalization tokens used inside URLs.
* To enable complete or base URL personalization, you must first add your accepted domains to the allowed list.
* Viewing, adding, or removing domains from the allowed list requires the Manage messages general settings and View messages general settings permissions.
* When adding a domain, do not include https:// or a trailing slash (enter `www.example.com` or `example.com`), or the domain is rejected.
* If you remove a domain already in use in a personalized URL, the safety of the link cannot be guaranteed; update any personalized URLs referencing it first.
* Dynamically generated URLs (where the entire URL or base domain resolves from a profile attribute at send time) have a known limitation: click data may not appear in journey or campaign reports.
* The resolved URL must start with `http` or `https` for every recipient; if it does not, tracking is silently skipped for that link.

**Terminology:**

* Canonical name: URL personalization — Acronym: n/a — variants: personalized URL, complete/base URL personalization
* Synonyms: "Allowed list - domains" = "allowed list of accepted domains"
* Do not confuse: "personalize a URL" (adding profile attributes to a URL) ≠ "complete/base URL personalization" (personalizing the entire URL or base domain, which requires the allowed list)
* Do not confuse: "configuration-level URL tracking" (applies to all URLs in the message) ≠ "per-link URL tracking parameter" (appended to a single link)

**FAQ:**

* **Q: Which link types support personalization?** — Only External link, Unsubscription link, and Opt-Out.
* **Q: What do I need before personalizing a complete or base URL?** — You must first add your accepted domains to the allowed list.
* **Q: Which permissions manage the allowed domains list?** — Manage messages general settings and View messages general settings.
* **Q: Why might click data be missing for a personalized link?** — For dynamically generated URLs, the tracking redirect is applied at design time before the final URL is known, so click data may not appear in journey or campaign reports; the resolved URL must also start with http/https or tracking is silently skipped.
* **Q: How can I keep reliable click tracking with personalization?** — Use a fixed base URL and append personalized parameters only, or pre-generate a personalized URL per recipient, store it as a profile attribute, and reference it in your content.
* **Q: How do I verify the final personalized URL?** — Send a proof and click the link in the received email; the URL should display the tracking parameter.

+++

<!-- ai-section-version: 1 | source-hash: 81ee0261 -->
