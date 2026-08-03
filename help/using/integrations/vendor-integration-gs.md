---
solution: Journey Optimizer
product: journey optimizer
title: Vendor Integration
description: Use Adobe Journey Optimizer Integrations with any external platform that exposes a valid API, plus engineering-tested vendor patterns for confidence when you design your setup.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
keywords: integration, vendor, third-party
subfeature_v2: []
feature_v2:
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
---

# Vendors integration {#vendor-integration}

>[!BEGINSHADEBOX]

**On this page:** Browse sample, Adobe-tested configurations for connecting Adobe Journey Optimizer Integrations to third-party vendors across content, loyalty, recommendation, data, and consent platforms.

>[!ENDSHADEBOX]

You can use **Integrations** in Adobe Journey Optimizer to call **external systems over HTTP** when each system exposes an **API endpoint** that suits your use case and is compatible with how Integrations issues requests and consumes responses. For complete workflow, see [Work with Integrations](integrations.md).

The list of third-party solutions described is illustrative, not exhaustive. Other platforms may be used where they satisfy product requirements.

## Operational guardrails {#operational-guardrails}

Apply the following when you configure any integration in this guide or a similar vendor:

* **Response format:** Integrations map fields from **JSON** or **HTML** responses. Design calls so the API returns JSON or HTML suitable for mapping at authoring time.
* **Payload and fields:** Request and map only the attributes you need. Smaller responses reduce latency and limit exposure of sensitive data.
* **Endpoint shape:** Prefer stable, **single-resource** retrieval (for example one entry, product, or member) over broad list or pagination endpoints when the product expects targeted lookups. See [Limitations & exclusions](#limitations-exclusions) and [Work with Integrations](integrations.md).
* **Volume and reliability:** Respect the vendor's **rate limits**. Configure **timeout**, **retry**, and **cache** policy for your channel (for example batch email vs transactional sends) and validate under load.
* **Security:** Store and rotate tokens, API keys, and OAuth credentials according to your organization's policies. Do not embed secrets in message content.


## Limitations & exclusions {#limitations-exclusions}

The third-party solutions list is **illustrative**, not exhaustive. Vendor APIs, hosts, rate limits, and JSON or HTML response shapes can change. Confirm endpoints, authentication, and field mapping with the vendor's current documentation and your subscription. Patterns here assume **read-oriented** calls suitable for personalization. Integrations supports mapping from **JSON** and **HTML** responses only. **Write-back**, **batch exports**, and responses in any other format are not supported.

## Quick navigation {#quick-navigation}

Use these grouped links to jump to the relevant vendor pattern quickly:

* **Content management system:** [Contentful](vendor-integration.md#contentful), [Sitecore](vendor-integration.md#sitecore), [Salsify](vendor-integration.md#salsify), [Contentstack](vendor-integration.md#contentstack), [Akeneo](vendor-integration.md#akeneo), [Magnolia](vendor-integration.md#magnolia)
* **Loyalty and rewards:** [Voucherify](vendor-integration.md#voucherify), [Talon.One](vendor-integration.md#talon-one), [Antavo](vendor-integration.md#antavo), [Salesforce Loyalty](vendor-integration.md#salesforce-loyalty), [Capillary](vendor-integration.md#capillary)
* **Templates, personalization and recommendations:** [Stensul](vendor-integration.md#stensul), [Marigold](vendor-integration.md#marigold), [Adobe Target Recommendations](vendor-integration.md#adobe-target-recommendations)
* **Data, weather, and operations:** [AccuWeather](vendor-integration.md#accuweather), [ShipStation](vendor-integration.md#shipstation), [RevenueCat](vendor-integration.md#revenuecat), [Databricks](vendor-integration.md#databricks)
* **Reviews, consent, and social:** [Bynder](vendor-integration.md#bynder), [Trustpilot](vendor-integration.md#trustpilot), [Bazaarvoice](vendor-integration.md#bazaarvoice), [OneTrust](vendor-integration.md#onetrust), [Meta](vendor-integration.md#meta), [Aprimo](vendor-integration.md#aprimo), [Epsilon (Epsilon3)](vendor-integration.md#epsilon)
