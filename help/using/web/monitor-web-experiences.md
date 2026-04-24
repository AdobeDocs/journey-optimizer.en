---
title: Monitor your web experiences
description: Learn how to monitor your web experiences in Journey Optimizer
feature: Web Channel, Reporting, Monitoring
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: d89795bb-c51d-4d1f-b7ed-2b2c5d278922
TQID: https://experienceleague.adobe.com/CEjKwnKx1ixUKA-mO7FfWGXaW9FyO-I-ZYyYm0scs88
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: e9001ce2-5245-4a8e-8601-dd958009072f
    internal-label: Web experience
---
# Monitor your web experiences {#monitor-web-experiences}

## Check the web reports {#check-web-reports}

Once your web experience is live, you can check the **[!UICONTROL Web]** tab of the  [Journey report](../reports/journey-global-report-cja-web.md) and [Campaign report](../reports/campaign-global-report-cja-web.md) to compare elements such as the number of impressions, click rate and number of engagements with your web page.

<!--You can check the **[!UICONTROL Web]** tab of the campaign reports. Learn more about the campaign web [live report](../reports/campaign-live-report.md#web-tab) and [global report](../reports/campaign-global-report-cja.md#web).-->

To further improve your web experience monitoring, you can also track the clicks on any specific element of your website. This allows you to display the number of clicks on that element in the web reports. [Learn how](#use-click-tracing)

## Use click tracking {#use-click-tracking}

The web designer allows you to select any element of your website and track the clicks on that element.

This information can be useful to improve your website users' experience. For example, if the [web reports](../reports/campaign-global-report-cja-web.md) show that many users click an element that is not actually clickable, you may want to add a link to that element.

1. Select an element in your page and choose **[!UICONTROL Click track element]** from the contextual menu.

    ![](assets/web-designer-click-track.png)
    
    >[!NOTE]
    >
    >Any item, clickable or not, can be selected.

1. The corresponding tracked action automatically displays in the **[!UICONTROL Click track]** pane on the left. 

    ![](assets/web-designer-click-track-pane.png)

1. Add a meaningful label to manage all your tracked elements and find them easily in the reports. The **[!UICONTROL CSS selector]** field shows information to locate the selected element.

1. Repeat the steps above to select as many other elements as you need for click tracking. The corresponding actions are all listed on the left pane.

    ![](assets/web-designer-click-tracking-actions.png)

1. To remove click tracking on an element, select the corresponding delete icon.

Once your campaign is live, you can check the number of clicks for each element in the campaign web [live report](../reports/campaign-live-report.md#web-tab) and [Customer Journey Analytics report](../reports/campaign-global-report-cja-web.md).
