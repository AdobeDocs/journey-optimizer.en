---
title: About Adobe Analytics data
description: Learn how to leverage Adobe Analytics data
feature: Events
topic: Administration
role: Admin
level: Intermediate
exl-id: 9d842722-e5eb-4743-849d-b7ba9448062f
---
# Leverage Adobe Analytics data{#analytics-data}

You can leverage all of the Adobe Analytics behavioral event data that you are already capturing and streaming into the Platform in order to trigger journeys and automate experiences for your customers.

>[!NOTE]
>
>This section only applies for rule-based events and customers who need to use Adobe Analytics data.

For this to work, you need to activate, in Adobe Experience Platform, the report suite that you want to leverage:

1. In Adobe Experience Platform, select **[!UICONTROL Sources]** then **[!UICONTROL Add data]** in the Adobe Analytics section. The list of available Adobe Analytics report suites is displayed.

1. Pick the report suite you want to enable, click **[!UICONTROL Next]** and click **[!UICONTROL Finish]**. 

This enables the Analytics source connector for that report suite. Whenever the data comes in, it is transformed into an Experience event and sent into Adobe Experience Platform. 

![](assets/jo-event9.png)

Learn more about Adobe Analytics source connector in  [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/sources/connectors/adobe-applications/analytics.html){target="_blank"} and [tutorial](https://experienceleague.adobe.com/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics.html){target="_blank"}.
