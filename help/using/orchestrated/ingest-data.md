---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to bring data into Adobe Experience Platform from supported sources such as SFTP, cloud storage, or databases.
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 7f1e7985-b68e-43d6-9c8f-fea2469f8af9
---
# Ingest data {#ingest-data}

+++ Table of Contents

| Welcome to Orchestrated campaigns | Launch your first Orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with Orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets</br> <ul><li>[Get started with Schemas and Datasets](gs-schemas.md)</li><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul>[Access and manage Orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an Orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

</br>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

>[!IMPORTANT]
>
>To change the data source for a dataset, you must first delete the existing dataflow before creating a new one that references the same dataset and the new source.
>
>Adobe Experience Platform enforces a strict one-to-one relationship between dataflows and datasets. This allows you to maintain synchronization between the source and the dataset for accurate incremental ingestion. 

Adobe Experience Platform allows data to be ingested from external sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services. You can ingest data from a variety of sources such as Adobe applications, cloud-based storages, databases, and many others.

## Supported Sources for Orchestrated campaigns {#supported}

The following Dources are supported for use with Orchestrated campaigns:

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Cloud Storage</td>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/s3">Amazon S3</a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/google-cloud-storage">Google Cloud Storage</a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/sftp">SFTP</a></td>
    </tr>
      <td rowspan="4">Cloud Data Warehouses</td>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/snowflake">Snowflake</a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/bigquery">Google BigQuery</a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/data-landing-zone">Data Landing Zone<a></td>
    </tr>
    <tr>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/databricks">Azure Databricks</a></td>
    </tr>
    <tr>
      <td rowspan="3">File-Based Uploads</td>
      <td><a href="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload">Local File Upload<a></td>
    </tr>

  </tbody>
</table>

## Configure a dataflow

This example demonstrates how to configure a data flow that ingests structured data into Adobe Experience Platform. The configured data flow supports automated, scheduled ingestion and enables real-time updates.

1. From the **[!UICONTROL Connections]** menu, access the **[!UICONTROL Sources]** menu.

1. Choose your source depending on the [Supported Sources for Orchestrated campaigns](#supported).

    ![](assets/admin_sources_1.png)

1. Connect your Cloud Storage or Google Cloud Storage account if you chose cloud based sources.

    ![](assets/admin_sources_2.png)

1. Choose the data you wishes to ingest into Adobe Experience Platform.

    ![](assets/S3_config_1.png)

1. From the **[!UICONTROL Dataset details]** page, check **[!UICONTROL Enable Change data capture]** to display only datasets that are mapped to relational schemas and include both a primary key and a version descriptor.

    >[!IMPORTANT]
    >
    > For **file-based sources only**, each row in the data file must include a `_change_request_type` column with values `U` (upsert) or `D` (delete). Without this column, the system will not recognize the data as supporting change tracking, and the Orchestrated Campaign toggle will not appear, preventing the dataset from being selected for targeting.

    ![](assets/S3_config_6.png)

1. Select your previously created Dataset and click **[!UICONTROL Next]**.

    ![](assets/S3_config_3.png)

1. If you are using a file-based sources only, from the **[!UICONTROL Select data]** window, upload your local files and preview their structure and contents.

    Note that the maximum supported size is 100MB.

1. In the **[!UICONTROL Mapping]** window, verify that each source file attribute is correctly mapped with the corresponding fields in the target schema.

    Click **[!UICONTROL Next]** once done.

    ![](assets/S3_config_4.png)

1. Configure the data flow **[!UICONTROL Schedule]** based on your desired frequency.

1. Click **[!UICONTROL Finish]** to create the data flow. It will execute automatically according to the defined schedule.

1. From the **[!UICONTROL Connections]** menu, select **[!UICONTROL Sources]** and access the **[!UICONTROL Data Flows]** tab to track flow execution, review ingested records, and troubleshoot any errors.

    ![](assets/S3_config_5.png)
    