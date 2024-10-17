---
solution: Journey Optimizer
product: journey optimizer
title: Campaign live report
description: Learn how to use data from the Campaign live report
feature: Reporting, Campaigns
topic: Content Management
role: User
level: Intermediate
exl-id: 925494b6-e08a-4bd3-8a2f-96a5d9cbc387
---
# Campaign live report {#campaign-live-report}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_report"
>title="Campaign live report"
>abstract="The Campaign live report allows you to measure and visualize in real-time the impact and performances of your campaigns only over the last 24 hours. Your report is divided into different widgets detailing your campaign's success and errors. Each reporting dashboard can be modified by resizing or removing widgets."

Live reports, accessible from the Last 24 hrs tab, display events that took place within the past 24 hours, with a minimum time interval of two minutes from the event occurrence. In comparison, Customer Journey Analytics reports focus on events that occurred at least two hours ago and cover events over a selected time period.

Campaign live report can be accessed directly from your campaign with the **[!UICONTROL Live view]** button. 

The Campaign **[!UICONTROL Live report]** page will be displayed with the following tabs:

* [Campaign](#campaign-live)
* [Email](#email-live)
* [In-app](#inapp-live)
* [Push](#push-live)
* [SMS](#sms-live)
* [Web](#web-tab)
* [Direct mail](#direct-mail-tab)

The Campaign **[!UICONTROL Live report]** is divided into different widgets detailing your campaign's success and errors. Each widget can be resized and deleted if needed. For more information on this, refer to this [section](../reports/live-report.md#modify-dashboard).

For a detailed list of every metric available in Adobe Journey Optimizer, refer to [this page](live-report.md#list-of-components-live).

## Campaign tab {#campaign-live}

### Delivery {#delivery-live}

![](assets/campaign_live_statistics.png)

The **[!UICONTROL Campaign's Statistics]** KPIs serve as a comprehensive dashboard, offering a detailed breakdown of key metrics from the last 24 hours related to your campaign. This includes essential information such as the number of profiles and the actions delivered, providing a thorough understanding of your campaign's performance and engagement.

+++ Learn more on Campaign's Statistics metrics

* **[!UICONTROL Audience]**: Number of targeted profiles.

* **[!UICONTROL Actions delivered]**: Total number of unique times an action has been delivered.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

+++

<!--
### Experimentation tab (#experimentation-live)

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Experimentation]** tab details the main information relative to how each variant is performing and if there is was winner during the test.
-->

## Email tab {#email-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Email]** tab details the main information relative to the email sent in your campaign.

### Email - Sending performance {#email-sending-performance}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_sending_statistics"
>title="Email - Sending statistics"
>abstract="The Email - Sending statistics graph summarizes essential data about your email such as Targeted or Delivered from the last 24 hours."

![](assets/campaign_email_live_sending.png)

The **[!UICONTROL Email - Sending Performance]** offers a thorough overview of data related to emails sent within the past 24 hours. It provides insights into essential metrics such as delivered and bounces, allowing for a detailed examination of the email sending process. 

+++ Learn more on Email Sending performance metrics

* **[!UICONTROL Delivered]**: Number of emails successfully sent.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Retries]**: Number of emails in the queue for retries.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.
+++

### Email - Statistics

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_statistics"
>title="Email - Statistics"
>abstract="The Email - Statistics table provides data on profile activity for your email from the last 24 hours."

![](assets/campaign_email_live_statistics.png)

The **[!UICONTROL Sending metrics by Email]** table offers a comprehensive summary of the data from the past 24 hours. It outlines essential metrics, including the size of the targeted audience and the count of successfully delivered emails. This provides valuable insights into the effectiveness and reach of your email campaigns.

+++ Learn more on Email - Statistics metrics

* **[!UICONTROL Execution time]**: Start time of every execution of your recurring email. To target only one or multiple recurring emails, select it from the **[!UICONTROL Execution time]** drop-down. 

* **[!UICONTROL Targeted]**: Total number of messages processed during the sending process.

* **[!UICONTROL Excluded]**: Number of user profiles, excluded from the targeted profiles, who did not receive the message.

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Delivered]**: Number of messages successfully sent.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Opens]**: Number of times a message was opened.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on.

* **[!UICONTROL Unsubscribe]**: Number of clicks on the unsubscription link.

* **[!UICONTROL Spam complaints]**: Number of times a message was declared as spam or junk.

* **[!UICONTROL Retries]**: Number of emails in the queue for retries.
+++

### Email - Bounce categories and reasons {#bounce-categories}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_bounce_categories"
>title="Email - Bounce categories"
>abstract="The Email - Bounce categories graphs and table provide data on both temporary and permanent errors from the last 24 hours."

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_bounce_reasons"
>title="Email - Bounces reasons"
>abstract="The Email - Bounces reasons graphs and table contain the data available related to bounced messages from the last 24 hours."

![](assets/campaign_live_email_bounce_categories.png)

The **[!UICONTROL Bounce reasons]** and **[!UICONTROL Bounce categories]** widgets compile the available data from the last 24 hours related to bounced messages, providing detailed insights into the specific reasons and categories behind email bounces.

For more information on bounces, refer to the [Suppression list](../reports/suppression-list.md) page.

+++ Learn more on Email - Bounce categories and reasons metrics

* **[!UICONTROL Hard bounce]**: The total number of permanent errors, such as a wrong email address. This involves an error message that explicitly states that the address is invalid, such as Unknown user.

* **[!UICONTROL Soft bounce]**: The total number of temporary errors, such as a a full inbox.

* **[!UICONTROL Ignored]**: The total number of temporary, such as Out of office, or a technical error, for example if the sender type is postmaster.

+++

### Email - Performance by date {#email-performance-date}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_performance_bydate"
>title="Email - Performance by date"
>abstract="The Email - Performance by date graph presents comprehensive data from the last 24 hours regarding sent emails, offering insights into key metrics like delivered and bounces, allowing for a detailed analysis of the email sending process."

![](assets/campaign_email_live_performance.png)

The **[!UICONTROL Email - Performance by date]** widget offers a detailed overview of key information related to your messages, presented through a graph, providing insights into the performance trends over the last 24 hours.

+++ Learn more on Email - Performance by date and reasons metrics

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Delivered]**: Number of messages successfully sent.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Opens]**: Number of times a message was opened.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on.

* **[!UICONTROL Unsubscriptions]**: Number of clicks on the unsubscription link.

* **[!UICONTROL Spam complaints]**: Number of times a message was declared as spam or junk.

+++

### Error Reasons {#email-error-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_error_reasons"
>title="Email - Error reasons"
>abstract="The Email - Error reasons graphs and table enable you to identify the specific errors that occurred during the sending process in the last 24 hours."

![](assets/campaign_email_live_error.png)

The **[!UICONTROL Error Reasons]** graphs and tables provide insight into the specific errors that occurred during the sending process in the last 24 hours. This information is valuable for understanding the nature and frequency of errors.

### Excluded Reasons {#email-exclude-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_excluded_reasons"
>title="Email - Excluded reasons"
>abstract="The Excluded Reasons graphs and table illustrate the various factors that led to user profiles, excluded from the targeted audience, not receiving the message in the last 24 hours."

![](assets/campaign_email_live_excluded.png)

The **[!UICONTROL Excluded Reasons]** graphs and table offer a comprehensive perspective on the various factors that led to the exclusion of user profiles from the targeted audience in the last 24 hours. 

Refer to [this page](exclusion-list.md) for the comprehensive list of exclusion reasons.

### Email - Best recipient domain {#email-best-recipient}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_email_best_recipient"
>title="Email - Best recipient domain"
>abstract="The Email - Best recipient domain graph and table provide a detailed breakdown of the domains that recipients most frequently use to open the email, offering valuable insights into recipient behavior from the last 24 hours."

![](assets/campaign_email_live_recipient.png)

The **[!UICONTROL Email - Best recipient domain]** graph and table provide a thorough breakdown of the domains most frequently used by profiles to open your emails in the last 24 hours. This provides valuable insights into profile behavior, helping you understand preferred platforms.

### Email- Offers {#email-offers}

>[!NOTE]
>
>The Offers widgets and metrics are only available if a decision was inserted in an email. For more information on Decision Management, refer to this [page](../offers/get-started/starting-offer-decisioning.md).

The **[!UICONTROL Offers statistic]** and **[!UICONTROL Offers statistics over time]** widgets measure your offer's success and impact on your targeted audience. It details the main information relative to your message with KPIs.

+++ Learn more on Email - Offers metrics

* **[!UICONTROL Offer sent]**: Total number of sends for the offer.

* **[!UICONTROL Offer impression]**: Number of times the offer was opened in your emails.

* **[!UICONTROL Offer clicks]**: Number of times an offer was clicked on in your emails.

+++

## In-app tab {#inapp-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL In-app]** tab details the main information relative to the In-app messages sent in your campaign.

### In-app performance {#inapp-performance}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_inapp_performance"
>title="In-app performance"
>abstract="The In-app performance KPIs provide essential insights into your visitors' engagement with In-app messages in the last 24 hours."

The **[!UICONTROL In-app performance]** KPIs provide essential insights into your profiles' engagement with In-app messages in the last 24 hours, providing essential metrics to assess the effectiveness and impact of your In-app campaigns.

+++ Learn more on In-app performance metrics

* **[!UICONTROL Impressions]**: total number of In-app messages sent to all users.

* **[!UICONTROL Interactions]**: total number of engagements with your In-app message. This includes any actions taken by the users, such as clicks, dismissals, or any other interactions.

+++

### In-app summary {#inapp-summary}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_inapp_summary"
>title="In-app summary"
>abstract="The In-app summary graph illustrates the progression of your In-app impressions and interactions over the last 24 hours."

The **[!UICONTROL In-app summary]** graph illustrates the progression of your In-app impressions and interactions in the last 24 hours, providing a comprehensive overview of your In-app messages performance.

+++ Learn more on In-app summary metrics

* **[!UICONTROL Impressions]**: total number of In-app messages delivered to all users.

* **[!UICONTROL Interactions]**: total number of engagements with your In-app message. This includes any actions taken by the users, such as clicks, dismissals, or any other interactions.

+++

### Interactions by type {#inapp-interactions}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_inapp_interactions"
>title="Interactions by type"
>abstract="The Interactions by type graphs and table details how users interacted with your in-app message by tracking any click, dismiss, or interaction from the last 24 hours."

The **[!UICONTROL Interactions by type]** graphs and table provide a detailed account of how profiles interacted with your In-app message in the last 24 hours, tracking actions such as clicks, dismissals, or any other forms of engagement.

## Push notification tab {#push-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Push notification]** tab details the main information relative to the push notification sent in your campaign.

### Push notification - Sending performance {#push-sending-performance}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_sending_performance"
>title="Push notification - Sending performance"
>abstract="The Push Notification Sending Performance graph summarizes essential data about your push notification such as Errors or Delivered messages from the last 24 hours."

![](assets/campain_push_live_sending_performance.png)

The **[!UICONTROL Push notification sending performance]** graph offers a thorough overview of data related to push notifications sent within the past 24 hours. It provides insights into essential metrics such as delivered and bounces, allowing for a detailed examination of the push notifications sending process. 

+++ Learn more on Push notification - Sending performance metrics

* **[!UICONTROL Delivered]**: Number of messages successfully sent.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

+++

### Push notification - Statistics {#push-statistics}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_statistics"
>title="Push notification - Statistics"
>abstract="The Push Statistics table provides data on recipient activity for your push notification from the last 24 hours."

![](assets/campaign_push_live_statistics.png)

The **[!UICONTROL Push notification - Statistics]** table provides a concise summary of essential data related to your push notifications within the last 24 hours, including key metrics such as the number of targeted messages and number of successfully delivered messages.

+++ Learn more on Push notification - Statistics metrics

* **[!UICONTROL Execution time]**: Start time of every execution of your recurring push notification. To target only one or multiple recurring push notifications, select it from the **[!UICONTROL Execution time]** drop-down. 

* **[!UICONTROL Targeted]**: Total number of messages processed during the sending process.

* **[!UICONTROL Excluded]**: Number of user profiles, excluded from the targeted profiles, who did not receive the message.

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Delivered]**: Number of messages successfully sent.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Opens]**: Number of times a message was opened.

+++

### Push notification - Sending summary {#push-sending-summary}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_sending_summary"
>title="Push notification - Sending summary"
>abstract="The Push Notification Sending Summary graph displays the data available for sent push notifications from the last 24 hours."

The **[!UICONTROL Push notification - Statistics]** graph offers a dynamic representation, displaying an analysis of your push notifications activity in the last 24 hours. This graphical representation provides a comprehensive breakdown of sent push notifications.

+++ Learn more on Push notification - Sending summary metrics

* **[!UICONTROL Opens]**: Number of times your push notification was opened.

* **[!UICONTROL Actions]**: Total number of actions on the push notification delivered, e.g. button click or dismissal.

* **[!UICONTROL Bounces]**: Total of errors cumulated and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Delivered]**: Number of messages successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Errors]**: Total number of errors that occurred preventing it from being sent to profiles.

