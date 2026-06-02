---
title: Get started with custom channels
description: Learn how to use Journey Optimizer's Channel Builder to bring any outbound messaging channel into AJO and use it in campaigns, journeys, and orchestrated campaigns.
feature: Custom Channel
topic: Content Management
role: User
level: Beginner
---

# Get started with custom channels {#get-started-custom-channel}

[!DNL Journey Optimizer]'s **Custom channels** capability lets you bring any outbound messaging channel into AJO so you can use it in campaigns, journeys, and orchestrated campaigns—just like any native channel. Using the **Channel Builder**, administrators can create and configure new channels without engineering involvement, and marketers can immediately start using them to communicate with customers.

>[!AVAILABILITY]
>
>Custom channels are available to all [!DNL Adobe Journey Optimizer] customers. Multilingual support, business rules enforcement, and [!DNL Adobe Experience Decisioning] integration are planned for a future release.

## What problem does it solve? {#why-custom-channels}

[!DNL Journey Optimizer] natively supports Email, SMS, Push notifications, WhatsApp, LINE, and other channels. However, many organizations use messaging platforms that are not natively integrated—such as WeChat, Kakao Talk, Messenger, or a proprietary messaging provider—and want to use them in [!DNL Journey Optimizer] for orchestration and campaign creation while still delivering with their own provider.

Custom channels fill this gap: they enable you to use any outbound HTTP endpoint as a full AJO channel, unlocking:

* **Full channel capabilities** – Content experimentation, OOTB reporting, consent and governance enforcement, and expression fragments. Multilingual and business rules are planned for a future release.
* **Unified orchestration** – Manage all your messaging channels in a single place, regardless of the underlying delivery provider.
* **No-code setup** – Admins configure the channel through the Channel Builder UI; no custom code or engineering effort is required.

## Custom Channel vs. Custom Action {#custom-channel-vs-custom-action}

If you have used **Custom Actions** in AJO journeys before, Custom Channels address a different set of use cases. The table below summarizes the main differences:

| | Custom Action | Custom Channel |
|---|---|---|
| **Primary use case** | Retrieve data from or send information to external systems (call centers, offline systems, logging) | Send messages to end users through channels not natively supported in AJO |
| **Available in** | Journeys only | Campaigns, Journeys, and Orchestrated Campaigns |
| **Full personalization (PE)** | No | Yes |
| **Visual/form editor** | No | Yes |
| **Preview and proof** | No | Yes |
| **Content experimentation** | No | Yes |
| **OOTB Reporting** | Yes | Yes |
| **Multilingual** | No | Future release |
| **Business rules** | No | Future release |
| **RBAC/ABAC** | No | Yes |

## Personas {#personas}

Three personas are involved in setting up and using custom channels:

* **Admin** – Creates the custom channel definition in the Channel Builder, configures API credentials and subdomains, and creates channel configurations.
* **Developer** – Builds authoring templates for the channel (future release) to simplify content creation for marketers.
* **Marketer** – Uses the custom channel in campaigns, journeys, and orchestrated campaigns to communicate with customers.

## How it works {#how-it-works}

Setting up and using a custom channel follows three main stages:

1. **Configure (Admin)** – An administrator creates a custom channel in the **Channel Builder**, defining the endpoint, authentication, throttling policy, and message payload structure. A channel configuration is then created and linked to the custom channel.
1. **Create (Marketer)** – A marketer adds the custom channel to a journey, campaign, or orchestrated campaign, selects a channel configuration, and authors the message payload using [!DNL Journey Optimizer]'s expression editor.
1. **Send** – When a profile qualifies, [!DNL Journey Optimizer] calls the configured endpoint with the personalized payload. The external system processes the call and delivers the message.

## Use cases {#use-cases}

Custom channels are ideal for:

* **Unsupported messaging platforms** – Channels like WeChat, Kakao Talk, Messenger, Telegram, or regional messaging services that do not have a native AJO connector.
* **Custom delivery providers** – Organizations that use a preferred messaging provider for delivery but want to leverage AJO for audience orchestration, personalization, and campaign creation.
* **Legacy channels** – Proprietary or legacy messaging gateways that expose an HTTP endpoint.
* **Industry-specific channels** – Secure messaging for healthcare, banking alert systems, or government notification services.

## Next steps {#next-steps}

* Review the prerequisites and permissions before setting up your first custom channel. [Learn more](custom-channel-prerequisites.md)
* Configure your first custom channel using the Channel Builder. [Learn more](custom-channel-configuration.md)
* Create a custom channel experience in a journey or campaign. [Learn more](create-custom-channel.md)
