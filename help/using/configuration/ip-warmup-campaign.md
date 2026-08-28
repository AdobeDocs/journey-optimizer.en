---
solution: Journey Optimizer
product: journey optimizer
title: Create IP warmup campaigns
description: Learn how to create an IP warmup campaign
feature: Campaigns, IP Warmup Plans
topic: Administration
role: Admin
level: Intermediate
keywords: IP, pools, deliverability
exl-id: a9995ca1-d7eb-4f8d-a9d9-fe56198ac325
TQID: https://experienceleague.adobe.com/mzP9buvUwW2h0QahDBXWxefokjZv-XziM-uFaPwg3Wg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c343082f-e963-4f57-a96b-b64d27f8118e
    internal-label: IP warmup plans
  - id: e23d48b5-7858-4d45-9c56-9e2b4be8500e
    internal-label: Business rules
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
  - id: fae48155-b23f-40d2-a252-a25bce350b4d
    internal-label: Email configuration
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Create IP warmup campaigns {#create-ip-warmup-campaign}

>[!BEGINSHADEBOX]

**On this page:** Learn how to create and activate email campaigns dedicated to IP warmup so they can be scheduled and used within an IP warmup plan.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_campaign_ip_warmup"
>title="Activate the IP warmup plan option"
>abstract="When you select this option, the campaign can be used in an IP warmup plan. The campaign schedule will then be driven by the IP warmup plan it is associated with."

Before creating the IP warmup plan itself in [!DNL Journey Optimizer], you first need to create one or more campaigns specifically designed for use in an IP warmup plan<!--through a dedicated option-->.

To create an IP warmup campaign, follow the steps below.

1. Create an email channel [configuration](channel-surfaces.md) for the domain and the IPs that you have identified for your warmup plan.
    
    Work with your deliverability consultant to identify the domain and IPs to be used. Learn how to select them in an email configuration in [this section](../email/email-settings.md#ip-pools).

    >[!CAUTION]
    >
    >Do not edit the email channel configuration after the IP warmup plan has [started](ip-warmup-execution.md).

1. Create a scheduled marketing [campaign](../campaigns/create-campaign.md) and select the [Email](../email/create-email.md#create-email) action.

    <!--Select the Marketing category. The IP warmup plan activation option is only available for  marketing-type campaigns.-->

1. Select the configuration that you created for IP warmup.

    ![](assets/ip-warmup-campaign-surface.png)

    <!--You must use the same configuration as the one that will be used for the asociated IP warmup plan. [Learn how to create an IP warmup plan](#create-ip-warmup-plan)-->

1. Click **[!UICONTROL Create]**.

1. From the **[!UICONTROL Schedule]** section, select **[!UICONTROL IP warmup plan activation]**.

    ![](assets/ip-warmup-campaign-plan-activation.png)

    The campaign [schedule](../campaigns/campaign-schedule.md) will be driven by the IP warmup plan it will be associated with, meaning that the schedule is not defined anymore in the campaign itself.

1. Complete the steps to create an email campaign, such as defining the campaign properties, [audience](../audience/about-audiences.md)<!--best practices for IP warmup in terms of audience?-->, and [content](../email/get-started-email-design.md#key-steps).

    >[!IMPORTANT]
    >
    >Audiences allowed in an IP warmup campaign must be [segment-based](../audience/creating-a-segment-definition.md) and created using the [default merge policy](https://experienceleague.adobe.com/en/docs/experience-platform/profile/merge-policies/overview#default-merge-policy){target="_blank"}.
    >
    >The following audience types are not supported in IP warmup campaigns and will result in an error upon campaign activation:
    >* **[CSV upload audiences](../audience/custom-upload.md)**
    >* [Data Distiller audiences](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller-audiences/overview){target="_blank"} (audiences built using SQL queries)

    For more information on how to configure a campaign, refer to [this page](../campaigns/get-started-with-campaigns.md).

1. Optionally, from the **[!UICONTROL Optimization]** section, add targeting rules to deliver different content to subsets of the audience based on profile attributes. [Learn more](../content-management/optimization-targeting.md)

    If using targeting rules, keep in mind the following:

    * The IP warmup campaign audience is evaluated **once** through the daily batch segmentation cycle. Profile membership is fixed at run activation and is not re-evaluated per run.
    * Profile attributes used in targeting rules are read at the time each run is executed, reflecting the most recently ingested batch profile data — not real-time profile updates.

1. [Activate](../campaigns/review-activate-campaign.md) the campaign. Its status changes to **[!UICONTROL Live]**.

    >[!NOTE]
    >
    >[Business rules](../conflict-prioritization/rule-sets.md#rule-sets) should not be used on IP warmup plans. Applying these rules could hinder reaching the desired number of targeted profiles for campaigns.
    
    For a live campaign with IP warmup plan activated, the **[!UICONTROL Delete]** button is available until it is associated with an IP warmup plan. Once used in a plan, the campaign cannot be deleted anymore.

1. The campaign is displayed in the **[!UICONTROL Campaigns]** list. To easily retrieve all the IP warmup campaigns created on the current sandbox, you can filter on the **[!UICONTROL IP warmup]** campaign option.

    ![](assets/ip-warmup-campaign-filter.png)

Once live, the campaign is ready for use in an IP warmup plan. [Learn more](ip-warmup-plan.md)

An IP warmup campaign can only be used in one IP warmup plan. However, the same campaign can be used in one or more phases of the same IP warmup plan. [Learn more](ip-warmup-plan.md#ip-warmup-plan-tab)

>[!NOTE]
>
>When a live campaign is used in an IP warmup plan, after the plan is [marked as completed](ip-warmup-execution.md#mark-as-completed), the [status](../campaigns/manage-campaigns.md#statuses) of that campaign changes to **[!UICONTROL Stopped]**.

