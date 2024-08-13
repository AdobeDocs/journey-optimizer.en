---
solution: Journey Optimizer
product: journey optimizer
title: Get started with IP warmup plans
description: Learn how to implement an IP warmup plan
feature: IP Warmup Plans
topic: Administration
role: Admin
level: Experienced
keywords: IP, deliverability
exl-id: 393f051d-b86d-4b4f-b564-7a9ae3a5d4b8
---
# Get started with IP warmup plans {#ip-warmup-gs}

With [!DNL Journey Optimizer], you can easily perform IP warmup workflows directly from the user interface in a standardized and efficient way that follows the best practices for optimal deliverability. When emails are sent using a new platform, Internet service providers (ISPs) are suspicious of IP addresses that are not recognized. If large volumes of emails are suddenly sent, the ISPs often mark them as spam.

To avoid being marked as spam, you can progressively increase the volume sent using the IP warmup plan feature. This new option in the **[!UICONTROL Administration]** menu allows you to do it more easily in a consolidated way instead of creating complex daily journeys.

<!--➡️ [Learn how to create and execute an IP warmup plan in this video](#video)-->

>[!CAUTION]
>
>* IP warmup plan is only available in production environments.
>
>* This capability is not available for organizations that have purchased the Adobe Healthcare Shield or the Privacy and Security Shield add-on offerings.
>
>* This capability only applies to the email channel.

<!--
Benefits

* Standardization on Campaign which will be easy for practitioners too > why?

* No more pain of creating queries, audiences and testing those as system will create the audiences. 

* Ease of excluding domains and changing the plan with help of simple toggles to exclude OR by editing numbers inline or create new phases or reupload plan if drastic change. No more pain of editing audience definitions, journey conditions

* There is an expectation that with this, it will ease around 30% of effort and will be much better experience for consultant/partner/practitioner - right from planning to execution to reporting
-->

The key steps to implement an IP warmup plan are as follows:

1. You first need to create one or more campaigns with the IP warmup option enabled. [Learn more](ip-warmup-campaign.md)

1. Create an IP warmup plan in [!DNL Journey Optimizer] and upload the Excel sheet prepared with the help of your deliverability consultant. [Learn more](ip-warmup-plan.md)

1. Select a campaign for each phase of your plan and activate the corresponding runs. [Learn more](ip-warmup-execution.md)

<!--Old UI
## How-to video {#video}

Learn how to create and execute an IP warmup plan.

>[!VIDEO](https://video.tv.adobe.com/v/3425965/?quality=12&learn=on)
-->


>[!NOTE]
>
>Learn more about increasing your email reputation with IP warming in the [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/generic-resources/increase-reputation-with-ip-warming.html).
