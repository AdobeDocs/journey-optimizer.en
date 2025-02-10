---
solution: Journey Optimizer
product: journey optimizer
title: Build segment definitions
description: Learn how to create audiences through segment definitions
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 289aac5d-6cdb-411f-985e-3acef58050a8
---
# Build segment definitions {#build-segments}

>[!CONTEXTUALHELP]
>id="ajo_ao_create_rule"
>title="Create a rule"
>abstract="The Build rule creation method allows you to create a new audience definition using Adobe Experience Platform Segmentation Service."

## Create a segment definition {#create}

In this example, we will build an audience to target all customers living in Atlanta, San Francisco, or Seattle and born after 1980. All these customers should have made a purchase within the last 7 days.

➡️ [Learn how to create audiences in this video](#video-segment)

1. From the **[!UICONTROL Audiences]** menu, click the **[!UICONTROL Create audience]** button and select **[!UICONTROL Build rule]**.
    
    ![](assets/create-segment.png)

    The segment definition screen allows you to configure all the required fields to define your audience. Learn how to configure audiences in the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html){target="_blank"}.

    ![](assets/segment-builder.png)

1. In the **[!UICONTROL Audience properties]** pane, provide a name and a description (optional) for the audience.

    ![](assets/segment-properties.png)

1. Drag and drop the desired fields from the left pane into the center workspace, then configure them according to your needs.

    The basic building blocks of segment definitions are **attributes** and **events**. In addition, the attributes and events contained in existing audiences can be used as components for new definitions. [Learn more in the Segmentation service documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#building-blocks){target="_blank"}

    >[!NOTE]
    >
    >Note that the fields available in the left pane vary depending on how the **XDM Individual Profile** and **XDM ExperienceEvent** schemas have been configured for your organization.  Learn more in the [Experience Data Model (XDM) documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

    ![](assets/drag-fields.png)

    In this example, we need to rely on **Attributes** and **Events** fields to build the audience:

    * **Attributes**: profiles living in Atlanta, San Francisco or Seattle born after 1980.

        ![](assets/add-attributes.png)
        
    * **Events**: profiles who made a purchase within the last 7 days.

        ![](assets/add-events.png)

1. As you are adding and configuring new fields in the workspace, the **[!UICONTROL Audience Properties]** pane is automatically updated with information on the estimated profiles belonging to the audience.

    ![](assets/segment-estimate.png)

1. Once the audience is ready, click **[!UICONTROL Save]**. It displays in the list of Adobe Experience Platform audiences. Note that a search bar is available to help you search a specific audience in the list.

The audience can now be used in your journeys. For more on this, refer to [this section](../audience/about-audiences.md).

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

After you have first defined an audience, profiles are added to the audience when they qualify. Backfilling the audience from prior data can take up to 24&nbsp;hours. After the audience has been backfilled, the audience is continuously kept up-to-date and is always ready for targeting.

## [!BADGE Limited Availability]{type=Informative} Flexible audience evaluation {#flexible}

>[!AVAILABILITY]
>
>Flexible audience evaluation is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

Adobe Experience Platform Audience Portal allows you to run a segmentation job on demand for selected audiences, ensuring that you always have the most up-to-date audience data before targeting them into Journey Optimizer journeys and campaigns.

With flexible audience evaluation, you can:

1. Create a fresh new segment based on your latest data.
1. Evaluate the audience in real time to ensure accuracy. To do so, choose the audiences you want to have evaluated and select "Evaluate audiences", provided they meet specific criteria (e.g., people-based, Segmentation Service origin).
1. Use the evaluated audience in Adobe Journey Optimizer
campaigns or journeys for precise targeting.

You can evaluate up to 20 audiences at a time, and ineligible audiences will be automatically excluded. For more details, see the [Audience Portal documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-portal#flexible-audience-evaluation). 

## How-to video{#video-segment}

Understand how Journey Optimizer uses rules to generate audience and learn how to use attributes, events, and existing audiences to create an audience.

>[!VIDEO](https://video.tv.adobe.com/v/3425020?quality=12)
