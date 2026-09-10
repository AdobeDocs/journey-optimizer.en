---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to define personalized values for dynamic subdomains, header parameters, and URL tracking parameters at the email channel configuration level, and how to view and check those settings in a campaign or journey.

**Intents:**

* Set up dynamic subdomains based on conditions in an email channel configuration
* Personalize email header parameters in a configuration
* Personalize URL tracking parameters in a configuration
* View read-only configuration details from within a campaign or journey
* Check a personalized configuration for errors using content simulation

**Glossary:**

* **Dynamic Subdomain**: A configuration option that lets you set up multiple sending subdomains selected by conditions defined in the personalization editor, instead of creating a separate configuration per case *(product-specific)*
* **Header parameters / Sender headers**: Configuration fields (for example From and Reply to names and emails) that can be given personalized values *(product-specific)*
* **URL tracking parameters**: Configuration-level parameters that are automatically appended to the end of content URLs and can be personalized with profile attributes *(product-specific)*
* **Simulate content**: The action to test content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: The option (from the Simulate content dropdown) to preview content with test profiles *(product-specific)*

**Guardrails:**

* You can add up to 50 dynamic subdomains per configuration.
* All Header parameters and optional Sender headers fields can be personalized, except the Error email prefix field.
* When editing an email configuration, you cannot add new profile attributes to header parameters — you must create a new channel configuration instead.
* For header personalization, only Profile attributes and Helper functions can be selected.
* If you disable the Dynamic Subdomain option after setting up dynamic subdomains, all dynamic values are removed; select a subdomain and submit the configuration for the change to take effect.
* Certain subdomains may be unavailable for selection due to pending feedback loop registration, which may take up to 10 business days.
* If a subdomain does not resolve for a selected test profile, or a profile has no value for a required header parameter, the email is not sent to that test profile.
* When dynamic subdomains are configured, the From email and Error email suffixes are populated from the resolved dynamic subdomain; Sender email, when set, is a full address and is not built from that subdomain suffix.

**Terminology:**

* Canonical name: Personalize email configuration settings — Acronym: n/a — variants: surface personalization, dynamic subdomains, personalized header, personalized URL tracking
* Synonyms: "Simulate content (AEP profiles)" = "preview with test profiles"
* Do not confuse: "Simulate content" (test content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview using test profiles)
* Do not confuse: "From email / Error email suffixes" (built from the resolved dynamic subdomain) ≠ "Sender email" (a full address, not built from that suffix)

**FAQ:**

* **Q: How many dynamic subdomains can a configuration have?** — Up to 50.
* **Q: Which header field cannot be personalized?** — The Error email prefix field; all other Header parameters and optional Sender headers fields can be personalized.
* **Q: Can I add a new profile attribute to header parameters when editing a configuration?** — No; you must create a new channel configuration instead.
* **Q: What happens if I disable the Dynamic Subdomain option?** — All dynamic values are removed; select a subdomain and submit the configuration for the change to take effect.
* **Q: How do I check a personalized configuration for errors?** — Preview the content using Simulate content, or Simulate content then Simulate content (AEP profiles) with a test profile; view details on the read-only Delivery settings screen.
* **Q: Why might a subdomain not resolve for a test profile?** — The profile has no value for the attribute used in the conditions (for example Country), or its value is not associated with any subdomain in the configuration; in that case the email is not sent to that test profile.

+++

<!-- ai-section-version: 1 | source-hash: 7d5f8680 -->
