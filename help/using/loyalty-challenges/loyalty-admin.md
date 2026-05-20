---
solution: Journey Optimizer
product: journey optimizer
title: Configure the loyalty program
description: Learn how to configure reward providers, event definitions, and org settings for your loyalty program in Adobe Journey Optimizer.
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

The **[!UICONTROL Loyalty Admin]** section is where you configure how Journey Optimizer connects to your loyalty program backend. Marketers use **[!UICONTROL Loyalty Challenges (Beta)]** to design challenges, tasks, content, and messaging; Loyalty Admin is a separate, one-time setup for reward fulfillment and event mapping.

When a customer completes a challenge (or reaches a reward milestone), Journey Optimizer calls the reward provider you configure here to deliver points or other rewards. Challenge **[!UICONTROL Content]**, **[!UICONTROL Messaging]**, and **[!UICONTROL Audience]** settings are not affected by Loyalty Admin configuration.

## Access Loyalty Admin {#access-loyalty-admin}

To open Loyalty Admin, sign in to Journey Optimizer and select **[!UICONTROL Loyalty Admin]** in the left navigation.

<!-- SCREENSHOT: Loyalty Admin entry in the left navigation -->

The admin interface is organized into tabs. Depending on your organization, you may see **[!UICONTROL Global settings]**, **[!UICONTROL Reward providers]**, **[!UICONTROL Event definitions]**, and **[!UICONTROL Product inventory]**.

## Global settings {#global-settings}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_global_settings"
>title="Global settings"
>abstract="Select the Adobe Experience Platform identity namespace for your loyalty program and copy your configuration ID. These org-level settings are required before reward providers can fulfill rewards correctly."

Use **[!UICONTROL Global settings]** to configure org-wide options for Loyalty Challenges.

1. Open the **[!UICONTROL Global settings]** tab.

1. In the **[!UICONTROL Namespace]** drop-down, select the [identity namespace](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces) from Adobe Experience Platform that your loyalty program uses. Select **[!UICONTROL Save]** to update the namespace on your organization's Loyalty Challenges configuration.

1. Copy the **[!UICONTROL Configuration ID]** if you need to share it with your implementation team or external systems.

<!-- SCREENSHOT: Global settings tab showing namespace drop-down, Save, and Configuration ID -->

## Reward providers {#reward-providers}

A **reward provider** tells Journey Optimizer where to send fulfillment calls when challenge progress is recorded or a challenge is completed—for example, an API that credits loyalty points or stars to a member account.

A reward provider includes:

* Basic connection details (name, description, API URL, headers)
* **[!UICONTROL Reward definitions]** — reward types this provider can issue (for example, stars or miles)
* **[!UICONTROL Reward proxies]** (optional) — route calls through a proxy instead of directly to your endpoint
* **[!UICONTROL Auth token generators]** — how Journey Optimizer obtains access tokens before calling your API

### Create a reward provider {#create-reward-provider}

Follow these steps to register a new reward provider and its related resources.

1. Open the **[!UICONTROL Reward providers]** tab and start creating a provider.

1. Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**, then the **[!UICONTROL API URL]** where fulfillment requests are sent.

1. Add **[!UICONTROL Headers]** as needed for your API (for example, API keys or content types). You can add or remove header rows in the UI.

1. Configure **[!UICONTROL Reward definitions]**:

   * Define each reward type your provider supports (for example, program points or stars).
   * Optionally mark one definition as the **default** for that provider.
   * Specify the **payload** sent with fulfillment calls for each definition.

1. Optionally configure a **[!UICONTROL Reward proxy]**:

   * **[!UICONTROL Host]**, **[!UICONTROL Port]**, and credentials
   * **[!UICONTROL Name]**, **[!UICONTROL Description]**, and whether the proxy is **enabled**

1. Configure an **[!UICONTROL Auth token generator]** if your API requires a token before each call:

   * Token endpoint URL and HTTP method (for example, **POST** for OAuth-style flows)
   * **[!UICONTROL Token key]** in the response (for example, `access_token`)
   * Headers required by your token endpoint

   Journey Optimizer requests a token from this configuration before calling your reward API so calls use a current credential.

1. Select **[!UICONTROL Create Reward Provider]**. The provider and its child resources (definitions, proxy, and token generator) are created together.

<!-- SCREENSHOT: Reward provider creation form with definitions, proxy, and auth token sections -->

