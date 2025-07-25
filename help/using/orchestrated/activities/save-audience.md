---
solution: Journey Optimizer
product: journey optimizer
title: Use the Save audience activity
description: Learn how to use the Save audience activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 7b5b03ba-fbb1-4916-8c72-10778752d8e4
---
# Save audience {#save-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_save_audience"
>title="Save audience activity"
>abstract="The **Save audience** activity is a **Targeting** activity that allows you to update an existing audience or create a new one from the population generated earlier in the orchestrated campaign. Once created, these audiences are added to the list of application audiences and can be accessed from the **Audiences** menu." 


+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](../gs-schemas.md)</li><li>[Manual schema](../manual-schema.md)</li><li>[File upload schema](../file-upload-schema.md)</li><li>[Ingest data](../ingest-data.md)</li></ul>[Access and manage orchestrated campaigns](../access-manage-orchestrated-campaigns.md)|[Key steps to create an orchestrated campaign](../gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the rule builder](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)<br/><br/>[Retargeting](../retarget.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Channel activities](channels.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - <b>[Save audience](save-audience.md)</b> - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

The **[!UICONTROL Save audience]** activity is a **[!UICONTROL Targeting]** activity used to create a new audience or update an existing one based on the population generated earlier in the orchestrated campaign. Once saved, the audience is added to the list of application audiences and becomes accessible from the **[!UICONTROL Audiences]** menu.

It is commonly used to capture audience segments built within the same campaign workflow, making them available for reuse in future campaigns. Typically, it is connected to other targeting activities, such as **[!UICONTROL Build audience]** or **[!UICONTROL Combine]**, to save the final targeted population.

## Configure the Save audience activity {#save-audience-configuration}

Follow these steps to configure the **[!UICONTROL Save audience]** activity:

1. Add a **[!UICONTROL Save audience]** activity to your orchestrated campaign.

1. Enter a **[!UICONTROL Audience label]** that will identify the saved audience.

1. Choose a **[!UICONTROL Profile mapping field​]** from your Campaign Targeting dimension.

    ➡️ [Follow the steps detailed in this page to create your Campaign Targeting dimension](../target-dimension.md)

    ![](../assets/save-audience-1.png)

1. Click **[!UICONTROL Add audience mappings]** if you want to associate the saved audience with additional identity fields.

    ![](../assets/save-audience-2.png)

1. Finalize your setup by saving and publishing the orchestrated campaign. This will generate and store your audience.

The content of the saved audience is then available in the detail view of the audience, which can be accessed from the **[!UICONTROL Audiences]** menu, or can be selected when targeting an audience, for example with a **[!UICONTROL Read audience]** activity.

 ![](../assets/save-audience-4.png)


## Example {#save-audience-example}

The following example demonstrates how to create a simple audience using targeting. A query identifies all recipients who booked a trip in the last 30 days by filtering this population within your orchestrated campaign. By choosing **Recipients - CRMID** as the **Targeting dimension**, the audience targets each individual booking event rather than just the recipient as a whole. The **[!UICONTROL Save audience]** activity then captures these profiles to create a reusable audience of recent purchasers.

![](../assets/save-audience-3.png)
