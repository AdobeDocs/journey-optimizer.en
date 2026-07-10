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
TQID: https://experienceleague.adobe.com/7EdZZJgxpZA2AtSo-lMpMEDV6C9zk78mmvNVhe5KXcw
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
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b4dd41a7-ccf8-4e9d-918e-acaab534a307
    internal-label: Data quality
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Get started with deliverability {#manage-deliverability}

>[!BEGINSHADEBOX]

**On this page:** Learn deliverability best practices for Adobe Journey Optimizer, including reducing complaint rates, leveraging suppression lists, establishing sender reputation, implementing DMARC, and understanding feedback loops.

>[!ENDSHADEBOX]

Deliverability is a measure of the success of your deliveries reaching your recipients inboxes.

>[!NOTE]
>
>For customers licensing Healthcare Shield, Adobe uses Transport Layer Security (TLS) 1.2 to secure the data exchange between users' systems (recipients) and Journey Optimizer (sender). If the receiving mail server doesn't support TLS 1.2, customers will experience deliverability issues including email bouncing back to the originating sender.

**Email deliverability** refers to the set of characteristics that determine a message's ability to reach its destination, via a personal e-mail address, within a short time, and with the expected quality in terms of content and format. These characteristics fall into four main categories: data quality, message and content, sending infrastructure, and reputation. Together, they form the foundation of a successful email deliverability program.

The **deliverability rate** is the number of messages that hit the recipients' inboxes compared to the number of messages that were delivered. It depends on numerous factors, particularly:

* Limited spam complaints
* Low hard bounce rates
* Quality of the targeted addresses 
* Message content
* Sender reputation

To optimize the deliverability of your [!DNL Journey Optimizer] experiences, we recommend using the best practices listed in this section. Deliverability problems are generally linked to protection against spam implemented by Internet service providers (ISPs) and mail server administrators.

For a deeper dive on what deliverability is and to learn more on key deliverability terms, concepts, and approaches, refer to the [Adobe Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/introduction.html){target="_blank"}.

## Reduce complaint rate {#reduce-complaint-rate}

ISPs usually have a prominent means of reporting a received message as spam. This makes it possible to identify unreliable sources. By rapidly honoring opt-out requests and therefore showing that you are a reliable sender, you can reduce complaint rates. [Learn more about opt-out management](../privacy/opt-out.md#opt-out-decision-management)

As a general rule, do not try to get in the way of recipients who want to opt-out by requiring them to fill out fields such as their email address or name, for example. The unsubscription landing page should have one validation button only.

Pay extra care when requesting additional confirmation: a user may have two email addresses redirected to the same box (for example: firstname.lastname@club.com and firstname.lastname@internet-club.com). If the profile is able to remember the first address only and wishes to unsubscribe via a message sent to the other one, the form will refuse this because the encrypted identifier and the email address entered will not match.

## Leverage suppression lists {#suppression-lists}

[!DNL Journey Optimizer] manages a suppression list that gathers spam complaints, hard bounces, and soft bounces that occur consistently.

To protect your deliverability, the recipients whose addresses are on the suppression list are excluded by default from all future deliveries, because sending to these contacts could hurt your sending reputation.

[Learn more about the suppression list](suppression-list.md)

## Use monitoring tools {#monitoring-tools}

Use the reporting features offered by [!DNL Journey Optimizer] to monitor your deliverability.

The campaign and journey reports allow you to check how your deliveries are performing through a set of real-time indicators. Amongst other things, they display:

* The number of messages that are successfully executed, sent and delivered.
* The number of messages that have been opened and the number of messages/links that have been clicked.

Learn more about [live report](../reports/live-report.md) and [all time report](../reports/report-gs-cja.md)

## Adapt message content {#adapt-message-content}

To a lesser degree, the content of certain messages may be detected as spam.

To improve your deliverability rate and make sure that your emails reach your recipients, follow the principles below when designing your message content:

* **Sender name and address**: The address has to explicitly identify the sender. The domain has to be owned by and registered to the sender. The domain registry must not be privatized.

* **Unsubscribe link and landing page**: The unsubscribe link is essential. It must be visible and valid, and the form must be functional.

[Learn more about designing email content](../email/get-started-email-design.md)

## Establish your reputation as a sender {#reputation}

If you recently moved to another email service provider, IP address, or email domain or subdomain, you need to establish your reputation as a sender. Otherwise, your deliveries might be blocked or moved to the spam folder of the recipients' mailbox.

When sending email on a brand new IP address, you can now easily perform IP warmup workflows directly from the user interface. 

Adobe Journey Optimizer offers a standardized and efficient way to warm up your IP adresses that follows the best practices for optimal deliverability.

[Learn more about IP warmup plans](../configuration/ip-warmup-gs.md)

<!--To warm up your IP, you can gradually ramp up the number of your deliveries. Learn more in this [use case](../building-journeys/ramp-up-deliveries-uc.md).-->

## Implement DMARC {#dmarc}

To help you mitigate the risk of legitimate emails being marked as spam or rejected, and prevent deliverability issues, [!DNL Journey Optimizer] allows you to set up DMARC record for all the subdomains that you delegate to Adobe.

Domain-based Message Authentication, Reporting, and Conformance (DMARC) is an email authentication method that allows domain owners to protect their domain from unauthorized use by malicious actors.

[Learn more about DMARC record](../configuration/dmarc-record.md)

## Know about feedback loops {#feedback-loops}

>[!CONTEXTUALHELP]
>id="ajo_surface_dynamic_subdomain_list"
>title="Some subdomains may be unavailable"
>abstract="Certain subdomains are currently unavailable for selection due to pending feedback loop registration. This process may take up to 10 business days. Once complete, you can choose from all available subdomains."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/delegate-subdomains/about-subdomain-delegation" text="Get started with subdomain delegation"

A feedback loop (FBL) is a service offered by some ISPs that allows the email sender to be automatically notified when the user who receives an email chooses to mark it as spam (also known as a "complaint").

After an end user generates a complaint which is sent back to Adobe by the ISP, the email address is automatically added to the [suppression list](../reports/suppression-list.md) and excluded from future deliveries. Indeed, sending emails to users who marked them as spam negatively impacts the sender reputation and may cause deliverability issues. [Learn more about spam complaints](../reports/suppression-list.md#spam-complaints)

>[!IMPORTANT]
>
>Not all ISPs provide a traditional FBL, such as Gmail. Gmail does not offer individual level feedback, and it cannot be used to track spam complaints to individual recipients, focusing instead on aggregate level reporting within their Google Postmaster Tools. [Learn more](#providers-no-fbl)


All Adobe customers are automatically enrolled in the traditional FBLs of the ISPs listed below.

+++ ISPs providing a traditional FBL:

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

+++

Adobe performs regular audits to ensure the latest available FBLs are added.

### Providers without per-recipient FBL {#providers-no-fbl}

Not all ISPs provide a traditional FBL. Several major mailbox providers do not return per-recipient spam complaints, which means that the absence of an entry in the suppression list is expected for recipients using those providers.

| Mailbox provider | Per-recipient complaint FBL? |
|---|---|
| **Gmail / Google Workspace** | No — aggregate reporting only via Google Postmaster Tools (Feedback-ID; not per-recipient). [Learn more](https://support.google.com/a/answer/6254652?hl=en){target="_blank"} |
| **Apple iCloud** (icloud.com, me.com, mac.com) | No — [Learn more](https://support.apple.com/en-us/102322){target="_blank"} |
| **Corporate Microsoft 365 / Exchange Online** | No — the Junk Mail Reporting Program (JMRP) covers the consumer Outlook.com network only; tenant junk reports from corporate M365 environments do not return to the sender. [Learn more](https://learn.microsoft.com/en-us/answers/questions/5787589/does-the-junk-mail-reporting-program-(jmrp)-send-c){target="_blank"} |

Together, these providers represent the majority of consumer and business inboxes. Because none of them return per-recipient complaints, a recipient using any of these services who marks a message as spam will **not** automatically appear in the suppression list.

## Use SMTP relay {#smtp-relay}

[!DNL Journey Optimizer] uses Adobe-owned Mail Transfer Agents (MTAs) and IPs to deliver your emails to the Internet Service Providers (ISPs). However, in some cases you may want to route final email deliveries through your own MTAs and IPs, or to perform final validations on the emails before sending them to your recipients.

In this cas, you can choose to have your emails relayed to SMTP servers hosted by your organization instead of being sent directly from Journey Optimizer to ISPs. 

>[!AVAILABILITY]
>
>The SMTP relay capacity is available on demand - contact your Adobe representative.
