---
solution: Journey Optimizer
product: journey optimizer
title: Use the Build audience activity
description: Learn how to use the Build audience activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 3959b5fa-0c47-42a5-828f-4d7ca9b7e72d
---
# Build audience {#build-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience"
>title="Build audience activity"
>abstract="The **Build audience** activity allows you to define the audience that will enter the orchestrated campaign. When sending messages in the context of an orchestrated campaign, the message audience is not defined in the channel activity, but in the **Build audience** activity."

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](../gs-campaign-creation.md)|[Create an orchestrated campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](../send-messages.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the Query Modeler](../orchestrated-query-modeler.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Split](split.md) -  [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

As a marketer, you can easily create complex queries using a user-friendly interface, enabling me to segment your audience based on a wide range of criteria and behaviors to tailor your campaigns more effectively.    

To perform this, use the  **Build audience** targeting activity. This activity allows you to define the audience that will enter the orchestrated campaign. When sending messages in the context of an orchestrated campaign, the message audience is not defined in the channel activity, but in the **Build audience** activity.

To define the audience population, you can:

* Select an existing audience.
* Select a predefined filter.
* Build a new audience with the query modeler by defining and combining filtering criteria.

>[!NOTE]
>
>Audiences loaded from a file cannot be targeted using a Build audience activity. To do this, you need to use a **Load file** activity followed by a **Reconciliation** activity.


## Configure the Build audience activity {#build-audience-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience_audienceselector"
>title="Audience"
>abstract="Select your audience, the same way you use an audience when designing a new delivery."

Follow these steps to configure the **Build audience** activity:

![](../assets/build-audience.png)

1. Add a **Build audience** activity. 
1. Define a label.
1. Define the audience type: **Create your own** or **Read audience**. 
1. Configure your audience by following the steps detailed in the tabs below.


To create your own query, follow these steps:

1. Select **Create your own (query)**.
1. Choose the **Targeting dimension**. The targeting dimension lets you define the population targeted by the operation: recipients, contract beneficiaries, operator, subscribers, etc. By default, the target is selected from the recipients.
1. Click **Continue**.
1. Use the query modeler to define your query. [Learn more about the Query modeler in this section](../orchestrated-query-modeler.md) 

## Examples{#build-audience-examples}

Here is an example of an orchestrated campaign with two **Build audience** activities. The first one targets the poker players audience, followed by an email delivery. The second one targets the VIP clients audience, followed by an SMS delivery.

![](../assets/workflow-audience-example.png)
