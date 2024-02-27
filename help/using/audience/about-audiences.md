---
solution: Journey Optimizer
product: journey optimizer
title: About Adobe Experience Platform audiences
description: Learn how to work with Adobe Experience Platform audiences
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 10d2de34-23c1-4a5e-b868-700b462312eb
---
# Get started with Adobe Experience Platform audiences {#about-segments}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_content_experiment_segment"
>title="Audience"
>abstract="By leveraging Real-Time Customer Profile data, Adobe Experience Platform enables you to easily build segment definitions to create targeted audiences that capture the unique behaviors and preferences of your customers."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_audience"
>title="Select the campaign audience"
>abstract="This list displays all available Adobe Experience Platform audiences. Select the audience to target with your campaign. The message configured in the campaign will be sent to all the individuals belonging to the selected audience. [Learn more on audiences](../audience/about-audiences.md)"

An audience is a set of people who share similar behaviors and/or characteristics. Learn more about audiences in the [Adobe Experience Platform Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/home.html){target="_blank"}.

[!DNL Journey Optimizer] allows you to build Adobe Experience Platform audiences directly from the **[!UICONTROL Audiences]** menu, and leverage them into your journeys or campaigns.

Audiences can be generated using different methods:

* **Segment definitions**: Create a new audience definition using Adobe Experience Platform Segmentation Service. [Learn how to build segment definitions](creating-a-segment-definition.md)
* **CSV file import**: Import an audience using a CSV file. Learn how to import audiences in Adobe Experience Platform [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience){target="_blank"}.
* **Audience composition**: Create a composition workflow to combine existing Adobe Experience Platform audiences into a visual canvas and leverage various activites (split, exclude...) to create new audiences. [Get started with audience composition](get-started-audience-orchestration.md)

## Target audiences in [!DNL Journey Optimizer] {#segments-in-journey-optimizer}

You can select in campaigns and journeys any audience generated using segment definitions, CSV file import or composition workflows.

