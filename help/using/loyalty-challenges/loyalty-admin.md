---
solution: Journey Optimizer
product: journey optimizer
title: Configure loyalty challenges
description: Learn how to configure reward providers, event definitions, product inventory, exclusions, and organization-level settings for Loyalty Challenges in Adobe [!DNL Journey Optimizer].
feature: Journeys
topic: Content Management
role: Admin
level: Intermediate
exl-id: f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c
feature_v2: []
subfeature_v2: []
---
# Configure loyalty challenges {#loyalty-admin}

## Overview {#access-loyalty-admin}

Loyalty Challenges configuration connects [!DNL Journey Optimizer] to your external loyalty systems by setting up reward fulfillment, event mapping, product inventory, and exclusions before marketers author challenges.

>[!NOTE]
>
>Loyalty Challenges configuration requires administrator access to your [!DNL Journey Optimizer] instance, in addition to the permissions needed for Loyalty Challenges. Contact your Adobe administrator to gain access.

To open the configuration interface, select the **[!UICONTROL Loyalty configurations]** menu from the left navigation. The interface is organized into tabs:

* **Global settings** — Select the Experience Platform identity namespace for your program. [Learn how to configure global settings](#global-settings)
* **Reward providers** — Connect the APIs that fulfill rewards when customers make progress or complete challenges. [Learn how to configure reward providers](#reward-providers).
* **Event definitions** — Map incoming experience events to activities used in **[!UICONTROL Custom event]** tasks. [Learn how to configure event definitions](#event-definitions).
* **Product inventory** — Upload item-to-group mappings for use in task eligibility rules. [Learn how to configure product inventory](#product-inventory)
* **Exclusions** — Upload organization-wide item and group exclusions for task configuration. [Learn how to configure exclusions](#exclusions)

## Global settings {#global-settings}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_global_settings"
>title="Global settings"
>abstract="Global settings define organization-level configuration for Loyalty Challenges, including the identity namespace used to identify members across events and challenges."

Open the **[!UICONTROL Global settings]** tab to configure global settings for Loyalty Challenges.

![](assets/admin-global-settings.png)

* In the **[!UICONTROL Organization configuration]** section, select the Adobe Experience Platform [identity namespace](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces) for Loyalty Challenges. This namespace must match how member profiles are identified in your data.

   ➡️ [Learn how to work with identity namespaces](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces){target="_blank"}

* Use the **[!UICONTROL Reporting]** section to set your organization's priority metric for the Loyalty Insights dashboard. This setting determines which insights receive emphasis in your feed, allowing you to focus on the metric that matters most to your business.

   Select one of the following KPI options:

   * **[!UICONTROL Revenue]** — Prioritize insights related to monetary transactions and sales performance
   * **[!UICONTROL Engagement]** — Prioritize insights related to member activity and participation
   * **[!UICONTROL Redemptions]** — Prioritize insights related to reward redemption rates and activity
   * **[!UICONTROL Conversions]** — Prioritize insights related to conversion metrics and goal completion

   When you select a KPI, insights related to that metric receive a scoring boost, which causes them to rise to the top of the feed. This means the most relevant insights for your selected KPI appear first. No insights are hidden: your complete insight feed continues to display, ranked by significance with your selected KPI prioritized above other metrics. This setting only affects how insights are ranked in the feed and does not modify how your loyalty program operates or how challenges are evaluated. You can change your KPI selection at any time, and the insight feed re-prioritizes on the next refresh cycle to reflect your new priority.

   For more information about loyalty insights and performance monitoring, see [Monitor loyalty challenge performance](loyalty-reporting.md).

## Reward providers {#reward-providers}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_reward_providers"
>title="Reward providers"
>abstract="A reward provider defines the external system that [!DNL Journey Optimizer] calls to fulfill rewards when customers complete challenges. Configure the provider endpoint, reward definitions, proxy settings, and authentication for each integration."

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_reward_providers_connection"
>title="Reward provider connection"
>abstract="Configure how [!DNL Journey Optimizer] connects to your reward API: provider name, description, endpoint URL, and HTTP headers required for fulfillment calls."

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_reward_providers_details"
>title="Reward definitions"
>abstract="Reward definitions specify each reward type this provider can issue (for example, points or stars) and the payload [!DNL Journey Optimizer] sends when rewards are fulfilled."

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_reward_providers_proxy"
>title="Reward proxy"
>abstract="Optionally route fulfillment calls through a proxy server instead of sending them directly to your reward API endpoint. Configure host, port, credentials, and whether the proxy is enabled. Credentials value typically looks like: `{ "userName": "test", "password": "xxxx" }`"

A **reward provider** tells [!DNL Journey Optimizer] where to send fulfillment calls when challenge progress is recorded or a challenge is completed. For example, an API that credits loyalty points or stars to a member account.

Use this section for end-to-end provider setup (connection, proxy, auth token generator, and reward definition resources). For focused guidance on reward definition design and payload strategy, see [Reward Definition guide](reward-definition-guide.md).

To create a reward provider, follow these steps:

1. Open the **[!UICONTROL Reward providers]** tab and select **[!UICONTROL Create reward provider]**.

   ![](assets/admin-reward.png)

1. Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**.

1. In the **[!UICONTROL URL]** field, enter the API endpoint that receives fulfillment requests.

1. Add **[!UICONTROL Headers]** as needed for your API (for example, API keys or content types).

1. Configure the resources associated with your reward provider. Expand each section below for field details:

   +++Reward definitions

   Add one entry per reward type your provider supports (for example, program points, stars, or money credit). For each definition:

   * Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**.
   * Specify whether the definition is **[!UICONTROL Enabled]**.
   * Toggle **[!UICONTROL Default]** to mark one definition as the default for this provider.
   * Define how the rewards payload will be transformed to the fulfillment payload request, using the JSONata expression.

   For more information, see [Reward definition guide](reward-definition-guide.md#writing-the-rewardjsonata-expression).

   ![](assets/admin-reward-definition.png)

   +++

   +++Reward proxy

   Route fulfillment calls through an intermediate server instead of sending them directly to your endpoint. On the reward provider and **[!UICONTROL Create proxy]** screens, use the **[!UICONTROL Credentials]** field for proxy authentication.

   * Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**.
   * Enter **[!UICONTROL Host]** and **[!UICONTROL Port]**.
   * Specify whether the proxy is **[!UICONTROL Enabled]**.
   * In **[!UICONTROL Credentials]**, enter the proxy username and password as JSON. Credentials value typically looks like:

     ```json
     { "userName": "test", "password": "xxxx" }
     ```

   ![](assets/admin-reward-proxies.png)

   +++

   +++Auth token generator

   Use when your API requires a bearer token or similar authentication.

   * Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**.
   * In **[!UICONTROL Auth type]**, enter the authentication type (for example, Bearer).
   * Select the HTTP method (for example, POST).
   * Enter the token endpoint URL and the **[!UICONTROL Token key]** in the response (for example, `access_token`).
   * Specify whether the auth token generator is **[!UICONTROL Enabled]**.
   * Add any headers required by your token endpoint.

   [!DNL Journey Optimizer] uses this configuration to obtain a fresh token before each call to your reward API.

   ![](assets/admin-reward-auth.png)

   +++

1. Select **[!UICONTROL Create reward provider]**. The provider and all configured resources are saved together.

After you save, the provider appears in the reward providers list. Marketers can select it when configuring challenge rewards. [Learn how to configure challenge rewards](create-challenges.md#rewards)

To edit a reward provider, open the **[!UICONTROL Reward providers]** tab, select the provider, and update fields in place. Changes to reward definitions, proxies, and auth token generators are automatically saved when you update them.

>[!NOTE]
>
>**[!UICONTROL Bring your own data]** challenges fulfill rewards through your own data integration. Reward providers configured here do not apply to those challenges. [Learn how to create Bring your own data challenges](create-challenges.md#create-the-challenge)

## Event definitions {#event-definitions}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_event_definitions"
>title="Event definitions"
>abstract="Event definitions tell [!DNL Journey Optimizer] how to identify and interpret incoming event data from your external sources. Each definition maps a specific event type — such as a purchase or check-in — so the system can track customer progress toward challenge tasks."

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_event_schema"
>title="Event schema and transformer"
>abstract="In the Event schema section, provide a **[!UICONTROL Transformer]** JSONata expression to map incoming event fields into the format Loyalty Challenges expects."

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_event_identification"
>title="Event identification"
>abstract="In the Event identification section, provide the event name and required XDM schema ID used to identify incoming events."

**[!UICONTROL Event definitions]** tell [!DNL Journey Optimizer] which incoming Adobe Experience Platform experience events to process. For example, a purchase or a hotel check-in. Marketers reference these definitions when they create **[!UICONTROL Custom event]** tasks in the task builder. Events that do not match any definition are ignored.

Use this section for end-to-end definition setup (event identification plus transformer expression). For focused guidance on transformer authoring, see [Event Transformer guide](event-transformer-guide.md).

When your organization sends events in its own JSON format, [**[!UICONTROL Transformer]**](event-transformer-guide.md#writing-the-transformer) helps [!DNL Journey Optimizer] map and parse incoming payloads so events can be tracked correctly.

To create an event definition, follow these steps:

1. Open the **[!UICONTROL Event definitions]** tab and create a new definition.

   ![](assets/admin-event-definition.png)

1. In **[!UICONTROL Event identification]**, enter the required values:

   * **[!UICONTROL Name]** — Label for the event definition (for example, `Coffee purchase`).
   * **[!UICONTROL XDM schema ID]** — ID of the Experience Platform XDM schema for this event type.

1. In **[!UICONTROL Event schema]**, provide the required [JSONata](event-transformer-guide.md#writing-the-transformer) expression that maps your payload into the format Loyalty Challenges expects.

1. Save the event definition. It appears in the **[!UICONTROL Event definitions]** list and is available when marketers create **[!UICONTROL Custom event]** tasks. [Learn how to create tasks](create-tasks.md#choose-activity)

## Product inventory {#product-inventory}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_product_inventory"
>title="Product inventory"
>abstract="Upload a CSV file that maps item identifiers to product groups. Marketers can reference these groups when configuring eligible items on purchase and spend tasks without entering every item ID."

The **[!UICONTROL Product inventory]** tab groups catalog items so marketers can target them in tasks without entering every item ID. Upload a **CSV file** that maps each item identifier to one or more **product groups** (the same item can belong to several groups). Imported groups are available when configuring task eligibility. [Learn how to create tasks](create-tasks.md)

To upload a product inventory file, follow these steps:

1. Prepare a CSV file that maps each item identifier to one or more product groups. Expand the section below to see an example.

   +++Product inventory CSV example

   ![](assets/admin-inventory-csv.png)

   +++

1. Open the **[!UICONTROL Product inventory]** tab.

1. Select **[!UICONTROL Upload]** and choose your CSV file.

   ![](assets/admin-inventory-upload.png)

1. Review the imported data in the inventory list. The list shows one row per item. The **[!UICONTROL Groups included in]** column shows every product group for that item as a pill, or several pills when the item belongs to multiple groups.

   ![](assets/admin-inventory-imported.png)

1. To see all items in a product group, select that group's pill in the **[!UICONTROL Groups included in]** column on any row. The group details view lists every item in the group.

   ![](assets/admin-inventory-group.png)

1. Open **[!UICONTROL Upload history]** to view previous CSV uploads.

## Exclusions {#exclusions}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_admin_exclusions"
>title="Exclusions"
>abstract="Upload a CSV file that defines catalog items and groups excluded program-wide. Imported exclusion groups appear when marketers configure eligible items and exclusions on tasks."

The **[!UICONTROL Exclusions]** tab defines catalog items and groups that are excluded program-wide, so marketers do not have to list the same exclusions on every task. Upload a **CSV file** that maps each item identifier to one or more **exclusion groups** (the same item can belong to several groups).

After import, excluded items and groups appear in the task builder when marketers configure **[!UICONTROL Eligible items & exclusions]**. [Learn how to define eligible items and exclusions on tasks](create-tasks.md#eligible-items-exclusions)

To upload exclusions, follow these steps:

1. Prepare a CSV file that maps each item identifier to one or more exclusion groups. Expand the section below to see an example.

   +++Exclusions CSV example

   ![](assets/admin-exclusions-csv.png)

   +++

1. Open the **[!UICONTROL Exclusions]** tab.

1. Select **[!UICONTROL Upload]** and choose your CSV file.

   ![](assets/admin-exclusions-upload.png)

1. Review the imported data in the exclusions list. The list shows one row per item. The **[!UICONTROL Groups included in]** column s'ows every exclusion group for that item as a pill, or several pills when the item belongs to multiple groups.

<!-- SCREENSHOT: Exclusions list after CSV upload -->

1. To see all items in an exclusion group, select that group's pill in the **[!UICONTROL Groups included in]** column on any row. The group details view lists every item in the group.

<!-- SCREENSHOT: Exclusion group details -->

1. Open **[!UICONTROL Upload history]** to view previous CSV uploads.
