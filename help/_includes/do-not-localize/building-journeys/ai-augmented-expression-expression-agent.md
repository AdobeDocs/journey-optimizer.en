---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the Expression Assistant, an AI-powered feature in the Journey advanced expression editor that generates valid journey expressions from plain language prompts.

**Intents:**

* Generate a journey expression from a natural language description using the Expression Assistant
* Apply a generated expression directly into the advanced expression editor with the Apply button
* Use the Expression Assistant inside Optimize activities, Condition activities, and custom-date Wait activities
* Provide example prompts for event-based conditions and `dateTimeOnly` wait expressions
* Troubleshoot failed generation by revising prompts to reference valid field names and data sources

**Glossary:**

* **Expression Assistant**: An AI-powered generative feature embedded in the Journey advanced expression editor that converts plain language prompts into valid journey expressions *(product-specific)*
* **Advanced expression editor**: The Journey Optimizer interface for writing complex expressions in conditions, Wait activities, and action parameter mapping *(product-specific)*
* **dateTimeOnly**: A date-time expression type without timezone, required for custom-date Wait activities *(product-specific)*
* **Optimize activity**: A journey activity that supports branching conditions configurable via the advanced expression editor *(product-specific)*

**Guardrails:**

* The Expression Assistant is currently in **public beta** — availability and behavior may change
* Generative AI guardrails and limitations from the main Generate Content documentation apply to this feature
* If the assistant references fields not present in your journey's data sources, it returns an error — revise the prompt to use available field names
* The exact generated expression syntax depends on the fields and activities configured in your specific journey

**Terminology:**

* Canonical name: Expression Assistant — Acronym: none — variants: Expression AI, journey expression generator
* Synonyms: "Expression Assistant" = "AI expression generator"
* Do not confuse: Expression Assistant (AI-powered generator) ≠ Advanced expression editor (the manual code editor itself)

**FAQ:**

* **Q: Where is the Expression Assistant available?** — It is available wherever the Journey advanced expression editor opens, including Condition activities, Optimize activities, and Wait activities with a custom date.
* **Q: What happens if the assistant cannot generate a valid expression?** — An error message appears; you should revise your prompt to use field names and data sources that exist in your journey configuration.
* **Q: How do I insert a generated expression into the editor?** — Click the **Apply** button in the assistant panel to insert it directly at the current cursor position in the advanced expression editor.
* **Q: Can the Expression Assistant generate `dateTimeOnly` expressions for Wait activities?** — Yes; for example prompting "30 days from now at 10 PM as date time only" generates the appropriate `dateTimeOnly` expression.
* **Q: Is the Expression Assistant generally available?** — No, it is currently in public beta. Check the Journey Optimizer release cycle page for availability updates.

+++
