---
solution: Journey Optimizer
product: journey optimizer
title: Use the Save audience activity
description: Learn how to use the Save audience activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
---
# Save audience {#save-audience}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Access and manage orchestrated campaigns](../access-manage-orchestrated-campaigns.md)|[Key steps for orchestrated campaign creation](../gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the rule builder](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)<br/><br/>[Retargeting](../retarget.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Channel activities](channels.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - <b>[Save audience](save-audience.md)</b> - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++


The **[!UICONTROL Save audience]** activity is a **[!UICONTROL Targeting]** activity that allows you to update an existing audience or create a new one from the population generated earlier in the orchestrated campaign. Once created, these audiences are added to the list of application audiences and can be accessed from the **[!UICONTROL Audiences]** menu.

This activity is particularly useful for preserving audience segments calculated within the same orchestrated campaign, making them available for reuse in future campaigns. It is typically connected to other targeting activities, such as **[!UICONTROL Build audience]** or **[!UICONTROL Combine]**, to capture and save the resulting population.

## Configure the Save audience activity {#save-audience-configuration}

Follow these steps to configure the **Save audience** activity:

1. Add a **Save audience** activity to your orchestrated campaign.

1. In the **Mode** drop-down, select the action you want to perform:

    * **Create or update an existing audience**: Define an **Audience label**. If the audience already exists, it is updated; otherwise, a new audience is created.

    * **Update an existing audience**: Choose the **Audience** you want to update from the list of existing audiences.

1. Select the **Update mode** that applies to existing audiences:

    * **Replace audience content with new data**: All audience content is replaced, and old data is lost. Only the data from the inbound transition of the **Save audience** activity is retained. This option erases the audience type and the targeting dimension of the updated audience.

    * **Complete audience with new data**: The old audience content is retained, and the data from the inbound transition of the **Save audience** activity is added to it.

1. Check the **Generate an outbound transition** option if you want to add a transition after the **Save audience** activity.

The content of the saved audience is then available in the detail view of the audience, which can be accessed from the **Audiences** menu. The columns available in this view correspond to the columns of the inbound transition of the orchestrated campaign **Save audience** activity.

## Example {#save-audience-example}

The following example illustrates a simple audience update from targeting. A scheduler runs the orchestrated campaign once a month. A query retrieves all profiles subscribed to the different applications available. The **Save audience** activity updates the audience by removing profiles that have unsubscribed from the service since the last orchestrated campaign execution and adding newly subscribed profiles.
