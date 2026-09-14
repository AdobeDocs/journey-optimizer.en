---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces personalization in Journey Optimizer — how the Handlebars-based personalization editor works, what data it uses, the interactive playground, Generate Content for expressions, and inline attribute editing in the Email Designer and Push editor.

**Intents:**

* Understand how Journey Optimizer personalization works (Handlebars syntax with double curly braces)
* Identify the data sources available for personalization (XDM Individual Profile schema, computed attributes, AEP dataset lookup in beta)
* Experiment with personalization using the interactive playground without a live sandbox
* Use AI to generate, explain, or fix personalization expressions from natural language
* Insert profile attributes inline in the Email Designer or Push editor by typing `{{`

**Glossary:**

* **Personalization editor**: The full-featured tool for building, customizing, and validating personalization expressions; available in any Journey Optimizer field that supports personalization. *(product-specific)*
* **XDM Individual Profile schema**: The only schema that can be used to personalize content in Journey Optimizer; defines all profile attributes available for personalization. *(product-specific)*
* **Computed attributes**: Pre-calculated profile attributes summarizing individual behavioral events into profile-level values; available as personalization data alongside standard XDM profile fields. *(product-specific)*
* **Personalization playground**: An interactive, simulated environment on Experience League for writing and testing personalization code with sample data — no live datasets or sandbox required. *(product-specific)*
* **Inline editing**: The ability to type `{{` in any text field in the Email Designer or Push channel editor to trigger an autocomplete dropdown and insert profile attributes without opening the full personalization editor. *(product-specific)*
* **Generate Content (personalization expressions)**: An AI tool in the personalization editor and Email Designer that generates personalization expressions from natural language, explains existing code, and fixes issues in a selection. *(product-specific)*

**Guardrails:**

* XDM Individual Profile schema is the only schema that can be used to personalize content in Journey Optimizer.
* AEP dataset lookup for personalization requires datasets to be enabled through an API call before use; this feature is currently in beta.
* Inline editing (typing `{{` in Email Designer or Push editor) supports profile attributes only.

**Terminology:**

* **Canonical name:** personalization — variants: content personalization, message personalization, expression personalization
* **Canonical name:** personalization editor — variants: personalization capabilities
* **Do not confuse:** Personalization editor (used to build content expressions in messages and offers — supports both Handlebars and PQL) ≠ Advanced expression editor (used in the journey for conditions on data sources and event information, custom wait activities, and action parameters mapping — provides built-in functions and operators that differ from those in the personalization editor)
* **Do not confuse:** inline editing (type `{{` in Email Designer or Push for quick attribute insertion without opening the full editor) ≠ personalization editor (full tool for complex expressions, helper functions, conditional rules, and fragments)
* **Do not confuse:** XDM Individual Profile schema (the only schema usable for personalization in Journey Optimizer) ≠ other AEP schemas (not usable for personalization unless exposed via dataset lookup)

**FAQ:**

* **Q: What data can be used for personalization in Journey Optimizer?** — Profile data from the XDM Individual Profile schema, computed attributes (behavioral events summarized at the profile level), and AEP record dataset lookup (currently beta — requires datasets to be enabled via API).
* **Q: What is the personalization playground?** — An interactive, simulated environment on Experience League where you can write and test personalization code using sample data, without requiring a live Journey Optimizer sandbox or real datasets.
* **Q: How does inline attribute editing work?** — Type `{{` in any text field in the Email Designer or Push channel editor to open an autocomplete dropdown at the cursor position. Start typing to filter profile attributes, then select one to insert it as a personalization token. Only profile attributes are available inline.
* **Q: What can Generate Content do in the personalization editor?** — It can generate new personalization expressions from natural language descriptions, explain what existing code does, and fix issues in a selected expression — then apply the output when it matches your intent.

+++

<!-- ai-section-version: 1 | source-hash: 248b894f -->
