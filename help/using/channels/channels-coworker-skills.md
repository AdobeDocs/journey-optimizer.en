---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for channels
description: Discover the CX Enterprise Coworker skills available for inspecting channel configurations and creating custom channels in Adobe Journey Optimizer, with sample prompts.
feature: Channel Configuration
topic: Artificial Intelligence
role: Admin
level: Beginner
mini-toc-levels: 1
exl-id: 24bdb491-699d-40be-aa4a-3cc91fbd4750
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
subfeature_v2:
  - id: dcce7166-436e-4b78-aa5f-c7012ff3a9e3
    internal-label: Custom Channels
---

# Coworker for channels {#channels-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Explore Coworker capabilities in Adobe Journey Optimizer for viewing and inspecting your channel configurations and for setting up a new custom channel.

>[!ENDSHADEBOX]

Coworker brings natural-language tools into Adobe Journey Optimizer to help you inspect and set up channels. Use Channel Operation to look up your existing channel configurations and their settings, and Channel Builder to create and test a new custom channel.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, Decisioning, and Channels in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

## Channel Operation {#channel-operation}

Channel Operation is a read-only skill that lets you view, list, search, and inspect your Journey Optimizer channel configurations (presets) and credentials for standard channels such as email, SMS, push, direct mail, in-app, and web. It also covers related credentials and resources: push credentials and app IDs, email subdomains, SMS credentials, WhatsApp credentials, file routings, LINE channel settings, and the Live Activity registry. Use it to quickly check sender domains, unsubscribe settings, IP pools, and other settings before using a channel configuration in a journey or campaign.

Channel Operation is available to all customers who have access to Coworker. The same read-only channel configuration tools are also available through the [Journey Optimizer MCP server](../integrations/ajo-mcp.md).

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>List and search channel configurations</strong><br>Filter channel configurations by name, status (draft, active, archived, deactivated), or channel type.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"What channel presets are available in my sandbox?"<br><br>"Show me all my email channel configurations."<br><br>"Do I have any WhatsApp configurations set up?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Inspect a channel configuration</strong><br>Retrieve the full details of a channel configuration, including sender and reply-to addresses, subdomains, IP pools, and unsubscribe settings.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"What sender address and reply-to are configured for my marketing email configuration?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Review supporting resources</strong><br>List and inspect the resources referenced by channel configurations, such as push credentials, email subdomains, IP pools, SMS credentials, and WhatsApp credentials.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Which IP pools are used by my email channel configurations?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Audit your channel setup</strong><br>Get an overview of your channel configurations across all channels.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"How many channel configurations do I have across all channels?"<br><br>"Which channel configurations are missing or incomplete?"</td></tr>
</table>

### Limitations

* Channel Operation is read-only. It does not create, update, or delete channel configurations.
* Channel Operation is intended for standard channel configurations (presets). To manage custom outbound channels, use [Channel Builder](#channel-builder).

<!-- TO CONFIRM (PM/dev): required permissions for Channel Operation. -->

## Channel Builder {#channel-builder}

Channel Builder helps administrators manage custom outbound channels in Journey Optimizer by chatting with Coworker. You can create, test, update, list, fetch, and delete a custom channel, either through a guided manual setup, from a curl command, or from an API document link (an OpenAPI/Swagger spec or an API reference page). The skill guides you through the required setup steps: channel configuration, authentication, throttling, and payload definition. This makes it faster to launch new messaging integrations, and can reduce new channel setup time by up to 50%.

Channel Builder is intended for custom outbound channels only. To inspect standard channel configurations such as email, SMS, push, or web, use [Channel Operation](#channel-operation).

Channel Builder is designed for the administrator persona. To learn more about custom channels, see [Get started with custom channels](../custom-channel/get-started-custom-channel.md).

<!-- TO CONFIRM (PM/dev): permissions required to use Channel Builder and current limitations. Add an AVAILABILITY block here once confirmed. -->

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Create a custom channel</strong><br>Describe the messaging service you want to connect, or provide a curl command or an API document link (OpenAPI/Swagger spec or API reference page), and let Coworker guide you through the channel setup. For more details on the manual steps, see <a href="../custom-channel/create-custom-channel.md">Create a custom channel</a>.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Help me create a new custom channel for my SMS provider."<br><br>"Set up a custom channel to send messages through my provider's API."<br><br>"Create a custom channel from this curl command."<br><br>"Create a custom channel from this API reference: [link]."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Configure authentication, throttling, and payload</strong><br>Walk through the authentication method, the sending rate limits, and the payload that your channel sends to the provider. For more details, see <a href="../custom-channel/custom-channel-oauth2.md">Configure OAuth 2.0 authentication</a>.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"What authentication does my custom channel need?"<br><br>"Define the payload for my custom channel."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Test a custom channel</strong><br>Test your new channel before using it in a campaign or journey. When you test the connection, Coworker asks which payload scenario to run before it executes the test. For more details, see <a href="../custom-channel/test-custom-channel.md">Test your custom channel experience</a>.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Test my new custom channel."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Manage existing custom channels</strong><br>List your custom channels, fetch the details of one, update it, or delete it.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"List my custom channels."<br><br>"Show me the details of my [channel name] custom channel."<br><br>"Update the throttling settings of my [channel name] custom channel."</td></tr>
</table>

<!-- TO CONFIRM (PM/dev): sample prompts above are drafted from the skill description and the custom channel docs; validate them against the skill's actual behavior in Coworker. -->

{{$include /help/_includes/do-not-localize/channels/ai-augmented-channels-coworker-skills.md}}
