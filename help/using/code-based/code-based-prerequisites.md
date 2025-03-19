---
title: Code-based experience prerequisites
description: To be able to edit apps and web pages using the Journey Optimizer code-based feature, follow the prerequisites on this page
feature: Code-based Experiences
topic: Content Management
role: Admin
level: Experienced
exl-id: ac901f88-5fde-4220-88c6-fe05433866cc
---
# Code-based experience prerequisites {#code-based-prerequisites}

To be able to use code-based experience actions in [!DNL Journey Optimizer] and deliver code content payload that can be used by your applications, follow the prerequisites below:

* To add modifications to your applications, you must have a specific implementation. [Learn more](#implementation-prerequisites)

* For the code-based experiences to be delivered correctly, make sure you define the Adobe Experience Platform settings detailed [here](#delivery-prerequisites).

* To enable data to display in your code-based experience reports, make sure you follow these [reporting prerequisites](#reporting-prerequisites).

* When creating a [code-based experience channel configuration](code-based-configuration.md), make sure you enter a string/path or a surface URI that matches the one declared in your own implementation. This ensures that the content is delivered to the desired location inside the specified app or page. Otherwise, the changes cannot be delivered. [Read more](code-based-surface.md)

## Implementation prerequisites {#implementation-prerequisites}

Code-based experience supports any type of customer implementation as shown in the options below. You can use either a client-side, server-side or a hybrid implementation method for your properties:

* Client-side only – To add modifications to your web pages or mobile apps, you need to implement either the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} on your website or the [Adobe Experience Platform Mobile SDK](https://developer.adobe.com/client-sdks/documentation/){target="_blank"} on you mobile apps.

* Hybrid mode – You can use the [AEP Edge Network Server API](https://experienceleague.adobe.com/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection.html){target="_blank"} to request for personalization server-side; the response is provided to the Adobe Experience Platform Web SDK to render the modifications client-side. Learn more in the Adobe Experience Platform [Edge Network Server API documentation](https://experienceleague.adobe.com/docs/experience-platform/edge-network-server-api/overview.html){target="_blank"}. You can find out more about the hybrid mode and check some implementation samples in [this blog post](https://blog.developer.adobe.com/hybrid-personalization-in-the-adobe-experience-platform-web-sdk-6a1bb674bf41){target="_blank"}.

* Server-side - You can use the [AEP Edge Network Server API](https://experienceleague.adobe.com/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection.html){target="_blank"} to request for personalization server-side. Your development team must handle the response and render the modifications client-side in your app implementation.

You can find samples for each of the implementation method above in [this section](code-based-implementation-samples.md).

## Delivery prerequisites {#delivery-prerequisites}

For the code-based experiences to be delivered correctly, the following settings must be defined:

* In the [Adobe Experience Platform Data Collection](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/overview.html){target="_blank"}, make sure you have a datastream defined such as under the **[!UICONTROL Adobe Experience Platform]** service you have the **[!UICONTROL Adobe Journey Optimizer]** option enabled.

    This ensures that the Journey Optimizer inbound events are correctly handled by the Adobe Experience Platform Edge. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/configure.html){target="_blank"}

    ![](../web/assets/web-aep-datastream-ajo.png)

* In [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"}, make sure you have one merge policy with the **[!UICONTROL Active-On-Edge Merge Policy]** option enabled. To do this, select a policy under the **[!UICONTROL Customer]** > **[!UICONTROL Profiles]** > **[!UICONTROL Merge Policies]** Experience Platform menu. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html#configure){target="_blank"}

    This merge policy is used by [!DNL Journey Optimizer] inbound channels to correctly activate and publish inbound campaigns on the edge. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html){target="_blank"}

    ![](../web/assets/web-aep-merge-policy.png)

* To troubleshoot the delivery of Journey Optimizer web experiences, you can use the **Edge Delivery** view within **Adobe Experience Platform Assurance**. This plugin enables you to inspect request calls in detail, verify whether the expected edge calls occur as anticipated, and examine profile data, including identity maps, segment memberships, and consent settings. Additionally, you can review the activities the request qualified for and identify those it did not.

    Using the **Edge Delivery** plugin helps you gain the insights needed to understand and troubleshoot your inbound implementations effectively.

    [Learn more on Edge Delivery view](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery)

## Reporting prerequisites {#reporting-prerequisites}

To enable reporting for the code-based channel, you need to make sure the [dataset](../data/get-started-datasets.md) used in your app implementation [datastream](https://experienceleague.adobe.com/docs/experience-platform/datastreams/overview.html){target="_blank"} is also included in your reporting configuration.

In other words, when configuring reporting, if you add a dataset that is not present in your app datastream, app data will not display in your reports.

Learn how to add datasets for reporting in [this section](../reports/reporting-configuration.md#add-datasets).

>[!NOTE]
>
>The dataset is used read-only by the [!DNL Journey Optimizer] reporting system and doesn't affect data collection or data ingestion.
