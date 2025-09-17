---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Orchestrated campaigns
description: Learn how to start with Orchestrated campaigns
short-description: Discover orchestrated campaign key features and use cases.
exl-id: 611dd06d-aa18-4fa3-a477-8a910cec21d8
version: Campaign Orchestration
---

# Get started with Orchestrated campaigns {#orchestrated-camp}

>[!CONTEXTUALHELP]
>id="campaigns_overview_orchestrated"
>title="campaigns_overview_orchestrated"
>abstract="<b>Campaign orchestration</b><br/>Split, combine, enrich and manipulate relational datasets to define your audience<br/><br/> <b>Leverage multi-entity data</b><br/>Learn how Orchestrated campaigns can take advantage of relational datasets to enrich data for segmentation & personalization<br/><br/><b>Ad-hoc segmentation & exact counts</b><br/>Build your segment step by step with exact counts<br/><br/><b>Available channels</b><br/>Email, SMS, Push notifications, Direct mail"

Campaign Orchestration in [!DNL Adobe Journey Optimizer] powers sophisticated, brand-initiated marketing campaigns across channels, helping you drive engagement, revenue, and customer loyalty at scale.

>[!IMPORTANT]
>
>To access Campaign Orchestration, your license must include either the **Journey Optimizer – Campaigns & Journeys** or the **Journey Optimizer - Campaigns** package. Contact your Adobe representative to confirm your license and update if needed.

While cross-channel marketing is essential, Orchestrated campaigns make it seamless. With a visual, drag-and-drop interface, you can design and automate complex marketing workflows, from segmentation to message delivery, across multiple channels. Everything happens in one intuitive environment, built for speed, control, and efficiency.

![](assets/canvas-example-diagram.png){zoomable="yes"}

➡️ [Discover Orchestrated campaigns in video](#video-oc) 

## Core capabilities

Campaign Orchestration is built around four key pillars:

<table style="table-layout:auto">
<tr style="border: 0;">
<td><img alt="On-demand audiences" src="assets/do-not-localize/icon-audience.svg" width="150px"></a></td><td><b>On-Demand Audiences</b><br/>Instantly query across datasets to create audience segments using any combination of data types and dimensions.</td></tr>
<tr style="border: 0;">
<td><img alt="Multi-entity segmentation & sending" src="assets/do-not-localize/icon-entity.svg" width="150px"></a></td><td><b>Multi-entity segmentation & sending</b><br/>Go beyond person-based campaigns—use entities like product catalogs, store locations, or service data to target with precision.<br/><br/>
Support multi-level sending, where one message is sent per Profile and per associated secondary entity. These secondary entities can include contact addresses, bookings, subscriptions, contracts, or other linked data. For example, this enables campaigns to be sent to all known addresses of a Profile or for each booking associated with that Profile.</td></tr>
<tr style="border: 0;">
<td><img alt="Pre-send visibility & precision" src="assets/do-not-localize/icon-visibility.svg" width="150px"></a></td><td><b>Pre-send visibility & precision</b><br/>Get exact segmentation counts and full campaign scope before launch, ensuring accuracy and confidence.</td></tr>
<tr style="border: 0;">
<td><img alt="Multi-step campaign workflows" src="assets/do-not-localize/icon-multistep.svg" width="150px"></a></td><td><b>Multi-step campaign workflows</b><br/>Design multi-steps campaigns, from daily messages to complex campaigns like seasonal promotions or major product launches.</td></tr>
</table>


>[!NOTE]
>
>Supported channels are: [Email](../email/get-started-email.md), [SMS/MMS/RCS](../sms/get-started-sms.md), [Push notifications](../push/get-started-push.md).
>
>Available channels vary based on your licensing model and add-ons.

## Orchestrated campaigns & journeys

Even though the Orchestrated campaigns visualization has similarities to journeys, it solves different purposes and use cases: 

* **Journeys** - 1 to 1 canvas where each profile travels through the different steps at their own pace. The state of each customer is maintained within its context to trigger real-time actions.

* **Orchestrated campaigns** - Unlike journeys, Orchestrated campaigns operate using a batch canvas that calculates segments. All profiles are processed together at the same time.

Both canvases are optimized for their respective use cases: Journey canvas publishes journey that tend to live for a longer period of time, while Campaign canvas is designed for iterative and incremental runs of a batch campaign.

## What's inside an Orchestrated campaign? {#gs-ms-campaign-inside}

The Orchestrated campaign canvas is a representation of what is supposed to happen. It describes the various tasks to be performed and how they are linked together. 

![image showing an Orchestrated campaign canvas](assets/canvas-example.png)

Each Orchestrated campaign contains:

* **Activities**: An activity is a task to be performed. The [various activities](activities/about-activities.md) are represented on the canvas by icons. Each activity has specific properties and other properties that are common to all activities.

    In an Orchestrated campaign canvas, a given activity can produce multiple tasks, in particular when there is a loop or recurrent actions.

* **Transitions**: Transitions link a source activity to a destination activity and define their sequence. 

* **Worktables**: The worktable contains all the information carried by the transition. Each Orchestrated campaign uses several worktables. The data conveyed in these tables can be used throughout the Orchestrated campaign's life cycle.


## Introduction video {#video-oc}

Learn key concepts and capabilities available with Orchestrated campaigns.


>[!VIDEO](https://video.tv.adobe.com/v/3471538/?learn=on&enablevpops)


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
