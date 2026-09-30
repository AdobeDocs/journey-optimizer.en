---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the Adobe Experience Platform settings you must configure so that Adobe Journey Optimizer can correctly deliver and report on content cards.

**Intents:**

* Create a datastream and add the Experience Platform service with the Edge Segmentation and Adobe Journey Optimizer options enabled
* Add the Experience Event – Proposition Interaction field group to your dataset to include content card data in reports
* Configure the default merge policy so content cards are delivered correctly
* Implement the Web SDK or Mobile SDK to deliver content cards on web pages or mobile apps
* Create a content card configuration in Journey Optimizer
* Troubleshoot mobile content card delivery and align datasets for content experiment reporting

**Glossary:**

* **Datastream**: The Adobe Experience Platform Data Collection configuration that routes Journey Optimizer events through the Adobe Experience Platform Edge Network *(product-specific)*
* **Active-On-Edge Merge Policy**: A merge policy option that must be enabled on the default merge policy for content card delivery *(product-specific)*
* **Journey Inbound dataset**: The dataset that must be added within a custom Dataset preference merge policy *(product-specific)*
* **Experience Event – Proposition Interaction field group**: The field group added to your dataset so proposition interaction data is included in reports *(product-specific)*
* **Edge Delivery view**: The view within Adobe Experience Platform Assurance used to troubleshoot mobile experiences by inspecting requests, verifying edge calls, and examining profile data *(product-specific)*
* **Pseudonymous profiles**: Unauthenticated visitors that can be targeted with content cards *(product-specific)*

**Guardrails:**

* You must enable the Edge Segmentation and Adobe Journey Optimizer options when adding the Experience Platform service to your datastream, so Journey Optimizer events are handled by the Adobe Experience Platform Edge Network.
* The default merge policy must have the Active-On-Edge Merge Policy enabled under Customer > Profiles > Merge Policies.
* When using a custom Dataset preference merge policy, you must add the Journey Inbound dataset within that merge policy.
* Add the Experience Event – Proposition Interaction field group to your dataset to include this data in your reports.
* The dataset used in your app's datastream must also be included in your content experiment reporting configuration; app data will not display in reports if the datasets do not match.
* When targeting pseudonymous profiles (unauthenticated visitors), consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs.

**Terminology:**

* Canonical name: Content cards prerequisites — Acronym: n/a — variants: content card channel prerequisites, content cards configuration prerequisites
* Do not confuse: "Datastream" (Adobe Experience Platform Data Collection configuration) ≠ "Merge policy" (profile merge configuration under Customer > Profiles)
* Do not confuse: "Web SDK" (implemented on your website) ≠ "Mobile SDK" (implemented on your mobile apps)

**FAQ:**

* **Q: Which options must be enabled on the datastream?** — Enable the Edge Segmentation and Adobe Journey Optimizer options after adding the Experience Platform service.
* **Q: What merge policy setting is required?** — The default merge policy must have the Active-On-Edge Merge Policy enabled; with a custom Dataset preference merge policy, add the Journey Inbound dataset within it.
* **Q: Why is app data not appearing in my content experiment reports?** — App data will not display if the dataset used in your app's datastream does not match the dataset in your content experiment reporting configuration.
* **Q: How can I troubleshoot mobile content card delivery?** — Use the Edge Delivery view within Adobe Experience Platform Assurance to inspect requests, verify edge calls, and examine profile data.
* **Q: What should I consider when targeting unauthenticated visitors?** — Consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs.

+++

<!-- ai-section-version: 1 | source-hash: 8dabeb24 -->
