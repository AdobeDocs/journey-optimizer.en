---
solution: Journey Optimizer
product: journey optimizer
title: Vendor Integration
description: Use Adobe Journey Optimizer Integrations with any external platform that exposes a valid API, plus engineering-tested vendor patterns for confidence when you design your setup.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
hide: true
keywords: integration, vendor, third-party
---

# Vendors integration {#vendor-integration}

>[!BEGINSHADEBOX]

Table of content:

* [Work with Integrations](integrations.md)
* **[Get started with Vendors integration](vendor-integration-gs.md)**
* [Available vendors](vendor-integration.md)
* [FAQ](vendor-integration-faq.md) 

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

* **Content management system:** [Contentful](#contentful), [Sitecore](#sitecore), [Salsify](#salsify), [Contentstack](#contentstack), [Akeneo](#akeneo), [Magnolia](#magnolia)
* **Loyalty and rewards:** [Voucherify](#voucherify), [Talon.One](#talon-one), [Antavo](#antavo), [Salesforce Loyalty](#salesforce-loyalty), [Capillary](#capillary)
* **Templates, personalization and recommendations:** [Stensul](#stensul), [Marigold](#marigold), [Adobe Target Recommendations](#adobe-target-recommendations)
* **Data, weather, and operations:** [AccuWeather](#accuweather), [ShipStation](#shipstation), [RevenueCat](#revenuecat), [Databricks](#databricks)
* **Reviews, consent, and social:** [Bynder](#bynder), [Trustpilot](#trustpilot), [Bazaarvoice](#bazaarvoice), [OneTrust](#onetrust), [Meta](#meta), [Aprimo](#aprimo), [Epsilon (Epsilon3)](#epsilon)
