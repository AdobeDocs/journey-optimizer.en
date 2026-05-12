---
solution: Journey Optimizer
product: journey optimizer
title: Updated reporting experience
description: Get started with all time report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: bfd88d2a-e7b8-4e3b-85a1-4a14b0ba56dc
TQID: https://experienceleague.adobe.com/lewg6KxoowTzp9By5yy62c8ebfa3hloA-FqkUZZfOY0
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: b32bb433-f8c6-4931-8e52-e657230a3bf2
    internal-label: Audiences
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
---
# Get started with all time report {#channel-report-gs-cja}

>[!CONTEXTUALHELP]
>id="cja_connections_enable_cja"
>title="Enable Customer Journey Analytics"
>abstract="To analyze this report in Customer Journey Analytics, contact your administrator to make sure your organization has purchased Customer Journey Analytics and that the integration is properly configured."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/design-email/add-content/content-components#add-content-components" text="Customer Journey Analytics"

Journey Optimizer reporting comes with an improved interoperability with Customer Journey Analytics capabilities, standardizing reporting across both platforms and improving data consistency and reliability. This seamless integration between Journey Optimizer and Customer Journey Analytics provides a clearer view of performance metrics, enabling users to make more informed decisions.

Access to these reporting capabilities depends on the context and product areas: 

* **Journeys** - If you want to target a journey or deliveries in the context of a journey, from the **[!UICONTROL Journeys]** menu, access your journey and click the **[!UICONTROL View report]** button. 

    From the list of existing journey, you can also select **[!UICONTROL Report]** from the advanced menu of your selected journey. [Learn more about the Journey report](journey-global-report-cja.md)

    ![](assets/gs-cja-report-3.png)

* **Campaigns** - If you want to target a campaign, from the **[!UICONTROL Campaigns]** menu, access your campaign and click the **[!UICONTROL Reports]** button then **[!UICONTROL View all time report]**.

    From the list of existing campaigns, you can also select **[!UICONTROL Report]** from the advanced menu of your selected campaign. [Learn more about the Campaign report](campaign-global-report-cja.md)

    ![](assets/gs-cja-report-2.png)

* **Global** - If you want to target metrics for all campaigns and journeys within your environment, access the **Overview** report by navigating to the **[!UICONTROL Reports]** menu within the **[!UICONTROL Journey Management]** section. [Learn more about the Overview report](channel-report-cja.md)

    ![](assets/gs-cja-report-1.png)

>[!IMPORTANT]
>
>Reporting in Adobe Journey Optimizer is currently standardized to UTC. The ability to customize the reporting timezone will be introduced in a future release.

## Prerequisites {#prerequisites}

* If you do **not** own Customer Journey Analytics, or if you own it but do **not** have access to any Customer Journey Analytics product profile, permissions are managed in Journey Optimizer. In this case, you need the **[!UICONTROL View channel reports]** permission or related roles. [Learn more](../administration/permissions.md)

* If you **own** Customer Journey Analytics and have access to a Customer Journey Analytics product profile, you need:

    * **[!UICONTROL Audience Creation]** and **[!UICONTROL Audience View]** permissions for Customer Journey Analytics. [Learn more](https://experienceleague.adobe.com/en/docs/analytics-platform/using/technotes/access-control){target="_blank"}

    * **[!UICONTROL Manage profiles]** permission for Adobe Journey Optimizer. [Learn more](../administration/permissions.md)

* Your Customer Journey Analytics dataviews need to be configured with the following setting: **Set as default data view in Adobe Journey Optimizer**. [Learn more about data views](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/create-dataview){target="_blank"}


## How-to video{#video}

The video below shows how to use the enhanced Journey Optimizer reporting with Customer Journey Analytics.

>[!VIDEO](https://video.tv.adobe.com/v/3430413)