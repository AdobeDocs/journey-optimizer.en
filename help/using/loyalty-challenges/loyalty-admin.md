---
solution: Journey Optimizer
product: journey optimizer
title: Configure the loyalty program
description: Learn how to configure reward providers, event definitions, and organization-level settings for your loyalty program in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: Admin
level: Intermediate
hide: true
badge: label="Private beta" type="Informative"
mini-toc-levels: 1
exl-id: f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c
---
# Configure the loyalty program {#loyalty-admin}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md)
* [Access & manage challenges and tasks](access-loyalty-challenges.md)
* [Create challenges](create-challenges.md)
* [Create tasks](create-tasks.md)
* [Monitor loyalty challenge performance](loyalty-reporting.md)
* **Configure the loyalty program** ◀︎ **You are here**
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta**. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../rn/releases.md).

The **[!UICONTROL Loyalty Admin]** section is where you configure how Journey Optimizer connects to your external loyalty systems. Marketers use **[!UICONTROL Loyalty Challenges (Beta)]** to design challenges, tasks, content, and messaging. **[!UICONTROL Loyalty Admin]** is a separate, administrator-only area for reward fulfillment, event mapping, and product inventory.

When a customer completes a challenge or reaches a reward milestone, Journey Optimizer calls the reward provider you configured to deliver points or other rewards. Configuration in **[!UICONTROL Loyalty Admin]** does not affect challenge **[!UICONTROL Content]**, **[!UICONTROL Messaging]**, or **[!UICONTROL Audience]** settings — those remain under marketer control.

## What you configure here vs. in Loyalty Challenges {#scope}

| Area | Configured in Loyalty Admin | Configured in Loyalty Challenges |
|------|----------------------------|----------------------------------|
| Reward fulfillment API | Yes — reward providers | No — select provider and amounts only |
| Event mapping for custom activities | Yes — event definitions | No — select event name on Custom event tasks |
| Product group mappings | Yes — product inventory | No — use groups when authoring Purchase/Spend tasks |
| Challenge structure, content, audience | No | Yes |

Adobe Journey Optimizer sends fulfillment calls to your reward provider when customers earn rewards. Your loyalty platform is responsible for crediting the member's account.

## Prerequisites {#prerequisites}

