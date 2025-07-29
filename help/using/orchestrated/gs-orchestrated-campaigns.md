---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Orchestrated campaigns
description: Learn how to start with Orchestrated campaigns
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 611dd06d-aa18-4fa3-a477-8a910cec21d8
---
# Get started with Orchestrated campaigns {#orchestrated-camp}

>[!CONTEXTUALHELP]
>id="campaigns_overview_orchestrated"
>title="campaigns_overview_orchestrated"
>abstract="<b>Campaign orchestration</b><br/>Split, combine, enrich and manipulate relational datasets to define your audience<br/><br/> <b>Leverage multi-entity data</b><br/>Learn how Orchestrated campaigns can take advantage of relational datasets to enrich data for segmentation & personalization<br/><br/><b>Ad-hoc segmentation & exact counts</b><br/>Build your segment step by step with exact counts<br/><br/><b>Available channels</b><br/>Email, SMS, Push notifications, Direct mail"

+++ Table of Contents

| Welcome to Orchestrated campaigns | Launch your first Orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|<b>[Get started with Orchestrated campaigns](gs-orchestrated-campaigns.md)</b><br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](gs-schemas.md)</li><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul>[Access and manage Orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an Orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

<br/>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

Campaign Orchestration in [!DNL Adobe Journey Optimizer] powers sophisticated, brand-initiated marketing campaigns across channels, helping you drive engagement, revenue, and customer loyalty at scale.

While cross-channel marketing is essential, Orchestrated campaigns make it seamless. With a visual, drag-and-drop interface, you can design and automate complex marketing workflows, from segmentation to message delivery, across multiple channels. Everything happens in one intuitive environment, built for speed, control, and efficiency.

![](assets/canvas-example-diagram.png){zoomable="yes"}

## Core capabilities

Campaign Orchestration is built around four key pillars:

<table style="table-layout:auto">
<tr style="border: 0;">
<td><img alt="On-demand audiences" src="assets/do-not-localize/icon-audience.svg" width="50px"></a></td><td><b>On-Demand Audiences</b><br/>Instantly query across datasets to create audience segments using any combination of data types and dimensions.</td></tr>
<tr style="border: 0;">
<td><img alt="Multi-entity segmentation & sending" src="assets/do-not-localize/icon-entity.svg" width="50px"></a></td><td><b>Multi-entity segmentation & sending</b><br/>Go beyond person-based campaigns—use entities like product catalogs, store locations, or service data to target with precision.<br/><br/>
Support multi-level sending, where one message is sent per Profile and per associated secondary entity. These secondary entities can include contact addresses, bookings, subscriptions, contracts, or other linked data. For example, this enables campaigns to be sent to all known addresses of a Profile or for each booking associated with that Profile.</td></tr>
<tr style="border: 0;">
<td><img alt="Pre-send visibility & precision" src="assets/do-not-localize/icon-visibility.svg" width="50px"></a></td><td><b>Pre-send visibility & precision</b><br/>Get exact segmentation counts and full campaign scope before launch, ensuring accuracy and confidence.</td></tr>
<tr style="border: 0;">
<td><img alt="Multi-step campaign workflows" src="assets/do-not-localize/icon-multistep.svg" width="50px"></a></td><td><b>Multi-step campaign workflows</b><br/>Design multi-steps campaigns, from daily messages to complex campaigns like seasonal promotions or major product launches.</td></tr>
</table>

## Orchestrated campaigns & journeys

Even though the Orchestrated campaigns visualization has similarities to journeys, it solves different purposes and use cases: 

* **Journeys** - 1 to 1 canvas where each profile travels through the different steps at their own pace. The state of each customer is maintained within its context to trigger real-time actions.

* **Orchestrated campaigns** - Unlike journeys, orchetsrated campaigns operate using a batch canvas that calculates segments. All profiles are processed together at the same time.

Both canvases are optimized for their respective use cases: Journey canvas publishes journey that tend to live for a longer period of time, while Campaign canvas is designed for iterative and incremental runs of a batch campaign.

## Prerequisites

Prior to working with Orchestrated Campaigns, it is essential to ensure that you have the appropriate permissions. Access to Orchestrated campaigns is restricted to users who are assigned to a relevant **[!UICONTROL Product Profile]**, such as Orchestrated Campaign Administrator, Orchestrated Campaign Approver, Orchestrated Campaign Manager, or Orchestrated Campaign Viewer.

If you are unable to access Orchestrated campaign functionalities, please contact your administrator to request the necessary permissions.

➡️ [Learn more about product profiles related to Orchestrated Campaigns](../administration/ootb-product-profiles.md)

## Let's dive deeper

Now that you have an understanding of what orcherstrated campaigns are, it's time to dive deeper into these documentation sections to start working with the feature.

<table><tr style="border: 0; text-align: center;">
<td>
<a href="gs-campaign-creation.md">
<img alt="Access and manage campaigns" src="assets/do-not-localize/workflow-access.jpeg">
</a>
<div>
<a href="gs-campaign-creation.md"><strong>Configuration steps</strong></a>
</div>
<p>
</td>
<td>
<a href="create-orchestrated-campaign.md">
<img alt="Lead" src="assets/do-not-localize/workflow-create.jpeg">
</a>
<div><a href="create-orchestrated-campaign.md"><strong>Create an Orchestrated campaign</strong>
</div>
<p>
</td>
<td>
<a href="activities/about-activities.md">
<img alt="Infrequent" src="assets/do-not-localize/workflow-activities.jpeg">
</a>
<div>
<a href="activities/about-activities.md"><strong>Work with activities</strong></a>
</div>
<p></td>
</tr></table>
