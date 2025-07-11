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

Orchestrated campaign provides two main data sources for this:

- **Message Feedback**: captures delivery-related events, e.g. message sent, opened, bounced, etc.

- **Email Tracking**: captures user actions e.g. clicks and opens.

## Create a Feedback-Based Retargeting Rule

Feedback-Based Retargeting Rule allows you to retarget recipients based on message delivery events captured in the **Message Feedback** dataset. These events include outcomes such as messages being sent, opened, bounced, or marked as spam.

Using this data, you can define rules to identify recipients who received a previous message but did not engage with it, enabling follow-up communication based on specific delivery statuses.

1. Create a new **Orchestrated Campaign**.

2. Add a **Build Audience** activity and set the targeting dimension to **Recipient (caas)**.

3. In the **Rule Builder**, click **Add Condition** and select **Message Feedback** from the Attributes Picker. Click **Confirm**.

4. Add a condition for **Feedback Status** and set the value to **Message Sent**.

5. To target a specific orchestrated campaign:

   - Add another condition, search for `entity`, and navigate to:  
     `_experience > CustomerJourneyManagement > Entities > AJO Orchestrated Campaign`.

   - Select **Orchestrated Campaign Name** and specify the campaign name.

6. To target a specific message or activity within that orchestrated campaign:

   - Add another condition, search for `entity`, and navigate to:  
     `_experience > CustomerJourneyManagement > Entities > AJO Orchestrated Campaign`.

   - Select **Orchestrated Campaign Action Name** and specify the campaign action name.
        
        Action names can be found by clicking the ![Information icon](assets/do-not-localize/info-icon.svg) next to an activity in the canvas.  

    >[!TIP]
    >
    >Instead of using names, you can also filter by the **Campaign ID** (UUID), which can be found in your Campaign properties.

## Create a Tracking-Based retargeting rule

Tracking-Based retargeting rule targets recipients based on their interactions with a message, using data from the **Email Tracking** dataset. It captures user actions such as email opens and link clicks.

To retarget recipients based on message interactions (e.g., open or click), use the **Email Tracking** entity as follows:

1. Create a new **Orchestrated Campaign**, then add a **Build audience** activity with **Recipient (caas)** as the targeting dimension to focus on previous orchestrated campaign recipients.

1. Add a new condition for **Email Tracking**. Click **Confirm** to create a "Email Tracking Exists such as" condition.

1. Within that condition, add a condition and search for **Interaction Type** attribute.

1. From the custom condition options, use **Included in** as the operator and select one or more values depending on your use case. For example:
   - **Message Opened**
   - **Message Link Clicked**

1. To associate the tracking data with a specific campaign:

   - Add a condition within the Email Tracking block.

   - Navigate to `_experience > CustomerJourneyManagement > Entities > AJO Orchestrated Campaign`.

   - Add conditions for both **Orchestrated Campaign Name** and, if needed, **Orchestrated Campaign Action Name**.

        Action names can be found by clicking the ![Information icon](assets/do-not-localize/info-icon.svg) next to an activity in the canvas.  

    >[!TIP]
    >
    >Instead of using names, you can also filter by the **Campaign ID** (UUID), which can be found in your Campaign properties.
