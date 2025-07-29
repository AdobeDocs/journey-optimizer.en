---
title: Create fallback offers
description: Learn how to create fallback offers to display for customers who are not eligible for any offer
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Intermediate
exl-id: 9ba16ad9-a5e7-4ce7-8ed6-7707d37178c6
---
# Create fallback offers {#create-fallback-offers}

The fallback offer is sent to customers if they are not eligible for other offers. The steps to create a fallback offer consist in creating one or several representations, like when creating an offer.

➡️ [Discover this feature in video](#video)

The list of fallback offers is accessible in the **[!UICONTROL Offers]** menu.

![](../assets/offers_list.png)

To create a fallback offer, follow these steps:

>[!NOTE]
>
>Note that, unlike personalized offers, fallback offers have no eligibility rules and constraint parameters, because they are presented to customers as last resorts with no condition.

1. Click **[!UICONTROL Create offer]**, then select **[!UICONTROL Fallback offer]**.

    ![](../assets/create_fallback.png)

1. Specify the fallback offer's name. You can also associate one or several existing collection qualifier(s) (previously known as "tags") to it, allowing you to search and organize the Offer Library more easily. 

    ![](../assets/fallback_details.png)

1. To assign custom or core data usage labels to the offer, select **[!UICONTROL Manage access]**. [Learn more about Object Level Access Control (OLAC)](../../administration/object-based-access.md)
    
1. Create one or several representations for the fallback offer. To do this, drag and drop placements from the left pane, like when creating a personalized offer. See [Create personalized offers](../offer-library/creating-personalized-offers.md).

    ![](../assets/fallback_content.png)

    >[!CAUTION]
    >
    >Fallback offers should contain all representations used within a [decision](../offer-activities/create-offer-activities.md). For example, if you have 5 offers in a decision and each of them has a different representation, 5 representations should be included in the fallback offer.

1. Once the fallback offer's representations have been added, a summary displays. If everything is configured properly and your fallback offer is ready to be presented to customers, click **[!UICONTROL Finish]**, then select **[!UICONTROL Save and approve]**.

    You can also save the fallback offer as a draft, in order to edit and approve it later on.

    ![](../assets/fallback_review.png)

1. The fallback offer displays in the list with the **[!UICONTROL Live]** or **[!UICONTROL Draft]** status, depending on whether you approved it or not in the previous step.

    It is now ready to be delivered to customers. You can select it to display its properties and edit it. <!-- no suppression? -->

    ![](../assets/fallback_created.png)

## How-to video {#video}

>[!VIDEO](https://video.tv.adobe.com/v/329383?quality=12)