+++

### Push notification - Excluded reasons {#push-excluded}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_excluded_reasons"
>title="Push notification - Excluded reasons"
>abstract="The Excluded Reasons graphs and table illustrate the various factors that led to user profiles, excluded from the targeted audience, not receiving the message in the last 24 hours."

The **[!UICONTROL Excluded Reasons]** graphs and table display the different reasons that prevented user profiles, excluded from the targeted profiles, from receiving your push notifications in the last 24 hours.

Refer to [this page](exclusion-list.md) for the comprehensive list of exclusion reasons.

### Push notification - Error reasons {#push-error}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_error_reasons"
>title="Push notification - Error reasons"
>abstract="The Error Reasons graphs and table enable you to identify the specific errors that occurred the last 24 hours during the sending process."

The **[!UICONTROL Error Reasons]** table and graphs provide you with the capability to identify the specific errors that occurred during the sending process of your push notifications within the last 24 hours, offering detailed insights into any issues encountered along the way.

### Push notification - Breakdown by platform {#push-breakdown-platform}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_push_breakdown_platform"
>title="Push notification - Breakdown by platform"
>abstract="The Breakdown by Platform graphs and table provide a breakdown of the success of your push notifications in the last 24 hours based on the recipient's operating system."

The **[!UICONTROL Push notification - Breakdown by platform]** graph and table provide a detailed analysis of the success of your push notifications in the last 24 hors, offering insights based on your profile's operating system. This breakdown enhances your understanding of how well your push notifications perform across different platforms.