After creation, the provider appears in the reward providers list. Marketers select this provider when [configuring challenge rewards](create-challenges.md#rewards).

### Edit a reward provider {#edit-reward-provider}

1. Open the **[!UICONTROL Reward providers]** tab and select a provider.

1. Update the provider's name, description, URL, or headers as needed.

1. To change **[!UICONTROL Reward definitions]**, **[!UICONTROL Reward proxies]**, or **[!UICONTROL Auth token generators]**, open the corresponding section and edit the fields. Changes to these child resources are saved when you update them in place.

<!-- SCREENSHOT: Reward provider detail view with child resource sections -->

>[!NOTE]
>
>For **[!UICONTROL Bring your own data]** challenges where tasks and rewards come entirely from your data integration, reward providers configured here may not apply. [Learn more about Bring your own data challenges](create-challenges.md#create-the-challenge).

## Event definitions {#event-definitions}

**[!UICONTROL Event definitions]** map incoming experience events in your brand's format to activities that Loyalty Challenges can use—especially **[!UICONTROL Custom event]** tasks. When data arrives from your channels, Journey Optimizer uses these definitions to decide whether an event is relevant and how to interpret it. Events that do not match any definition are ignored.

### Create an event definition {#create-event-definition}

1. Open the **[!UICONTROL Event definitions]** tab and create a new definition.

1. Enter a **[!UICONTROL Name]** for the event (for example, `Coffee purchase`). This name is what marketers select when they configure a **[!UICONTROL Custom event]** task.

1. Specify how to identify the event in incoming payloads:

   * **[!UICONTROL Identifier path]** — JSON path to the field that identifies the event or member (for example, `data.memberId`)
   * **[!UICONTROL Identifier values]** — values that must be present for this definition to match

1. Optionally specify an **[!UICONTROL XDM schema ID]** and/or use the **[!UICONTROL Schema]** and **[!UICONTROL Transformer]** fields to paste schema and transformation strings your team uses to parse and validate incoming JSON before processing.

   You can provide an XDM schema ID, an identifier path, or both, depending on how your events are structured.

1. Save the event definition.

<!-- SCREENSHOT: Event definition form with identifier path, values, and schema fields -->

Most organizations create multiple event definitions—one per activity they want to track (for example, purchase, check-in, or site visit). [Learn how to use Custom event tasks in challenges](create-tasks.md#choose-activity).

## Product inventory {#product-inventory}

The **[!UICONTROL Product inventory]** tab lets you upload a CSV file to map product or item identifiers (for example, MPG IDs) to product groups used in task eligibility. This supports scenarios where tasks reference grouped products rather than individual SKUs typed manually.

1. Open the **[!UICONTROL Product inventory]** tab.

1. Upload your mapping file by dragging it into the upload area or browsing to select it.

1. Review the imported mappings in the inventory list. Select a product group to see all items in that group. Use search to find items by name or ID.

1. Use **[!UICONTROL Upload history]** to see previous uploads.

<!-- SCREENSHOT: Product inventory list after CSV upload -->

>[!NOTE]
>
>**[!UICONTROL Global exclusions]** for product inventory is planned for a future release and is not documented here.

## How Loyalty Admin relates to challenges {#how-admin-relates-to-challenges}

| Area | Configured in Loyalty Admin | Configured in Loyalty Challenges |
|------|----------------------------|----------------------------------|
| Reward fulfillment API | Yes — reward providers | No — select provider and amounts only |
| Event mapping for custom activities | Yes — event definitions | No — select event name on Custom event tasks |
| Product group mappings | Yes — product inventory | No — use groups when authoring Purchase/Spend tasks |
| Challenge structure, content, audience | No | Yes |

Typical setup order:

1. Configure **[!UICONTROL Global settings]** and at least one **[!UICONTROL Reward provider]** in Loyalty Admin.
1. Optionally add **[!UICONTROL Event definitions]** and **[!UICONTROL Product inventory]** if your program uses custom events or CSV-based product groups.
1. Create [tasks](create-tasks.md) and [challenges](create-challenges.md) in **[!UICONTROL Loyalty Challenges (Beta)]**, selecting the reward provider and definitions you configured.

Adobe Journey Optimizer sends fulfillment calls to your provider when customers earn rewards; your loyalty platform owns crediting the member's account.

## Prerequisites {#prerequisites}

Loyalty Admin is intended for a small set of administrators in your organization. In addition to the permissions needed for [Loyalty Challenges](get-started.md#prerequisites), you need access to configure org-level loyalty settings.

Contact your administrator if **[!UICONTROL Loyalty Admin]** does not appear in the left navigation or if you cannot save global settings or reward providers.
