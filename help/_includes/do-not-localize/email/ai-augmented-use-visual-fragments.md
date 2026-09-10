---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to insert reusable visual fragments into emails, customize their editable fields, manage conditional content in fragments, and break or keep their inheritance with the original fragment.

**Intents:**

* Insert a reusable visual fragment into an email or content template using the Email Designer
* Search, sort, and display the visual fragments available on the current sandbox
* Customize the editable fields of a customizable fragment
* Manage conditional (dynamic) content when using visual fragments
* Break or keep the inheritance between a fragment instance and the original fragment
* Use implicit input and output variables in fragments

**Glossary:**

* **Visual fragment**: A reusable component that can be referenced in one or more emails across Journey Optimizer campaigns, journeys, or content templates *(product-specific)*
* **Break inheritance**: Copying the fragment content into the current design so changes are no longer synchronized with the original fragment *(product-specific)*
* **Locked fragment**: A fragment locked by its author whose unlock icon is greyed out, so inheritance cannot be broken and it remains synchronized everywhere it appears *(product-specific)*
* **Editable fields**: Portions of a fragment made editable, whose default value can be overridden after adding the fragment to content *(product-specific)*
* **Implicit variables**: Input variables fragments can use and output variables they can create, usable in campaign and journey content *(product-specific)*
* **Simulate content**: Action to see how the editable content and styling render; also used to preview a fragment's actual dynamic content with a profile that meets its conditions *(product-specific)*

**Guardrails:**

* You can add up to 30 fragments in a given delivery.
* Fragments can only be nested up to 1 level.
* Nesting fragments with conditional content is not supported: you cannot place a fragment containing conditional content inside an unlocked fragment that also contains conditional content (can cause loss of conditional content variant mappings, compatibility mode warnings, and inconsistent email rendering).
* You can add any Draft or Live fragment to your content, but you cannot activate the journey or campaign if a fragment with Draft status is used in it; at publication, draft fragments show an error and must be approved.
* If a fragment uses dynamic content and its default state is empty, it may appear blank in the Email Designer; the system uses the default variant as a fallback.
* When both the label and URL of a button component are made editable in a fragment, tracking reports show the URL instead of the button label.
* Locked fragments cannot have their inheritance broken (unlock icon greyed out) and remain synchronized everywhere they appear.
* Fragments created before the rich-text editing capability was introduced have editable fields set to text-only mode by default until rich-text mode is enabled.

**Terminology:**

* Canonical name: visual fragment — Acronym: n/a — variants: fragment, customizable fragment, locked fragment
* Synonyms: "break the inheritance" = "break inheritance"
* Do not confuse: "Draft" fragment status ≠ "Live" fragment status
* Do not confuse: synchronized fragment (inheritance kept, changes propagated) ≠ fragment with broken inheritance (content copied, changes not synchronized)
* Do not confuse: "Allow inheritance to be broken" (author setting to permit breaking) ≠ locked fragment (inheritance cannot be broken)

**FAQ:**

* **Q: How many fragments can I add to a delivery?** — Up to 30 fragments in a given delivery.
* **Q: How deeply can fragments be nested?** — Fragments can only be nested up to 1 level.
* **Q: Can I use a Draft fragment in my content?** — Yes, you can add any Draft or Live fragment, but you cannot activate the journey or campaign while a Draft fragment is used; draft fragments show an error at publication and must be approved.
* **Q: Can I nest fragments that contain conditional content?** — No. Nesting fragments with conditional content is not supported and can cause loss of variant mappings, compatibility mode warnings, and inconsistent email rendering.
* **Q: Why does my fragment appear blank in the Email Designer?** — If the fragment uses dynamic content and its default state is empty, it may appear blank because the system uses the default variant as a fallback; simulate the email with a profile that meets the fragment's dynamic content conditions to preview the actual content.
* **Q: What happens when I break inheritance?** — The fragment content is copied into the current design, it becomes a standalone element no longer linked to the original fragment, and changes are no longer synchronized.
* **Q: Why can't I break the inheritance of a fragment?** — It may be a locked fragment, whose unlock icon is greyed out; the author can later reset its behavior to Allow inheritance to be broken.

+++

<!-- ai-section-version: 1 | source-hash: b1ea87f5 -->