**[!UICONTROL Loyalty Admin]** is intended for a small number of administrators per organization. In addition to the permissions required for [Loyalty Challenges](get-started.md#prerequisites), you need administrator-level access for your Journey Optimizer instance. Contact your Adobe administrator to request access.

## Access Loyalty Admin {#access-loyalty-admin}

To open **[!UICONTROL Loyalty Admin]**, select it from the left navigation in Journey Optimizer.

<!-- SCREENSHOT: Loyalty Admin entry in the left navigation -->

**[!UICONTROL Loyalty Admin]** is organized into tabs: **[!UICONTROL Global settings]**, **[!UICONTROL Reward providers]**, **[!UICONTROL Event definitions]**, and **[!UICONTROL Product inventory]**. The tabs available to you depend on your organization's permissions and feature configuration.

## Global settings {#global-settings}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_global_settings"
>title="Global settings"
>abstract="Select the Adobe Experience Platform identity namespace for your loyalty program and copy your configuration ID. These org-level settings are required before reward providers can fulfill rewards correctly."

Use **[!UICONTROL Global settings]** to configure organization-wide options for Loyalty Challenges.

1. Open the **[!UICONTROL Global settings]** tab.

1. In the **[!UICONTROL Namespace]** drop-down, select the [identity namespace](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces) used by your loyalty program.

1. Select **[!UICONTROL Save]** to apply the namespace to your Loyalty Challenges configuration.

1. Copy the **[!UICONTROL Configuration ID]** when you need to share it with your implementation team or external systems — for example, when configuring inbound event delivery.

<!-- SCREENSHOT: Global settings tab showing namespace drop-down, Save, and Configuration ID -->

## Reward providers {#reward-providers}

A **reward provider** tells Journey Optimizer where to send fulfillment calls when challenge progress is recorded or a challenge is completed — for example, an API that credits loyalty points or stars to a member account.

A reward provider configuration includes:

* Basic connection details (name, description, API URL, headers)
* **[!UICONTROL Reward definitions]** — the reward types this provider can issue (for example, stars or miles)
* **[!UICONTROL Reward proxies]** (optional) — an intermediate proxy that calls are routed through instead of your endpoint directly
* **[!UICONTROL Auth token generators]** — the mechanism Journey Optimizer uses to obtain access tokens before calling your API

### Create a reward provider {#create-reward-provider}

1. Open the **[!UICONTROL Reward providers]** tab and select **[!UICONTROL Create reward provider]**.

1. Enter a **[!UICONTROL Name]**, **[!UICONTROL Description]**, and the **[!UICONTROL API URL]** that receives fulfillment requests.

1. Add **[!UICONTROL Headers]** as needed for your API (for example, API keys or content types).

1. Configure **[!UICONTROL Reward definitions]** — one entry per reward type your provider supports (for example, program points or stars). For each definition:

   * Specify the **payload** sent with fulfillment calls.
   * Optionally mark one definition as the **default** for this provider.

1. Optionally configure a **[!UICONTROL Reward proxy]** to route fulfillment calls through an intermediate server:

   * **[!UICONTROL Name]**, **[!UICONTROL Description]**, and whether the proxy is **enabled**
   * **[!UICONTROL Host]**, **[!UICONTROL Port]**, and credentials

1. Configure an **[!UICONTROL Auth token generator]** if your API requires a bearer token for authentication:

   * Token endpoint URL and HTTP method (for example, **POST** for OAuth-style flows)
   * **[!UICONTROL Token key]** in the response (for example, `access_token`)
   * Headers required by your token endpoint

   Journey Optimizer uses this configuration to obtain a fresh token before calling your reward API.

1. Select **[!UICONTROL Create reward provider]**. The provider and all configured child resources are saved together.

<!-- SCREENSHOT: Reward provider creation form with definitions, proxy, and auth token sections -->

After you save, the provider appears in the reward providers list. Marketers select this provider when [configuring challenge rewards](create-challenges.md#rewards).

To edit an existing reward provider, open the **[!UICONTROL Reward providers]** tab, select the provider, and update fields in place. Changes to child resources (reward definitions, proxies, auth token generators) are saved when you update them.

<!-- SCREENSHOT: Reward provider detail view with child resource sections -->

>[!NOTE]
>
>**[!UICONTROL Bring your own data]** challenges fulfill rewards through your own data integration. The reward providers configured here do not apply to those challenges. [Learn more about Bring your own data challenges](create-challenges.md#create-the-challenge).

## Event definitions (optional) {#event-definitions}

**[!UICONTROL Event definitions]** map experience events from your systems — in whatever JSON or XDM format your brand uses — to activities that Loyalty Challenges can act on, most notably **[!UICONTROL Custom event]** tasks. When events arrive, Journey Optimizer uses these definitions to decide whether to process them. Events that do not match any definition are ignored.

### Create an event definition {#create-event-definition}

1. Open the **[!UICONTROL Event definitions]** tab and create a new definition.

1. Enter a **[!UICONTROL Name]** for the event (for example, `Coffee purchase`) — this is the name marketers see when configuring a **[!UICONTROL Custom event]** task.

1. Specify how to identify the event in incoming payloads:

   * **[!UICONTROL Identifier path]** — JSON path to the field that identifies the event or member (for example, `data.memberId`)
   * **[!UICONTROL Identifier values]** — values that must be present for this definition to match

1. Optionally specify an **[!UICONTROL XDM schema ID]** if your event payloads conform to an Experience Platform schema.

1. Optionally use the **[!UICONTROL Schema]** and **[!UICONTROL Transformer]** fields to provide custom schema and transformation strings for parsing and validating incoming JSON.

   You can provide an XDM schema ID, an identifier path, or both, depending on how your events are structured.

1. Save the event definition.

<!-- SCREENSHOT: Event definition form with identifier path, values, and schema fields -->

Most organizations create multiple event definitions — one per activity they want to track (for example, purchase, check-in, or site visit). [Learn how to use Custom event tasks in challenges](create-tasks.md#choose-activity).

## Product inventory (optional) {#product-inventory}

Use the **[!UICONTROL Product inventory]** tab to upload a CSV file that maps product or item identifiers (for example, MPG IDs) to product groups. Marketers can then reference these groups in task eligibility rules instead of typing individual SKUs.

1. Open the **[!UICONTROL Product inventory]** tab.

1. Upload your mapping file.

1. Review the imported mappings in the inventory list. Select a product group to see all items in that group, or use search to find items by name or ID.

1. Use **[!UICONTROL Upload history]** to see previous uploads.

<!-- SCREENSHOT: Product inventory list after CSV upload -->

>[!NOTE]
>
>**[!UICONTROL Global exclusions]** for product inventory is planned for a future release and is not documented here.
