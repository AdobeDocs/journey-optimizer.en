---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to insert, customize, and manage expression fragments in the personalization editor — including implicit variables, using fragments inside loops, editable fields, dynamic resolution, and breaking inheritance.

**Intents:**

* Insert an expression fragment from the Fragments menu and understand automatic change propagation
* Use implicit variables: input variables (declared outside the fragment, used inside) and output variables (declared inside the fragment, used in surrounding message content)
* Use expression fragments inside loops — leverage global variables for fragment access; understand the limitation on passing loop-scoped variables as parameters
* Override editable fields in a customizable fragment using `<fieldId>="<value>"` syntax
* Resolve fragment IDs dynamically at runtime based on profile attributes, dataset lookups, or context data
* Break inheritance by pasting fragment content directly into the editor

**Glossary:**

* **Expression fragment**: A reusable personalization expression component referenced by ID across campaigns and journeys; changes to the fragment propagate automatically to all content referencing it. *(product-specific)*
* **Implicit variables**: Variables that extend the fragment functionality — input variables (declared in campaign/journey content, consumed inside the fragment) and output variables (declared inside the fragment, available in the surrounding message content). *(product-specific)*
* **Input variable**: A variable declared outside the fragment (in campaign or journey content) that the fragment can reference and use internally.
* **Output variable**: A variable declared or computed inside a fragment that becomes available for use in the surrounding message content after the fragment is called.
* **Editable fields**: Fragment variables exposed to allow the inserting user to override default values using `<fieldId>="<value>"` syntax, without editing the fragment source. *(product-specific)*
* **Dynamic fragment resolution**: The ability to resolve a fragment ID at runtime (based on profile attributes, dataset lookups, or context data) rather than embedding a static fragment ID at design time. *(product-specific)*
* **Break inheritance**: Using "Paste fragment" from the contextual menu copies the fragment's content into the editor as a standalone element that no longer synchronizes with the original fragment. *(product-specific)*

**Guardrails:**

* Maximum 30 fragments can be added in a given delivery.
* Fragments can only be nested up to 1 level.
* A journey or campaign cannot be activated or published if it contains a fragment with Draft status; draft fragments must be approved before publication.
* Expression fragments cannot receive loop-scoped variables (the current `{{#each}}` iteration item) as parameters — this is a known limitation. Use global variables or inline logic as a workaround.
* If a fragment containing multiple line breaks is used in SMS or push content, line breaks are preserved; test the content before sending.

**Terminology:**

* **Canonical name:** expression fragment — variants: fragment, expression fragment
* **Synonyms:** "fragment ID" = the identifier used to reference the fragment in expressions
* **Do not confuse:** inserting a fragment by ID (referenced; changes propagate automatically to all content) ≠ breaking inheritance / paste fragment (content copied into editor; standalone element, no longer linked to original)
* **Do not confuse:** input variables (declared outside the fragment, consumed inside) ≠ output variables (declared inside the fragment, consumed outside in surrounding message content)
* **Do not confuse:** Draft fragment (can be added to content but blocks journey/campaign publication until approved) ≠ Live fragment (fully published; safe for active journeys and campaigns)

**FAQ:**

* **Q: How many fragments can be added in a single delivery?** — Up to 30 fragments.
* **Q: Can fragments be nested inside other fragments?** — Yes, but only up to 1 level of nesting.
* **Q: What happens if I use a Draft fragment in a journey or campaign?** — You can add a Draft fragment to content, but you cannot activate or publish the journey or campaign until the fragment is approved and its status changes to Live.
* **Q: Can an expression fragment receive the current loop item (e.g., `product` in `{{#each}}`) as a parameter?** — No. Expression fragments cannot receive loop-scoped variables as parameters. Use global variables declared outside the loop (which the fragment can access), or include the personalization logic directly within the loop instead of using a fragment.
* **Q: What is breaking inheritance and when should I use it?** — Breaking inheritance means using "Paste fragment" from the contextual menu to copy the fragment's content directly into the editor. The pasted content becomes a standalone element that no longer synchronizes with the original fragment — use this when you need to customize the content beyond what editable fields allow, knowing future changes to the original fragment will not propagate to this copy.

+++

<!-- ai-section-version: 1 | source-hash: 64745ff0 -->
