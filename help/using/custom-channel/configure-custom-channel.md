---
title: Configure a custom channel – overview
description: Learn the steps an administrator must complete to configure a custom channel in Adobe Journey Optimizer, from creating the channel to setting up a channel configuration.
feature: Channel Configuration
topic: Content Management
role: Admin
level: Experienced
badge: label="Limited Availability" type="Informative"
---

# Configure a custom channel {#custom-channel-configuration}

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

Configuring a custom channel is an administrator task that happens once per channel. After the channel is configured, marketers can immediately select it in campaigns, journeys, and orchestrated campaigns — just like any native [!DNL Journey Optimizer] channel.

The configuration process covers four steps: defining the channel itself (endpoint, authentication, payload), managing the API credentials used to authenticate requests, optionally delegating a subdomain for link tracking, and finally creating a channel configuration that marketers will select at authoring time.

>[!NOTE]
>
>Before you begin, review the prerequisites and guardrails for custom channels, including the required permissions and supported authentication methods.

## Configuration steps {#steps}

The configuration process for a custom channel consists of four steps. Each step is described in detail in the linked articles below.

| Step | What you do | Why it matters | Link |
| --- | --- | --- | --- |
| **1. Create the custom channel** | Define the endpoint URL, headers, throttling policy, authentication type, and message payload structure in the Channel Builder. | This is the core definition of your channel. It tells [!DNL Journey Optimizer] how to send a message and what that message looks like. | [Learn more](create-custom-channel.md) |
| **2. Manage API credentials** | Create and manage the sets of credentials used to authenticate requests to your endpoint. | Multiple credential sets let you reuse the same channel definition across different brands or environments without duplicating the channel. | [Learn more](custom-channel-api-credentials.md) |
| **3. Delegate a subdomain** *(optional)* | Delegate a subdomain specifically for your custom channel. | Required only if your message payload contains trackable links. Without a delegated subdomain, link tracking is unavailable for this channel. | [Learn more](custom-channel-subdomains.md) |
| **4. Create a channel configuration** | Create a named preset that links the custom channel to a specific set of credentials, a subdomain, and optional payload defaults. | When building campaigns or journeys, marketers select a custom channel and an associated channel configuration. You can create multiple configurations for the same channel (for example, one per brand or region). | [Learn more](custom-channel-configuration.md) |

<!--
## Get started {#get-started}

1. [Create the custom channel](create-custom-channel.md) by defining its endpoint, authentication method, and message payload structure in the Channel Builder.
1. [Set up API credentials](custom-channel-api-credentials.md) to authenticate requests sent to your endpoint — required for all authentication types other than **None**.
1. [Delegate a subdomain](custom-channel-subdomains.md) if your message payload includes trackable links and you want them served from a branded domain.
1. [Create a channel configuration](custom-channel-configuration.md) to produce the named preset that marketers will select when building campaigns and journeys.


-->