---
solution: Journey Optimizer
product: journey optimizer
title: Export datasets to cloud storage locations
description: Learn how to export your datasets using Adobe Experience Platform cloud storage destinations.
feature: Datasets
role: User
level: Beginner
keywords: platform, data lake, create, lake, datasets, profile
exl-id: 66b5c691-ddc4-4e9b-9386-2ce6c307451c
---
# Export datasets to cloud storage locations {#export-datasets}

Journey Optimizer allows you to establish a live connection with cloud storage locations in order to export the content of your datasets.

By periodically exporting your data, you can ensure that you have a complete and up-to-date record of your customer interactions, making it readily available for reporting, archival, or data analysis purposes.

## Available cloud storage destinations {#destinations}

You can export datasets to 6 cloud storage destinations which are accessible from the **[!UICONTROL Destinations]** menu, in the **[!UICONTROL Catalog]** tab.

![](assets/dataset-export-setup.png)

Detailed information on each destination is available in Adobe Experience Platform documentation:

* [Amazon S3](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/amazon-s3.html){target="_blank"}
* [Azure Blob](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/azure-blob.html){target="_blank"}
* [Azure Data Lake Gen 2](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/adls-gen2.html){target="_blank"}
* [Data Landing Zone](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/data-landing-zone.html){target="_blank"}
* [Google Cloud Storage](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage.html){target="_blank"}
* [SFTP](https://experienceleague.adobe.com/docs/experience-platform/destinations/catalog/cloud-storage/sftp.html){target="_blank"}.

 
## Prerequisites {#prerequisites}

To export datasets, you need the [access control permissions](https://experienceleague.adobe.com/docs/experience-platform/access-control/home.html#permissions){target="_blank"} listed below. Read the [access control overview](https://experienceleague.adobe.com/docs/experience-platform/access-control/ui/overview.html){target="_blank"} or contact your product administrator to obtain the required permissions.

|Category|Permission|
|--|--|
|Destinations|Manage and Activate Dataset Destinations|
|Data Management|View Datasets|
|Destinations|View Destinations|

## Key steps to export datasets {#main-steps}

The main steps to export a dataset to a cloud storage location are as follows:

![](assets/dataset-export-process.png)

Detailed information on each step is available in [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html){target="_blank"}.

1. **Setup your cloud storage destination**. If you have not done so already, connect to a cloud storage destination from the destinations catalog. Learn how to create a new destination connection in [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/connect-destination.html#setup){target="_blank"}.

    <!--![](assets/dataset-export-setup.png)-->

1. **Select the cloud storage destination** where you want to export your datasets. In the destinations catalog, click the **[!UICONTROL Export datasets]** button on the desired card and select the connection to use.

    <!--![](assets/dataset-export-destination.png)-->

    >[!NOTE]
    >
    >If you are using Adobe Journey Optimizer along with Real-Time Customer profiles, destination cards will display an **Activate** button, allowing you to both export datasets and activate audiences for this destination, depending on the permissions you have enabled.

1. **Select the dataset(s)** that you want to export to the selected destination. [Learn more on Journey Optimizer datasets available for exporting](#datasets)

    <!--![](assets/dataset-export-dataset-selection.png)-->

1. **Schedule the export** of your dataset. Specify when the export should start and at which frequency it should occur.

    <!--![](assets/dataset-export-schedule.png)-->

1. **Review and confirm the export** by checking the summary that displays at the end of the configuration.

    <!--![](assets/dataset-export-review.png)-->

Once the export is complete, the content of your dataset is deposited on your cloud storage location according to the schedule you have configured. [Learn how to verify successful dataset export](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate/export-datasets.html#verify){target="_blank"}.

## Available datasets for exporting {#datasets}

Understand from the table below which Journey Optimizer datasets you can export.

|Dataset|Description|
| ------- | ------- | 
| AJO BCC Feedback Event Dataset | AJO BCC Feedback Event Dataset |
| AJO Classification Dataset | Dataset for ingesting email and push application feedback events from Journey Optimizer. Created through SDK. | 
| AJO Consent Service Dataset | Stores consent information of a profile. |
| AJO Email Tracking Experience Event Dataset | Interaction logs for Email channel which is used for reporting and audience creation purposes.  |
| AJO Entity Dataset | Dataset to store entity metadata for messages sent to the end user.  | 
| AJO Inbound Activity Event Dataset | Dataset for Journey Optimizer web & inApp channels for delivery & interaction events. |
| AJO Interactive Messaging Profile Dataset | Stores profiles created to support API-triggered Campaigns |
| AJO Message Feedback Event Dataset | Message delivery logs. Information on all message delivery from Journey Optimizer for reporting and audience creation purposes. Feedback from Email ISPs on bounces is also recorded in this dataset. | 
| AJO Profile Counters Extension | Holds a map of objects containing counter_value and expiryDate, keyed by counter_id |
| AJO Push Profile Dataset | Stores push tokens of a profile. |
| AJO Push Tracking Experience Event Dataset | Interaction logs for Push channel which is used for reporting and audience creation purposes. |
| AJO Surfaces Dataset | Empty dataset related to Journey Optimizer Inbound Surfaces schema |
| AOOutputForUPSDataset | Contains all AO audience memberships to be written back to UPS |
| Audience Orchestration Profile Dataset | Generated by audience composition for audience composition audiences. Contains all audience composition audiences, their attributes and enrichment data |
| Decision Object Repository - Activities | also known as Decisions in the user interface. But these are the objects a user creates that puts all the building blocks together including the decisioning logic. For example, for a particular placement (location), which offers should be considered (offer collection), and what ranking method to use on those offers. |
| Decision Object Repository - Fallback Offers | this is the repository for the other type of offer that a user creates. Specifically if they are not eligible to see a personalized offer and they need to see something, they will at least see the fallback offer. This dataset contains the attributes for this type of offer |
| Decision Object Repository - Personalized Offers | this is the repository for a type of offer that a user creates. So this dataset contains the attributes about this type of offer | 
| Decision Object Repository - Placements | this is the repository of objects that define the location of where an offer needs to be displayed. |
| Journey Step Events | Captures All Journey Step Experience Events generated from Journey Optimizer to be consumed by services like Reporting. |
| Journeys | Metadata dataset housing information of each step in a journey |
| ODE DecisionEvents - prod decisioning | Anytime we make a decision based on a request, we count that as a decision event |