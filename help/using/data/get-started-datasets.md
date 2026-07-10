---
solution: Journey Optimizer
product: journey optimizer
title: Get Started with datasets
description: Learn how to use Adobe Experience Platform datasets in Adobe Journey Optimizer
feature: Data Model, Datasets, Data Management
role: Developer, Admin
level: Experienced
keywords: platform, data lake, create, lake, datasets, profile
exl-id: dcdd3c81-0f00-4259-a8a5-9062a4c40b6f
TQID: https://experienceleague.adobe.com/VYD0k1jjQB-7iEShgFWKDfaVl5BFvtnxxjSrqBiYThw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: a1cdc218-59b7-4eef-b5cf-2a7ad74b3371
    internal-label: Journey Optimizer schemas
  - id: d6e5c7fd-c1d6-4137-98cd-138ccde6752f
    internal-label: Datasets
  - id: cf3fbcd7-c075-4ae4-8de5-96e736ab2ea3
    internal-label: Data ingestions
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
---
# Get Started with datasets {#datasets-gs}

>[!BEGINSHADEBOX]

**On this page:** Learn how to access, create, and govern Adobe Experience Platform datasets so you can store and explore the data that powers journeys, campaigns, and reporting in Adobe Journey Optimizer.

>[!ENDSHADEBOX]

All data that is ingested into Adobe Experience Platform is persisted within the Data Lake as datasets. A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows).

## Guardrails & limitations

* As of November 1st, 2024, streaming segmentation no longer supports send and open events from [!DNL Journey Optimizer] tracking and feedback datasets. For implementing Frequency Capping or Fatigue Management, please use Business Rules instead. You can find more details in [this section](../conflict-prioritization/rule-sets.md), including a use case explanation for daily capping [here](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/elevate-customer-experience-with-daily-frequency-capping-in-ajo/ba-p/761510){target="_blank"}.

* As of February 2025, a time-to-live (TTL) guardrail is being rolled out to Journey Optimizer system-generated datasets. [Learn more](datasets-ttl.md)

