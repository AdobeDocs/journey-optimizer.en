---
solution: Journey Optimizer
product: journey optimizer
title: Work with Orchestrated campaign activities
description: Learn how to Orchestrated campaign activities
exl-id: 02f986b2-8200-4e0e-8918-44e528a6a3ec
version: Campaign Orchestration
---

# About Orchestrated campaign activities {#orchestrated-campaign-activities}

Orchestrated campaign activities are grouped into three categories. Depending on the context, available activities may differ. 

All activities are detailed in the sections below:

* [Targeting activities](#targeting)
* [Channel activities](#channel)
* [Flow control activities](#flow-control)

![List of activities available in the canvas](../assets/orchestrated-activities.png){width="80%" align="left"}


>[!NOTE]
>
>* Depending on your licensing model, your permissions and your implementation, available activities may differ.
>
>* The number of activities in an Orchestrated campaign is limited to 500.


## Targeting activities {#targeting}

These activities are specific to targeting. They let you build one or more targets by defining an audience and splitting or combining these audiences using intersection, union or exclusion operations.

![List of targeting activities](../assets/targeting-activities.png){width="40%" align="left"}

Available targeting activities are:

* [Build audience](build-audience.md): Define your target population. You can either select an existing audience or use the rule builder to define your own query.
* [Change dimension](change-dimension.md): Change the targeting dimension as you are building your Orchestrated campaign.
* [Combine](combine.md): Perform segmentation on your inbound population. You can use a union, an intersection or an exclusion.
* [Deduplication](deduplication.md): Delete duplicates in the result(s) of the inbound activities.
* [Enrichment](enrichment.md): Define additional data to process in your Orchestrated campaign. With this activity, you can leverage the inbound transition and configure the activity to complete the output transition with additional data.
* [Reconciliation](reconciliation.md): Define the link between the data in Journey Optimizer data and the data in a work table, for example data loaded from an external file.
* [Split](split.md): Segment incoming population into several subsets.

## Channel activities {#channel}

Adobe Journey Optimizer allows you to automate and execute marketing campaigns across multiple channels. You can combine [channel activities](channels.md) into the canvas to create cross-channel Orchestrated campaign that can trigger actions based on customer behavior. 

Learn how to [create a channel action in an Orchestrated campaign](channels.md).

## Flow control activities {#flow-control}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_end"
>title="End activity"
>abstract="The **End** activity allows you to graphically mark the end of an Orchestrated campaign. This activity has no functional impact and is therefore optional."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_signal"
>title="External signal"
>abstract="external signal"

The following activities are specific to organizing and executing Orchestrated campaigns. Their main task is to coordinate the other activities.

![List of flow control activities](../assets/flow-control-activities.png){width="20%" align="left"}

Available flow control activities are:

* [And-join](and-join.md): Synchronize multiple execution branches of an Orchestrated campaign.
* [Fork](fork.md): Create outbound transitions to start several activities at the same time.
* [Wait](wait.md): Momentarily pause execution of a part of an Orchestrated campaign.
<!--* [Test](test.md): Enable transitions based on specified conditions.-->

>[!NOTE]
>The **End** activity graphically marks the end of an Orchestrated campaign. This activity has no functional impact and is therefore optional
