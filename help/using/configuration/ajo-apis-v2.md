---
solution: Journey Optimizer
product: journey optimizer
title: Use Journey Optimizer APIs
description: Find the Journey Optimizer REST APIs by task, learn how to authenticate, and jump to the API reference and the matching guide for each one.
feature: Integrations, Data Ingestion
role: Developer
level: Intermediate
hide: true
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
subfeature_v2:
  - id: cf3fbcd7-c075-4ae4-8de5-96e736ab2ea3
    internal-label: Data ingestions
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bbbea26f-9621-49eb-9ab8-e06fb3bbce8c
    internal-label: Artificial intelligence
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eb30f47f-d87a-400f-8f78-63ce7979ff56
    internal-label: Machine learning
---
# Work with [!DNL Journey Optimizer] APIs {#apis-gs}

>[!BEGINSHADEBOX]

**On this page:** Find the Journey Optimizer REST API you need by task, set up authentication, and go to the API reference and the matching user guide.

>[!ENDSHADEBOX]

Journey Optimizer REST APIs let you automate operations that you would otherwise perform in the user interface, such as triggering a message from your own system or managing content and suppression lists programmatically. The complete reference, with request and response schemas and an interactive console, is on the [Journey Optimizer API portal](https://developer.adobe.com/journey-optimizer-apis){target="_blank"}.

## Before you start {#before-you-start}

All Journey Optimizer APIs use OAuth Server-to-Server authentication. The JWT method is deprecated.

1. Create a project in [Adobe Developer Console](https://developer.adobe.com/console){target="_blank"} and add the Journey Optimizer API to it.
1. Ask your administrator to add the permissions required by each endpoint to the product profile linked to your integration.
1. Send the access token, API key, organization ID, and sandbox name with each call. API calls run against one sandbox, so use a development sandbox while you test.

For the detailed steps, the required headers, and the permissions per endpoint, see [Authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}.

>[!NOTE]
>
>Not a developer? See [Get started for developers](../start/path/developer.md) for the full implementation path, including SDKs, events, and custom actions.

## Find an API by task {#apis-by-task}

| I want to | API reference | Guide |
| --------- | ------------- | ----- |
| Trigger a transactional or marketing message from my system | [Interactive Message Execution API](https://developer.adobe.com/journey-optimizer-apis/references/messaging){target="_blank"} · [Code samples](https://developer.adobe.com/journey-optimizer-apis/references/messaging-samples){target="_blank"} | [Work with API-triggered campaigns](../campaigns/api-triggered-campaigns.md) · [High throughput mode](../campaigns/api-triggered-high-throughput.md) |
| Retrieve and filter Action campaigns | [Campaigns API](https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve){target="_blank"} | [Get started with campaigns](../campaigns/get-started-with-campaigns.md) |
| Preview campaigns and send proofs | [Simulations API](https://developer.adobe.com/journey-optimizer-apis/references/simulations){target="_blank"} | [Work with API-triggered campaigns](../campaigns/api-triggered-campaigns.md) |
| List and retrieve journeys | [Journeys API](https://developer.adobe.com/journey-optimizer-apis/references/journeys-retrieve){target="_blank"} | [Journeys](../building-journeys/journey.md) |
| Protect external systems called by journeys | [Capping and throttling API](https://developer.adobe.com/journey-optimizer-apis/references/journeys-throttling){target="_blank"} | [Capping](capping.md) · [Throttling](throttling.md) · [External systems](external-systems.md) |
| Create and manage content templates and fragments | [Content API](https://developer.adobe.com/journey-optimizer-apis/references/content){target="_blank"} | [Content templates](../content-management/content-templates.md) · [Fragments](../content-management/fragments.md) |
| Exclude email addresses or domains from sending | [Suppression API](https://developer.adobe.com/journey-optimizer-apis/references/suppression){target="_blank"} | [Manage the suppression list](manage-suppression-list.md) |
| Validate datasets, trigger, and monitor Orchestrated campaigns | [Dataset validation](https://developer.adobe.com/journey-optimizer-apis/references/orchestrated-campaign-dataset){target="_blank"} · [Orchestrated campaigns API](https://developer.adobe.com/journey-optimizer-apis/references/orchestrated-campaigns){target="_blank"} | [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) · [Enable datasets](../orchestrated/manual-schema.md) |
| Manage loyalty challenges and their state | [Loyalty challenges API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"} · [State API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges-state){target="_blank"} | [Loyalty challenges APIs](../loyalty-challenges/loyalty-challenges-api.md) |
| Manage decision items, collections, strategies, and rules (Experience Decisioning) | [Decisioning API](../experience-decisioning/api-reference/getting-started.md) | [Get started with Experience Decisioning](../experience-decisioning/gs-experience-decisioning.md) |
| Manage offers, placements, and decisions (Decision Management, legacy) | [Offer Library API reference](../../rp_landing_pages/api-reference-landing-page.md) | [Decision Management API developer guide](../offers/api-reference/getting-started.md) |
| Migrate Decision Management entities to Decisioning | [Decisioning migration API](../experience-decisioning/decisioning-migration-api.md) | [Benefits of migrating to Decisioning](../experience-decisioning/migrate-to-decisioning.md) |

>[!NOTE]
>
>* The Simulations API is not supported for Orchestrated campaigns. Use the preview and proof workflow in the Orchestrated campaigns user interface instead.
>* The Decision Management APIs are legacy. If you use the Decisioning capability, use the Experience Decisioning APIs instead.
>* The Object Copy API is deprecated. To copy objects between sandboxes, use [sandbox tooling](copy-objects-to-sandbox.md).

## Troubleshoot API calls {#troubleshooting}

For authentication and permission errors (`401` and `403`), check your credentials and product profile permissions in [Authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}. For errors returned by a specific API, use the page that matches your task:

| If you work with | See |
| ---------------- | --- |
| API-triggered campaigns and Action campaigns | [Campaign errors](../campaigns/campaign-errors.md) |
| Journeys and capping or throttling | [Error codes reference](../building-journeys/error-codes-reference.md) · [Troubleshoot custom actions](../action/troubleshoot-custom-action.md) |
| Content templates and fragments | [Content authoring errors](../content-management/content-authoring-errors.md) · [Fragments and AEM content errors](../content-management/fragments-errors.md) |
| Simulations and proofs | [Proof and simulation errors](../content-management/proof-simulation-errors.md) |
| Orchestrated campaigns | [Orchestrated campaign errors](../orchestrated/orchestrated-campaign-errors.md) |
| Experience Decisioning | [Troubleshoot Decisioning](../experience-decisioning/decisioning-troubleshooting.md) |

For other errors, start from the [Troubleshooting overview](../../rp_landing_pages/troubleshooting-overview-landing-page.md).

## Related topics {#related-topics}

* [Integrations with other solutions](../integrations/ajo-integrations.md)
* [Custom actions in journeys](../action/about-custom-action-configuration.md)
* [Manage custom channel API credentials](../custom-channel/custom-channel-api-credentials.md)
* [Configure SMS webhooks](../mobile/mobile-webhook.md)
* [Adobe Experience Platform APIs](https://developer.adobe.com/experience-platform-apis){target="_blank"}
