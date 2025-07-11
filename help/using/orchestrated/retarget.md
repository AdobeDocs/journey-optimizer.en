---
solution: Journey Optimizer
product: journey optimizer
title: Start and monitor orchestrated campaigns with Adobe Journey Optimizer
description: Learn how to start and monitor orchestrated campaigns with Adobe Journey Optimizer.
hide: yes
hidefromtoc: yes
exl-id: 3c1cad30-3ed7-4df1-a46a-60394a834e79
---
# Building retargeting queries {#retarget}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/><b>[Retargeting](retarget.md)</b>|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

</br>

>[!BEGINSHADEBOX]

Documentation in progress

>[!ENDSHADEBOX]

Retargeting allows you to follow up with recipients based on how they responded to a previous orchestrated campaign. For example, you can send a second email to profiles who received but did not click the first one.

**[!UICONTROL Orchestrated Campaign]** provides two main data sources for this:

* **[!UICONTROL Message Feedback]**: captures delivery-related events, e.g. message sent, opened, bounced, etc.
* **[!UICONTROL Email Tracking]**: captures user actions, e.g. clicks and opens.

## Create a Feedback-Based Retargeting Rule {#feedback-retarget}

Feedback-Based Retargeting Rule allows you to retarget recipients based on message delivery events captured in the **Message Feedback** dataset. These events include outcomes such as messages being sent, opened, bounced, or marked as spam.

Using this data, you can define rules to identify recipients who received a previous message enabling follow-up communication based on specific delivery statuses.

1. Create a new **[!UICONTROL Orchestrated Campaign]**.

1. Add a **[!UICONTROL Build Audience]** activity and set the targeting dimension to **[!UICONTROL Recipient (caas)]**.

1. In the **[!UICONTROL Rule Builder]**, click **[!UICONTROL Add Condition]** and select **[!UICONTROL Message Feedback]** from the **[!UICONTROL Attributes Picker]**. Click **[!UICONTROL Confirm]** to create a **Message Feedback Exists such as** condition.

    ![](assets/retarget_1.png)

1. Choose the **[!UICONTROL Feedback Status]** attribute to target message delivery events.

   +++ Detailed step-by-step

   1. Add another condition linked to the **[!UICONTROL Message feedback]** attribute.

   1. Search for the **[!UICONTROL Feedback Status]** attribute and click **[!UICONTROL Confirm]**.

      ![](assets/retarget_3.png)

   1. In the **[!UICONTROL Custom condition]** menu, choose which delivery status to track in the **[!UICONTROL Value]** drop-down. 

      ![](assets/retarget_4.png)

   +++

1. Choose the **[!UICONTROL Orchestrated Campaign Name]** attribut to target a specific orchestrated campaign.

    +++ Detailed step-by-step

   1. Add another condition linked to the **[!UICONTROL Message feedback]** attribute, search for **[!UICONTROL entity]**, and navigate to:

         `_experience > CustomerJourneyManagement > Entities > AJO Orchestrated Campaign entity`.

   1. Select **[!UICONTROL Orchestrated Campaign Name]**.

      ![](assets/retarget_5.png)

   1. In the **[!UICONTROL Custom condition]** menu, specify the campaign name in the **[!UICONTROL Value]** field.

   +++

1. Choose the **[!UICONTROL Orchestrated Campaign Action Name]** attribut to target a specific message or activity within an orchestrated campaign.

   +++ Detailed step-by-step

   1. Add another condition linked to the **[!UICONTROL Message feedback]** attribute, search for **[!UICONTROL entity]**, and navigate to:

      `_experience > CustomerJourneyManagement > Entities > AJO Orchestrated Campaign entity`.

   1. Select **[!UICONTROL Orchestrated Campaign Action Name]**.

      ![](assets/retarget_6.png)

   1. In the **[!UICONTROL Custom condition]** menu, specify the campaign action name in the **[!UICONTROL Value]** field.

      Action names can be found by clicking the ![Information icon](assets/do-not-localize/info-icon.svg) next to an activity in the canvas.
   
   ++

1. Alternativaly, you can also filter by the **[!UICONTROL Campaign ID]** (UUID), which can be found in your Campaign properties.

## Create a Tracking-Based retargeting rule

Tracking-Based retargeting rule targets recipients based on their interactions with a message, using data from the **[!UICONTROL Email Tracking]** dataset. It captures user actions such as email opens and link clicks.

To retarget recipients based on message interactions (e.g., open or click), use the **[!UICONTROL Email Tracking]** entity as follows:

1. Create a new **[!UICONTROL Orchestrated Campaign]**.

1. Add a **[!UICONTROL Build Audience]** activity and set the targeting dimension to **[!UICONTROL Recipient (caas)]** to focus on previous orchestrated campaign recipients.

1. In the **[!UICONTROL Rule Builder]**, click **[!UICONTROL Add Condition]** and select **[!UICONTROL Email Tracking]** from the **[!UICONTROL Attributes Picker]**. 

   Click **[!UICONTROL Confirm]** to create a **Email Tracking Exists such as** condition.

    ![](assets/retarget_2.png)

1. To target profiles' interactions with a message, add another condition linked to the **[!UICONTROL Email tracking]** attribute and search for the **[!UICONTROL Interaction Type]** attribute.

   ![](assets/retarget_7.png)

1. From the custom condition options, use **[!UICONTROL Included in]** as the operator and select one or more values depending on your use case, e.g. **[!UICONTROL Message Opened]** or **[!UICONTROL Message Link Clicked]**.

   ![](assets/retarget_8.png)

1. To associate the tracking data to a specific campaign, add a new **[!UICONTROL Message feedback]** condition and follow the steps detailed [in this section](#feedback-retarget).
