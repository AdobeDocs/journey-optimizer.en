---
solution: Journey Optimizer
product: journey optimizer
title: Suppression list
description: Learn how to use the suppression list is
feature: Deliverability
topic: Content Management
role: Admin
level: Intermediate, Experienced
exl-id: a4653378-b70f-454c-a446-ab4a14d2580a
---
# Suppression list {#suppression-list}

A suppression list consists of addresses and domains that you want to exclude from your deliveries, because sending to these contacts could hurt your sending reputation and delivery rates.

The [!DNL Journey Optimizer] suppression list is managed at your own environment level, i.e. for a given sandbox.

It gathers email addresses and domains that are suppressed across all mailings in a single client environment, meaning specific to an organization ID associated with a sandbox ID.

>[!NOTE]
>
>Adobe keeps an updated list of known bad addresses which have been proven to be detrimental to engagement and mailing reputation, and ensures emails are not delivered to them. This list is managed in a global suppression list which is common across all Adobe customers. The addresses and domain names contained in the global suppression list are hidden. Only the number of excluded recipients is indicated in the delivery reports.

In addition, you can leverage Journey Optimizer **Suppression REST API** to control your outgoing messages using suppression and allow lists. [Learn how to work with the Suppression REST API](https://developer.adobe.com/journey-optimizer-apis/references/suppression/){target="_blank"}

## Why a suppression list? {#why-suppression-list}

To control the email messages that are received by their inbox owners and ensure they only receive those they want, Internet service providers (ISPs) and commercial spam filters have their proprietary algorithms to track the overall reputation of email senders based on the IP addresses and sending domain(s) they use.

If you do not take their feedback (such as spam complaints, bounces, etc.) into account, they will rate your reputation down. The suppression list helps you with honoring the ISPs' feedback.

The recipients whose email addresses are suppressed are automatically excluded from message delivery. This will speed up deliveries, as the error rate has a significant effect on delivery speed.

## What's on the suppression list? {#what-s-on-suppression-list}

Addresses are added to the suppression list as follows:

* All **hard bounces** and **spam complaints** automatically send the corresponding addresses to the suppression list after a single occurrence. Learn more on spam complaints in [this section](#spam-complaints).

* **Soft bounces** do not immediately send an address to the suppression list, but they increment an error counter. Several [retries](../configuration/retries.md) are then performed, and when the error counter reaches the threshold, the address is added to the suppression list.

* You can also [**manually** add an address or a domain](../configuration/manage-suppression-list.md#add-addresses-and-domains) to the suppression list.

Learn more on hard bounces and soft bounces in [this section](#delivery-failures).

>[!NOTE]
>
>Unsubscribed users' addresses cannot be sent to the suppression list as they are not receiving emails from [!DNL Journey Optimizer]. Their choice is handled at the Experience Platform level. Learn more on [opting-out](../privacy/opt-out.md).

For each address, the basic reason for being suppressed and the suppression category (soft, hard, etc.) are displayed in the suppression list. Learn more on accessing and managing the suppression list in [this section](../configuration/manage-suppression-list.md).

>[!NOTE]
>
>The profiles with **[!UICONTROL Suppressed]** status are excluded during the message sending process. Therefore, while the **Journey reports** will show these profiles as having moved through the journey ([Read Audience](../building-journeys/read-audience.md) and [message activities](../building-journeys/journeys-message.md)), the **Email reports** will not include them in the **[!UICONTROL Sent]** metrics as they are filtered out prior to email sending.
>
>Learn more on the [Live Report](../reports/live-report.md) and [Global Report](../reports/global-report.md). To find out the reason for all exclusion cases, you can use the [Adobe Experience Platform Query Service](https://experienceleague.adobe.com/docs/experience-platform/query/api/getting-started.html){target="_blank"}.

### Delivery failures {#delivery-failures}

There are two types of errors when a delivery fails:

* **Hard bounce**. A hard bounce indicates an invalid email address (i.e. an email address that does not exist). This involves a bounce message from the receiving email server that explicitly states that the address is invalid.
* **Soft bounce**. This is a temporary email bounce that occurred for a valid email address.

A **hard bounce** automatically adds the email address to the suppression list.

A **soft bounce** <!--or an **ignored** error--> that occurs too many times also sends the email address to the suppression list after several retries. [Learn more on retries](../configuration/retries.md)

If you continue sending to these addresses, it may affect your delivery rates, because it tells ISPs that you may not be following email address list maintenance best practices, and therefore may not be a trustworthy sender.

### Spam complaints {#spam-complaints}

The suppression list collects email addresses that mark your message as spam. For example, if someone writes to a customer service requesting to never receive mail again from you, the email address of that person will be suppressed across your instance and you won't be able to deliver to that address anymore.

Sending to recipients after they submit a spam complaint may have a huge impact on your sending reputation, because it informs ISPs that you may send unwanted emails and may not listen to your recipients.

This could lead to your IP address or sending domain being blocked, which can be avoided with these addresses being on the suppression list.

Some ISPs offer a feedback loop (FBL) that allows the email sender to be automatically notified when the user who receives an email chooses to mark it as spam. [Learn more](deliverability.md#feedback-loops)
