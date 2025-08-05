---
solution: Journey Optimizer
product: journey optimizer
title: Use the AND-join activity
description: Learn how to use the AND-join activity in an Orchestrated campaign
exl-id: 1b99313e-f131-44f7-a129-f85e1977fb05
---

# AND-join {#join}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_and-join"
>title="AND-join activity"
>abstract="The **And-join** activity allows you to synchronize multiple execution branches of an Orchestrated campaign. It is triggered once all of the preceding activities have finished. This allows you to make sure that certain activities are finished before continuing to execute the Orchestrated campaign."

The **[!UICONTROL And-join]** activity is a **[!UICONTROL Flow control]** activity. It allows you to synchronize multiple execution branches of an Orchestrated campaign.

This activity only triggers its outbound transition once all the inbound transitions are activated, in other words, once all of the preceding activities have finished. This allows you to make sure that certain activities have finished before continuing to execute the Orchestrated campaign.

## Configure the And-join activity{#and-join-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_and-join_merging"
>title="Merging options"
>abstract="Select which activities you want to join. In the **Primary set** drop-down, choose which inbound transition population you want to keep."

Follow these steps to configure the **[!UICONTROL AND-join]** activity:

![](../assets/workflow-andjoin.png)

1. Add multiple activities, such as channel activities, to create at least two distinct execution branches.

1. Insert an **[!UICONTROL AND-join]** activity into one of the branches.

1. Under the **[!UICONTROL Merging options]** section, select all preceding activities you want to join.
 
1. From the **[!UICONTROL Primary set]** drop-down, choose the inbound transition population you want to retain.

## Example{#and-join-example}

This example illustrates two coordinated campaign branches, each featuring an email delivery, one targeting gold members and the other silver. The **[!UICONTROL AND-join]** activates once both incoming transitions are triggered, and the SMS will be sent only after both email deliveries are completed, following a 7-day delay.

![](../assets/workflow-andjoin-example.png){zoomable="yes"}
