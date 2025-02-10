---
solution: Journey Optimizer
product: journey optimizer
title: About Adobe Experience Platform audiences
description: Learn how to work with Adobe Experience Platform audiences
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 78b95ccd-bc28-46cd-937a-f68e3f34cc1e
---
# Audience activation in [!DNL Journey Optimizer] {#segments-in-journey-optimizer}

You can select in campaigns and journeys any audience generated using segment definitions, custom upload, composition workflows or Federated Audience Composition.

>[!AVAILABILITY]
>
>The use of audiences and attributes from audience composition is currently unavailable for use with Healthcare Shield or Privacy and Security Shield. [Learn how to use audiences enrichment attributes in Journey Optimizer](../audience/about-audiences.md#enrichment)

## Audiences activation delay {#activation}

Audiences are ready for use in Journey Optimizer right after ingestion completes. While this is typically within one hour, it's subject to some variability. Audiences resulting from compositions should be available 24 hours after publishing.

## Custom upload & Federated Audience Composition

For Custom upload and Federated Audience Composition audiences, please note the following guardrails:

* **Preview and proof support:** Currently, preview and proof is not supported for audiences created using CSV upload or Federated Audience Composition. Keep this in mind when planning your campaigns.

* **Targeting new profiles:** When a match is not found between a record and a UPS profile, a new empty profile is created. This profile is linked to the enrichment attributes which are stored in the data lake. Because this new profile is empty, targeting fields typically used in Journey Optimizer (e.g., personalEmail.address, mobilePhone.number) are empty and therefore cannot be used for targeting.

    To solve this, you can specify the "execution field" (or "execution address" depending on the channel) in the channel configuration as 'identityMap'. This will ensure that the attribute chosen as the identity at audience creation will be the one used for targeting in Journey Optimizer.

* **Activated records & identity stitching:** Every record in the audience is activated, including any duplicates. During the next UPS profile export, these records will go through identity stitching. As a result, the number of activated records may differ from the number of profiles after identity stitching.

## Target audiences in [!DNL Journey Optimizer]

You can leverage audiences in **[!DNL Journey Optimizer]** in different ways:

* Choose an audience for a **campaign**, where the message is sent to all the individuals belonging to the selected audience. [Learn how to define the audience of a campaign](../campaigns/create-campaign.md#define-the-audience-audience).

* Use a **Read audience** orchestration activity in a journey to make all individuals in the audience enter the journey and receive the messages included in your journey. Let's say you have a "silver customer" audience. With this activity, you can make all silver customers enter a journey and send them a series of personalized messages. [Learn how to configure a Read audience activity](../building-journeys/read-audience.md#configuring-segment-trigger-activity).

    >[!NOTE]
    >
    >Any journey that utilizes an audience from audience composition or custom upload in the "Read Audience" activity will have profile attributes as fresh as the last batch evaluation. This includes consent/suppressions in the journey.

* Use the **Condition** activity in a journey to build conditions based on audience membership. [Learn how to use audiences in conditions](../building-journeys/condition-activity.md#using-a-segment).

* Use the **Audience qualification** event activity in a journey to make individuals enter or move forward in the journey based on Adobe Experience Platform audience entrances and exits. For example, you can make all new silver customers enter a journey and send them messages. For more on how to use this activity, refer to [Learn how to configure an Audience qualification activity](../building-journeys/audience-qualification-events.md).

    >[!NOTE]
    >
    >Due to the batch nature of audiences created using composition workflows, custom upload or Federated Audience Composition, you cannot target these audiences in an "Audience Qualification" activity. Only audiences created using segment definitions can be leveraged in this activity.
