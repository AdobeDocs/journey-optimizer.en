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