>[!AVAILABILITY]
>
>The use of audiences and attributes from audience composition and custom upload (CSV file) audiences is currently unavailable for use with Healthcare Shield or Privacy and Security Shield. [Learn how to use audiences enrichment attributes in Journey Optimizer](../audience/about-audiences.md#enrichment)
 
You can leverage audiences in **[!DNL Journey Optimizer]** in different ways:

* Choose an audience for a **campaign**, where the message is sent to all the individuals belonging to the selected audience. [Learn how to define the audience of a campaign](../campaigns/create-campaign.md#define-the-audience-audience).

* Use a **Read audience** orchestration activity in a journey to make all individuals in the audience enter the journey and receive the messages included in your journey.

    Let's say you have a "silver customer" audience. With this activity, you can make all silver customers enter a journey and send them a series of personalized messages. [Learn how to configure a Read audience activity](../building-journeys/read-audience.md#configuring-segment-trigger-activity).

* Use the **Audience qualification** event activity in a journey to make individuals enter or move forward in the journey based on Adobe Experience Platform audience entrances and exits.

    For example, you can make all new silver customers enter a journey and send them messages. For more on how to use this activity, refer to [Learn how to configure an Audience qualification activity](../building-journeys/audience-qualification-events.md).

* Use the **Condition** activity in a journey to build conditions based on audience membership. [Learn how to use audiences in conditions](../building-journeys/condition-activity.md#using-a-segment).

## Use audiences enrichment attributes in Journey Optimizer {#enrichment}

When targeting an audience generated using composition workflows, you can leverage enrichment attributes from these audiences to build your journey and personalize your messages.

* Create multiple path in a journey based on rules that leverage the targeted audience's enrichement attributes. To do this, target the audience using a [Read audience](../building-journeys/read-audience.md) activity then create rules in a [Condition](../building-journeys/condition-activity.md) activity based on the audience's enrichment attributes.

    ![](assets/audience-enrichment-attribute-condition.png){zoomable="yes"}

* Personalize your messages in journeys or campaigns by adding enrichment attributes from the targeted audience in the Expression editor. [Learn how to work with the Expression editor](../personalization/personalization-build-expressions.md)

    ![](assets/audience-enrichment-attribute-perso.png){zoomable="yes"}

## Audience evaluation methods {#evaluation-method-in-journey-optimizer}

In Adobe Journey Optimizer, audiences are generated from segment definitions using one of three evaluation methods below.

+++ Streaming segmentation

The profiles list for the audience is kept up-to-date in real-time as new data flows into the system.

Streaming segmentation is an ongoing data selection process that updates your audiences in response to user activity. Once a segment definition has been built and the resulting audience has been saved, the segment definition is applied against incoming data to Journey Optimizer. This means that individuals are added or removed from the audience as their profile data changes, ensuring that your target audience is always relevant. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/streaming-segmentation.html){target="_blank"}

>[!NOTE]
>
>Make sure to use the right events as streaming segmentation criteria. [Learn more](#streaming-segmentation-events-guardrails)

+++

+++ Batch segmentation

The profiles list for the audience is evaluated every 24 hours.

Batch segmentation is an alternative to streaming segmentation that processes all profile data at once through segment definitions. This creates a snapshot of the audience that can be saved and exported for use. However, unlike streaming segmentation, batch segmentation does not continuously update the audience list in real-time, and new data that comes in after the batch process will not be reflected in the audience until the next batch process. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/segmentation/home.html#batch){target="_blank"}

+++

+++ Edge segmentation

Edge segmentation is the ability to evaluate segments in Adobe Experience Platform instantaneously [on the edge](https://experienceleague.adobe.com/docs/experience-platform/edge/home.html){target="_blank"}, enabling same-page and next-page personalization use cases. Currently only select query types can be evaluated with edge segmentation. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/edge-segmentation.html#query-types){target="_blank"}

+++

If you know what evaluation method you want to use, select it using the drop-down list. You can also click the browse icon folder icon with a magnifying glass to see a list of the available segment definition evaluation methods. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/segment-builder.html#segment-properties){target="_blank"}

![](assets/evaluation-methods.png)

<!--The determination between batch segmentation and streaming segmentation is made by the system for each audience, based on the complexity and the cost of evaluating the segment definition rule. You can view the evaluation method for each audience in the **[!UICONTROL Evaluation method]** column of the audience list.
    
![](assets/evaluation-method.png)

>[!NOTE]
>
>If the **[!UICONTROL Evaluation method]** column does not display, you  need to add it using configuration button on the top right of the list.-->

After you have first defined an audience, profiles are added to the audience when they qualify.

Backfilling the audience from prior data can take up to 24&nbsp;hours. After the audience has been backfilled, the audience is continuously kept up-to-date and is always ready for targeting.

### Event usage with streaming segmentation {#streaming-segmentation-events-guardrails}

Streaming segmentation is useful for real-time personalization with high-value use cases. However, it is important to choose the right [events](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/segment-builder.html#events){target="_blank"} to use as segmentation criteria.

Consequently, for streaming segmentation optimal performance, avoid using the following events:

* **Message Opened** Interaction Type event

    When building your audience, the use of **Message Opened** interaction events became unreliable, because they are not actual indicators of user activity and can negatively impact segmentation performance. Learn why in this [Adobe Blog post](https://blog.adobe.com/en/publish/2021/06/24/what-apples-mail-privacy-protection-means-for-email-marketers){target="_blank"}.

    Hence, Adobe recommends not using **Message Opened** interaction events with streaming segmentation. Instead, use real user-activity signals like clicks, purchases, or beacon data.

* **Message sent** Feedback Status event

    The **Message sent** feedback event is often used for frequency or suppression checking prior to sending an email. Adobe recommends avoiding it as it puts pressure on performance and may cause degradation of the system.

    Therefore, for frequency or suppression logic, use business rules rather than **Message sent** feedback events. Note that daily frequency caps for individual profiles will soon be available, complementing the existing monthly cadence for business rules.

>[!NOTE]
>
>You can use **Message Opened** and **Message Sent** events in batch segmentation without any performance concerns.