+++ Learn more on Push notification - Breakdown by platform metrics

* **[!UICONTROL Targeted]**: Total number of messages processed during the analysis.

* **[!UICONTROL Delivered]**: Number of messages successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Opens]**: Number of times your push notification was opened.

* **[!UICONTROL Actions]**: Total number of actions on the push notification delivered, e.g. button click or dismissal.

* **[!UICONTROL Bounces]**: Total of errors cumulated and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Errors]**: Total number of errors that occurred preventing it from being sent to profiles.

* **[!UICONTROL Excluded]**: Number of profiles which have been excluded by Adobe Journey Optimizer.

+++

## SMS tab {#sms-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL SMS]** tab details the main information relative to the SMS message sent in your campaign.

### SMS - Statistics {#sms-statistics}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_sms_statistics"
>title="SMS - Statistics"
>abstract="The SMS Sending Statistics table summarizes essential data about your SMS messages such as Targeted or Delivered messages from the last 24 hours."

![](assets/campaign_live_sms_statistics.png)

The **[!UICONTROL SMS - Statistics]** table provides a concise summary of essential data related to your SMS messages within the last 24 hours, encompassing key metrics such as the number of targeted messages and the count of successfully delivered messages.

+++ Learn more on SMS - Statistics metrics

* **[!UICONTROL Execution time]**: Start time of every execution of your recurring SMS message. To target only one or multiple recurring SMS messages, select it from the **[!UICONTROL Execution time]** drop-down. 

