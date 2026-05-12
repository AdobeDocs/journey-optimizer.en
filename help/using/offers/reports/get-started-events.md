---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Work with Decision Management events
description: Learn how to create Decision Management reports in Adobe Experience Platform.
badge: label="Legacy" type="Informative"
feature: Decision Management, Datasets
topic: Integrations
role: User, Developer
level: Intermediate
exl-id: 51830c63-fa88-47e7-8605-192297fcf6b8
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/r3bOKyWcAT-sqI7KXA3J-Yi5TUax9KGi-8JY62QD6tA
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: c132d929-fa62-4271-803e-b823be07b914
    internal-label: Profile
  - id: c20d46e7-1c7d-476c-a50e-3961d4dce35f
    internal-label: Reporting
  - id: ed0d8d0e-04b9-4326-be72-a0fbca265377
    internal-label: Integrations
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Get started with Decision management events {#monitor-offer-events}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

Each time Decision management makes a decision for a given profile, information related to these events are automatically sent to Adobe Experience Platform. 

This allows you yo gain insights on your decisions, for example, to know which offer was presented to a given profile. You can export these data to analyze them into your own reporting system, or leverage Adobe Experience Platform [Query Service](https://experienceleague.adobe.com/docs/experience-platform/query/home.html) in combination with other tools for enhanced analysis and reporting purposes.

## Key information available in datasets {#key-information}

Each event that is sent when a decision is made contains four key data points that you can leverage for analysis and reporting purposes:

![](../assets/events-dataset-preview.png)

* **[!UICONTROL Fallback]**: Name and ID of the fallback offer, if no personalized offer was selected,
* **[!UICONTROL Placement]**: Name, ID and channel of the placement used to deliver the offer,
* **[!UICONTROL Selections]**: Name and ID of the offer selected for the profile,
* **[!UICONTROL Activity]**: Name and ID of the decision.

Additionally, you can also leverage the **[!UICONTROL identityMap]** and **[!UICONTROL Timestamp]** fields to retrieve information on the profile and the time at which the offer was delivered.

For more information on all the XDM fields that are sent with each decision, refer to [this section](xdm-fields.md).

## Access datasets {#access-datasets}

The datasets containing Decision management events are accessible from Adobe Experience Platform **[!UICONTROL Datasets]** menu. One dataset is automatically created on provisioning for each of your instances.

![](../assets/events-datasets-list.png)

These datasets are based on the **[!UICONTROL ODE DecisionEvents]** schema, which contains all the XDM fields that are required to send information from Decision Management to Adobe Experience Platform.  

>[!NOTE]
>
>Note that ODE DecisionEvents datasets are **non-profile datasets**, meaning that they cannot be ingested into Experience Platform for use by Real-time Customer Profile.
