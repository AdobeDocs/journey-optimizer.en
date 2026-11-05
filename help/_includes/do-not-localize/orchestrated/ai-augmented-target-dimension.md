---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a Targeting dimension for Orchestrated campaigns by mapping a relational schema to the customer profile so messages can be delivered at the entity level.

**Intents:**

* Understand the difference between a Profile targeting dimension and a custom targeting dimension.
* Configure Targetable Schemas to specify which relational schemas are eligible for targeting.
* Configure Profile Linkage so the system can map the target schema to the Profile schema through a shared identity field.
* Create a Targeting dimension by choosing a previously configured schema and selecting its Identity value.
* Delete a Targeting dimension that is not referenced by an active channel configuration.

**Glossary:**

* **Profile targeting dimension**: the built-in default targeting dimension, which targets recipients directly using the Profile schema *(product-specific)*
* **Custom targeting dimension**: a targeting dimension that targets recipients through a relational schema (for example, Recipients, Visitors, Customers), used to deliver messages at the entity level rather than at the profile level *(product-specific)*
* **Targetable Schemas**: the configuration aspect that specifies which relational schemas are eligible for targeting *(product-specific)*
* **Profile Linkage**: the configuration aspect that defines how the target schema maps to the Profile schema through a shared identity field configured as an identity namespace *(product-specific)*
* **Identity value**: the field selected on the chosen schema that represents the entity to target (for example, crmID) *(product-specific)*

**Guardrails:**

* Although all relational schemas are displayed when choosing a schema, only those with a direct identity relationship to Profile are eligible for selection.
* Orchestrated campaigns allow targeting on any schema that has a direct or related relationship to the Profile schema; usage is primarily intended for 1:1 relationships, but 1:N relationships (such as Account to Recipients) are also supported as long as the relationship path is properly modeled in the data model.
* Once created, a Target dimension cannot be edited.
* A Target dimension cannot be deleted if it is referenced by an active channel configuration.

**Terminology:**

* Canonical name: Targeting dimension — variants: Target Dimension, Campaign Target Dimension
* Do not confuse: "Profile targeting dimension" (targets using the Profile schema directly) ≠ "Custom targeting dimension" (targets through a relational schema at the entity level)

**FAQ:**

* **Q: What is the difference between a Profile targeting dimension and a custom targeting dimension?** — The Profile targeting dimension is the built-in default that targets recipients directly using the Profile schema; a custom targeting dimension targets recipients through a relational schema to deliver messages at the entity level.
* **Q: Which relational schemas can be selected when creating a Targeting dimension?** — Only schemas with a direct identity relationship to Profile are eligible for selection, even though all relational schemas are displayed.
* **Q: Can a Targeting dimension be edited after it is created?** — No, once created, a Target dimension cannot be edited.
* **Q: Can a Targeting dimension always be deleted?** — No, a Target dimension cannot be deleted if it is referenced by an active channel configuration.
* **Q: What are the two key aspects defined when configuring a custom targeting dimension?** — Targetable Schemas and Profile Linkage.

**Related pages:**

* For choosing a previously configured schema when creating a Targeting dimension, see previously configured Schema (orchestrated/gs-schemas.md)

**Personas:**

* **marketer:** Can create a Targeting dimension by choosing a previously configured schema and selecting its Identity value, then select Save to complete the setup. Can configure Targetable Schemas to specify which relational schemas are eligible for targeting, and configure Profile Linkage through a shared identity field. Can access the advanced menu to delete a Target dimension. The page states that a Target dimension cannot be edited once created and cannot be deleted if it is referenced by an active channel configuration. Where: "Create your Targeting dimension".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** From Administration, access the Configurations menu and select Campaign Target Dimension.
* **Success check:** Messages are delivered at the subscription level rather than to the main customer profile, with each contract receiving its own personalized message.
* **Previous:** Choose a previously configured schema for your Targeting dimension: Configuration steps (orchestrated/gs-schemas.md)

+++

<!-- ai-section-version: 1 | source-hash: a56c1d33 -->
