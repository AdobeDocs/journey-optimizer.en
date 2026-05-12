---
solution: Journey Optimizer
product: journey optimizer
title: Get started with [!DNL Journey Optimizer] channels configuration
description: Learn more about [!DNL Journey Optimizer] channels configuration
role: Admin, Developer
level: Intermediate, Experienced
exl-id: 0964a484-f957-4aae-a571-61b2a1615026
feature: Application Settings
topic: Administration
keywords: configuration, configure, messages, channel, sandbox, optimizer
TQID: https://experienceleague.adobe.com/zHp3C6KVKfRsQbi4B710ACFuMQhGuVxjaNIrXkxwhMc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c343082f-e963-4f57-a96b-b64d27f8118e
    internal-label: IP warmup plans
  - id: cf64c7f6-7428-4ae5-b158-8df9771f38f4
    internal-label: Channel configurations
  - id: e23d48b5-7858-4d45-9c56-9e2b4be8500e
    internal-label: Business rules
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
  - id: e5329d1b-e590-4e24-a3fb-ef3fe0f2c721
    internal-label: Subdomains
  - id: efb19423-4da4-4fd1-88d8-5ee8c71ae766
    internal-label: Application settings
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e9001ce2-5245-4a8e-8601-dd958009072f
    internal-label: Web experience
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Get started with channels configuration {#start-optimizer-configuration}

>[!CONTEXTUALHELP]
>id="ajo_channels_rate_controls"
>title="Rate controls for channels"
>abstract="Rate controls for channels"

When accessing [!DNL Journey Optimizer] for the first time, you are provisioned a production sandbox and allocated a certain number of IPs depending on your contract.

To be able to send messages, you need to go through the configuration steps listed below:

1. As an [Adobe Journey Optimizer system administrator](../start/path/administrator.md), define your channel-specific configurations. Learn how to set up these configurations in the following pages:

    <table style="table-layout:fixed"><tr style="border: 0;">
    <td><a href="../email/get-started-email-config.md"><img alt="email" src="../channels/assets/do-not-localize/email.png"></a>
    <div align="center"><a href="../email/get-started-email-config.md"><strong>Email</strong></a></div></td>
    <td><a href="../sms/sms-configuration.md"><img alt="sms" src="../channels/assets/do-not-localize/sms.png"></a>
    <div align="center"><a href="../sms/sms-configuration.md"><strong>SMS</strong></a></div></td>
    <td><a href="../push/push-configuration.md"><img alt="push" src="../channels/assets/do-not-localize/push.png"></a>
    <div align="center"><a href="../push/push-configuration.md"><strong>Push notification</strong></a></div></td>
    <td><a href="../direct-mail/direct-mail-configuration.md"><img alt="direct mail" src="../channels/assets/do-not-localize/direct-mail.jpg"></a>
    <div align="center"><a href="../direct-mail/direct-mail-configuration.md"><strong>Direct mail</strong></a></div></td>
    </tr></table>

    <table style="table-layout:fixed"><tr style="border: 0;">
    <td><a href="../in-app/inapp-configuration.md"><img alt="in-app" src="../channels/assets/do-not-localize/inapp.jpg"></a>
    <div align="center"><a href="../in-app/inapp-configuration.md"><strong>In-app</strong></a></div></td>
    <td><a href="../web/web-configuration.md"><img alt="web" src="../channels/assets/do-not-localize/web.jpg"></a>
    <div align="center"><a href="../web/web-configuration.md"><strong>Web</strong></a></div></td>
    <td><a href="../code-based/code-based-configuration.md"><img alt="code-based experience" src="../channels/assets/do-not-localize/code.png"></a>
    <div align="center"><a href="../code-based/code-based-configuration.md"><strong>Code-based experience</strong></a></div></td>
    <td><a href="../content-card/content-card-configuration-prereq.md"><img alt="content cards" src="../channels/assets/do-not-localize/cards.png"></a>
    <div align="center"><a href="../content-card/content-card-configuration-prereq.md"><strong>Content cards</strong></a></div></td>
    </tr></table>

    For additional channels, refer to: [iOS Live activities](../mobile-live/mobile-live-configuration.md), [WhatsApp](../whatsapp/whatsapp-configuration.md), and [LINE](../line/line-configuration.md).

    >[!NOTE]
    >
    >For mobile channels, the [Guided channel setup](set-mobile-config.md) facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to start with campaign and journey creation.

1. Once done, you must configure all the technical parameters required to deliver messages by creating **channel configurations**. [Learn more about channel configurations](channel-surfaces.md)

1. Depending on the channels you are using, your environments and your needs, you must also perform the following steps:

    * Subdomain configuration and delegation for your channels, such as [emails](about-subdomain-delegation.md), [SMS](../sms/sms-subdomains.md), [landing pages](../landing-pages/lp-subdomains.md), and [web experiences](../web/web-delegated-subdomains.md).

    * Set up IP warmup plans for optimal deliverability. [Learn more](ip-warmup-gs.md)

    * Define an allowed list for email sending. [Learn more](allow-list.md)

    * Manage the number of days during which retries are performed before sending email addresses to the suppression list. [Learn more](manage-suppression-list.md)

    * Enable the **BCC email option** to keep a copy of messages sent to individuals. [Learn more](archiving-support.md#enable-bcc)

    * Configure **business rules** to avoid over-solicitating your recipients. [Learn more](../conflict-prioritization/rule-sets.md)

    * Determine which email address and/or phone number to use in priority for your recipients when several addresses/numbers are available in Adobe Experience Platform. [Learn more](primary-email-addresses.md)

## Additional resources

* **[Configure channel surfaces](channel-surfaces.md)** - Learn how to set up and manage channel surfaces for email, push, SMS, and other channels.
* **[Subdomain delegation](delegate-subdomain.md)** - Understand how to delegate subdomains to Adobe for email deliverability and branding.
* **[IP warmup](ip-warmup-gs.md)** - Discover best practices for IP address warmup to improve email deliverability and sender reputation.
* **[Manage suppression list](manage-suppression-list.md)** - Learn how to manage suppression lists to handle bounces and maintain list hygiene.
* **[Configure mobile apps](set-mobile-config.md)** - Set up mobile app configurations for push notifications and in-app messaging.
* **[Configure iOS Live activities](../mobile-live/mobile-live-configuration.md)** - Set up your environment to send Live activities to the iPhone Lock Screen and Dynamic Island.
* **[Configure WhatsApp](../whatsapp/whatsapp-configuration.md)** - Set up WhatsApp messaging via Meta's Cloud API for campaigns and journeys.
* **[Configure LINE](../line/line-configuration.md)** - Set up LINE messaging for campaigns and journeys.
* **[Configuration tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/configuration/channel-configuration/configure-channels){target="_blank"}** - Explore step-by-step video tutorials on channel configuration and best practices.
