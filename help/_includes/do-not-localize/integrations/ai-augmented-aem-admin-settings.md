---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how an administrator connects a sandbox to an Adobe Experience Manager repository in the AEM Integration menu, choosing author-only or publish access, custom domains, and authentication, so marketers can use AEM Content Fragments in journeys and campaigns.

**Intents:**

* Connect a sandbox to an Adobe Experience Manager as a Cloud Service or Managed Service repository
* Create a repository configuration from Administration > Channels > AEM Integration
* Choose between Author only setup and Publish instance setup
* Enable authentication by sending service credentials to the publish instance
* Provide a custom domain when the default AEM publish host is blocked
* Confirm the integration by testing with a Content Fragment

**Glossary:**

* **AEM Integration**: The Administration menu where repository settings are created, edited, or disabled; saves settings per sandbox *(product-specific)*
* **Author only setup**: A configuration where Journey Optimizer reads Content Fragments from the Adobe Experience Manager author environment only *(product-specific)*
* **Publish instance setup**: The configuration that turns on publish instance settings, used when the publish instance is authenticated or requires a custom publish domain *(product-specific)*
* **Send token to publish instance**: An option that includes service credentials with requests to the publish instance *(product-specific)*
* **Service Credential JSON**: The Adobe Experience Manager service credential pasted for authentication of publish instance requests *(product-specific)*
* **Content Advisor**: The selector window used to pick the Content Fragment that confirms the integration works *(product-specific)*

**Guardrails:**

* AEM Integration saves repository settings per sandbox; each sandbox keeps its own integrations and they do not apply across sandboxes.
* Only one integration is stored per organization, sandbox, and Adobe Experience Manager repository; saving a new integration for the same combination replaces the previous settings and only the latest configuration is kept.
* With Author only setup, replication from author to publish and live publish updates are not supported.
* For an Adobe Experience Manager Managed Services repository, the AMS repository hostname must end with `adobecqms.net`.
* Authenticating the publish instance requires enabling Send token to publish instance and pasting a valid Service Credential JSON.
* When you save with a test Content Fragment selected, validation runs automatically; if validation fails, an error list is displayed so you can fix the configuration.

**Terminology:**

* Canonical name: AEM Integration — Acronym: n/a — variants: Adobe Experience Manager Configuration, repository configuration
* Synonyms: "author-only" = "Author only setup"
* Do not confuse: "Author only setup" (reads Content Fragments from the author environment only) ≠ "Publish instance setup" (uses the publish instance, the default for AEM as a Cloud Service)

**FAQ:**

* **Q: Where are repository settings configured?** — In Administration > Channels > AEM Integration, using Create configuration.
* **Q: Do repository settings apply across sandboxes?** — No; AEM Integration saves settings per sandbox and they do not apply across sandboxes.
* **Q: What happens if I save a new configuration for the same repository?** — It replaces the previous settings for that organization, sandbox, and repository, and only the latest configuration is kept.
* **Q: When do I need Publish instance setup?** — When your publish instance is authenticated or you must use a custom publish domain; otherwise the default publish configuration can be used without changes.
* **Q: How do I confirm the integration works?** — Pick a Content Fragment in the Content Advisor window and save; validation runs automatically and shows an error list if it fails.

+++

<!-- ai-section-version: 1 | source-hash: 7b3f420c -->
