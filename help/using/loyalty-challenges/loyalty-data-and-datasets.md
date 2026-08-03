---
solution: Journey Optimizer
product: journey optimizer
title: Loyalty data and datasets
description: Learn which Adobe Experience Platform profile data and datasets Loyalty Challenges requires, and how dataset time-to-live (TTL) affects retention.
feature: Journeys
topic: Content Management
role: Admin, Developer
level: Intermediate
exl-id: a7c4e1b2-8f3d-4a6c-9e0b-1d2e3f4a5b6c
feature_v2: []
subfeature_v2: []
---
# Loyalty data and datasets {#loyalty-data-and-datasets}

## Overview {#overview}

Loyalty Challenges relies on Adobe Experience Platform for identity, profile attributes, experience events, and audiences. Use this page to learn which data to prepare, which datasets are involved, and how **time-to-live (TTL)** affects retention before you author challenges or use the Loyalty Challenges APIs.

Contact your Adobe administrator for Journey Optimizer program setup, or configure reward fulfillment and event mapping in the **[!UICONTROL Loyalty configurations]** menu. [Learn how to configure loyalty challenges](loyalty-admin.md). For REST endpoints and authentication, see the [Loyalty challenge metadata API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"} and the [Loyalty challenge state API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges-state){target="_blank"}.

## Loyalty connectors via Sources {#loyalty-connectors-sources}

If your loyalty data is managed in an external rewards platform, you can ingest that data into Adobe Experience Platform using **Sources** connectors, then use it in Loyalty Challenges.

Loyalty and rewards connectors listed in Journey Optimizer documentation include:

* **Talon.One**
* **Capillary**
* **Kobie**

For connector onboarding and end-to-end setup, see [Get started with sources connectors](../start/get-started-sources.md) and the [Experience Platform sources catalog](https://experienceleague.adobe.com/docs/experience-platform/sources/home.html#sources-catalog){target="_blank"}.

## Adobe Experience Platform data {#aep-data}

### Profile attributes {#profile-attributes}

Challenge audiences, personalization, and reporting use profiles in the **[!DNL XDM Individual Profile]** class. Align the identity [namespace](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces){target="_blank"} you use for Loyalty Challenges with how members are identified in your profile data and with the namespace selected in **[!UICONTROL Global settings]** in the **[!UICONTROL Loyalty configurations]** menu.

For standard loyalty attributes on the profile (points, tier, program, status, and related fields), use the Experience Platform **[Loyalty Details](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/loyalty-details){target="_blank"}** schema field group. That field group defines the `loyalty` object and its properties (for example `points`, `tier`, `program`, and `status`).

➡️ [Loyalty Details schema field group](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/loyalty-details){target="_blank"}

➡️ [AJO schema dictionary](https://experienceleague.adobe.com/tools/ajo-schemas/schema-dictionary.html?lang=en){target="_blank"}

### Experience events {#experience-events}

**[!UICONTROL Purchase]**, **[!UICONTROL Spend]**, and **[!UICONTROL Custom event]** tasks depend on experience events ingested into Adobe Experience Platform. For **[!UICONTROL Custom event]** tasks, matching event definitions (identifier path, XDM schema ID, schema, and transformer) must be configured in the **[!UICONTROL Loyalty configurations]** menu before marketers can enter custom event values in the task builder. [Learn how to configure event definitions](loyalty-admin.md#event-definitions)

Ensure event payloads use the same identity namespace as your Loyalty Challenges configuration so progress can be attributed to the correct profile.

### Audiences and reporting {#audiences-reporting}

Marketers select Platform [audiences](../audience/about-audiences.md) when configuring challenge eligibility. Loyalty reporting dashboards use Adobe Customer Journey Analytics. [Learn how to monitor loyalty challenge performance](loyalty-reporting.md)

## Dataset time-to-live (TTL) {#dataset-ttl}

Loyalty Challenges stores operational and reporting data in Adobe Experience Platform datasets (including event and personalization-related datasets created for your program). Dataset **time-to-live (TTL)** controls how long data is retained in the data lake and, when applicable, in the Profile store.

Journey Optimizer applies TTL guardrails to many system-generated datasets. Loyalty-related datasets follow the same Platform retention model for your sandbox.

➡️ [Datasets Time-to-live (TTL) guardrails in Journey Optimizer](../data/datasets-ttl.md)

>[!NOTE]
>
>Organization-level loyalty configuration can include archive and retention settings (for example, archive duration) managed through the Loyalty metadata service. Coordinate with your Adobe administrator if you need to adjust retention for your organization.

