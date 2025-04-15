---
solution: Journey Optimizer
product: journey optimizer
title: Get started with [!DNL Journey Optimizer] cchannels onfiguration
description: Learn more about [!DNL Journey Optimizer] channels configuration
role: Admin, Developer
level: Intermediate, Experienced
exl-id: 0964a484-f957-4aae-a571-61b2a1615026
feature: Application Settings
topic: Administration
keywords: configuration, configure, messages, channel, sandbox, optimizer
---

# Get started with channels configuration {#start-optimizer-configuration}

When accessing [!DNL Journey Optimizer] for the first time, you are provisioned a production sandbox and allocated a certain number of IPs depending on your contract.


To be able to send messages, you need to go through the configuration steps listed below.

>[!NOTE]
>
>* These steps must be performed by an [Adobe Journey Optimizer system administrator](../start/path/administrator.md).
>
>* For mobile channels, the [Guided channel setup](set-mobile-config.md) facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to start with campaign and journey creation.


1. Define and test specific configurations depending on the channel. Learn how to set up these configurations in the following pages:

    * [Email channel configuration](../email/get-started-email-config.md)
    * [Push channel configuration](../push/push-configuration.md)
    * [SMS channel configuration](../sms/sms-configuration.md)
    * [Direct mail configuration](../direct-mail/direct-mail-configuration.md)
    * [Web channel configuration](../web/web-configuration.md)
    * [Code-based experiences configuration](../code-based/code-based-configuration.md)
    * [Content cards configuration](../content-card/content-card-configuration-prereq.md)
    

1. Once done, you must create **channel configurations** to configure all the technical parameters required to deliver messages. [Learn more about channel configurations](channel-surfaces.md)

1. You can also:

    * Manage the number of days during which retries are performed before sending email addresses to the suppression list. [Learn more](manage-suppression-list.md)

    * Enable the **BBC email option** to keep a copy of messages sent to individuals. [Learn more](archiving-support.md#enable-bcc)

    * Configure **business rules** to avoid over-solicitating your recipients. [Learn more](../configuration/rule-sets.md)

    * Determine which email address and/or phone number to use in priority for your recipients when several addresses/numbers are available in Adobe Experience Platform. [Learn more](primary-email-addresses.md)
