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

## Guardrails & limitations {#guardrails}

* **Healthcare Shield or Privacy and Security Shield** - The use of audiences and attributes from audience composition is currently unavailable with Healthcare Shield or Privacy and Security Shield. [Learn how to use audiences enrichment attributes in [!DNL Journey Optimizer]](../audience/about-audiences.md#enrichment)

* **Custom upload & Federated Audience Composition** - For Custom upload and Federated Audience Composition audiences, please note the following guardrails:

    * **Preview and proof support:** Currently, preview and proof are not supported for audiences created using CSV upload or Federated Audience Composition. Keep this in mind when planning your campaigns.

    * **Targeting new profiles:** When a match is not found between a record and a Unified Profile Service profile, a new empty profile is created. This profile is linked to the enrichment attributes which are stored in the data lake. Because this new profile is empty, targeting fields typically used in [!DNL Journey Optimizer] (e.g., personalEmail.address, mobilePhone.number) are empty. Therefore, these fields cannot be used for targeting.

        To solve this, you can specify the "execution field" (or "execution address" depending on the channel) in the channel configuration as 'identityMap'. This ensures that the attribute chosen as the identity at audience creation will be the one used for targeting in [!DNL Journey Optimizer].

    * **Activated records & identity stitching:** Every record in the audience is activated, including any duplicates. During the next Unified Profile Service profile export, these records go through identity stitching. As a result, the number of activated records may differ from the number of profiles after identity stitching.

## Audiences activation delay {#activation}

Audiences are ready for use in [!DNL Journey Optimizer] right after ingestion completes. While this is typically within one hour, it's subject to some variability. Audiences resulting from compositions should be available 24 hours after publishing.

For audiences resulting from batch segmentation jobs, activation may be delayed due to batch ingestion variability. For Read-audience journeys scheduled daily, you can define a time window in the journey properties to ensure fresh audience data is available before journey execution.

If the segmentation job does not complete within the defined time window, the journey will be skipped until its next occurrence. [Learn how to schedule a Read-audience journey](../building-journeys/read-audience.md)

## Target audiences in [!DNL Journey Optimizer]

You can leverage audiences in **[!DNL Journey Optimizer]** in different ways:

* Choose an audience for a **campaign**, where the message is sent to all the individuals belonging to the selected audience. [Learn how to define the audience of a campaign](../campaigns/create-campaign.md#define-the-audience-audience).

* Use a **Read audience** orchestration activity in a journey to make all individuals in the audience enter the journey and receive the messages included in your journey. Let's say you have a "silver customer" audience. With this activity, you can make all silver customers enter a journey. You can then send them a series of personalized messages. [Learn how to configure a Read audience activity](../building-journeys/read-audience.md#configuring-segment-trigger-activity). To segment, exclude, or merge branches after they enter, see [Audience targeting in journeys](../building-journeys/read-audience.md#audience-targeting-in-journeys).

    After entry, use **Condition** activities to [segment by attributes or behavior, exclude part of the population, or merge branches](../building-journeys/read-audience.md#audience-targeting-in-journeys).

    For journeys using audiences from audience composition or custom upload, profile attributes are as fresh as the last batch evaluation at journey entry. However, after a **Wait** activity, the journey refreshes profile attributes from the Unified Profile Service (UPS), fetching the latest available data, which means profile attributes may change during journey execution. [Learn more about profile refresh after a Wait activity](../building-journeys/wait-activity.md#profile-refresh)

* Use the **Optimize** activity in a journey to build conditions based on audience membership. [Learn how to use audiences in conditions](../building-journeys/conditions.md#using-a-segment).

* Use the **Audience Qualification** event activity in a journey to make individuals enter or move forward in the journey based on Adobe Experience Platform audience entrances and exits. For example, you can make all new silver customers enter a journey and send them messages. [Learn how to configure an Audience qualification activity](../building-journeys/audience-qualification-events.md).

    >[!NOTE]
    >
    >Due to the batch nature of audiences created using composition workflows, custom upload or Federated Audience Composition, you cannot target these audiences in an "Audience Qualification" activity. Only audiences created using segment definitions can be leveraged in this activity.

## Activation of non supported audience types in [!DNL Journey Optimizer]

Only audiences generated using **segment definition**, **audience compositions**, **custom upload (CSV file)**, and **Federated audience composition** can be targeted directly in Journey Optimizer journeys and campaigns. [Learn more on available audience types](../audience/about-audiences.md#types)

If you need to target profiles from a non supported audience, such as a Customer Journey Analytics audience, you need to wrap it in a new segment definition in the Audience portal. Detailed information on how to add audiences in a segment definition is available in the [Segment Builder documentation](https://experienceleagu;e.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#adding-audiences){target="_blank"}

Once done, wait for the segmentation evaluation to complete to use it in your journeys and campaigns.
