---
solution: Journey Optimizer
product: journey optimizer
title: Use the AND-join activity
description: Learn how to use the AND-join activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 1b99313e-f131-44f7-a129-f85e1977fb05
---
# AND-join {#join}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_and-join"
>title="AND-join activity"
>abstract="The **And-join** activity allows you to synchronize multiple execution branches of an orchestrated campaign. It is triggered once all of the preceding activities have finished. This allows you to make sure that certain activities are finished before continuing to execute the orchestrated campaign."

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](../gs-campaign-creation.md)|[Create an orchestrated campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](../send-messages.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the Query Modeler](../orchestrated-query-modeler.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Split](split.md) -  [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

The **And-join** activity is a **Flow control** activity. It allows you to synchronize multiple execution branches of an orchestrated campaign.

This activity only triggers its outbound transition once all the inbound transitions are activated, in other words, once all of the preceding activities have finished. This allows you to make sure that certain activities have finished before continuing to execute the orchestrated campaign.

## Configure the And-join activity{#and-join-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_and-join_merging"
>title="Merging options"
>abstract="Select which activities you want to join. In the **Primary set** drop-down, choose which inbound transition population you want to keep."

Follow these steps to configure the **AND-join** activity:

![](../assets/workflow-andjoin.png)

1. Add multiple activities such as channel activities to form at least two different execution branches.
1. Add an **AND-join** activity to any of the branches.
1. In the **Merging options** section, check all the previous activities you wish you join. 
1. In the **Primary set** drop-down, choose which inbound transition population you want to keep. The outbound transition can only contain one of the inbound transition populations.

## Example{#and-join-example}

The following example shows two orchestrated campaign branches with an email and SMS delivery. The AND-join will trigger when both inbound transitions are enabled. The push notifications will then be sent only after both deliveries are finished. 

![](../assets/workflow-andjoin-example.png){zoomable="yes"}