* Enabling a dataset for Profile has permanent implications at the schema level. Plan your schema and identity design carefully before enabling. [Learn more](#profile-datasets)

## Access datasets {#access}

The **Datasets** workspace in [!DNL Adobe Journey Optimizer] user interface allows you to explore data and create datasets. To open the Datasets dashboard, select **Datasets** in the left-navigation.

![](assets/datasets-home.png)

Select the **Browse** tab to display the list of all available datasets for your organization. Details are displayed for each listed dataset, including its name, the schema the dataset adheres to, and status of the most recent ingestion run. By default, only the datasets that you have ingested into are shown. If you want to see the system-generated datasets, enable the **Show system datasets** toggle from the filter.

![](assets/ajo-system-datasets.png)


Select the name of a dataset to access its Dataset activity screen and see details of the dataset you selected. The activity tab includes a graph visualizing the rate of messages being consumed as well as a list of successful and failed batches.

To preview a dataset, select **Preview dataset** near the top-right corner of your screen to preview the most recent successful batch in this dataset. When a dataset is empty, the preview link is deactivated.

![](assets/dataset-preview.png)

## [!DNL Journey Optimizer] system datasets {#system-datasets}

This sections lists system datasets used by [!DNL Journey Optimizer]. To view the complete list of fields and attributes for each schema, consult the [Journey Optimizer schema dictionary](https://experienceleague.adobe.com/tools/ajo-schemas/schema-dictionary.html){target="_blank"}.

>[!CAUTION]
>
> System datasets **must not be modified**. Any change is automatically reverted with every product update.

* Reporting

    * _Reporting - Message Feedback Event Dataset_: Message delivery logs. Information on all message delivery from Journey Optimizer for reporting and audience creation purposes. Feedback from Email ISPs on bounces is also recorded in this dataset. **This dataset uses batch ingestion — expect a data latency of up to 2 hours.**
    * _Reporting - Email Tracking Experience Event Dataset_: Interaction logs for the Email channel, and WhatsApp channel context data under the `whatsAppChannelContext` field group. Used for reporting and audience creation. Information stored includes actions performed by the end-user on email (opens, clicks, etc.) and WhatsApp interactions.
    * _Reporting - Push Tracking Experience Event Dataset_: Interaction logs for Push channel which is used for reporting and audience creation purposes. Information stored informs on actions performed by the end-user on push notifications.
    * _Reporting - Journey Step Event_: Captures All Journey Step Experience Events generated from Journey Optimizer to be consumed by services like Reporting. Also critical for building reports in Customer Journey Analytics for YoY analysis. Tied to a Journey Metadata.
    * _Reporting - Journeys_: Metadata dataset housing information of each step in a journey.
    * _Reporting - BCC_: Feedback Event Dataset which stores the delivery logs for BCC emails. To be used for reporting purposes.

* Consent

    _Consent Service Dataset_: stores consent information of a profile.

* Message Export

    _AJO Message Export Dataset_: stores the content of sent email and SMS messages for export purposes. Records are retained for 7 calendar days from ingestion. Available only for organizations that have purchased the Message Export add-on. [Learn more](../configuration/message-export.md)

* Intelligent Services

    _Send-Time Optimization Scores / Engagement Scores_: Output scores of Journey AI.

* Inbound

    _AJO Inbound Activity Event Dataset_: Stores inbound activity events for incoming messages received in [!DNL Journey Optimizer].

>[!NOTE]
>
>A profile must have at least one message sent from [!DNL Journey Optimizer] before incoming messages are captured in this dataset.

## Create datasets{#create-datasets}

Adding data to [!DNL Adobe Experience Platform] is the foundation to building a Profile. You will then be able to leverage profiles in [!DNL Adobe Journey Optimizer]. First define schemas, use ETL tools to prepare and standardize your data, then create datasets based on your schemas.

You can create a dataset from schema or a CSV file. Detailed information on how to create datasets is available in [!DNL Adobe Experience Platform] documentation:

* [Create a dataset with an existing schema](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/user-guide#schema){target="_blank"}
* [Map a CSV file to an existing XDM schema](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/tutorials/map-csv/existing-schema){target="_blank"}

Watch this video to learn how to create a dataset, map it to a schema, add data to it, and confirm that the data has been ingested.

>[!VIDEO](https://video.tv.adobe.com/v/334293?quality=12)

## Enable datasets for Profile {#profile-datasets}

When you create a dataset, you can enable it to contribute to [Real-Time Customer Profile](../audience/get-started-profiles.md). This allows the data it contains to be used for segmentation, personalization, and journey conditions in [!DNL Journey Optimizer].

Before enabling, keep the following in mind:

* **Schema enablement is permanent.** Once the schema underlying a dataset is enabled for Profile, this cannot be reversed — the schema cannot be disabled or deleted. Only the dataset itself can be disabled or deleted separately.
* **Disabling a dataset has consequences.** You can disable or delete a dataset for Profile independently of its schema, but doing so removes the associated profile records and may disrupt segmentation and activation workflows.
* **Plan your configuration before enabling.** Identity fields and field group selections become harder to change after Profile enablement. Finalize your schema design first.

For detailed guidance, refer to the Adobe Experience Platform documentation:

* [Profile enablement planning](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/profile-enablement-planning){target="_blank"} — pre-enablement checklist covering identity configuration, field group selection, and dataset purpose validation.
* [Managing profile-enabled schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/best-practices#managing-profile-enabled-schemas){target="_blank"} — guidance on deprecating profile-enabled schemas, including renaming strategies.

## Data Governance

In a dataset, browse the **Data Governance** tab to check labels at the dataset and field level. Data Governance categorize data according to the type of policies that apply.

One of the core capabilities of [!DNL Adobe Experience Platform] is to bring data from multiple enterprise systems together to better allow marketers to identify, understand, and engage customers. This data may be subject to usage restrictions defined by your organization or by legal regulations. It is therefore important to ensure that your data operations are compliant with data usage policies.

[!DNL Adobe Experience Platform Data Governance] allows you to manage customer data and ensure compliance with regulations, restrictions, and policies applicable to data use. It plays a key role within Experience Platform at various levels, including cataloging, data lineage, data usage labeling, data usage policies, and controlling usage of data for marketing actions.

Learn more about Data Governance and data usage labels in the [Data Governance documentation](https://experienceleague.adobe.com/docs/experience-platform/data-governance/labels/user-guide.html){target="_blank"}

## Sample & use cases {#samples}

* [Tutorial - Ingest data into Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/ingestion/tutorials/ingest-batch-data.html){target="_blank"}
* [End-to-end use case](../audience/creating-test-profiles.md) - Create a schema, a dataset and ingest data to add Test profiles in [!DNL Adobe Journey Optimizer]
* [Query examples](../data/datasets-query-examples.md) - [!DNL Adobe Journey Optimizer] datasets and related use cases.

>[!MORELIKETHIS]
>
>* [Get started with data management in Journey Optimizer](gs-data.md)
>* [Datasets documentation](https://experienceleague.adobe.com/docs/experience-platform/catalog/datasets/overview.html){target="_blank"}
>* [Data Ingestion documentation](https://experienceleague.adobe.com/docs/experience-platform/ingestion/home.html){target="_blank"}.
>* [Data management license entitlement best practices](https://experienceleague.adobe.com/en/docs/experience-platform/landing/license/data-management-best-practices#data-management-best-practices){target="_blank"}
>* [Managing profile-enabled schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/best-practices#managing-profile-enabled-schemas){target="_blank"}
