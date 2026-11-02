---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through building an Orchestrated campaign that re-engages recipients with personalized email reminders about products saved to their wishlist, using a Build audience activity, an Enrichment activity, and an email activity.

**Intents:**

* Build an Orchestrated campaign that re-engages recipients with personalized email reminders about products saved to their wishlist.
* Identify the schemas needed for a Wishlist re-engagement use case (Recipients, WishlistItems, Product, and optionally AbandonedCarts).
* Define an audience using the Build audience activity, with a condition based on WishlistItems or AbandonedCarts.
* Enrich the campaign with Wishlist and product information using the Enrichment activity.
* Personalize the re-engagement email using the enriched product data.
* Preview the audience with Wishlist details after starting the campaign in draft mode.

**Glossary:**

* **Recipients**: schema used to target the audience for this use case *(product-specific)*
* **WishlistItems**: schema with fields creationDate, product, and Wishlistid, used to track items saved to a recipient's wishlist *(product-specific)*
* **Product**: schema with fields description, priceref, and imageurl, used to enrich campaign content with product information *(product-specific)*
* **AbandonedCarts**: optional schema with field lastmodified, used to include recipients with an abandoned cart within the defined timeframe *(product-specific)*
* **Build audience activity**: activity used to identify the group of customers to target based on Wishlist behavior *(product-specific)*
* **Enrichment activity**: activity used to personalize the campaign with Wishlist and product information *(product-specific)*

**FAQ:**

* **Q: What schemas are needed for this use case?** — Recipients, WishlistItems, Product, and optionally AbandonedCarts.
* **Q: Is the AbandonedCarts schema required?** — No, it is listed as optional for this use case.
* **Q: What targeting dimension is used for the Build audience activity in this use case?** — Recipients.
* **Q: What does the audience condition for this use case represent?** — Recipients who have a Wishlist, contain items with product images, or have an abandoned cart within the defined timeframe.
* **Q: What information does the Enrichment activity add to the campaign?** — Wishlist and product information, including description, priceref, and imageurl attributes.
* **Q: How is the campaign run after setup?** — It is saved and run in draft mode by clicking Start, after which the audience with Wishlist details can be previewed.

**Related pages:**

* To configure the relational schemas needed for this use case: Learn how to configure relational schemas (orchestrated/gs-schemas.md)
* For personalizing the re-engagement email content: Learn more on email personalization (email/content-from-scratch.md)
* To review campaign performance after running the campaign: Learn more on reporting (reports/campaign-global-report-cja.md)

**Personas:**

* **marketer:** Can build an Orchestrated campaign that re-engages recipients with personalized email reminders about products saved to their Wishlist. Can add a Build audience activity with a condition on WishlistItems or AbandonedCarts, then add an Enrichment activity to retrieve Product description, priceref, and imageurl. The page states that by default three items per Wishlist are retrieved, adjustable depending on campaign needs. Where: "Intents".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Create a new campaign specifically aimed at Wishlist re-engagement.
* **Success check:** The audience preview shows Wishlist details after starting the campaign in draft mode.
* **Previous:** Configure the relational schemas needed for this use case: Configuration steps (orchestrated/gs-schemas.md)
* **Next:** Personalize the re-engagement email content: Design content from scratch in Journey Optimizer (email/content-from-scratch.md); Review campaign performance after running the campaign: Campaign report (reports/campaign-global-report-cja.md)

+++

<!-- ai-section-version: 1 | source-hash: cc3ae6b9 -->
