---
solution: Journey Optimizer
product: journey optimizer
title: Enable External Integrations
description: Integrate external integrations into the channel authoring process to enrich content with personalized and dynamic information
feature: Integrations
topic: Content Management
role: User
level: Beginner
keywords: integration
hide: true
exl-id: 104f283e-f6a5-431b-919a-d97b83d19632
---
# Work with Integrations {#external-sources}

>[!BEGINSHADEBOX]

Table of content:

* **[Work with Integrations](integrations.md)**
* [Get started](vendor-integration-gs.md)
* [Available vendors](vendor-integration.md)
* [FAQ](vendor-integration-faq.md) 

>[!ENDSHADEBOX]

## Overview

The **Integrations** feature links Adobe Journey Optimizer to third-party systems whose data and composable content you already manage elsewhere. You can surface that material during authoring and at send time, which supports more responsive, personalized experiences across the channels you use in Journey Optimizer.

You can use this feature to access external data and pull content from third-party tools such as:

* **Rewards Points** from loyalty systems.
* **Price Information** for products.
* **Product Recommendations** from recommendation engines.
* **Logistics Updates** like delivery status.

To start using Integrations, users need to be granted the **[!UICONTROL Manage AJO integration configuration]** and **[!UICONTROL View AJO integration]** permissions. [Learn more on permissions](../administration/permissions.md)

+++ Learn how to assign Integrations related permissions

1. In the **[!UICONTROL Permissions]** product, go to the **[!UICONTROL Roles]** tab and select the desired **[!UICONTROL Role]**.

1. Click **[!UICONTROL Edit]** to modify the permissions.

1. Add the **[!UICONTROL AJO Integration Configuration]** resource, then select the appropriate Integrations permissions from the drop-down menu.

    ![](assets/external-integration-config-9.png)

1. Click **[!UICONTROL Save]** to apply changes.

    Any users already assigned to this role will have their permissions automatically updated.

1. To assign this role to new users, navigate to the **[!UICONTROL Users]** tab within the **[!UICONTROL Roles]** dashboard and click **[!UICONTROL Add User]**.

1. Enter the user's name, email address, or choose from the list, then click **[!UICONTROL Save]**.

