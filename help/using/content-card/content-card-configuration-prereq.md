---
title: Content cards configuration
description: Content cards channel prerequisites
feature: Channel Configuration
topic: Content Management
role: Admin
level: Experienced
---
# Content cards prerequisites {#content-card-configuration-prereq}

For Adobe Journey Optimizer to correctly display content cards, you must configure the following Adobe Experience Platform settings:

* **Adobe Experience Platform Data Collection**

    [Create a datastream](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure) and [add the Experience Platform service](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure#aep). Enable the **[!UICONTROL Edge Segmentation]** and **[!UICONTROL Adobe Journey Optimizer]** options. This ensures that Journey Optimizer events are handled by the Adobe Experience Platform Edge Network. 
    Add the **Experience Event – Proposition Interaction** field group to your dataset to include this data in your reports. [Learn more on datastreams](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure)

* **Adobe Experience Platform**

    Ensure the default merge policy has **Active-On-Edge Merge Policy** enabled under **[!UICONTROL Customer]** > **[!UICONTROL Profiles]** > **[!UICONTROL Merge Policies]** Experience Platform menu. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html#configure){target="_blank"}

    >[!NOTE]
    >
    >When using a custom **[!UICONTROL Dataset preference]** merge policy, make sure to add the **[!UICONTROL Journey Inbound]** dataset within the specified merge policy.

* **Adobe Experience Platform Mobile or Platform Web SDK** 

    For mobile and web applications, to add modifications to your web pages or mobile apps, you need to implement either the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/en/docs/platform-learn/implement-web-sdk/overview) on your website or [Adobe Experience Platform Mobile SDK](https://developer.adobe.com/client-sdks/home/) on your mobile apps.

* **Journey Optimizer**

    Create a [Content card configuration](#content-card-configuration).

* **Troubleshooting**

    Use the **Edge Delivery** view within **Adobe Experience Platform Assurance** to troubleshoot mobile experiences. It can inspect requests, verify edge calls, and examine profile data. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery)

* **Content Experiments**

    Ensure the dataset used in your app's [datastream](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/overview#_blank) is also included in your content experiment reporting configuration. App data will not display in reports if datasets do not match.

    Learn how to add datasets for content experiment reporting in [this section](../reports/reporting-configuration.md).
