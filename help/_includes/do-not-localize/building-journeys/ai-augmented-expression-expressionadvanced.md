---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the Journey advanced expression editor — its access points, interface panels, and capabilities for building complex conditions, custom wait timers, and action parameter mappings using events, data sources, functions, and operators.

**Intents:**

* Access the advanced expression editor from a data source condition, custom wait activity, or action parameter mapping
* Build advanced boolean conditions using event fields, data source fields, audience membership, and journey properties
* Switch between simple mode and advanced mode when configuring conditions
* Reference external data source parameters directly within the main expression using the `params` keyword
* Use AI-powered expression generation to create expressions from natural language prompts

**Glossary:**

* **Advanced expression editor**: The Journey Optimizer code editor for writing complex expressions; distinct from the simpler point-and-click condition editor *(product-specific)*
* **Simple mode**: A point-and-click condition editor; less flexible than the advanced editor but easier for non-developers *(product-specific)*
* **Journey properties**: Technical fields about the journey instance (ID, version, errors, current node) accessible in the expression editor *(product-specific)*
* **Generate expressions with AI**: An AI-powered capability (public beta) inside the advanced editor that generates expressions from plain language prompts *(product-specific)*

**Guardrails:**

* Creating expressions using experience events directly is not supported — use alternative approaches such as computed attributes
* Conditions always return a boolean type regardless of editor mode
* Expressions must not contain hidden or non-printable characters, and should use single-line format to avoid parsing errors
* External data source parameter values can only come from journey events or the Experience Platform data source — not from other external data sources
* The advanced expression editor functions differ from those in the personalization editor

**Terminology:**

* Canonical name: Advanced Expression Editor — Acronym: none — variants: advanced editor, expression editor
* Synonyms: "Advanced mode" = "advanced expression editor"
* Do not confuse: advanced expression editor (journey conditions/actions) ≠ personalization editor (message content personalization)

**FAQ:**

* **Q: When must I use the advanced expression editor instead of the simple mode?** — Use the advanced editor when you need to query collections, use functions, reference journey properties, or build multi-condition logic that the simple editor cannot express.
* **Q: How do I pass a parameter to an external data source in the expression?** — Use the `params` keyword in the expression syntax, e.g. `#{DataSource.fieldGroup.field, params: {paramName: value}}`.
* **Q: What does the autocompletion mechanism do?** — It displays contextual field and function suggestions as you type, helping you build valid expressions faster.
* **Q: Where is Generate expressions with AI accessed?** — Via the AI control inside the advanced expression editor; it is currently in public beta.
* **Q: Do conditions in the advanced editor return a different type than in simple mode?** — No; conditions always return a boolean in both modes.

+++
