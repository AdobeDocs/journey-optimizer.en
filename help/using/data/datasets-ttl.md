---
solution: Journey Optimizer
product: journey optimizer
title: About datasets Time-to-live (TTL) guardrails
description: Datasets Time-to-live guardrails in [!DNL Adobe Journey Optimizer]
feature: Data Model, Datasets, Data Management
role: Developer, Admin
level: Experienced
keywords: platform, data lake, create, lake, datasets, profile
exl-id: 08633a79-5601-4e36-b8cf-080234956d99
---
# Datasets Time-to-live (TTL) guardrails {#ttl-guardrail}

As of February 2025, a time-to-live (TTL) guardrail is rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* 90 days for data in the profile store,
* 13 months for data in the data lake.

This change is being rolled out to **existing customer sandboxes** in a subsequent phase.

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
|Entity Event Dataset|13 months|n/a|
|Journeys|13 months|n/a|
|Journey Step Events|13 months|n/a|
|Decision Object Repository - Personalized Offers|13 months|n/a|
|Decision Object Repository - Fallback Offers|13 months|n/a|
|Decision Object Repository - Placements|13 months|n/a|
|Decision Object Repository - Activities|13 months|n/a|
|Experience Decisioning Object Repository - Personalized Offer Items|13 months|n/a|
|ODE DecisionEvents - prod decisioning|13 months|n/a|

## Frequently Asked Questions {#faq}

You will find below Frequently Asked Questions about datasets Time-to-live (TTL).

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en){target="_blank"}.

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

TTLs extensions are not currently supported. Customers can export data through Destinations to retain data longer. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank}. Additionally, customers with a **[!DNL Data Distiller]** entitlement can create derived datasets to store the data in data lake without a TTL. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller/derived-datasets/overview){target="_blank}

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

* **Experience Platform data source**: Not applicable - Experience event retrieval is not supported via data sources. 
* **Computed attributes**: Yes - Initial backfill calculation will be limited to last 90 days of data; computed attribute will be updated based on incremental events for subsequent updates. As soon as the subsequent updates reach the look-back period (max 6 months), the TTL essentially no longer affects the computed attribute. Learn more. 
* **Segmentation and retargeting**: Yes - Segmentation is dependent on data in the profile store; therefore, look-back is limited to 90 days on affected dataset data. 
* **Tracking**: Yes - Reduces effective max look-back period of impacted dataset data to 90 days. Data from impacted datasets resides for 13 months in data lake. 

+++

+++What timestamp is used for TTL enforcement (e.g., for backfill use cases)? 

The event timestamp is used (i.e., not the ingestion date).

+++

+++How does the new TTL affect use cases that require longer data retention (e.g., excluding profiles who received an email in the past 120 days, or capping emails over a year)?

The new TTL policy will limit the look-back period for system-generated dataset data in the profile store to 90 days and in the data lake to 13 months. Use cases that require access to data beyond these periods will be impacted. For example, audience segmentation or frequency capping based on events older than 90 days in the profile store will no longer be possible using system datasets.

+++

+++What alternatives are available for retaining data longer than the TTL?

Customers who require longer retention should consider exporting relevant data from AJO datasets to external storage before the TTL expiration. Adobe Journey Optimizer supports exporting datasets to various cloud storage destinations (Amazon S3, Azure Blob, Google Cloud Storage, etc.). [Learn more](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank}

+++

+++What should customers do to prepare for the TTL change?

* Review your use cases and identify any that require data retention beyond the new TTLs.
* Set up automated exports for critical datasets to external storage before data is purged.
* Work with your Adobe representative to discuss any additional needs or potential TTL extensions (planned for future releases).

+++

+++Will customers be notified before the TTL is enforced on existing sandboxes?

Yes, impacted customers will be notified in advance, and the product team will work with them to ensure a smooth transition.

+++
