---
title: Code-based experience prerequisites
description: To be able to edit apps and web pages using the Journey Optimizer code-based feature, follow the prerequisites on this page
feature: Offers
topic: Content Management
role: User
level: Experienced
hide: yes
hidefromtoc: yes
badge: label="Beta"
exl-id: ac901f88-5fde-4220-88c6-fe05433866cc
---
# Prerequisites and guardrails {#web-prerequisites}

>[!BEGINSHADEBOX]

What you'll find in this documentation guide:

* [Get started with code-based channel](get-started-code-based.md)
* **[Code-based prerequisites](code-based-prerequisites.md)**
* [Code-based implementation samples](code-based-implementation-samples.md)
* [Create code-based experiences](create-code-based.md)

>[!ENDSHADEBOX]

To be able to use code-based experience actions in [!DNL Journey Optimizer] and deliver code content payload that can be used by your applications, follow the prerequisites below:

* To add modifications to your applications, you need to have a specific implementation. [Learn more](#implementation-prerequisites)

* For the code-based experiences to be delivered correctly, make sure you define the Adobe Experience Platform settings detailed [here](#delivery-prerequisites).

## Caution notes {#caution-notes-web}

* The code-based experience channel is currently available as a beta to select users only. To join the beta program, contact Adobe Customer Care.

* Currently in [!DNL Journey Optimizer] you can only create code-based experiences in **campaigns**. [Learn more](../campaigns/create-campaign.md#configure)

## Implementation prerequisites {#implementation-prerequisites}

Code-based experience supports any type of customer implementation as shown in the options below. You can use either a client-side, server-side or a hybrid implementation method for your properties:

* Client-side only – To add modifications to your web pages or mobile apps, you need to implement either the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} on your website or [Adobe Experience Platform Mobile SDK](https://developer.adobe.com/client-sdks/documentation/){target="_blank"} on you mobile apps.

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

## Content experiment prerequisites {#experiment-prerequisites}

To enable content experiments for the code-based channel, you need to make sure the [dataset](../data/get-started-datasets.md) used in your app implementation [datastream](https://experienceleague.adobe.com/docs/experience-platform/datastreams/overview.html){target="_blank"} is also included in your reporting configuration.

In other words, when configuring experiment reporting, if you add a dataset that is not present in your app datastream, app data will not display in the content experiment reports.

Learn how to add datasets for content experiment reporting in [this section](../campaigns/reporting-configuration.md#add-datasets).

>[!NOTE]
>
>The dataset is used read-only by the [!DNL Journey Optimizer] reporting system and doesn't affect data collection or data ingestion.
