---
solution: Journey Optimizer
product: journey optimizer
title: Get started with deliverability
description: Learn deliverability guidelines
feature: Deliverability
topic: Content Management
role: Admin
level: Intermediate, Experienced
exl-id: 8f33dda7-9bd5-4293-8d0d-222205cbc7d5
---
# Get started with deliverability {#manage-deliverability}

Deliverability is a measure of the success of your deliveries reaching your recipients inboxes.

>[!NOTE]
>
>For customers licensing Healthcare Shield, Adobe uses Transport Layer Security (TLS) 1.2 to secure the data exchange between users' systems (recipients) and Journey Optimizer (sender). If the receiving mail server doesn't support TLS 1.2, customers will experience deliverability issues including email bouncing back to the originating sender.

**Email deliverability** refers to the set of characteristics that determine a message's ability to reach its destination, via a personal e-mail address, within a short time, and with the expected quality in terms of content and format. These characteristics fall into four main categories: data quality, message and content, sending infrastructure, and reputation. Together, they form the foundation of a successful email deliverability program.

The **deliverability rate** is the number of messages that hit the recipients' inboxes compared to the number of messages that were delivered. It depends on numerous factors, particularly:

* Limited spam complaints
* Low hard bounce rates
* Quality of the addresses targeted
* Message content
* Sender reputation

To optimize the deliverability of your [!DNL Journey Optimizer] experiences, we recommend using the best practices listed in this section. Deliverability problems are generally linked to protection against spam implemented by Internet service providers (ISPs) and mail server administrators.

For a deeper dive on what deliverability is and to learn more on key deliverability terms, concepts, and approaches, refer to the [Adobe Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/introduction.html){target="_blank"}.

## Reduce complaint rate {#reduce-complaint-rate}

ISPs usually have a prominent means of reporting a received message as spam. This makes it possible to identify unreliable sources. By rapidly honoring opt-out requests and therefore showing that you are a reliable sender, you can reduce complaint rates. [Learn more about opt-out management](../privacy/opt-out.md#opt-out-management)

As a general rule, do not try to get in the way of recipients who want to opt-out by requiring them to fill out fields such as their email address or name, for example. The unsubscription landing page should have one validation button only.

Pay extra care when requesting additional confirmation: a user may have two email addresses redirected to the same box (for example: firstname.lastname@club.com and firstname.lastname@internet-club.com). If the profile is able to remember the first address only and wishes to unsubscribe via a message sent to the other one, the form will refuse this because the encrypted identifier and the email address entered will not match.

## Leverage suppression lists {#suppression-lists}

[!DNL Journey Optimizer] manages a suppression list that gathers spam complaints, hard bounces, and soft bounces that occur consistently.

To protect your deliverability, the recipients whose addresses are on the suppression list are excluded by default from all future deliveries, because sending to these contacts could hurt your sending reputation.

[Learn more about the suppression list](suppression-list.md)

## Use monitoring tools {#monitoring-tools}

Use the features offered by [!DNL Journey Optimizer] to monitor your deliverability.

The **[!UICONTROL Executions]** tab of the message list allows you to check how your deliveries are performing through a set of real-time indicators. Amongst other things, this tab displays:
* The number of messages that are successfully executed, sent and delivered.
* The number of messages that have been opened and the number of messages/links that have been clicked.

## Adapt message content {#adapt-message-content}

To a lesser degree, the content of certain messages may be detected as spam.

To improve your deliverability rate and make sure that your emails reach your recipients, follow the principles below when designing your message content:

* **Sender name and address**: The address has to explicitly identify the sender. The domain has to be owned by and registered to the sender. The domain registry must not be privatized.

* **Unsubscribe link and landing page**: The unsubscribe link is essential. It must be visible and valid, and the form must be functional.

[Learn more about designing email content](../email/get-started-email-design.md)

## Establish your reputation as a sender {#reputation}

If you recently moved to another email service provider, IP address, or email domain or subdomain, you need to establish your reputation as a sender. Otherwise, your deliveries might be blocked or moved to the spam folder of the recipients' mailbox.

<!--To warm up your IP, you can gradually ramp up the number of your deliveries. Learn more in this [use case](../building-journeys/ramp-up-deliveries-uc.md).-->

## Implement DMARC {#dmarc}

To help you mitigate the risk of legitimate emails being marked as spam or rejected, and prevent deliverability issues, [!DNL Journey Optimizer] allows you to set up DMARC record for all the subdomains that you delegate to Adobe.

Domain-based Message Authentication, Reporting, and Conformance (DMARC) is an email authentication method that allows domain owners to protect their domain from unauthorized use by malicious actors.

[Learn more on DMARC record](../configuration/dmarc-record.md)

## Know about feedback loops {#feedback-loops}

A feedback loop (FBL) is a service offered by some ISPs that allows the email sender to be automatically notified when the user who receives an email chooses to mark it as spam (also known as a "complaint").

After an end user generates a complaint which is sent back to Adobe by the ISP, the email address is automatically added to the [suppression list](../reports/suppression-list.md) and excluded from future deliveries. Indeed, sending emails to users who marked them as spam negatively impacts the sender reputation and may cause deliverability issues. [Learn more on spam complaints](../reports/suppression-list.md#spam-complaints)

>[!IMPORTANT]
>
>Not all ISPs provide a traditional FBL, such as Gmail. Gmail does not offer individual level feedback, and it cannot be used to track spam complaints to individual recipients, focusing instead on aggregate level reporting within their Google Postmaster Tools. [Learn more](https://support.google.com/a/answer/6254652?hl=en){target="_blank"}

All Adobe customers are automatically enrolled in the traditional FBLs of the following ISPs:

* 1&1

* AOL

* BlueTie

* Comcast

* Fastmail

* Gandi

* Italia Online

* La Poste

* Liberty Global (Chello, UPC, Unity Media)

* Locaweb

* Mail.RU

* Microsoft

* OpenSRS

* Rackspace

* SEZNM

* SFR

* SilverSky

* Swisscom

* Synacor

* Telecom Italia

* Telenet

* Telenor

* Telstra

* Terra

* UOL

* Virgin Media

* Yahoo

* Ziggo

Adobe audits these FBLs regularly to ensure the latest available FBLs are added.
