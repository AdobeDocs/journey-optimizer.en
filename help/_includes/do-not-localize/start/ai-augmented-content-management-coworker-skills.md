---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the CX Coworker Content Management tools in Adobe Journey Optimizer, which use 15 read and write-capable MCP tools to discover, create, update, clone, and publish content templates, fragments, landing pages, and journey/campaign inline message content through natural language prompts.

**Intents**

* Browse and inspect content templates, fragments, landing pages, and campaign/journey inline message content.
* Create a new content template or fragment for a channel.
* Update an existing content template, or update, clone, or publish a fragment.
* Update a channel variant of a campaign or journey action node's inline message content.
* Learn which content management capabilities are not supported, such as deletion or full-text search.

**Glossary**

* **Content Management tools** *(product-specific)*: CX Coworker capability, powered by 15 read and write-capable MCP tools, that discovers and manages content templates, fragments, landing pages, and journey/campaign inline message content using natural language prompts.
* **Fragment**: an HTML or expression content asset that can be created, updated, cloned, or published through Content Management tools.
* **Inline message content**: the channel variant content configured on a journey or campaign action node, retrievable and updatable through Content Management tools.

**Guardrails**

* Content Management is available for all customers who have access to CX Coworker.
* Update operations replace content in full — provide the complete HTML body or variant content in the prompt.
* Content Management tools do not support full-text search across templates or fragments, template or fragment validation (orphaned references, broken links, deprecated components), creating or publishing landing pages, or deleting content templates, fragments, or landing pages.

**Terminology**

* Do not confuse: "content templates" (create and update, full-channel assets) are managed differently from "fragments" (create, update, clone, and publish) and "inline message content" (update a channel variant only) — each has its own set of supported operations on this page.

**FAQ**

* **How many MCP tools power Content Management in CX Coworker?** 15 read and write-capable MCP tools.
* **Can Content Management tools delete a content template, fragment, or landing page?** No, deleting content templates, fragments, or landing pages is not supported.
* **Can Content Management tools create or publish a landing page?** No, creating or publishing landing pages is not supported.
* **Can a fragment be cloned under a new name?** Yes, cloning an existing fragment under a new name is a supported capability.
* **What should I do before asking Coworker to publish a fragment?** Review the fragment's content after creating or updating it, before asking Coworker to publish it.

+++

<!-- ai-section-version: 3 | source-hash: 89361eb2 -->
