---
solution: Journey Optimizer
product: journey optimizer
title: Migrate batch audiences from Audience Qualification journeys
description: Learn how to migrate journeys that use batch audiences in an Audience Qualification node before the August 3, 2026 enforcement date.
feature: Journeys, Activities, Audiences
topic: Content Management
role: User
level: Intermediate
hide: true
keywords: audience qualification, batch audience, deprecation, migration, read audience, streaming audience
exl-id: f3c2a7d1-b58e-4a92-c3d5-0e871f2a9b4c
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
---

# Migrate batch audiences from Audience Qualification journeys {#aq-batch-migration}

Starting August 3, 2026, Journey Optimizer will block publication for journeys that use a batch audience in an Audience Qualification node. Identify your use case below and follow the recommended migration path. 

>[!CAUTION]
>
>**Enforcement date: August 3, 2026.** New, draft, and duplicated journeys using a batch audience in an Audience Qualification node cannot be published after this date. A validation warning is already surfaced in the journey canvas since the June 2026 release.

## Why this change {#why}

The **[Audience Qualification](audience-qualification-events.md)** node is designed to react in near-real time as individual profiles enter or exit an audience — qualification events arrive continuously, one by one. It is intended for **[streaming audiences](../audience/creating-a-segment-definition.md#evaluation-method-in-journey-optimizer)**.

When a batch audience is used with an Audience Qualification node instead, all qualification events arrive simultaneously during the ingestion window. This can trigger tens of thousands or millions of journey entries at the same instant, causing severe system strain and unpredictable behavior in downstream systems. This is not the intended design of the Audience Qualification node.

The **[Read Audience](read-audience.md)** activity is the right tool for batch-based use cases: it is built to handle scheduled, bulk processing in a controlled and predictable way.

## How your journeys are affected {#impact}

A live journey that uses a batch audience in an Audience Qualification node continues to run after August 3, 2026. However, if you stop, duplicate, or republish the journey, it will be blocked until the configuration is updated.


| Journey status | Impact after August 3, 2026 |
| --- | --- |
| **Live journeys** | Not impacted. Existing live journeys continue to run. No automatic stopping. |
| **New journeys** | Blocked from publication until the batch audience is replaced. |
| **Draft journeys** | Blocked from publication until the batch audience is replaced. |
| **Duplicated journeys** | Blocked from publication until the batch audience is replaced. |


## Migration guide {#migration-paths}

If you are using a batch audience in an Audience Qualification node, identify your use case below and follow the recommended migration path.

### Use case 1 — Audience built on AJO message tracking events {#use-case-1}

**What it looks like:** Your Audience Qualification audience uses conditions based on email sends, opens, or clicks from Journey Optimizer's internal tracking datasets — for example, *"profile received an email"* or *"profile opened an email."*

>[!NOTE]
>
>Since November 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking datasets. Audiences based on these events are now evaluated in batch mode. [Learn more about audience evaluation methods](../audience/creating-a-segment-definition.md#evaluation-method-in-journey-optimizer)

**Recommended alternatives:**

* **Reacting to opens or clicks within the same journey** — Use the **[Reaction event](reaction-events.md)** node. It is purpose-built to respond to opens and clicks from a message sent within that same journey, without requiring a separate audience. [See an end-to-end example using Reaction events](journeys-uc.md#send-multi-channel-messages)

* **Cross-journey click targeting** — Build a [streaming audience](../audience/creating-a-segment-definition.md#evaluation-method-in-journey-optimizer) from click events and use the Audience Qualification node with that streaming audience instead.

* **Bounce-based suppression** — Use Journey Optimizer's native [suppression list](../configuration/manage-suppression-list.md) rather than modeling bounce behavior as an audience condition.

* **Any remaining send/open logic** — Switch to a **[Read Audience](read-audience.md)** journey on a scheduled run to process the batch audience safely.


### Use case 2 — Journey waiting for fresh batch segmentation data {#use-case-2}

**What it looks like:** You schedule a journey to run after a daily segmentation job, and use an Audience Qualification node to ensure the journey only fires once the latest audience data is available.

**Recommended alternative:**

Use a **[Read Audience](read-audience.md)** journey with the **[!UICONTROL Trigger after batch audience evaluation]** option enabled. This built-in feature holds journey execution until the segmentation job completes, then starts immediately when fresh data is available — without requiring an Audience Qualification node. [Learn how to configure this option](read-audience.md#schedule)


### Use case 3 — Large periodic batch audience activation {#use-case-3}

**What it looks like:** You activate or refresh a large audience (potentially millions of profiles) on a periodic basis, and the Audience Qualification journey fires for all newly qualified profiles at once.

**Recommended alternative:**

Use a **[Read Audience](read-audience.md)** journey. It is purpose-built for processing large audiences in bulk, handling profiles in controlled batches and delivering more predictable, reliable journey execution at scale. [See an end-to-end example](message-to-subscribers-uc.md)

## What if none of the alternatives work for your use case? {#exceptions}

If your use case cannot be solved using any of the migration paths above, contact your Adobe representative. Cases that cannot be addressed with existing alternatives will be reviewed individually.

## Related resources {#related}

* [Audience Qualification events](audience-qualification-events.md) — full configuration guide and guardrails
* [Read Audience activity](read-audience.md) — how to configure scheduled batch audience entry
* [Reaction events](reaction-events.md) — how to react to opens and clicks within the same journey
* [Audience evaluation methods](../audience/creating-a-segment-definition.md#evaluation-method-in-journey-optimizer) — batch, streaming, and edge segmentation explained
* [About audiences](../audience/about-audiences.md) — audience types and how they are built in Journey Optimizer
* [Manage the suppression list](../configuration/manage-suppression-list.md) — how to access and configure bounce suppression
* [Journey guardrails and limitations](limitations.md)
* [Journey entry and exit criteria](entry-exit-criteria-guide.md) — understand real-time vs batch entry patterns with real-world examples
* [Send multi-channel messages](journeys-uc.md#send-multi-channel-messages) — end-to-end use case combining Read Audience, Reaction events, email, and push
* [Send a message to subscribers](message-to-subscribers-uc.md) — end-to-end use case for bulk audience activation with Read Audience
