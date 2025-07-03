---
solution: Journey Optimizer
product: journey optimizer
title: Use the Fork activity
description: Learn how to use the Fork activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 52e8057b-dac1-45f5-9dd0-1b28a59adde9
---
# Fork {#fork}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_fork"
>title="Fork activity"
>abstract="The **Fork** activity allows you to create outbound transitions to start several activities at the same time."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_fork_transitions"
>title="Fork activity transitions"
>abstract="By default, two transitions are created with a **Fork** activity. Click the **Add transition** button to define an additional outbound transition, and enter its label."

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)|[Key steps for orchestrated campaign creation](gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/><b>[Start and monitor the campaign](start-monitor-campaigns.md)</b><br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

<br/>

The **[!UICONTROL Fork]** activity is a **[!UICONTROL Flow control]** component that lets you create multiple outbound transitions, enabling several activities to run in parallel.

## Configure the Fork activity{#fork-configuration}

Follow these steps to configure the **[!UICONTROL Fork]** activity:

![](../assets/workflow-fork.png)

1. Add a **[!UICONTROL Fork]** activity to your orchestrated campaign.

1. Define a **[!UICONTROL Label]**.

1. Assign a label to each outbound transition. By default, two transitions are provided.

1. To remove a transition, click the ![](../assets/do-not-localize/Smock_Delete_18_N.svg) icon.

1. If needed, click **[!UICONTROL Add transition]** to add an additional outbound transition. 
