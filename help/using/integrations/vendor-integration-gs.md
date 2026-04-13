---
solution: Journey Optimizer
product: journey optimizer
title: Vendor Integration
description: Use Adobe Journey Optimizer Integrations with any external platform that exposes a valid API, plus engineering-tested vendor patterns for confidence when you design your setup.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
keywords: integration, vendor, third-party
---

# Get started with Vendors integration {#vendor-integration}

You can use **Integrations** in Adobe Journey Optimizer to call **external systems over HTTP** when each system exposes an **API endpoint** that suits your use case and is compatible with how Integrations issues requests and consumes responses. For complete workflow, see [Work with Integrations](external-sources.md).

The list of third-party solutions described is illustrative, not exhaustive. Other platforms may be used where they satisfy product requirements.

## Operational guardrails {#operational-guardrails}

Apply the following when you configure any integration in this guide or a similar vendor:

* **Response format:** Integrations map fields from **JSON** responses. Design calls so the API returns JSON suitable for mapping at authoring time.
* **Payload and fields:** Request and map only the attributes you need. Smaller responses reduce latency and limit exposure of sensitive data.
* **Endpoint shape:** Prefer stable, **single-resource** retrieval (for example one entry, product, or member) over broad list or pagination endpoints when the product expects targeted lookups. See [Limitations & exclusions](#limitations-exclusions) and [Work with Integrations](external-sources.md).
* **Volume and reliability:** Respect the vendor's **rate limits**. Configure **timeout**, **retry**, and **cache** policy for your channel (for example batch email vs transactional sends) and validate under load.
* **Security:** Store and rotate tokens, API keys, and OAuth credentials according to your organization's policies. Do not embed secrets in message content.

## Limitations & exclusions {#limitations-exclusions}

The third-party solutions list is **illustrative**, not exhaustive. Vendor APIs, hosts, rate limits, and JSON response shapes can change. Confirm endpoints, authentication, and field mapping with the vendor's current documentation and your subscription. Patterns here assume **read-oriented** calls suitable for personalization. Write-back, batch exports, or non-JSON responses may be out of scope unless noted.

## Quick navigation {#quick-navigation}

Use these grouped links to jump to the relevant vendor pattern quickly:

* **Content and CMS:** [Contentful](#contentful), [Sitecore](#sitecore), [Salsify](#salsify), [Contentstack](#contentstack), [Akeneo](#akeneo), [Magnolia](#magnolia)
* **Loyalty and rewards:** [Voucherify](#voucherify), [Talon.One](#talon-one), [Antavo](#antavo), [Salesforce Loyalty](#salesforce-loyalty), [Capillary](#capillary)
* **Templates and messaging:** [Stensul](#stensul), [Marigold](#marigold), [Adobe Target Recommendations](#adobe-target-recommendations)
* **Data, weather, and operations:** [AccuWeather](#accuweather), [ShipStation](#shipstation), [RevenueCat](#revenuecat), [Databricks](#databricks)
* **Reviews, consent, and social:** [Bynder](#bynder), [Trustpilot](#trustpilot), [Bazaarvoice](#bazaarvoice), [OneTrust](#onetrust), [Meta](#meta), [Aprimo](#aprimo), [Epsilon (Epsilon3)](#epsilon)
