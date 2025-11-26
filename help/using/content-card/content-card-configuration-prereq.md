---
title: Content cards configuration
description: Content cards channel prerequisites
feature: Channel Configuration, Content Cards
topic: Content Management
role: Admin
level: Experienced
exl-id: df92e319-1e42-486f-b688-595964a762c9
---
# Content cards prerequisites {#content-card-configuration-prereq}

For Adobe Journey Optimizer to correctly display content cards, you must configure the following Adobe Experience Platform settings:

* **Adobe Experience Platform Data Collection**

    [Create a datastream](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure){target="_blank"} and [add the Experience Platform service](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure#aep){target="_blank"}. Enable the **[!UICONTROL Edge Segmentation]** and **[!UICONTROL Adobe Journey Optimizer]** options. This ensures that Journey Optimizer events are handled by the Adobe Experience Platform Edge Network. 
    Add the **Experience Event – Proposition Interaction** field group to your dataset to include this data in your reports. [Learn more about datastreams](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/configure){target="_blank"}

* **Adobe Experience Platform**

    Ensure the default merge policy has **Active-On-Edge Merge Policy** enabled under **[!UICONTROL Customer]** > **[!UICONTROL Profiles]** > **[!UICONTROL Merge Policies]** Experience Platform menu. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html#configure){target="_blank"}

    >[!NOTE]
    >
    >When using a custom **[!UICONTROL Dataset preference]** merge policy, make sure to add the **[!UICONTROL Journey Inbound]** dataset within the specified merge policy.

* **Adobe Experience Platform Mobile or Platform Web SDK** 

    For mobile and web applications, to add modifications to your web pages or mobile apps, you need to implement either the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/en/docs/platform-learn/implement-web-sdk/overview){target="_blank"} on your website or [Adobe Experience Platform Mobile SDK](https://developer.adobe.com/client-sdks/home/){target="_blank"} on your mobile apps.

* **Journey Optimizer**

    Create a [Content card configuration](#content-card-configuration).

* **Troubleshooting**

    Use the **Edge Delivery** view within **Adobe Experience Platform Assurance** to troubleshoot mobile experiences. It can inspect requests, verify edge calls, and examine profile data. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery){target="_blank"}

* **Content Experiments**

    Ensure the dataset used in your app's [datastream](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/overview#_blank){target="_blank"} is also included in your content experiment reporting configuration. App data will not display in reports if datasets do not match.

    Learn how to add datasets for content experiment reporting in [this section](../reports/reporting-configuration.md).

## Profile management guardrail {#profile-management-guardrail}

[!DNL Journey Optimizer] content cards can target pseudonymous profiles, meaning profiles that are not authenticated or not known yet because they have not been engaged before on other channels. This is the case for example when targeting all visitors or audiences based on temporary IDs like ECID.

This increases your total engageable profile count, which may have cost implications if the contractual number of engageable profiles you purchased is exceeded. License metrics for each package are listed on the [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} page. You can check the number of engageable profiles in the [license usage dashboard](../audience/license-usage.md).

To keep your engageable profiles within reasonable limits, Adobe recommends setting a Time-To-Live (TTL) to automatically delete pseudonymous profiles from the Real-Time Customer Profile if they haven't been seen or engaged within a specific time window.

>[!NOTE]
>
>Learn how to configure data expiration for pseudonymous profiles in the [Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/pseudonymous-profiles){target="_blank"}.

Adobe recommends setting the TTL value to 14 days to match the current Edge profile TTL.