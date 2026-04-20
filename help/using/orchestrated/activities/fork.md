---
solution: Journey Optimizer
product: journey optimizer
title: Use the Fork activity
description: Learn how to use the Fork activity in an Orchestrated campaign
exl-id: 52e8057b-dac1-45f5-9dd0-1b28a59adde9
version: Campaign Orchestration
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

The **[!UICONTROL Fork]** activity is a **[!UICONTROL Flow control]** component that lets you create multiple outbound transitions, enabling several activities to run in parallel.

## Configure the Fork activity{#fork-configuration}

Follow these steps to configure the **[!UICONTROL Fork]** activity:

![](../assets/workflow-fork.png)

1. Add a **[!UICONTROL Fork]** activity to your Orchestrated campaign.

1. Define a **[!UICONTROL Label]**.

1. Assign a label to each outbound transition. By default, two transitions are provided.

1. To remove a transition, click the ![](../assets/do-not-localize/Smock_Delete_18_N.svg) icon.

1. If needed, click **[!UICONTROL Add transition]** to add an additional outbound transition. 

## Examples {#fork-examples}

Here is a typical use of the **[!UICONTROL Fork]** activity: targeting the same audience with two different email channels — one Marketing and one Transactional — to compare delivery behavior.

After a **[!UICONTROL Build audience]** activity selects the target population, a **[!UICONTROL Fork]** creates two parallel branches:

* **Branch 1** connects to a Marketing email channel activity. Messages follow standard business rules and are sent only to opted-in profiles.
* **Branch 2** connects to a Transactional email channel activity. Messages bypass business rules and are delivered to all profiles regardless of opt-in status.

![](../assets/workflow-fork.png)

This pattern is useful for understanding how channel category settings affect delivery behavior, and for sending different message types to the same audience in a single campaign run.