* **[!UICONTROL Targeted]**: Number of user profiles who qualify as target profiles.

* **[!UICONTROL Excluded]**: Number of user profiles, excluded from the targeted profiles, who did not receive the message.

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Clicks]**: Total number of URL visits.

+++

### SMS - Performance by date {#sms-perfomance-date}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_sms_performance"
>title="SMS - Performance by date"
>abstract="The SMS Performance by Date widget provides key information from the last 24 hours about your messages through a graphical representation."

![](assets/campaign_live_sms_performance_date.png)

The **[!UICONTROL SMS Performance by date]** widget offers a detailed overview of key information related to your messages, presented through a graph, providing insights into the performance trends over the last 24 hours.

+++ Learn more on SMS - Performance by date metrics

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Bounces]**: Total of errors cumulated during the sending process and automatic return processing.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

+++

### SMS - Error Reasons {#sms-error-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_sms_error_reasons"
>title="SMS - Error reasons"
>abstract="The SMS - Error Reasons graphs and table enable you to identify the specific errors that occurred in the last 24 hours during the sending process."

The **[!UICONTROL Excluded Reasons]** graphs and table allow you to identify the specific errors that occurred during the sending process of your SMS messages within the last 24 hours, facilitating a thorough analysis of any issues encountered.

### SMS - Excluded Reasons {#sms-excluded-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_sms_excluded_reasons"
>title="SMS - Excluded reasons"
>abstract="The Excluded Reasons graphs and table illustrate the various factors that led to user profiles, excluded from the targeted audience, not receiving the message in the last 24 hours."

