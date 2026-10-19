---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to tag, add, and personalize Adobe Experience Manager Content Fragments in Journey Optimizer campaigns and journeys, how to work with variations, and how to use Content Fragments as offer item attributes in Experience Decisioning.

**Intents:**

* Understand the Experience Manager to Journey Optimizer data flow (configure Dispatcher, create and author, tag, publish, access, integrate)
* Create and assign the Journey Optimizer tag in Experience Manager so a Content Fragment appears in the selector
* Add and personalize an AEM Content Fragment in a campaign or journey using the AEM Content Advisor
* Declare placeholders as parameters and map them to profile attributes, contextual attributes, static strings, or variables
* Use AEM Content Fragments as offer item attributes in Experience Decisioning
* Choose and work with Content Fragment variations

**Glossary:**

* **AEM Content Advisor**: AI-powered, unified interface for discovering and selecting Assets, Content Fragments, and Dynamic Media directly within AJO authoring workflows; replaces the existing Asset Selector and Content Fragment selector experiences *(product-specific)*
* **Main**: The core content of a Content Fragment that always exists, cannot be deleted, and is the basis for all variations *(product-specific)*
* **Variations**: One or more permutations of Main that authors create for specific channels or scenarios, living inside the fragment rather than as separate assets *(product-specific)*
* **Pills experience**: An option that improves readability by hiding long attribute paths *(product-specific)*
* **ajo-enabled tag**: Tag with the ID format `ajo-enabled:{OrgId}/{SandboxName}` that a Content Fragment must carry to appear in Journey Optimizer for your organization and sandbox *(product-specific)*

**Guardrails:**

* Configuring the Dispatcher is a prerequisite for Journey Optimizer to access Content Fragments via the Content Fragment Management API.
* A Content Fragment appears in the Content Fragment selector only when it carries a tag matching `ajo-enabled:{AJO-OrgId}/{AJO-SandboxName}` for your organization and sandbox.
* When a Content Fragment is published in Experience Manager, if the update is successful it becomes available in Journey Optimizer within approximately 5 minutes for Unitary journeys, and in the next processing batch for batch use cases.
* For Healthcare customers, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Extended Security for Healthcare add-on offerings.
* Relative image URLs from Experience Manager are not supported; use absolute URLs.
* All placeholders used within a Content Fragment must be explicitly declared by the user as parameters in the fragment helper tag.
* In Experience Decisioning, only Content Fragments in a published state are available, they must be tagged with `ajo-enabled:{OrgId}/{SandboxName}`, and you can add up to five AEM Content Fragments to a single decision item.
* Using AEM Content Fragments in Experience Decisioning is available for channels with Decisioning support.

**Terminology:**

* Canonical name: AEM Content Fragments — Acronym: n/a — variants: Content Fragment, AEM content fragment
* Synonyms: "AEM Content Advisor" = "Open AEM Content Advisor"
* Do not confuse: "AEM Content Fragments" (authored in Experience Manager, used in Journey Optimizer) ≠ "Fragments" (reusable content components created in Journey Optimizer) ≠ "Journey Fragments" (reusable sets of journey nodes inserted into journeys)
* Do not confuse: "Main" (core content, cannot be deleted) ≠ "Variations" (permutations of Main for specific channels or scenarios)

**FAQ:**

* **Q: Why does my Content Fragment not appear in Journey Optimizer?** — It must be tagged in Experience Manager with a tag matching `ajo-enabled:{OrgId}/{SandboxName}` for your organization and sandbox, and the Dispatcher must be configured.
* **Q: What happens if I do not select a variation?** — The Main variation is used automatically at delivery time.
* **Q: How many AEM Content Fragments can I add to a single decision item?** — Up to five, and only Content Fragments in a published state are available.
* **Q: What happens when I republish a fragment used in active campaigns or journeys?** — Republishing it in Experience Manager updates every referenced variation in active campaigns or journeys automatically.
* **Q: How do I enable real-time personalization in a fragment?** — Declare all placeholders as parameters in the fragment helper tag and map them to profile attributes, contextual attributes, static strings, or predefined variables.

+++

<!-- ai-section-version: 1 | source-hash: 9e522485 -->
