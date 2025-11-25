---
solution: Journey Optimizer
product: journey optimizer
title: License usage dashboard
description: Learn about the Journey Optimizer License usage dashboard
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 7e91face-c8f4-4e70-9123-9e36bae7e67e
---
# License usage dashboard {#license-usage}

The [!DNL Adobe Journey Optimizer] [user interface](../start/user-interface.md) provides a dashboard that displays important information about your organization's license usage, as captured during a daily snapshot.

To access this dashboard, go to **[!UICONTROL Administration]** > **[!UICONTROL License Usage]**. This opens the **[!UICONTROL Overview]** tab, which displays the dashboard.

![License usage dashboard overview](assets/license-usage-dashboard.png)

>[!NOTE]
>
>* To view the dashboard, you must have the [View License Usage Dashboard](https://experienceleague.adobe.com/docs/experience-platform/dashboards/permissions.html#available-permissions){target="_blank"} permission.
>
>* Certain metrics (e.g., compute hours, emails) are not displayed for development sandboxes, as indicated by `N/A` in the quota column. Only non-null values are displayed in the dashboard: when metrics are zero or close to zero, they are not populated.


For [!DNL Adobe Journey Optimizer], the dashboard allows you to check the number of **Engageable Profiles**. 

## What is an Engageable Profile? {#what-is-engageable-profile}

An **Engageable Profile** is a record of information representing an individual that is stored in the Profile Service and has been engaged by journeys or campaigns. 

Key characteristics of Engageable Profiles:

* **12-month rolling window**: Engageable Profiles are counted based on engagement over the past 12 months. This metric shows the number of unique profiles that you have attempted to engage with using Journey Optimizer's authoring, decisioning, delivery, experimentation, or orchestration capabilities.

* **Unique count per sandbox**: If a profile enters multiple journeys or campaigns within a sandbox, it is counted only once as a single Engageable Profile for that sandbox.

* **Based on Addressable Audience**: Engageable Profiles are calculated from your Addressable Audience. The count represents the audience engaged in the past 12 months using any of Journey Optimizer's capabilities, out of your total Addressable Audience.

* **Metric behavior**: The Engageable Profiles count:
    * Can increase when new profiles are engaged through journeys or campaigns
    * Cannot decrease unless there is no engagement with certain profiles for over 12 months
    * Can decrease when pseudonymous profiles are stitched to known profiles

>[!NOTE]
>
>**Understanding sudden increases**: A sudden spike in Engageable Profiles may occur when:
>
>* New journeys target large audiences that haven't been engaged recently
>* Datasets containing many profiles (including pseudonymous profiles) are enabled for Profile Service
>* Batch audience exports introduce many new profiles into journey execution
>
>To monitor and control your Engageable Profiles count:
>
>* Review journeys targeting large audiences using [Query Service](../reports/query-examples.md#engageable-profiles-queries)
>* Apply filters at the audience level before initiating journeys or campaigns
>* Monitor datasets enabled for profiling to ensure they don't contain excessive Experience Cloud IDs (ECIDs)
>* Consider reducing your addressable audience size by deleting pseudonymous profiles if necessary

## Related documentation {#related-documentation}

Learn more in the Adobe Experience Platform documentation:

* [License usage dashboard overview](https://experienceleague.adobe.com/docs/experience-platform/dashboards/guides/license-usage.html){target="_blank"}
* [Exploring the license usage dashboard](https://experienceleague.adobe.com/docs/experience-platform/dashboards/guides/license-usage.html#exploring-the-license-usage-dashboard){target="_blank"}
* [Available metrics](https://experienceleague.adobe.com/docs/experience-platform/dashboards/guides/license-usage.html#available-metrics){target="_blank"}
* [Pseudonymous Profile data expiration](https://experienceleague.adobe.com/docs/experience-platform/profile/pseudonymous-profiles.html){target="_blank"}