![](assets/campaign_live_sms_excluded.png)

The **[!UICONTROL Excluded Reasons]** graphs and table visually depict the diverse factors that led to the exclusion of user profiles from the targeted audience, preventing them from receiving your SMS messages in the last 24 hours.

Refer to [this page](exclusion-list.md) for the comprehensive list of exclusion reasons.

### SMS - Bounces reasons {#sms-bounces-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_sms_bounces_reasons"
>title="SMS - Bounces reasons"
>abstract="The Bounces Reasons graphs and table contain the data available from the last 24 hours related to bounced messages."

The **[!UICONTROL Bounces Reasons]** graphs and table provide a comprehensive overview of data related to bounced SMS messages, delivering valuable insights into the specific reasons behind instances of SMS message bounces in the last 24 hours.

## Web tab {#web-tab}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Web]** tab details the main information relative to your Web pages.

### Web performance {#web-performance}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_web_performance"
>title="Web performance"
>abstract="The Web Performance KPIs provide comprehensive information about your visitors' engagement with your web experiences from the last 24 hours."

![](assets/campaign_live_web_performance.png)

The **[!UICONTROL Web performance]** KPIs offer comprehensive insights into your visitors' engagement with your web pages in the last 24 hours, encompassing key metrics such as Impressions and Interactions.

+++ Learn more on Web performance metrics

* **[!UICONTROL Impressions]**: total number of web experiences delivered to all users.

* **[!UICONTROL Interactions]**: total number of engagements with your Web page. This includes any actions taken by the users, such as clicks or any other interactions.

