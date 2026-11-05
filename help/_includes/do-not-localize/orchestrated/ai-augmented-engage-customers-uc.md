---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through an Orchestrated campaign use case that re-engages customers by reading a browsing-activity audience, deduplicating it, splitting it by churn risk, and sending personalized follow-up messages to low/medium-risk customers while saving a separate audience for high-risk customers.

**Intents:**

* Build an Orchestrated campaign that targets customers based on browsing activity.
* Deduplicate an audience by an attribute such as email before further processing.
* Split an audience into segments based on churn probability.
* Save a high-risk segment as a new audience for separate, targeted communication.
* Enrich a campaign with related entity data (such as Wishlist fields) to personalize messages.
* Retarget engaged customers and divide them across mobile message and push follow-ups.

**Glossary:**

* **Read audience**: the activity used to select a pre-defined audience from Adobe Experience Platform *(product-specific)*
* **Deduplication**: the activity that removes duplicate values (here, email addresses) from an audience so each customer receives only one message *(product-specific)*
* **Split**: the activity used to segment customers into groups (here, Low risk, Medium risk, High risk) based on a condition such as churn probability *(product-specific)*
* **Condition editor**: the tool used to set the specific values that determine each customer's churn risk within a Create filter step *(product-specific)*
* **Save Audience**: the activity used to save a segment (here, the high-risk segment) as a new audience in Adobe Experience Platform *(product-specific)*
* **Union**: the activity used to combine segments (here, Low and Medium risk) *(product-specific)*
* **Enrichment**: the activity used to add attributes from another schema (here, Wishlist description, priceref, imageurl) to personalize a campaign *(product-specific)*
* **Churn risk**: how likely someone is to stop engaging or buying, used as the basis for the Split activity *(product-specific)*

**Guardrails:**

* This use case starts with an audience that already exists in Adobe Experience Platform; the page notes it is specifically a real-time web behavior audience that collects browsing activity as it occurs.

**Applicability:**

* Applies to Orchestrated campaigns.

**Terminology:**

* Canonical name: Orchestrated campaign — context: this use case is built as a campaign using Read audience, Deduplication, Split, Save Audience, Union, and Enrichment activities.
* Do not confuse: "Save Audience" (saves a segment, here the high-risk group, as a new Adobe Experience Platform audience for separate communication) ≠ "Split" (segments an audience into groups within the same campaign flow).

**FAQ:**

* **Q: What audience does this use case start with?** — An audience that already exists in Adobe Experience Platform, specifically a real-time web behavior audience that collects browsing activity as it occurs.
* **Q: How is the audience deduplicated?** — With a Deduplication activity, using email as the attribute for deduplication.
* **Q: How are customers segmented by churn risk?** — With a Split activity that creates Low risk, Medium risk, and High risk segments, using Create filter and the Condition editor to define churn probability values for each group.
* **Q: What happens to high-risk customers?** — They are saved as a separate audience with a Save Audience activity, for later use in a specific targeted campaign.
* **Q: What happens to low and medium risk customers?** — They are combined with a Union activity, enriched with Wishlist information (description, priceref, imageurl) through an Enrichment activity, and sent follow-up messages through mobile message or push notifications.
* **Q: What schemas are needed for this use case?** — Recipients (with email and churnprop fields, used as the targeting dimension) and Wishlist (with description, priceref, and imageurl fields).

**Related pages:**

* For configuring the relational schemas needed for this use case: Learn how to configure relational schemas (orchestrated/gs-schemas.md)
* For reviewing performance metrics and insights after the campaign has run: Learn more on reporting (reports/campaign-global-report-cja.md)

**Personas:**

* **marketer:** Can build an Orchestrated campaign that reads an audience, deduplicates it by email, and splits customers into Low, Medium, and High risk segments. Can save the High risk segment as a new audience, combine Low/medium risk segments, and enrich them with Wishlist description, priceref, and imageurl. The page states that this use case starts with an audience that already exists in Adobe Experience Platform. Where: "Intents".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Set up a new campaign aimed at Wishlist re-engagement.
* **Success check:** After the campaign has run, the reporting dashboard shows performance metrics and key insights.
* **Previous:** Configure the relational schemas needed for this use case before building the campaign: Configuration steps (orchestrated/gs-schemas.md)
* **Next:** Review performance metrics and key insights after the campaign has run: Campaign report (reports/campaign-global-report-cja.md)

+++

<!-- ai-section-version: 1 | source-hash: e40989d5 -->
