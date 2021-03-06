---
title: Campaign live report
description: Learn how to use data from the Campaign live report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
exl-id: 925494b6-e08a-4bd3-8a2f-96a5d9cbc387
---
# Campaign live report {#campaign-live-report}

Campaign live report can be accessed directly from your campaign with the **[!UICONTROL Live view]** button. 

The Campaign **[!UICONTROL Live report]** page will be displayed with the following tabs:

* [Campaign](#campaign-live)
* [Email](#email-live)
* [Push](#push-live)

The Campaign **[!UICONTROL Live report]** is divided into different widgets detailing your campaign's success and errors. Each widget can be resized and deleted if needed. For more information on this, refer to this [section](../reports/live-report.md#modify-dashboard).

## Campaign tab {#campaign-global}

### Delivery {#delivery-global}

The **[!UICONTROL Campaign Statistics]** widget details the main information relative to your campaign:

* **[!UICONTROL Entered profiles]**: Number of profiles who started the journey.

<!--
### Experimentation tab (#experimentation-live)

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Experimentation]** tab details the main information relative to how each variant is performing and if there is was winner during the test.
-->
## Email tab {#email-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Email]** tab details the main information relative to the email deliveries sent in your campaign.

The **[!UICONTROL Email Sending Statistics]** widget details the main information relative to your message:

* **[!UICONTROL Delivered]**: Number of messages successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Bounces]**: Total of errors cumulated during delivery and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Errors]**: Total number of errors that occurred during a delivery preventing it from being sent to profiles.

The **[!UICONTROL Sending metrics by Email]** table and **[!UICONTROL Email Summary]** graph details the success of your delivery:

* **[!UICONTROL Sent]**: Total number of sends for the delivery.

* **[!UICONTROL Delivered]**: Number of messages successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Bounces]**: Total of errors cumulated during delivery and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Errors]**: Total number of errors that occurred during a delivery preventing it from being sent to profiles.

* **[!UICONTROL Opens]**: Number of times a message was opened in a delivery.

* **[!UICONTROL Clicks]**: Number of times a content was clicked in a delivery.

* **[!UICONTROL Unsubscribe]**: Number of clicks on the unsubscription link.

* **[!UICONTROL Spam complaints]**: Number of times a message was declared as spam or junk.

The **[!UICONTROL Bounce Reasons]**, **[!UICONTROL Bounce categories]** and **[!UICONTROL Hard and bounce - by Email]** widgets contain the data available related to bounced messages, such as:

* **[!UICONTROL Hard bounce]**: The total number of permanent errors, such as a wrong email address. This involves an error message that explicitly states that the address is invalid, such as Unknown user.

* **[!UICONTROL Soft bounce]**: The total number of temporary errors, such as a a full inbox.

* **[!UICONTROL Ignored]**: The total number of temporary, such as Out of office, or a technical error, for example if the sender type is postmaster.

The **[!UICONTROL Error Reasons]** and **[!UICONTROL Exclude Reasons]** graphs and tables allow you to see which error and exclusions occurred during your delivery.

The **[!UICONTROL Email - Top recipient domain]** graph and table details which domains are the most used by recipients to open the email.

## Push tab {#push-live}

From your Campaign **[!UICONTROL Live report]**, the **[!UICONTROL Push]** tab details the main information relative to the push deliveries sent in your campaign.

**[!UICONTROL Push notification sending performance]**, **[!UICONTROL Push notification summary]** and **[!UICONTROL Sending metrics - by Push]** widgets details the main information relative to your message:

* **[!UICONTROL Sent]**: Total number of sends for the delivery.

* **[!UICONTROL Delivered]**: Number of messages successfully sent, in relation to the total number of sent messages.

* **[!UICONTROL Bounces]**: Total of errors cumulated during delivery and automatic return processing in relation to the total number of sent messages.

* **[!UICONTROL Errors]**: Total number of errors that occurred during a delivery preventing it from being sent to profiles.

* **[!UICONTROL Opens]**: Number of times a message was opened in a delivery.

* **[!UICONTROL Actions]**: Total number of actions on the push notification delivered, e.g. button click or dismissal.

* **[!UICONTROL Engagements]**: Total number of opens and actions for this push notification, i.e. if the profile opened the push or if a button was clicked on.

The **[!UICONTROL Error Reasons]** and **[!UICONTROL Exclude Reasons]** graphs and tables allow you to see which error and exclusions occurred during your delivery.

The **[!UICONTROL Sending statistics - Failed]** widget allows you to see how many errors and bounces occurred.

The **[!UICONTROL Tracking by platform]**, **[!UICONTROL Sending by platform]** and **[!UICONTROL Breakdown by platform]** graphs and tables details the success of your push notification depending on the operational system.

## Additional resources

* [Get started with campaigns](get-started-with-campaigns.md)
* [Create a campaign](create-campaign.md)
* [Create API-triggered campaigns](api-triggered-campaigns.md)
* [Modify or stop a campaign](modify-stop-campaign.md)
* [Campaign global report](campaign-global-report.md)
