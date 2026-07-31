---
title: Get started with custom channels
description: Learn how to use [!DNL Journey Optimizer]'s Channel Builder to bring any outbound messaging channel into [!DNL Journey Optimizer] and use it in campaigns and journeys.
feature: Channel Configuration
topic: Content Management
role: User
level: Beginner
badge: label="Limited Availability" type="Informative"
---

# Get started with custom channels {#get-started-custom-channel}

>[!BEGINSHADEBOX]

**On this page:** Learn what custom channels are in Adobe Journey Optimizer, how they compare to custom actions, and the overall workflow for bringing any outbound HTTP endpoint into AJO so you can use it in campaigns and journeys.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

<!--Multilingual support, business rules enforcement, and [!DNL Adobe Experience Decisioning] integration are planned for a future release.-->

[!DNL Journey Optimizer]'s **Custom channels** capability lets you bring any outbound channel into [!DNL Journey Optimizer] so you can use it in campaigns and journeys—just like any native channel. Using the **Channel Builder**, administrators can create and configure new channels without engineering involvement, and marketers can immediately start using them to communicate with customers.

## What problem does it solve? {#why-custom-channels}

[!DNL Journey Optimizer] natively supports Email, SMS, Push notifications, WhatsApp, LINE, and other channels. However, many organizations use messaging platforms that are not natively integrated—such as WeChat, Kakao Talk, Messenger, or an external provider—and want to use them in [!DNL Journey Optimizer] for orchestration and campaign creation while still delivering with their own vendor.

<!--TBC: Another use case is when organizations have a legacy messaging gateway that exposes an HTTP endpoint, and they want to use it in [!DNL Journey Optimizer] without having to build a custom integration.-->

Custom channels fill this gap: they enable you to use any outbound HTTP endpoint as a full [!DNL Journey Optimizer] channel, unlocking:

* **Full channel capabilities** – Optimization (content experimentation and targeting), OOTB reporting and monitoring, consent and governance enforcement, and expression fragments. <!--Multilingual and business rules are planned for a future release.-->
* **Unified orchestration** – Manage all your messaging channels in a single place, regardless of the underlying delivery provider.
* **No-code setup** – Admins configure the channel through the Channel Builder UI; no custom code or engineering effort is required.

## Custom channel vs. custom actions {#custom-channel-vs-custom-action}

If you have used [custom actions](../action/action.md) in [!DNL Journey Optimizer] journeys before, custom channels address a different set of use cases. 

**Use custom channels when** you need to send messages to end users through a platform not natively supported in [!DNL Journey Optimizer]—such as WeChat, Kakao Talk, or a custom messaging gateway. Custom channels are available in campaigns and journeys, and support:

* Full personalization through the personalization editor, similar to native outbound channels
* Visual/form payload editor, preview and proof
* Content experimentation and targeting
* OOTB reporting and monitoring
* Multiple API credentials and channel configurations
* RBAC/ABAC

Custom channels support POST as the only HTTP method.

**Use custom actions when** you need to retrieve data from or push information to an external system—such as a call center, logging platform, or offline database—as a step within a journey. Custom actions are available in journeys only and support GET, PUT, and POST methods.

<!--
| | Custom Action | Custom Channel |
| --- | --- | --- |
| **Primary use case** | Retrieve data from or send information to external systems (call centers, offline systems, logging) | Send messages to end users through channels not natively supported in [!DNL Journey Optimizer] |
| **Available in** | Journeys only | Campaigns, journeys, and orchestrated campaigns |
| **Supported HTTP methods** | GET, PUT, POST | POST only |
| **Full personalization (PE)** | No | Yes, through the personalization editor, similar to native outbound channels |
| **Visual/form editor** | No | Yes |
| **Preview and proof** | No | Yes |
| **Content experimentation** | No | Yes |
| **Targeting** | No | Yes |
| **OOTB Reporting** | Yes | Yes |
| **Multiple API credentials and channel configurations** | No | Yes |
| **RBAC/ABAC** | No | Yes |
-->

>[!TIP]
>
>As a general recommendation, use custom channels for channel use cases where you are sending messages to end users. For other connector-like use cases that are needed in journeys—such as retrieving data or triggering external systems—you can continue to use custom actions.

## Use cases {#use-cases}

Custom channels are ideal for:

* **Unsupported messaging platforms** – Channels like WeChat, Kakao Talk, Messenger, Telegram, or regional messaging services that do not have a native [!DNL Journey Optimizer] channel.
* **Custom delivery providers** – Organizations that have invested in an external provider they want to keep using for message delivery, but prefer to leverage [!DNL Journey Optimizer] for orchestration, personalization, and campaign management.
* **Legacy channels** – Proprietary or legacy messaging gateways that expose an HTTP endpoint.
* **Industry-specific channels** – Secure messaging for healthcare, banking alert systems, or government notification services.

## How it works {#how-it-works}

Setting up and using a custom channel follows the main stages below:

1. **Configure** (Admin) – An administrator creates a custom channel in the **Channel Builder**, defining the endpoint, authentication, throttling policy, and message payload structure. A channel configuration is then created and linked to the custom channel. [Learn more](configure-custom-channel.md)
1. **Create** (Marketer) – A marketer adds the custom channel to a journey or campaign, selects a channel configuration, and authors the message payload using [!DNL Journey Optimizer]'s personalization editor. [Learn more](create-custom-experience.md)
1. **Send** – When a profile qualifies, [!DNL Journey Optimizer] sends the personalized payload to the configured endpoint. The external system processes the call and delivers the message.
1. **Monitor** (Admin/Marketer) – Administrators and marketers can monitor the custom channel's performance and reliability through [!DNL Journey Optimizer]'s reporting and monitoring dashboards. [Learn more](monitor-custom-channel.md)

<!--
## Next steps {#next-steps}

* Review the prerequisites and permissions before setting up your first custom channel. [Learn more](custom-channel-prerequisites.md)
* Configure your first custom channel using the Channel Builder. [Learn more](custom-channel-configuration.md)
* Create a custom channel experience in a journey or campaign. [Learn more](create-custom-experience.md)
-->