If the user was not previously created, refer to [this documentation](https://experienceleague.adobe.com/en/docs/experience-platform/access-control/abac/permissions-ui/users).

+++

## Configure your Integration {#configure}

>[!AVAILABILITY]
>
> This integration feature is restricted to outbound channels (Email, SMS, and Push) and provides data in JSON or HTML formats. Please note that the API is read-only, supporting retrieval operations only.

As an administrator, you can set up external integrations by following these steps:

1. Navigate to the **[!UICONTROL Configurations]** section in the left menu and click **[!UICONTROL Manage]** from the **[!UICONTROL Integrations]** card.
    
    Then, click **[!UICONTROL Create Integration]** to start a new configuration.

    ![](assets/external-integration-config-1.png)

1. Optionally, paste a **cURL** command to auto-fill the URL, HTTP method, headers, and query parameters.

1. Provide a **[!UICONTROL Name]** and **[!UICONTROL Description]** for your integration. 

    >[!NOTE]
    >
    >These fields cannot contain spaces.

1. Enter the API endpoint **[!UICONTROL URL]**, which may include path parameters with variables that can be defined using labels and default values.

1. Configure the **[!UICONTROL Path Template]** with **[!UICONTROL Name]** and **[!UICONTROL Default value]**.

    ![](assets/external-integration-config-2.png)

1. Select the **[!UICONTROL HTTP Method]** between GET and POST.

1. Click **[!UICONTROL Add Header]** and/or **[!UICONTROL Add Query Parameters]** as needed for your integration. For each parameter, provide the following details:

    * **[!UICONTROL Parameter]**:: A unique identifier used internally to reference the parameter.

    * **[!UICONTROL Name]**: The actual name of the parameter as expected by the API.

    * **[!UICONTROL Type]**: Choose **Constant** for a fixed value or **Variable** for dynamic input.

    * **[!UICONTROL Value]**: Enter the value directly for constants, or select a variable mapping.

    * **[!UICONTROL Mandatory]**: Specify whether this parameter is required.

    ![](assets/external-integration-config-3.png)

1. Choose an **[!UICONTROL Authentication Type]**:

    * **[!UICONTROL No Authentication]**: For open APIs that do not require any credentials.

    * **[!UICONTROL API key]**: Authenticate requests using a static API key. Enter your **[!UICONTROL API Key Name ​]**, **[!UICONTROL API Key Value ​]** and specify your **[!UICONTROL Location]**.

    * **[!UICONTROL Basic Auth]**: Use standard HTTP Basic Authentication. Enter **[!UICONTROL Username]** and **[!UICONTROL Password]**.

    * **[!UICONTROL OAuth 2.0]**: Authenticate using the OAuth 2.0 protocol. Click the ![edit](assets/do-not-localize/Smock_Edit_18_N.svg) icon to configure or update the **[!UICONTROL Payload]**.

    ![](assets/external-integration-config-4.png)

1. Set  **[!UICONTROL Policy configuration]** such as **[!UICONTROL Timeout]** period for API requests and choose to enable throttling, cache and/or retry.

    When throttling is enabled, supported rates range from **50** TPS (minimum) to **5000** TPS (maximum).
    When retry is enabled, other failures follow **three** retries by default, with **200 ms**, **400 ms**, and **800 ms** between successive attempts.

1. With the **[!UICONTROL Response payload]** field, you can decide which fields of the sample output needs to be used for message personalization. 
    
    Click the ![edit](assets/do-not-localize/Smock_Edit_18_N.svg) icon and paste a sample JSON response payload to automatically detect data types.

1. Choose the fields to expose for personalization and specify their corresponding data types.

    ![](assets/external-integration-config-5.png)

    >[!NOTE]
    >
    >The **[!UICONTROL Response payload]** configuration defines the expected response for authoring including any schema applied in that step. Marketers may reference only exposed fields, tokens for other paths fail validation in the editor.

1. Use **[!UICONTROL Send test connection]** to validate the integration.
    
    Once validated, click **[!UICONTROL Activate]**.

### Send-time limits and behavior {#configure-send-time}

At send time, responses from the external API may be up to **4 MB** by default. Anything larger is treated as an integration error, and **retries are not attempted** when the failure is caused by response size. 

Calls honor the **throttling** rate you configured: Journey Optimizer schedules attempts up to that limit even when the external system is down or returning errors. If **cache** is enabled, only **successful** responses are stored and reused until the cache **TTL** you defined expires; failed responses are never cached.

Each queued message also carries a validity window (TTL). If processing falls behind and a message sits past that window, the system **discards** it and emits a **`MessageValidityExclusion`** event so stale work clears from the queue and resources stay available.


## Using External integrations for personalization {#personalization}

Before you use external integrations for personalization, note that the scheduling and isolation of integration calls depend on execution context:

* **Batch execution** (batch campaigns, orchestrated campaigns, and API-triggered marketing campaigns): each batch run operates in a dedicated, isolated environment. Concurrent batch executions that call external systems therefore do not contend with or obstruct one another.

* **Unitary execution** (unitary journeys, batch journeys, and API-triggered transactional campaigns): integration traffic is isolated per brand sandbox, so a slow external API for one brand does not delay another. Within your sandbox, concurrent integrations can briefly delay other integration-backed messages; each message is attempted for up to 12 hours before expiration.

As a marketer, you can use configured integrations to personalize your content. Follow these steps:

1. Access your campaign content and click **[!UICONTROL Add personalization]** from your Text or HTML **[!UICONTROL Components]**. 

    [Learn more on components](../email/content-components.md)

    ![](assets/external-integration-content-1.png)

1. Navigate to the **[!UICONTROL Integrations]** section and click **[!UICONTROL Open integrations]** to view all active integrations.
    
    Note that Content Fragments is available with Integrations but support outbound channels only, inbound publication will not succeed. Once a fragment is published, adding and saving new integrations is disabled to avoid impact on existing journeys and campaigns.

    ![](assets/external-integration-content-2.png)

1. Select an integration and click **[!UICONTROL Save]**.
    
    ![](assets/external-integration-content-3.png)

1. Enable the **[!UICONTROL Pills]** mode to unlock the advanced integration menu.

    ![](assets/external-integration-content-4.png)

1. When you author integration personalization, the Integrations helper includes a **`required`** field that defines how failures or missing data interact with default content:

    * **`required=true`** (default): Rendering stops for that message. The send is excluded with **`ExternalDataLookupExclusion`**, and that exclusion is recorded in the **message feedback dataset**.
    * **`required=false`**: The result variable is set to **`null`** and rendering continues. Use default text, fallbacks, or conditional logic in your template so profiles do not receive empty content when the integration does not return data.

        ![](assets/external-integration-content-8.png)

1. To complete your integration setup, define your integration attributes, which were previously specified during [configuration](#configure). 

    You can assign values to these attributes using either static values, which remain constant, or profile attributes, which dynamically pull information from user profiles.

    ![](assets/external-integration-content-5.png)

1. Once integration attributes are defined, you can now use the integration fields in your content for personalized messaging by clicking the ![add](assets/do-not-localize/Smock_Add_18_N.svg) icon.

    ![](assets/external-integration-content-6.png)

    >[!NOTE]
    >
    >Tokens in your template must use only fields the administrator exposed in the integration configuration. For example, `{{weatherResponse.temperature}}` is valid when `temperature` is exposed; `{{weatherResponse.humidity}}` is rejected in the editor if `humidity` was not exposed.

1. Click **[!UICONTROL Save]**.

Your integration personalization is now successfully applied to your content, ensuring each recipient receives a tailored, relevant experience based on the attributes you have configured.

![](assets/external-integration-content-7.png)