+++ 

### Web summary {#web-summary}

![](assets/campaign_live_web_summary.png)

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_web_summary"
>title="Web summary"
>abstract="The Web Summary graph illustrates the progression of your web experiences, including impressions, unique impressions, and interactions, from the last 24 hours."

The **[!UICONTROL Web summary]** graph shows the evolution of your web experiences (impressions, unique impressions and interactions) in the last 24 hours.

+++ Learn more on Web summary metrics

* **[!UICONTROL Impressions]**: total number of web experiences delivered to all users.

* **[!UICONTROL Interactions]**: total number of engagements with your Web page. This includes any actions taken by the users, such as clicks or any other interactions.

+++ 

### Interactions by element {#web-interactions}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_web_interactions"
>title="Interactions by element"
>abstract="The Interactions by Element table provides key information regarding your visitors' engagement with different elements on your web pages in the last 24 hours."

The **[!UICONTROL Interactions by element]** table presents comprehensive information regarding your visitors' engagement with the various elements on your web pages in the last 24 hours, offering valuable insights into user interactions and preferences.

## Direct mail tab {#direct-mail-tab}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Direct mail]** tab details the main information relative to your Direct mail.

### Direct Mail - Sending statistics {#direct-mail-sending}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_direct_sending_statistics"
>title="Direct Mail - Sending statistics"
>abstract="The Direct Mail Sending Statistics table summarizes essential data from the last 24 hours about your Direct Mail messages such as Targeted or Delivered messages."

![](assets/campaign_live_directmail_statistics.png)

The **[!UICONTROL Direct Mail - Sending statistics]** table provides a concise summary of essential data related to your Direct Mail messages, encompassing key metrics such as the number of targeted messages and the count of successfully delivered messages within the last 24 hours.

+++ Learn more on Direct Mail - Sending statistics metrics

* **[!UICONTROL Targeted]**: Number of user profiles who qualify as target profiles.

* **[!UICONTROL Sent]**: Total number of sends.

* **[!UICONTROL Errors]**: Total number of errors that occurred during the sending process preventing it from being sent to profiles.

* **[!UICONTROL Excluded]**: Number of user profiles, excluded from the targeted profiles, who did not receive your Direct mail.

+++

### Direct Mail - Error reasons {#direct-mail-error-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_direct_error_reasons"
>title="Direct Mail - Error reasons"
>abstract="The Direct Mail - Error Reasons graphs and table enable you to identify the specific errors that occurred in the last 24 hours."

![](assets/campaign_live_error_reasons.png)

The **[!UICONTROL Direct Mail - Error reasons]** graphs and table provide the means to identify specific errors that occurred during the sending process of your direct mail messages, allowing for a detailed analysis of any issues encountered in the last 24 hours.

### Direct Mail - Excluded reasons {#direct-mail-excluded-reasons}

>[!CONTEXTUALHELP]
>id="ajo_campaign_live_direct_excluded_reasons"
>title="Direct Mail - Excluded reasons"
>abstract="The Direct Mail Excluded Reasons graphs and table illustrate the various factors that led to user profiles, excluded from the targeted audience, not receiving the message in the last 24 hours."

![](assets/campaign_live_directmail_excluded.png)

The **[!UICONTROL Direct Mail - Excluded reasons]** graphs and table visually illustrate the various factors that resulted in the exclusion of user profiles from the targeted audience, preventing them from receiving your direct mail messages in the last 24 hours.

Refer to [this page](exclusion-list.md) for the comprehensive list of exclusion reasons.

## Additional resources

* [Get started with campaigns](../campaigns/get-started-with-campaigns.md)
* [Create a campaign](../campaigns/create-campaign.md)
* [Create API-triggered campaigns](../campaigns/api-triggered-campaigns.md)
* [Modify or stop a campaign](../campaigns/modify-stop-campaign.md)
* [Campaign report](campaign-global-report-cja.md)
