---
solution: Journey Optimizer
product: journey optimizer
title: Use the Read audience activity
description: Learn how to use the Read audience activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: ef8eba57-cd33-4746-8eb4-5214ef9cbe2f
---
# Read audience {#read-audience}


>[!CONTEXTUALHELP]
>id="ajo_orchestration_read_audience"
>title="Build audience activity"
>abstract="The **Read audience** activity allows you to select the audience that will enter the the orchestrated campaign. This audience can be an existing Adobe Experience Platform audience or an audience pulled from a CSV file. When sending messages in the context of an orchestrated campaign, the message audience is not defined in the channel activity, but in a **Read audience** or a **Build audience** activity."


+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](../gs-schemas.md)</li><li>[Manual schema](../manual-schema.md)</li><li>[File upload schema](../file-upload-schema.md)</li><li>[Ingest data](../ingest-data.md)</li></ul>[Access and manage orchestrated campaigns](../access-manage-orchestrated-campaigns.md)|[Key steps to create an orchestrated campaign](../gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the rule builder](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)<br/><br/>[Retargeting](../retarget.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Channel activities](channels.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Save audience](save-audience.md) - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

The **[!UICONTROL Read audience]** activity allows you to retrieve an existing audience—previously saved or imported—and reuse it within an orchestrated campaign. This activity is especially useful for targeting a predefined set of profiles without the need to execute a new segmentation process.

Once the audience is loaded, you can optionally refine it by selecting a unique identity field and enriching the audience with additional profile attributes for targeting, personalization, or reporting purposes.

## Configure the Read audience activity {#read-audience-configuration}

Follow these steps to configure the **[!UICONTROL Read audience]** activity:

1. Add a **[!UICONTROL Read audience]** activity to your orchestrated campaign.
    
    ![](../assets/read-audience-1.png)

1. Enter a **[!UICONTROL Label]** to your activity.

1. Click ![folder search icon](../assets/do-not-localize/folder-search.svg) to select the audience you wish to target for your orchestrated campaign.

    ![](../assets/read-audience-2.png)

1. Select the **[!UICONTROL Entity]** used to uniquely identify profiles in your audience.

    ![](../assets/read-audience-3.png)

1. Select **[!UICONTROL Add profile attribute]** to enrich your selected audience with additional data. The resulting audience will contain a list of recipients, each enriched with the selected profile attributes.

1. Choose the **[!UICONTROL Attributes]** you want to add to your audience.

    ![](../assets/read-audience-4.png)

## Example

In the example below, the **[!UICONTROL Read audience]** activity is used to retrieve a previously created and saved audience of profiles who subscribed to the newsletter. The audience is then enriched with the **Loyalty membership** attribute to enable targeting of users who are registered members of the loyalty program.

![](../assets/read-audience-5.png)
