---
solution: Journey Optimizer
product: journey optimizer
title: Configure the loyalty program
description: Learn how to configure reward providers, event definitions, and organization-level settings for your loyalty program in Adobe [!DNL Journey Optimizer].
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
>This feature is currently in **private beta**. For full details about the release cycle and availability phases in [!DNL Journey Optimizer], see [release cycle](../rn/releases.md).

Use the loyalty program configuration in [!DNL Journey Optimizer] to connect to your external loyalty systems. Marketers use **[!UICONTROL Loyalty Challenges (Beta)]** to design challenges, tasks, content, and messaging. Loyalty program configuration is a separate, administrator-only area for reward fulfillment, event mapping, product inventory, and exclusions.

## Prerequisites {#prerequisites}

Loyalty program configuration is intended for administrators. In addition to the permissions required for Loyalty Challenges, you need administrator-level access to your [!DNL Journey Optimizer] instance. Contact your Adobe administrator to request access.

## Access loyalty program configuration {#access-loyalty-admin}

Navigate to **[!UICONTROL Loyalty]** and select **[!UICONTROL Loyal admin]** to access the loyalty program configuration interface.

The interface is organized into tabs:

* **Global settings** — Set the Experience Platform identity namespace. [Learn how to configure global settings](#global-settings)
* **Reward providers** — Connect external APIs that fulfill rewards, including reward types, proxies, and authentication. [Learn how to configure reward providers](#reward-providers)
* **Event definitions** — Map incoming experience events to activities you can use in **[!UICONTROL Custom event]** tasks. [Learn how to configure event definitions](#event-definitions)
* **Product inventory** — Upload item-to-group mappings so you can use product groups in task eligibility rules. [Learn how to configure product inventory](#product-inventory)
* **Exclusions** — Upload organization-wide item and group exclusions that apply when marketers configure tasks. [Learn how to configure exclusions](#exclusions)

## Global settings {#global-settings}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_global_settings"
>title="Global settings"
>abstract="Select the Adobe Experience Platform identity namespace for your loyalty program."

Open the **[!UICONTROL Global settings]** tab. For now, the main configuration available in this tab is selecting the Adobe Experience Platform identity namespace used by your loyalty program in the **[!UICONTROL Namespace]** drop-down.

![](assets/admin-global-settings.png)

➡️ [Learn how to work with identity namespaces](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces){target="_blank"}

## Reward providers {#reward-providers}

A **reward provider** tells [!DNL Journey Optimizer] where to send fulfillment calls when challenge progress is recorded or a challenge is completed, for example, an API that credits loyalty points or stars to a member account.

A reward provider configuration includes:

![](assets/admin-reward.png)

* Basic connection details (name, description, URL, headers).
* **[!UICONTROL Reward definitions]** — the reward types this provider can issue (for example, stars or miles).
* **[!UICONTROL Reward proxies]** — an intermediate proxy that calls are routed through instead of your endpoint directly.
* **[!UICONTROL Auth token generators]** — the mechanism [!DNL Journey Optimizer] uses to obtain access tokens before calling your API.

To create a reward provider, follow these steps:

1. Open the **[!UICONTROL Reward providers]** tab and select **[!UICONTROL Create reward provider]**.

1. Enter a **[!UICONTROL Name]** and a  **[!UICONTROL Description]**.

1. In the **[!UICONTROL URL]** field, enter the API URL that receives fulfillment requests.

1. Add **[!UICONTROL Headers]** as needed for your API (for example, API keys or content types).

1. Configure the resources below associated to your reward provider. Expand each section for more information:

   +++Reward definitions — One entry per reward that is supported by your provider (for example, program points or stars, money credit)

   For each definition:

   * Provide a name and a description.
   * Specify whether the definition is **[!UICONTROL Enabled]**.
   * Toggle on the **![!UICONTROL Default]** option to mark one definition as the default for this provider.
   * Specify the **payload** sent with fulfillment calls.

   ![](assets/admin-reward-definition.png)

   +++

   +++Reward proxy - Routes fulfillment calls through an intermediate server instead of directly to the endpoint

   * Provide a name and description.
   * Enter **[!UICONTROL Host]**, **[!UICONTROL Port]** information.
   * Specify whether the proxy is **[!UICONTROL Enabled]**.
   * Add the proxy **[!UICONTROL Credential]**.

   ![](assets/admin-reward-proxies.png)

   +++

   +++Auth token generatoér - If your API requires a bearer token for authentication

   * Enter a name and description.
   * In the Auth type field, enter the type of authentication (for example Bearer).
   * Select the HTTP method to use (for example POST).
   * Enter the token endpoint URL. and add the **[!UICONTROL Token key]** in the response (for example, `access_token`).
   * Specify whether the auth token generator is **[!UICONTROL Enabled]**.
   * Add headers required by your token endpoint if required.

   [!DNL Journey Optimizer] uses this configuration to obtain a fresh token before calling your reward API.

   ![](assets/admin-reward-auth.png)

   +++

1. Select **[!UICONTROL Create reward provider]**. The provider and all configured resources are saved together.

After you save, the provider appears in the reward providers list. Marketers can select this provider when configuring challenge rewards. [Learn how to configure challenge rewards](create-challenges.md#rewards)

To edit an existing reward provider, open the **[!UICONTROL Reward providers]** tab, select the provider, and update fields in place. Changes to child resources (reward definitions, proxies, auth token generators) are saved when you update them.

>[!NOTE]
>
>**[!UICONTROL Bring your own data]** challenges fulfill rewards through your own data integration. The reward providers configured here do not apply to those challenges. [Learn how to create Bring your own data challenges](create-challenges.md#create-the-challenge)

## Event definitions (optional) {#event-definitions}

**[!UICONTROL Event definitions]** map experience events from your systems (for example, purchase, hotel check-in) to activities that Loyalty Challenges can act on, most notably **[!UICONTROL Custom event]** tasks. When events arrive, [!DNL Journey Optimizer] uses these definitions to decide whether to process them. Events that do not match any definition are ignored.

### Create an event definition {#create-event-definition}

1. Open the **[!UICONTROL Event definitions]** tab and create a new definition.

   ![](assets/admin-event-definition.png)

1. Enter a **[!UICONTROL Name]** for the event (for example, `Coffee purchase`) — this is the name marketers see when configuring a **[!UICONTROL Custom event]** task.

1. Specify how [!DNL Journey Optimizer] recognizes the event in incoming payloads. Provide an **[!UICONTROL Identifier path]**, an **[!UICONTROL XDM schema ID]**, or both:

   * **[!UICONTROL Identifier path]** — Path to the field that identifies the event or member (for example, `data.memberId`). Use this when matching events by values in the payload.
   * **[!UICONTROL Identifier values]** — Values at the identifier path that must be present for this definition to match.
   * **[!UICONTROL XDM schema ID]** — ID of the Experience Platform XDM schema for this event type. Use this when events are captured against a known schema.

1. When brands send events in their own JSON format, paste strings into **[!UICONTROL Schema]** and **[!UICONTROL Transformer]** so [!DNL Journey Optimizer] can identify the data, parse it, and decide whether to track it.

   * **[!UICONTROL Schema]** — Validation string for the incoming payload.
   * **[!UICONTROL Transformer]** — Transformation expression (for example, JSONata) that maps your payload into the format Loyalty Challenges expects.

1. Save the event definition. It appears in the **[!UICONTROL Event definitions]** list. You can now use it in challenges. [Learn how to create challenges](create-challenges.md)

## Product inventory {#product-inventory}

The **[!UICONTROL Product inventory]** tab lets you group catalog items so you can target them in tasks without listing every item ID. You upload a **CSV file** that maps each item identifier to one or more **product groups** (the same item can appear in multiple groups). After import, those groups are available when you configure task eligibility. [Learn how to create tasks](create-tasks.md)

1. Prepare a CSV file that maps each item identifier to one or more product groups. Expand the section below to see an example.

   +++Product inventory CSV example

   ![](assets/admin-inventory-csv.png)

   +++

1. Open the **[!UICONTROL Product inventory]** tab.

1. Click the **[!UICONTROL Upload]** button and select your CSV file.

   ![](assets/admin-inventory-upload.png)

1. Review the imported file in the inventory list. The list shows one row per item. In the **[!UICONTROL Groups included in]** column, you see every product group that item belongs to. Each group appears as a pill (several pills if the item is in several groups).

   ![](assets/admin-inventory-imported.png)

1. To see every item in a product group, select that group’s pill in the **[!UICONTROL Groups included in]** column on any row. The group details view lists all items in the group, not only the item on the row you selected.

   ![](assets/admin-inventory-group.png)

1. Use **[!UICONTROL Upload history]** to see previous uploads of CSV files.

## Exclusions {#exclusions}

The **[!UICONTROL Exclusions]** tab lets you define catalog items and groups that are excluded across your loyalty program without listing every item ID in each task. You upload a **CSV file** that maps each item identifier to one or more **exclusion groups** (the same item can appear in multiple groups). After import, those items and groups are available in the task builder: excluded items are marked automatically and cannot be included in a task; exclusion groups can only be added to the task’s exclude list, not the include list. [Learn how to define eligible items and exclusions on tasks](create-tasks.md#eligible-items-exclusions)

1. Prepare a CSV file that maps each item identifier to one or more exclusion groups. Expand the section below to see an example.

   +++Exclusions CSV example

   ![](assets/admin-exclusions-csv.png)

   +++

1. Open the **[!UICONTROL Exclusions]** tab.

1. Click the **[!UICONTROL Upload]** button and select your CSV file.

   ![](assets/admin-exclusions-upload.png)

1. Review the imported file in the exclusions list. The list shows one row per item. In the **[!UICONTROL Groups included in]** column, you see every exclusion group that item belongs to. Each group appears as a pill (several pills if the item is in several groups).

1. To see every item in an exclusion group, select that group’s pill in the **[!UICONTROL Groups included in]** column on any row. The group details view lists all items in the group, not only the item on the row you selected.

1. Use **[!UICONTROL Upload history]** to see previous uploads of CSV files.
