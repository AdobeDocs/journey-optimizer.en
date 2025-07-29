---
solution: Journey Optimizer
product: journey optimizer
title: Use the Build audience activity
description: Learn how to use the Build audience activity in an Orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 3959b5fa-0c47-42a5-828f-4d7ca9b7e72d
---
# Build audience {#build-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience"
>title="Build audience activity"
>abstract="The **Build audience** activity allows you to define the audience that will enter the Orchestrated campaign. When sending messages in the context of an Orchestrated campaign, the message audience is not defined in the channel activity, but in a **Build audience** activity."

+++ Table of Contents

| Welcome to Orchestrated campaigns | Launch your first Orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with Orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](../gs-schemas.md)</li><li>[Manual schema](../manual-schema.md)</li><li>[File upload schema](../file-upload-schema.md)</li><li>[Ingest data](../ingest-data.md)</li></ul>[Access and manage Orchestrated campaigns](../access-manage-orchestrated-campaigns.md)|[Key steps to create an Orchestrated campaign](../gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the rule builder](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)<br/><br/>[Retargeting](../retarget.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - <b>[Build audience](build-audience.md)</b> - [Change dimension](change-dimension.md) - [Channel activities](channels.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Save audience](save-audience.md) - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++


<br/>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

As a marketer, you can create complex audience segments through an intuitive interface, allowing you to target users based on a wide range of criteria and behaviors to tailor your campaigns more effectively.

To do this, use the **[!UICONTROL Build audience]** targeting activity. This activity defines the audience that enters the Orchestrated campaign. When sending messages as part of an Orchestrated campaign, the audience is defined in the **[!UICONTROL Build audience]** activity, not within the Orchestrated campaign.

## Configure the Build audience activity {#build-audience-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience_audienceselector"
>title="Audience"
>abstract="Select your audience, the same way you use an audience when designing a new delivery."

Follow these steps to configure the **[!UICONTROL Build audience]** activity:

1. Add a **[!UICONTROL Build audience]** activity.

    ![](../assets/build-audience.png)

1. Define a **[!UICONTROL Label]**.

1. Configure your audience by following the steps detailed in the tabs below.

1. Choose the **[!UICONTROL Targeting dimension]**. The targeting dimension lets you define the population targeted by the operation: recipients, contract beneficiaries, operator, subscribers, etc. By default, the target is selected from the recipients.

1. Click **[!UICONTROL Continue]**.

1. Use the query modeler to define your query. [Learn more about the Query modeler in this section](../orchestrated-rule-builder.md) 

1. Specify whether an outbound transition should be generated when the audience is empty.

## Examples{#build-audience-examples}

Here is an example of an Orchestrated campaign with two **[!UICONTROL Build audience]** activities. The first targets profiles that have items in their cart, followed by an email delivery. The second targets profiles with a wishlist, followed by an SMS delivery.

![](../assets/build-audience-2.png)
