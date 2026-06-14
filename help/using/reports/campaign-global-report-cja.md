---
solution: Journey Optimizer
product: journey optimizer
title: Campaign report
description: Learn how to usecampaign data from the Campaign report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: b74d3137-2dd9-4302-a56e-73503d318d18
TQID: https://experienceleague.adobe.com/-1IfHcdK07JLG54DYR1GNNN-sU0VyHjfBjCLbNdKA-8
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a9f73820-6899-47c2-a597-3fec28ab756a
    internal-label: Reporting
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
subfeature_v2:
  - id: d145add9-d5b9-481b-aa8a-e15e6bb7f813
    internal-label: Performance monitoring
  - id: a7289281-9ae4-47b1-b8cf-4028b98af776
    internal-label: Deliverability
  - id: b5afe8bf-bda6-41b5-ba06-922638872d63
    internal-label: Metrics catalog
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Campaign report {#campaign-global-report-cja}

>[!BEGINSHADEBOX]

**On this page:** Learn how to read the Campaign report in Adobe Journey Optimizer to review campaign KPIs, the campaign overview and funnel, tracked links, and targeting performance across all channels used in your campaign.

>[!ENDSHADEBOX]

>[!BEGINSHADEBOX]

You can access your Campaign report by clicking the **[!UICONTROL Reports]** button from your campaign, then selecting **[!UICONTROL View all time report]**. [Learn more](report-gs-cja.md)

![](assets/report-access.png)

>[!ENDSHADEBOX]

## Campaign KPIs {#campaign-kpis}

![](assets/cja-email-kpis.png)

The **[!UICONTROL Campaign]** Key Performance Indicators (KPIs) function as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your campaign. This encompasses details such as the count of clicks and number of delivered messages, offering a comprehensive insight into your campaign's effectiveness and level of engagement.

The KPIs will vary based on the channels used in your campaign.

+++ Learn more about Campaign KPIs metrics

* **[!UICONTROL Click through rate]**: Percentage of users who interacted with the message.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on in your message.

* **[!UICONTROL Delivered]**: Number of emails successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Displays]**: Number of times the message was opened.

+++

>[!AVAILABILITY]
>Orchestrated campaigns only support the SMS, Email, and Push channels. Other channels (In-app, Web, Direct mail, etc.) are not available in orchestrated campaigns and do not appear in reporting.

### Campaign overview {#delivery-global}

![](assets/cja-campaign-overview.png)

The **[!UICONTROL Campaign overview]** table serve as a comprehensive dashboard, offering a detailed breakdown of key metrics related to your campaign. This includes essential information such as the number of profiles and the actions delivered, providing a thorough understanding of your campaign's performance and engagement.

Note that metrics will vary based on the channels used in your campaign.

+++ Learn more about Campaign overview metrics

* **[!UICONTROL People]**: Number of user profiles who qualify as target profiles for your messages.

* **[!UICONTROL Click through rate]**: Percentage of users who interacted with the message.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on in your message.

* **[!UICONTROL Unique Clicks]**: Number of profiles who clicked on a content in your message.

* **[!UICONTROL Delivered]**: Number of emails successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Bounces for outbound channels]**: Total number of errors cumulated during the sending process and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Outbound Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Outbound Exclusions]**: Number of profiles which have been excluded by Adobe Journey Optimizer. [Learn more about how exclusions are counted](exclusion-list.md#exclusion-list).

* **[!UICONTROL Displays]**: Number of times the message was opened.

* **[!UICONTROL Unique displays]**: Number of times the message was opened, multiple interactions of one profile are not taken into account.

+++

### Campaign funnel results {#campaign-funnel}

![](assets/cja-campaign-funnel.png)

The **[!UICONTROL Campaign funnel results]** graph presents a detailed analysis of your profiles' engagement with your messages, offering valuable insights into how various profiles interacted with your content.

+++ Learn more about Campaign funnel results metrics

* **[!UICONTROL Delivered]**: Number of emails successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on in your message.
+++

### Tracked link label {#campaign-track}

![](assets/cja-campaign-tracked-link.png)

The **[!UICONTROL Tracked link label]** table offers essential insights into your visitors' engagement with the URLs included in your messages, providing valuable information about which links attract the most interaction.

+++ Learn more about Tracked link label metrics

* **[!UICONTROL Unique Clicks]**: Number of profiles who clicked on a content in your message.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on in your message.

+++

## Targeting overview {#targeting}

![](assets/cja-journey-targeting-overview.png)

If you set up **[!UICONTROL Targeting rules]** for your content, the **[!UICONTROL Targeting overview]** table provides a detailed view of key engagement metrics, showing how the targeted profiles for each rule interacted with your content.

➡️ [Learn more on Targeting rules](../content-management/optimization-targeting.md)

+++ Learn more about Targeting overview metrics

* **[!UICONTROL People]**: Number of user profiles who qualify as target profiles for your events.

* **[!UICONTROL Unique Clicks]**: Number of profiles who clicked on a content in an email.

* **[!UICONTROL Unique click rate]**: Percentage of targeted profiles who clicked at least once.

+++
