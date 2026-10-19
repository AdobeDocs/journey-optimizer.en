---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the prerequisites and configuration required to send In-app messages with Journey Optimizer, including delivery prerequisites, creating an In-app channel configuration, and reporting prerequisites.

**Intents:**

* Complete the configuration steps required before sending In-app messages
* Set up the delivery prerequisites in Adobe Experience Platform Data Collection and Profile merge policies
* Create an In-app channel configuration under Channels > General settings > Channel configurations
* Configure per-platform targeting (Web, iOS, Android) for the channel configuration
* Enable reporting for the In-app channel by aligning datasets and field groups

**Glossary:**

* **In-app channel configuration**: A channel configuration created in Journey Optimizer that you select when creating an In-app message *(product-specific)*
* **Active-On-Edge Merge Policy**: A merge policy option in Adobe Experience Platform *(product-specific)*
* **Journey Inbound dataset**: A dataset in Adobe Experience Platform *(product-specific)*
* **Edge Delivery view**: A view within Adobe Experience Platform Assurance *(product-specific)*
* **Marketing action**: A selection that associates consent policies with messages using the configuration, so customer preferences are respected *(product-specific)*
* **Pages matching rule**: An App configuration option for Web that targets multiple URLs following the same pattern, using **Domain** and **Page** criteria *(product-specific)*
* **Time-To-Live (TTL)**: A setting for automatic profile deletion *(product-specific)*

**Guardrails:**

* Configuration names must begin with a letter (A-Z) and can only contain alpha-numeric characters, plus the underscore, dot, and hyphen characters.
* For iOS and Android platforms, delivery is based solely on the app ID. If both apps share the same app ID, content is delivered to both, regardless of the platform selected in the channel configuration. To restrict delivery to a specific platform, implement device-specific rules within your journey or campaign logic.

**Prerequisites and permissions:**

* Correct permissions on Journey Optimizer campaigns, required even if you plan to use In-app messages only in journeys.
* An Adobe Experience Platform Data Collection datastream with the Adobe Experience Platform Edge and the **Adobe Journey Optimizer** option enabled under the **Adobe Experience Platform** service, so that Journey Optimizer inbound events are correctly handled by the Adobe Experience Platform Edge.
* In Adobe Experience Platform, a default merge policy with the **Active-On-Edge Merge Policy** option enabled. Inbound channels use it to activate and publish inbound campaigns on the edge. When using a custom **Dataset preference** merge policy, add the **Journey Inbound** dataset within that merge policy.
* An In-app channel configuration, which you select when creating an In-app message.
* For reporting: the dataset used in your In-app implementation datastream must also be included in your reporting configuration. If you are not using the `AEP Web SDK ExperienceEvent` and `Consumer Experience Event` field groups for your dataset schema, add the `Experience Event - Proposition Interactions`, `Application Details`, `Commerce Details`, and `Web Details` field groups.

**Applicability:**

* In-app messages: the configuration steps apply to sending In-app messages in journeys and in campaigns.
* `context.datastream` attributes: supported only for Web channel campaigns in Journey Optimizer; not supported in In-app messages.

**Terminology:**

* Canonical name: In-app channel configuration; variants: In-app message channel configuration, In-app configuration
* Synonyms: "pseudonymous profiles" = "unauthenticated visitors"
* Do not confuse: "Delivery prerequisites" (datastream and merge policy setup) ≠ "Reporting prerequisites" (datasets and field groups for reporting)
* Do not confuse: "Page URL" (target a specific page) ≠ "Pages matching rule" (target multiple URLs following the same pattern)

**FAQ:**

* **Q: What permissions do I need before configuring In-app?** — You need the correct permissions on Journey Optimizer campaigns, even if you plan to use In-app messages only in journeys, because campaign permissions are still required.
* **Q: Can I use `context.datastream` in In-app messages?** — No; it is currently supported only for Web channel campaigns, and attempting to use it in In-app messages results in validation errors such as `Invalid syntax Missing schema field: 'datastream`.
* **Q: Where do I create an In-app channel configuration?** — Under Channels > General settings > Channel configurations, using Create channel configuration.
* **Q: How is delivery handled for iOS and Android?** — Delivery is based solely on the app ID; if both apps share the same app ID, content is delivered to both regardless of the platform selected, unless you add device-specific rules in your journey or campaign logic.
* **Q: Why is my In-app data not showing in reports?** — The dataset used in your In-app implementation datastream must also be included in your reporting configuration. If you add a dataset that is not present in your app datastream, app data will not display in your reports.

**Troubleshooting:**

* **Validation error `Invalid syntax Missing schema field: 'datastream`**: occurs when attempting to use `context.datastream` attributes in In-app messages.
* **App data does not display in reports**: occurs when you add a dataset that is not present in your app datastream to the reporting configuration.
* **Troubleshooting the delivery of Journey Optimizer mobile experiences**: use the **Edge Delivery** view within **Adobe Experience Platform Assurance** to inspect request calls in detail, verify whether the expected edge calls occur, and examine profile data, including identity maps, segment memberships, and consent settings. You can also review the activities the request qualified for and identify those it did not.

**Examples:**

* **Pages matching rule (Web):** to edit elements displayed on all the sales product pages of a Luma website, select Domain > Starts with > luma and Page > Contains > sales.

**Best practices:**

* When targeting pseudonymous profiles (unauthenticated visitors) with In-app messages, consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs (recommended).

**Related pages:**

* To create, configure, and send your first In-app message: Create an In-app message (in-app/create-in-app.md)
* To design the content of an In-app message: Design In-app message (in-app/design-in-app.md)
* To check the campaign permissions: Get started with campaigns, Prerequisites (campaigns/get-started-with-campaigns.md)
* To learn more about setting a Time-To-Live (TTL) when targeting pseudonymous profiles: Journey Optimizer guardrails and limitations, Profile management with inbound channels (start/guardrails.md)
* To assign data usage labels with **Manage access**: Object Level Access Control (OLAC) (administration/object-based-access.md)
* To associate consent policies through marketing actions: Work with consent policies (action/consent.md)
* To add datasets for reporting: Configure Journey Optimizer reporting for experimentation (reports/reporting-configuration.md)
* To view In-app reporting: In-app report (reports/campaign-global-report-cja-inapp.md)

+++

<!-- ai-section-version: 2 | source-hash: f8aa46e4 -->
