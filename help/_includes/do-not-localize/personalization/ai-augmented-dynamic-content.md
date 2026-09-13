---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use conditional rules to add dynamic content to messages — either via expression tags in the personalization editor or as content component variants in the Email Designer.

**Intents:**

* Add dynamic content to personalization expressions using `{%if%}` / `{%/if%}` conditional tags
* Preview multiple dynamic content variants using simulation
* Enable conditional content on an Email Designer content component
* Create multiple component variants each linked to a conditional rule
* Manage the Default variant displayed when no conditions are met at send time

**Glossary:**

* **Dynamic content**: Message content that varies based on conditional rules; different content is displayed depending on whether defined conditions are met at send time. *(product-specific)*
* **Conditional content**: An Email Designer feature that applies conditional rules to a content component, creating multiple display variants. *(product-specific)*
* **Default variant**: The content displayed for a component when none of the defined conditional rules are met when sending the message. *(product-specific)*
* **`{%if%}` / `{%/if%}` tags**: Personalization editor expression syntax used to wrap content blocks that display only when a conditional rule is met.

**Guardrails:**

* Conditional content variants are evaluated against their associated rules in the order they are displayed; the Default variant is always displayed if no other conditions are met.
* When simulating or rendering proofs for emails with multiple conditional variants, Journey Optimizer may require more processing time; consider reducing the number of variants or simplifying conditional rules if timeouts or errors occur.
* If the Email Designer fails to render properly after adding conditional blocks, verify that each condition's syntax is correct and that no duplicate or conflicting statements exist.

**Terminology:**

* **Canonical name:** dynamic content — variants: conditional content, personalized content
* **Synonyms:** "conditional content" (Email Designer UI label) = "dynamic content" (general term used throughout)
* **Do not confuse:** adding dynamic content in expressions (using `{%if%}` tags in the personalization editor) ≠ adding dynamic content in emails (creating component variants in the Email Designer — two distinct workflows)
* **Do not confuse:** "Default variant" (displayed when no conditional rules are met) ≠ a named variant (each associated with a specific conditional rule)

**FAQ:**

* **Q: What happens if none of the defined conditions are met when the message is sent?** — The content component displays the content defined in the Default variant.
* **Q: In what order are conditional content variants evaluated?** — Variants are evaluated against their associated rules in the order they are displayed. The Default variant is always shown if no other conditions are met.
* **Q: Where can dynamic content be added in Journey Optimizer?** — In any field where personalization can be added — including subject lines, links, push notification content, and text-type offer representations — via the personalization editor, and in Email Designer content components via conditional variants.
* **Q: What should I do if the Email Designer fails to render after adding conditional blocks?** — Verify that each condition's syntax is correct and that no duplicate or conflicting statements exist. If issues persist, rebuild the problematic sections in a fresh template and test each conditional block incrementally.

+++

<!-- ai-section-version: 1 | source-hash: e6005d80 -->
