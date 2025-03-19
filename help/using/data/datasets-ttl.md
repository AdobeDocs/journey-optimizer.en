---
solution: Journey Optimizer
product: journey optimizer
title: About datasets Time-to-live (TTL) guardrails
description: Datasets Time-to-live guardrails in [!DNL Adobe Journey Optimizer]
feature: Data Model, Datasets, Data Management
role: Data Engineer, Data Architect, Admin
level: Experienced
keywords: platform, data lake, create, lake, datasets, profile
exl-id: 08633a79-5601-4e36-b8cf-080234956d99
---
# Datasets Time-to-live (TTL) guardrails {#ttl-guardrail}

As of February 2025, a time-to-live (TTL) guardrail is rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* 90 days for data in the profile store,
* 13 months for data in the data lake.

This change will be rolled out to **existing customer sandboxes** in a subsequent phase.

## Impacted datasets {#datasets}

The table below lists all impacted datasets and their respective Time-To-Live in the data lake and the profile store.

|Dataset|Data Lake TTL|Profile Store TTL|
|------|-----|-----|
|AJO Message Feedback Event Dataset|13 months|90 days|
|AJO Email Tracking Experience Event Dataset|13 months|90 days|
|AJO Push Tracking Experience Event Dataset|13 months|90 days|
|AJO Entity Dataset|13 months|90 days|
|AJO Surfaces Dataset|13 months|n/a|
|AJO Inbound Activity Event Dataset|13 months|90 days|
|AJO Classification Dataset|13 months|n/a|
|AJO Email BCC Feedback Event Dataset|13 months|n/a|
|acpEntity Event Dataset|13 months|n/a|
|Journeys|13 months|n/a|
|Journey Step Events|13 months|n/a|
|Decision Object Repository - Personalized Offers|13 months|n/a|
|Decision Object Repository - Fallback Offers|13 months|n/a|
|Decision Object Repository - Placements|13 months|n/a|
|Decision Object Repository - Activities|13 months|n/a|
|ODE DecisionEvents - prod decisioning|13 months|n/a|

## Frequently Asked Questions {#faq}

The following is a list of answers to frequently asked questions about datasets TLL.

+++Will this change apply to production sandboxes only or will it apply to dev sandboxes as well?

This change will apply to all sandbox types.

+++

+++For the 90 day TTL in profile store, are profiles themselves impacted?

The system-generated dataset data in the profile is dropped after 90 days, not the profiles themselves.

+++

+++If a system-generated dataset data is pushed to [!DNL Customer Journey Analytics] (CJA), will the data in CJA also be impacted by the TTL?

Data in [!DNL Customer Journey Analytics] is kept in sync with Experience Platform. Therefore, a removal of data due to a TTL on system-generated dataset data will also impact the data in [!DNL Customer Journey Analytics].

+++

+++ Can customers increase the TTL for [!DNL Journey Optimizer] system dataset data in profile store? 

TTLs extensions are not currently supported. However, work is planned to optimize the TTL process to allow for these extension requests sometime starting the latter-half of 2025. 

>[!NOTE]
>
>Data stored in the profile is subject to the Total Data Volume entitlement. Therefore, any data storage increase on the profile as a result of a TTL extension would count against the Total Data Volume entitlement. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/landing/license/total-data-volume.html){target="_blank}

+++

+++Can customers increase the TTL for [!DNL Journey Optimizer] system dataset data in data lake? 

TTLs extensions are not currently supported. Customers with a Real-Time CDP entitlement can export data through Destinations to retain data longer. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank}

+++

+++Will the following capabilities be impacted by the TTLs? 

* **Look-up store**: No 
* **Journey capping**: No 
* **Offer capping**: No 
* **Send Time Optimization (STO)**: No 
* **Message frequency capping** (i.e., Business rules): No 
* **Reporting**: No

    >[!NOTE]
    >
    >A TTL is already implemented on the [!DNL Customer Journey Analytics] (CJA) connection, which reduces effective max look-back period of impacted dataset data to 13 months.

* **Experience Platform data source**: Yes - Experience event retrieval is subject to the 90 day TTL. 
* **Computed attributes**: Yes - Initial backfill calculation will be limited to last 90 days of data; computed attribute will be updated based on incremental events for subsequent updates. As soon as the subsequent updates reach the look-back period (max 6 months), the TTL essentially no longer affects the computed attribute. Learn more. 
* **Segmentation and retargeting**: Yes - Segmentation is dependent on data in the profile store; therefore, look-back is limited to 90 days on affected dataset data. 
* **Tracking**: Yes - Reduces effective max look-back period of impacted dataset data to 90 days. Data from impacted datasets resides for 13 months in data lake. 

+++

+++What timestamp is used for TTL enforcement (e.g., for backfill use cases)? 

The event timestamp is used (i.e., not the ingestion date).

+++
