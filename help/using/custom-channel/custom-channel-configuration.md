---
title: Configure a custom channel
description: Learn how to use the Channel Builder in Adobe Journey Optimizer to create and configure a custom channel, manage API credentials, and create a channel configuration.
feature: Custom Channel
topic: Content Management
role: Admin
level: Experienced
badge: label="Limited Availability" type="Informative"
---

# Configure a custom channel {#custom-channel-configuration}

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

Before marketers can use a custom channel in campaigns or journeys, an administrator must complete the following steps:

1. Create the custom channel. [Learn more](#create-custom-channel)
1. Set up API credentials (if the channel uses authentication). [Learn more](#api-credentials)
1. Delegate a subdomain (optional — required for link tracking). [Learn more](#subdomain-delegation)
1. Create a channel configuration linked to the custom channel. [Learn more](#create-channel-config)

>[!NOTE]
>
>Before you begin, review the [prerequisites and guardrails](custom-channel-prerequisites.md) for custom channels.

## Step 1: Create a custom channel {#create-custom-channel}

>[!CONTEXTUALHELP]
>id="ajo_custom_channel_settings"
>title="About custom channels"
>abstract="A custom channel lets Adobe Journey Optimizer send personalized messages to an external system through your own API endpoint. Define the general properties, endpoint, authentication, and payload, then test and activate your new custom channel. Once done, you can use it when creating a channel configuration so marketers can use it in journeys and campaigns."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/custom-channel/get-started-custom-channel.html" text="Get started with custom channels"

<!--Contextual help final location TBC (here or in Settings subsection-->

To be able to use a custom channel in campaigns and journeys, an administrator must first create the channel. This involves defining the endpoint, authentication, throttling policy, and message payload structure.

The **Channel Builder** section is the central interface for defining new custom channels. <!--It is accessible to users with the **[!UICONTROL Administrator]** role. -->It enables you to create and configure custom channels, but also manage API credentials, and delegate subdomains.

>[!IMPORTANT]
>
>To access the Channel Builder and manage custom channels, you must have the **[!UICONTROL Administrator]** role. Learn more about [roles and permissions](../administration/roles-permissions.md). <!--TBC-->

## Access the Channel Builder {#access-channel-builder}

To access the **Channel Builder**, follow the steps below.

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** in the left navigation rail.

1. Select **[!UICONTROL Custom channels]** under the **[!UICONTROL Channel builder]** section.

   ![Custom channels inventory](assets/custom_channels_inventory.png){width="70%"}

1. The inventory lists all custom channels in your sandbox.

   You can filter them by status or creation author. You can also search by name.

1. Click the **[!UICONTROL Create custom channel]** button to open the channel creation form.

### Define custom channel general settings {#general-settings}

Start by defining the general settings for your custom channel.

![General settings](assets/custom_channel_properties.png){width="70%"}

1. In the **[!UICONTROL Properties]** section, enter a **[!UICONTROL Name]** for your custom channel. This name will appear in the journeys canvas, campaign action selector, and orchestrated campaigns channel list.

   >[!NOTE]
   >
   >Names must begin with a letter (A-Z), include only alpha-numeric characters or special chars ( _, ., -) and should be greater than 1 character.
   >
   >The name must be unique and cannot be changed after the channel is created. <!--TBC-->

1. You can select an icon from the default icon library, or select a SVG file from your computer.

   >[!NOTE]
   >
   >The file must be no larger than 150KB.

   This icon will be displayed next to the channel name in the journey canvas. If no icon is uploaded, the default icon is used.

1. Enter an optional **[!UICONTROL Description]**.

<!--
1. Optionally, assign **[!UICONTROL Access labels]** to restrict access to this channel based on data usage policies. Learn more-->

### Set the endpoint configuration {#endpoint-configuration}

You must configure the endpoint, which is the HTTP URL of your external messaging system. [!DNL Journey Optimizer] sends a POST request to this endpoint with the personalized payload when a profile qualifies in a campaign or journey.

![Endpoint configuration](assets/custom_channel_endpoint_configuration.png){width="70%"}

1. In the **[!UICONTROL Endpoint configuration]** section, enter the host **[!UICONTROL URL]** of your external messaging system.

   >[!NOTE]
   >
   >The HTTP method to is currently set to **POST**.

1. Add **[!UICONTROL Headers]** as needed. Headers are key-value pairs that are sent with every request to the endpoint. They can be used for authentication, content type specification, or any other purpose required by your external system.

   At minimum, `Content-Type` and `Charset` are available as default headers. <!--TBC-->

   ![Headers configuration](assets/custom_channel_endpoint_headers.png)

   For each header, you can define whether its value is:

   * **[!UICONTROL Constant]** – A static value set once and included in every request. For example, you can define the`Content-Type`parameter with the value `application/json` or the `Charset` parameter with the value `UTF-8`.
   * **[!UICONTROL Variable]** – If a default value is entered here, it is used unless overridden in the channel configuration. For example, you can define a variable for the user ID that is resolved at runtime. [Learn more](#create-channel-config) <!--From Custom actions section: For these parameters, you can define where to get this information (example: events, data sources), pass values manually or use the advanced expression editor for advanced use cases. Advanced uses cases can be data manipulation and other function usage. Refer to this [page](expression/expressionadvanced.md).-->

1. Optionally, add **[!UICONTROL Query parameters]** using the same constant/variable pattern. Variable query parameters are appended to the endpoint URL dynamically at send time. For example, you can use a variable query parameter to pass a user identifier resolved from the profile.

   ![Query parameters](assets/custom_channel_endpoint_query_param.png){width="70%"}

1. In the **[!UICONTROL Policy configuration]** section, define how [!DNL Journey Optimizer] handles request throughput and failures. This is important to ensure that your external system can handle the volume of requests and to avoid overwhelming it.

   ![Policy configuration](assets/custom_channel_endpoint_policy_config.png)

   * **[!UICONTROL Enable throttling]** – Disabled by default. Set the maximum number of requests per second (default: **5,000c**). Once the limit is reached, requests are queued and sent as soon as possible.
   * **[!UICONTROL Enable retry]** – Enabled by default. Set the maximum retry count (default: **3**, configurable range: 0–10) for failed requests. This helps to avoid overwhelming the endpoint during transient failures.
   * **[!UICONTROL Timeout]** – Default: **5,000 milliseconds**. Set the maximum time to wait for a response from the endpoint before considering the request failed.
   <!--* **[!UICONTROL Enable cache]** – Disabled by default. Set the caching duration (default TTL: **600 seconds**). After the TTL (Time To Live) expires, the next request is sent to the endpoint. Caching is useful for endpoints that return the same response for identical requests, reducing load and improving performance.-->

### Authentication settings {#authentication-settings}

>[!CONTEXTUALHELP]
>id="ajo_custom_channel_authentication"
>title="Define the authentication type"
>abstract="Authentication ensures that only authorized requests are sent to your external messaging system. You can choose from several authentication methods, including API Key, Basic Auth, and OAuth 2.0. Upon activation, Adobe Journey Optimizer automatically generates an initial set of API credentials for the channel, which can be managed in the API credentials inventory. However, even if you can change the credentials later, you must provide the authentication details here to test the connection to your endpoint before activating the channel."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/custom-channel/create-custom-channel-config.html#api-credentials" text="Learn more about API credentials"

Select the **[!UICONTROL Authentication type]** that you need to use for this channel. The available options depend on the authentication methods supported by your external messaging system.

![Authentication type](assets/custom_channel_authentication_type.png){width="70%"}

Provide the authentication details as required by your endpoint.

* **[!UICONTROL None]** – The request is sent without credentials.
* **[!UICONTROL API Key]** – Provide the key name, value, and location (query parameter or header).
* **[!UICONTROL Basic auth]** – Provide a username and password.
* **[!UICONTROL OAuth 2.0]** – Configure the payload for OAuth 2.0 authentication.
<!--* **[!UICONTROL Custom]** – Define the authentication configuration using a JSON payload.-->

When the authentication type is anything other than **None**, [!DNL Journey Optimizer] automatically generates an initial set of API credentials for this channel when it is activated. You can change these credentials and create new ones in the API credentials inventory. [Learn more](#api-credentials) <!--TBC-->

However, the authentication details are needed here to test the connection to your endpoint before activating the channel. A **[!UICONTROL Test connection]** button is available to validate the authentication setup. [Learn more](#test-the-connection)

### Payload configuration {#payload-configuration}

>[!CONTEXTUALHELP]
>id="ajo_custom_channel_payload_config"
>title="Enable for channel configuration"
>abstract="If enabled, the fields in this column appear in the channel configuration, allowing administrators to set different values per configuration (for example, a different sender ID per brand or region). This is useful for fields that may vary based on the context of the campaign or journey, such as sender information or message templates."
additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/custom-channel/create-custom-channel-config.html" text="Learn more on custom channel configuration"

<!--Create a page on Custom channel config to explain how to use the payload in a channel configuration.-->

The payload is sent to the endpoint when a profile qualifies in a campaign or journey.

In the payload configuration, define the structure of the message payload and which fields marketers can author and personalize.

1. Click **[!UICONTROL Define payload]**, and choose how to define the payload:

   * **[!UICONTROL Paste sample JSON payload]** – Paste a representative JSON object, and [!DNL Journey Optimizer] automatically infers a schema from it.
   * **[!UICONTROL Import JSON schema]** – Upload a complete JSON schema file.

1. After the schema is generated, [!DNL Journey Optimizer] displays all detected fields in a form view.

    ![](assets/custom_channel_payload_configuration.png)

    For each field, configure the following settings:

   | Setting | Description |
   | --- | --- |
   | **[!UICONTROL Default value]** | Optional. Used if no personalized value is provided at authoring time. |
   | **[!UICONTROL Type]** | Read-only, derived from the payload. Supported types: `string`, `integer`, `decimal`, `boolean`, `dateTime`, `dateTimeOnly`, `dateOnly`, `listObject`, `listString`, `listInteger`, `listDecimal`, `listBoolean`, `listDateTime`, `listDateTimeOnly`, `listDateOnly`. |
   | **[!UICONTROL Required]** | If enabled, the field must have a value when the channel is used in a campaign or journey. Missing required fields trigger a validation error that prevents saving or activating. |
   | **[!UICONTROL Channel config]** | If enabled, the field appears in the channel configuration, allowing administrators to set different values per configuration (for example, a different sender ID per brand or region). [Learn more](#create-channel-config) |

   Nested fields are represented using dot notation (for example, `image.id`).<!--TBC-->

### Test and activate {#test-activate}

While the channel is in **[!UICONTROL Draft]** status, use the **[!UICONTROL Test connection]** button on top of the screen to send a test request to your endpoint and validate the end-to-end connection.

![Test connection button](assets/custom_channel_test_connection.png){width="70%"}

Check your external system's logs to confirm that the request was received with the expected authentication and payload.

Once the test is successful, you can save or activate the channel.

* Click **[!UICONTROL Save as draft]** to save your progress without making the channel available.
* Click **[!UICONTROL Activate]** to make the channel available for use in channel configurations, campaigns, and journeys.

>[!IMPORTANT]
>
>After a channel is activated, only the following fields remain editable: name, description, icon, throttling, and retry configuration. Endpoint URL, headers, query parameters, authentication, and payload structure are locked.<!--TBC-->

<!--TBC: An activated channel can be **archived** (hidden from all selection drop-downs while existing journeys and campaigns continue to function), but it cannot be **deleted**. Deletion is only possible while the channel is in **[!UICONTROL Draft]** status.TBC-->

## Step 2: Manage API credentials {#api-credentials}

When a custom channel is created with an authentication type other than **None**, an initial set of API credentials is automatically generated when the channel is activated.

You can view and manage credentials from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**.
 
 ![API credentials](assets/custom_channel_api_credentials.png){width="100%"}

Having multiple credentials for the same channel lets you attach different authentication values to different channel configurations - for example, for different brands or use cases - without duplicating the channel definition.

To create additional credentials for the same channel, follow the steps below.

1. From the **[!UICONTROL API credentials]** list, click **[!UICONTROL Create API credentials]**.

1. Provide a name and description.

   ![Create API credentials](assets/custom_channel_create_api_credentials.png){width="100%"}

1. Select the **[!UICONTROL Channel]** for which you are creating credentials.

   >[!NOTE]
   >
   >Only activated custom channels with an authentication type other than **None** display in the drop-down list.

1. Select the **[!UICONTROL Authentication type]** from the list.
1. Fill in the authentication-specific fields:
   * **[!UICONTROL API Key]** – Provide the key name, value, and location (query parameter or header).
   * **[!UICONTROL Basic auth]** – Provide a username and password.
   * **[!UICONTROL OAuth 2.0]** – Configure the payload for OAuth 2.0 authentication.
1. Click **[!UICONTROL Save]**.

## Step 3: Delegate a subdomain {#subdomain-delegation}

<!--TBC if optional or required for custom channels.-->
To allow link tracking within message payloads, you need to delegate a subdomain for your custom channel. They are distinct from email, SMS or landing page subdomains and need to be created and managed in their own inventory.

To delegate a subdomain for custom channels:

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL Subdomains]**.

   ![Subdomain inventory](assets/custom_channel_subdomains.png){width="100%"}

1. Click **[!UICONTROL Create custom channel subdomain]** to open the subdomain creation form.

1. You can either use a delegated subdomain from the list, or create a new one.

   ![Use existing subdomain](assets/custom_channel_create_subdomain.png){width="100%"}

1. **[!UICONTROL Submit]** to create the subdomain.

## Step 4: Create a channel configuration {#create-channel-config}

A channel configuration links your custom channel to a named, reusable preset that marketers select when building campaigns and journeys.

To create a channel configuration for a custom channel:

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel configurations]** and click **[!UICONTROL Create channel configuration]**. Learn more on [creating a channel configuration](../configuration/channel-configurations.md).

1. From the **[!UICONTROL Select channel]** drop-down list, select one of your activated custom channels.

   ![Select channel](assets/custom_channel_select_channel.png){width="100%"}

1. If the selected channel uses authentication (type is not **None**), the **[!UICONTROL API credentials]** field appears. Select the credentials to use for this configuration.

   ![Select API credentials](assets/custom_channel_config_api_credentials.png){width="100%"}

1. If the channel has headers or query parameters defined as **Variable**, the **[!UICONTROL Dynamic parameters]** section appears. Enter the value for each variable parameter. You can use the personalization editor to inject dynamic values (for example, a user identifier resolved from the profile).

   ![Dynamic parameters](assets/custom_channel_config_dynamic_parameters.png){width="100%"}

1. If the channel has payload fields with the **[!UICONTROL Channel config]** checkbox enabled, those fields appear in the **[!UICONTROL Payload configuration]** section. [Learn more](#payload-configuration)

   ![Payload fields](assets/custom_channel_config_payload.png){width="100%"}

   Configure a value for each field as appropriate for this configuration.

<!-->
1. For Orchestrated Campaigns, complete the **[!UICONTROL Execution details]** section to map profile dimensions and specify the execution address.
-->

1. Click **[!UICONTROL Submit]** to save and activate the channel configuration.

<!--TBC
>[!CAUTION]
>
>If your organization uses approval policies, you may need to request approval before activating journeys or campaigns that use this channel configuration. [Learn more](../test-approve/gs-approval.md)
-->

## Next steps {#next-steps}

Your custom channel is now fully configured. Marketers can start using it to build customer experiences:

* [Create custom channel experiences](create-custom-channel.md)
* [Test your custom channel](test-custom-channel.md)
* [Manage and monitor custom channels](manage-custom-channel.md)
