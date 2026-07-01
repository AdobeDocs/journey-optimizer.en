---
title: Get started with custom channels
description: Learn how to use [!DNL Journey Optimizer]'s Channel Builder to bring any outbound messaging channel into [!DNL Journey Optimizer] and use it in campaigns, journeys, and orchestrated campaigns.
feature: Custom Channel
topic: Content Management
role: User
level: Beginner
badge: label="Limited Availability" type="Informative"
---

# Get started with custom channels {#get-started-custom-channel}

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

<!--Multilingual support, business rules enforcement, and [!DNL Adobe Experience Decisioning] integration are planned for a future release.-->

[!DNL Journey Optimizer]'s **Custom channels** capability lets you bring any outbound messaging channel into [!DNL Journey Optimizer] so you can use it in campaigns, journeys, and orchestrated campaigns—just like any native channel. Using the **Channel Builder**, administrators can create and configure new channels without engineering involvement, and marketers can immediately start using them to communicate with customers.

## What problem does it solve? {#why-custom-channels}

[!DNL Journey Optimizer] natively supports Email, SMS, Push notifications, WhatsApp, LINE, and other channels. However, many organizations use messaging platforms that are not natively integrated—such as WeChat, Kakao Talk, Messenger, or a proprietary messaging provider—and want to use them in [!DNL Journey Optimizer] for orchestration and campaign creation while still delivering with their own provider.

<!--TBC: Another use case is when organizations have a legacy messaging gateway that exposes an HTTP endpoint, and they want to use it in [!DNL Journey Optimizer] without having to build a custom integration.-->

Custom channels fill this gap: they enable you to use any outbound HTTP endpoint as a full [!DNL Journey Optimizer] channel, unlocking:

* **Full channel capabilities** – Content experimentation, OOTB reporting and monitoring, consent and governance enforcement, and expression fragments. <!--Multilingual and business rules are planned for a future release.-->
* **Unified orchestration** – Manage all your messaging channels in a single place, regardless of the underlying delivery provider.
* **No-code setup** – Admins configure the channel through the Channel Builder UI; no custom code or engineering effort is required.

## Custom channel vs. custom actions {#custom-channel-vs-custom-action}

If you have used [custom actions](../action/action.md) in [!DNL Journey Optimizer] journeys before, custom channels address a different set of use cases. 

Custom actions are designed to retrieve data from or send information to external systems (for example, call centers, offline systems, or logging), while **custom channels** are designed to send messages to end users through channels not natively supported in [!DNL Journey Optimizer].

They are available in different contexts: custom actions are available in journeys only, while custom channels are available in campaigns, journeys, and orchestrated campaigns. Custom channels also support full personalization, a visual/form editor, preview and proof, content experimentation, and RBAC/ABAC.

<!--The table below summarizes the main differences:

| | Custom Action | Custom Channel |
| --- | --- | --- |
| **Primary use case** | Retrieve data from or send information to external systems (call centers, offline systems, logging) | Send messages to end users through channels not natively supported in [!DNL Journey Optimizer] |
| **Available in** | Journeys only | Campaigns, Journeys, and Orchestrated Campaigns |
| **Full personalization (PE)** | No | Yes |
| **Visual/form editor** | No | Yes |
| **Preview and proof** | No | Yes |
| **Content experimentation** | No | Yes |
| **OOTB Reporting** | Yes | Yes |
| **Multilingual** | No | Future release |
| **Business rules** | No | Future release |
| **RBAC/ABAC** | No | Yes |
-->

## Use cases {#use-cases}

Custom channels are ideal for:

* **Unsupported messaging platforms** – Channels like WeChat, Kakao Talk, Messenger, Telegram, or regional messaging services that do not have a native [!DNL Journey Optimizer] connector.
* **Custom delivery providers** – Organizations that have invested in a messaging provider they want to keep using for message delivery, but prefer to leverage [!DNL Journey Optimizer] for orchestration, personalization, and campaign management.
* **Legacy channels** – Proprietary or legacy messaging gateways that expose an HTTP endpoint.
* **Industry-specific channels** – Secure messaging for healthcare, banking alert systems, or government notification services.

## How it works {#how-it-works}

Setting up and using a custom channel follows the main stages below:

1. **Configure** (Admin) – An administrator creates a custom channel in the **Channel Builder**, defining the endpoint, authentication, throttling policy, and message payload structure. A channel configuration is then created and linked to the custom channel. [Learn more](configure-custom-channel.md)
1. **Create** (Marketer) – A marketer adds the custom channel to a journey, campaign, or orchestrated campaign, selects a channel configuration, and authors the message payload using [!DNL Journey Optimizer]'s expression editor. [Learn more](create-custom-experience.md)
1. **Send** – When a profile qualifies, [!DNL Journey Optimizer] calls the configured endpoint with the personalized payload. The external system processes the call and delivers the message.
1. **Monitor** (Admin/Marketer) – Administrators and marketers can monitor the custom channel's performance and reliability through [!DNL Journey Optimizer]'s reporting and monitoring dashboards. [Learn more](manage-custom-channel.md)

<!--
## Next steps {#next-steps}

* Review the prerequisites and permissions before setting up your first custom channel. [Learn more](custom-channel-prerequisites.md)
* Configure your first custom channel using the Channel Builder. [Learn more](custom-channel-configuration.md)
* Create a custom channel experience in a journey or campaign. [Learn more](create-custom-experience.md)-->
