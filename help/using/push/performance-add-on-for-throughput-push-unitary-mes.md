---
solution: Journey Optimizer
product: journey optimizer
title: Performance Add-on for throughput - (Push) Unitary - Message Delivery
description: Learn how to configure and use Performance Add-on for throughput - (Push) Unitary - Message Delivery in Adobe Journey Optimizer.
feature: Push
topic: Content Management
role: User
level: Intermediate
exl-id: 2d0677ad-41c8-4299-a7c8-0e4f8a1716f7
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b6b77c26-2a48-4a62-9ceb-5ae67f4dfde5
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---

# Performance Add-on for throughput - (Push) Unitary - Message Delivery {#performance-add-on-for-throughput-push-unitary-mes}

>[!AVAILABILITY]
>
>This capability is available from **AJO26.7** (2026-07-27).

## Overview {#overview}

Adobe Journey Optimizer introduces **Performance Add-on for throughput - (Push) Unitary - Message Delivery**, enabling organizations to deliver more relevant, personalized customer experiences across push channels.

This page explains how to configure and use this feature in your campaigns and journeys.

## Prerequisites {#prerequisites}

Before you begin:

* You have access to Adobe Journey Optimizer with the required **Push** permissions.
* A Push channel surface is configured. See [Configure Push channel](../configuration/channel-surfaces.md).

## How it works {#how-it-works}

Performance Add-on for throughput - (Push) Unitary - Message Delivery integrates directly with the AJO execution engine. When a profile reaches a push action in a journey or campaign, the feature applies the configured parameters at send time.

Key capabilities:

* **Profile-level personalization** — settings adapt per recipient using profile and context attributes.
* **Journey and campaign support** — works in both orchestrated journeys and one-off campaigns.
* **Real-time metrics** — results appear in the [Push reports](../reports/push-report.md).

## Configure Performance Add-on for throughput {#configure}

1. In the AJO left menu, navigate to **Channels** > **Push configurations**.
1. Select or create a channel configuration.
1. In the **Performance Add-on for** section, enable the feature.
1. Set the required parameters.
1. Click **Save**.

>[!NOTE]
>
>Configuration changes apply to new journey executions. In-progress journeys are unaffected.

## Related topics {#related-topics}

* [Get started with Push](get-started-push.md)
* [Create a Push notification](create-push.md)
* [AJO26.7 Release Notes](../rn/release-notes.md)
