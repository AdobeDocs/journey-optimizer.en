---
solution: Journey Optimizer
product: journey optimizer
title: Loyalty data and datasets
description: Learn which Adobe Experience Platform profile data and datasets Loyalty Challenges requires, and how dataset time-to-live (TTL) affects retention.
feature: Journeys
topic: Content Management
role: Admin, Developer
level: Intermediate
hide: true
badge: label="Private beta" type="Informative"
mini-toc-levels: 1
exl-id: a7c4e1b2-8f3d-4a6c-9e0b-1d2e3f4a5b6c
---
# Loyalty data and datasets {#loyalty-data-and-datasets}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation** 

[Get started with Loyalty Challenges](get-started.md)

+++Create and manage challenges

* [Access & manage challenges and tasks](access-loyalty-challenges.md)
* [Create challenges](create-challenges.md)
* [Create tasks](create-tasks.md)
* [Monitor loyalty challenge performance](loyalty-reporting.md)

+++

+++Configure and integrate

<!-- * [Configure loyalty challenges](loyalty-admin.md) -->
* **Loyalty data and datasets** ◀︎ **You are here**
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}

+++

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta**. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../rn/releases.md).

## Overview {#overview}

Loyalty Challenges relies on Adobe Experience Platform for identity, profile attributes, experience events, and audiences. Use this page to learn which data to prepare, which datasets are involved, and how **time-to-live (TTL)** affects retention before you author challenges or use the Loyalty Challenges APIs.

Contact your Adobe administrator for Journey Optimizer program setup (reward fulfillment and event mapping). For REST endpoints and authentication, see the [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}.

## Adobe Experience Platform data {#aep-data}

### Profile attributes {#profile-attributes}

Challenge audiences, personalization, and reporting use profiles in the **[!DNL XDM Individual Profile]** class. Align the identity [namespace](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces){target="_blank"} you use for Loyalty Challenges with how members are identified in your profile data.

For standard loyalty attributes on the profile (points, tier, program, status, and related fields), use the Experience Platform **[Loyalty Details](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/loyalty-details){target="_blank"}** schema field group. That field group defines the `loyalty` object and its properties (for example `points`, `tier`, `program`, and `status`).

➡️ [Loyalty Details schema field group](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/loyalty-details){target="_blank"}

### Experience events {#experience-events}

**[!UICONTROL Purchase]**, **[!UICONTROL Spend]**, and **[!UICONTROL Custom event]** tasks depend on experience events ingested into Adobe Experience Platform. For **[!UICONTROL Custom event]** tasks, your administrator must configure matching event definitions (identifier path, optional XDM schema ID, schema, and transformer) before you can select them in the task builder.

Ensure event payloads use the same identity namespace as your Loyalty Challenges configuration so progress can be attributed to the correct profile.

### Audiences and reporting {#audiences-reporting}

Marketers select Platform [audiences](../audience/about-audiences.md) when configuring challenge eligibility. Loyalty reporting dashboards use Adobe Customer Journey Analytics. [Learn how to monitor loyalty challenge performance](loyalty-reporting.md)

## Dataset time-to-live (TTL) {#dataset-ttl}

Loyalty Challenges stores operational and reporting data in Adobe Experience Platform datasets (including event and personalization-related datasets created for your program). Dataset **time-to-live (TTL)** controls how long data is retained in the data lake and, when applicable, in the Profile store.

Journey Optimizer applies TTL guardrails to many system-generated datasets. Loyalty-related datasets follow the same Platform retention model for your sandbox.

➡️ [Datasets Time-to-live (TTL) guardrails in Journey Optimizer](../data/datasets-ttl.md)

>[!NOTE]
>
>Organization-level loyalty configuration can include archive and retention settings (for example, archive duration) managed through the Loyalty metadata service. Coordinate with your Adobe administrator if you need to adjust retention for your private beta environment.

<!-- For UI-based setup (reward providers, event definitions, product inventory, and exclusions), see [Configure loyalty challenges](loyalty-admin.md). -->
