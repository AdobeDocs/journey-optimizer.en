---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use audience enrichment attributes from composition workflows, custom uploads, and Federated Audience Composition to create journey paths and personalize messages in Journey Optimizer.

**Intents:**

* Use enrichment attributes from targeted audiences to build journeys and personalize messages
* Create multiple paths in a journey based on rules that leverage the audience's enrichment attributes
* Personalize messages in journeys or campaigns using enrichment attributes in the personalization editor
* Add enrichment attributes from composition workflows to a Field Group in the ExperiencePlatform Data Source
* Understand where enrichment attributes can be used and when their values are updated

**Glossary:**

* **Enrichment attributes**: Additional attributes that are contextual and specific to an audience, not associated with the profile, and typically used for personalization purposes *(product-specific)*
* **Enrich activity**: The activity in audience composition through which enrichment attributes are linked to an audience; enrichment attributes are also linked to an audience through the custom upload process *(product-specific)*
* **Field Group (ExperiencePlatform Data Source)**: The Field Group within the "ExperiencePlatform" Data Source to which composition-workflow enrichment attributes must be added before use *(product-specific)*

**Guardrails:**

* Audiences created through CSV file custom upload before October 1, 2024, are not eligible for personalization; to use their attributes, re-create and re-upload the external CSV audience.
* Consent policies do not support enrichment attributes; consent policy rules should be based only on attributes found in the profile.
* To use enrichment attributes from audiences created using composition workflows, they must be added to a Field Group within the "ExperiencePlatform" Data Source.
* Currently, enrichment attribute values are not updated after a journey starts; even after wait or event nodes, the values remain the same as when the journey started.

**Terminology:**

* Canonical name: Enrichment attributes — Acronym: n/a — variants: audience enrichment attributes
* Synonyms: "custom upload" = "custom (CSV file) audience"
* Do not confuse: "Enrichment attributes" (contextual, specific to an audience, not associated with the profile) ≠ "profile attributes" (found in the profile; the basis for consent policy rules)

**FAQ:**

* **Q: What are enrichment attributes?** — Additional attributes that are contextual and specific to an audience; they are not associated with the profile and are typically used for personalization.
* **Q: Where can I use enrichment attributes within Journey Optimizer?** — Enrichment attributes from audiences can be used in the Optimize activity with the Condition method (Journeys), Custom action attributes (Journeys), and Message personalization (Journeys and campaigns).
* **Q: How do I enable enrichment attributes from composition workflows in journeys?** — Add them to a Field Group within the "ExperiencePlatform" Data Source.
* **Q: Are enrichment attribute values updated after a journey starts?** — Currently no; even after wait or event nodes, values remain the same as when the journey started.
* **Q: Are older CSV custom upload audiences eligible?** — Audiences created through CSV custom upload before October 1, 2024, are not eligible for personalization and must be re-created and re-uploaded.

**Personas:**

* **marketer:** Can create multiple paths in a journey by using a Read audience activity and an Optimize activity with the targeted audience's enrichment attributes. Can personalize messages in journeys and campaigns by adding enrichment attributes from the targeted audience in the personalization editor. The page states that audiences created through CSV file custom upload before October 1, 2024, are not eligible for personalization. Where: "Use audiences enrichment attributes".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Target the audience using a Read audience activity, then create rules in an Optimize activity based on the audience's enrichment attributes.
* **Success check:** Once enrichment attributes are added to a Field Group, you can use them in Journey Optimizer at the locations listed above.
* **Previous:** Learn about audience activation timing and guardrails: About Adobe Experience Platform audiences (audience/target-audiences.md); Configure a data source to add enrichment attributes to a Field Group: Configure a data source (datasource/configure-data-sources.md)
* **Next:** Target the audience using a Read audience activity: Use an audience in a journey (building-journeys/read-audience.md); Personalize messages using the personalization editor: Add personalization (personalization/personalization-build-expressions.md)

+++

<!-- ai-section-version: 1 | source-hash: 4942b12e -->
