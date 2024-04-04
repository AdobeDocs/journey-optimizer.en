---
title: Get started with offer delivery APIs
description: Learn more on the APIs available to deliver personalized offers.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 7bc1a4ec-113c-4af7-b549-ee17b843b818
---
# Get started with offer delivery APIs {#about-decisioning-apis}

You can deliver offers using either the **Decisioning** or the **Edge Decisioning** API. Additionally, the **Batch Decisioning** API allows you to deliver offers to all profiles in a given audience in one call. The offer content for each profiles in the audience is placed in an Adobe Experience Platform dataset where it is available for custom batch workflows.

In this page, you will find information on specific functionalities that are available with the **Decisioning** and **Edge Decisioning** APIs. While both allow you to deliver offers to your customers, we recommend using the **Edge Decisioning** API whenever possible for inbound use cases and to ensure better latency and throughput on your platform.

For more information on how to work with the APIs, refer to these sections:
* [Decisioning API](decisioning-api.md)
* [Edge Decisioning API](edge-decisioning-api.md)
* [Batch Decisioning API](batch-decisioning-api.md)

## Edge Decisioning API capabilities {#edge}

**Unique request for experience events and decisioning requests**

With the Edge Decisioning API, you can send in one single request the experience event itself along with the decisioning request, rather than having two different requests.

For example, if a customer visits your website, the request will include the experience event (the customer's visit to the page), and get an offer back to populate the visited page.

**Context data storage into Adobe Experience Platform**

Context data refers to data that you only know at the time you want an offer back. For example, the color of the purchased article, the weather at the time of the purchase, etc.

When passing context data with an Edge Decisioning API request, data is stored into the Adobe Experience Platform profile, allowing future reuse. 

>[!NOTE]
>
>In order for the context data to be stored, you need to have a dedicated XDM schema configured.

**Frequency capping counter update**

If frequency capping has been enabled for some of your offers to define how often their capping count is reset, the counter is updated and available in an Edge Decisioning API decision in less than 3 seconds. [Learn how to add constraints to an offer](../../offer-library/add-constraints.md)

## Decisioning API capabilities {#decisioning}

The functionalities listed below are only available with the Decisioning API. If you need to leverage one of them to meet your requirements, use the Decisioning API. Otherwise, we recommend using the Edge Decisioning APIs.

* **Offer content and characteristics**: you can choose not to return the content and characteristics of an offer using a dedicated option.
* **Offer metadata**: enable an option to return the metadata of an offer.
* **Merge policy**: use in your request a different merge policy from the one associated to your sandbox.
* **Decisioning events and frequency capping**: block decisioning events from being counted by any frequency capping that happens.
* **Duplicate propositions**: enable an option not to deduplicate propositions.
