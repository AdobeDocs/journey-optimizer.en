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
TQID: https://experienceleague.adobe.com/DvcQ6AcWhNIZXnTtmPozvSTp1Ait-oo-8wlo8hQ6xlI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
subfeature_v2:
  - id: a1cdc218-59b7-4eef-b5cf-2a7ad74b3371
    internal-label: Journey Optimizer schemas
  - id: d6e5c7fd-c1d6-4137-98cd-138ccde6752f
    internal-label: Datasets
  - id: cf3fbcd7-c075-4ae4-8de5-96e736ab2ea3
    internal-label: Data ingestions
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
  - id: ff2b9b37-92e0-45fc-b853-379d44c08c89
    internal-label: Audience segmentation
---
# Datasets Time-to-live (TTL) guardrails {#ttl-guardrail}

>[!BEGINSHADEBOX]

**On this page:** Understand the time-to-live retention limits on Journey Optimizer system-generated datasets so you can plan how long tracking, feedback, and journey data stays available and retain critical data before it expires.

>[!ENDSHADEBOX]

As of February 2025, a time-to-live (TTL) guardrail is rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* 90 days for data in the profile store,
* 13 months for data in the data lake.

This change will be enforced on **existing customer sandboxes** starting **October 1, 2026**.

## Impacted datasets {#datasets}

The table below lists all impacted datasets and their respective Time-To-Live in the data lake and the [Profile Store](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html#profile-data-store){target="_blank"}.

|Dataset|Data Lake TTL|Profile Store TTL|
|------|-----|-----|
|AJO Message Feedback Event Dataset|13 months|90 days|
|AJO Email Tracking Experience Event Dataset|13 months|90 days|
|AJO Push Tracking Experience Event Dataset|13 months|90 days|
|AJO Surfaces Dataset|13 months|n/a|
|AJO Inbound Activity Event Dataset|13 months|90 days|
|AJO Secondary Recipient Feedback Event Dataset|13 months|n/a|
|Entity Event Dataset|13 months|n/a|
|Journey Step Events|13 months|n/a|
|ODE DecisionEvents - prod decisioning|13 months|n/a|

## Frequently asked questions {#faq}

You will find below Frequently Asked Questions about datasets Time-to-live (TTL).

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en){target="_blank"}.

+++Which types of datasets are subject to TTL?

TTL applies only to time-series datasets. Record-type datasets (such as entity datasets, classification datasets, and decision object repositories) are not subject to TTL and therefore do not appear in the Impacted datasets table above.

+++

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
>Data stored in the profile is subject to the Total Data Volume entitlement. Therefore, any data storage increase on the profile as a result of a TTL extension would count against the Total Data Volume entitlement. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/landing/license/total-data-volume.html){target="_blank"}

+++

+++Can customers increase the TTL for [!DNL Journey Optimizer] system dataset data in data lake? 

TTLs extensions are not currently supported. Customers can export data through Destinations to retain data longer. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank"}. Additionally, customers with a **[!DNL Data Distiller]** entitlement can create derived datasets to store the data in data lake without a TTL. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller/derived-datasets/overview){target="_blank"}

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

Customers who require longer retention have two options:

* **Export to external storage**: export relevant data from AJO datasets before the TTL expiration. Adobe Journey Optimizer supports exporting datasets to various cloud storage destinations (Amazon S3, Azure Blob, Google Cloud Storage, etc.). [Learn more](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank"}
* **Data Distiller derived datasets**: customers with a Data Distiller entitlement can set up automated queries to copy critical data into a derived dataset in the data lake, which can be stored without a TTL. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller/derived-datasets/overview){target="_blank"}

+++

+++What should customers do to prepare for the TTL change?

* Review your use cases and identify any that require data retention beyond the new TTLs.
* Set up automated queries to copy critical data to derived datasets before data is deleted.
* Work with your Adobe representative to discuss any additional needs or potential TTL extensions (planned for future releases).

+++

+++How are customers notified before the TTL is enforced on existing sandboxes?

Adobe notifies impacted customers before enforcing the TTL on existing sandboxes. For this rollout, Adobe sent an in-product notification and published this change in the product release notes, giving customers about two months' notice before the guardrail takes effect on October 1, 2026.

+++

+++Can I delete Journey Optimizer system-generated datasets?

Journey Optimizer system-generated datasets are protected and cannot be deleted through the standard Adobe Experience Platform UI. These datasets are essential for Journey Optimizer functionality and are managed by the system.

If you need to permanently remove a Journey Optimizer system dataset (e.g., for QA environments, sandbox cleanup, or specific data hygiene requirements), please contact Adobe Engineering or Adobe Customer Care. These datasets require specialized backend procedures to ensure complete and safe removal.

>[!NOTE]
>
>For routine data cleanup within these system datasets, use the **[!UICONTROL Data Lifecycle]** operations available through the Privacy Service to delete specific records or identities. [Learn more](../privacy/data-hygiene.md)


+++
