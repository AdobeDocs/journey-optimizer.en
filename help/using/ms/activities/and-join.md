---
solution: Journey Optimizer
product: journey optimizer
title: Use the AND-join activity
description: Learn how to use the AND-join activity in a multi-step campaign
hide: yes
hidefromtoc: yes
exl-id: 1b99313e-f131-44f7-a129-f85e1977fb05
---
# AND-join {#join}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_and-join"
>title="AND-join activity"
>abstract="The **And-join** activity allows you to synchronize multiple execution branches of a multi-step campaign. It is triggered once all of the preceding activities have finished. This allows you to make sure that certain activities are finished before continuing to execute the multi-step campaign."

The **And-join** activity is a **Flow control** activity. It allows you to synchronize multiple execution branches of a multi-step campaign.

This activity only triggers its outbound transition once all the inbound transitions are activated, in other words, once all of the preceding activities have finished. This allows you to make sure that certain activities have finished before continuing to execute the multi-step campaign.

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

The following example shows two multi-step campaign branches with an email and SMS delivery. The AND-join will trigger when both inbound transitions are enabled. The push notifications will then be sent only after both deliveries are finished. 

![](../assets/workflow-andjoin-example.png){zoomable="yes"}
