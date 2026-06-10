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

The **Channel builder** section is the central interface for defining new custom channels.

1. To access it, go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** in the left navigation rail.

1. Select **[!UICONTROL Custom channels]** under the **[!UICONTROL Channel builder]** section.

    ![](assets/custom_channels_inventory.png)

1. The inventory lists all custom channels in your sandbox.

      You can filter them by status or creation author. You can also search by name.

1. Click the **[!UICONTROL Create custom channel]** button to open the channel creation form.

### Define the general settings {#general-settings}

![](assets/custom_channel_properties.png)

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

![](assets/custom_channel_endpoint_configuration.png)

1. In the **[!UICONTROL Endpoint configuration]** section, enter the host **[!UICONTROL URL]** of your external messaging system.

   >[!NOTE]
   >
   >The HTTP method to is currently set to **POST**.

1. Add **[!UICONTROL Headers]** as needed.

      At minimum, `Content-Type` and `Charset` are available as default headers. <!--TBC-->
   ![](assets/custom_channel_endpoint_headers.png)


   For each header, you can define whether its value is:

   * **[!UICONTROL Constant]** – A static value set once and included in every request.
   * **[!UICONTROL Variable]** – If a default value is entered here, it is used unless overridden in the channel configuration. [Learn more](#create-channel-config)

1. Optionally, add **[!UICONTROL Query parameters]** using the same constant/variable pattern. Variable query parameters are appended to the endpoint URL dynamically at send time.

   ![](assets/custom_channel_endpoint_query_param.png)

1. In the **[!UICONTROL Policy configuration]** section, define how [!DNL Journey Optimizer] handles request throughput and failures.

   ![](assets/custom_channel_endpoint_policy_config.png)

   * **[!UICONTROL Enable throttling]** – Disabled by default. Set the maximum number of requests per second (default: **5,000 req/sec**).
   * **[!UICONTROL Timeout]** – Default: **5,000 milliseconds**.
   * **[!UICONTROL Enable cache]** – Disabled by default. Set the caching duration (default TTL: **600 seconds**).
   * **[!UICONTROL Enable retry]** – Enabled by default. Set the **[!UICONTROL Retry count]** (default: **3**, configurable range: 0–10).

### Authentication settings {#authentication-settings}

Select the **[!UICONTROL Authentication type]** required by your endpoint.

![](assets/custom_channel_authentication_type.png)

* **[!UICONTROL None]** – The request is sent without credentials.
* **[!UICONTROL API Key]** – Provide the key name, value, and location (query parameter or header).
* **[!UICONTROL Basic auth]** – Provide a username and password.
* **[!UICONTROL OAuth 2.0]** – Configure the payload for OAuth 2.0 authentication.
<!--* **[!UICONTROL Custom]** – Define the authentication configuration using a JSON payload.-->

A **[!UICONTROL Test connection]** button is available to validate the authentication setup. [Learn more](#test-the-connection)

>[!NOTE]
>
>When the authentication type is anything other than **None**, [!DNL Journey Optimizer] automatically generates an initial set of API credentials for this channel when it is activated. Additional credentials can be created in the API credentials inventory. [Learn more](#api-credentials)

### Payload configuration {#payload-configuration}

The payload configuration defines the structure of the message payload and which fields marketers can author and personalize.

1. Click **[!UICONTROL Define pyload]**, and choose how to define the payload:

   * **Paste sample JSON payload** – Paste a representative JSON object. [!DNL Journey Optimizer] automatically infers a schema from it.
   * **Import JSON schema** – Upload a complete JSON schema file.

1. After the schema is generated, [!DNL Journey Optimizer] displays all detected fields in a form view.

    ![](assets/custom_channel_payload_configuration.png)

    For each field, configure the following metadata:

   | Setting | Description |
   |---------|-------------|
   | **[!UICONTROL Type]** | Read-only, derived from the payload. Supported types: `string`, `integer`, `decimal`, `boolean`, `dateTime`, `dateTimeOnly`, `dateOnly`, `listObject`, `listString`, `listInteger`, `listDecimal`, `listBoolean`, `listDateTime`, `listDateTimeOnly`, `listDateOnly`. |
   | **[!UICONTROL Default value]** | Optional. Used if no personalized value is provided at authoring time. |
   | **[!UICONTROL Required]** | If enabled, the field must have a value when the channel is used in a campaign or journey. Missing required fields trigger a validation error that prevents saving or activating. |
   | **[!UICONTROL Channel config]** | If enabled, the field appears in the channel configuration, allowing administrators to set different values per configuration (for example, a different sender ID per brand or region). |

   Nested fields are represented using dot notation (for example, `image.id`).

### Test the connection {#test-connection}

While the channel is in **[!UICONTROL Draft]** status, use the **[!UICONTROL Test]** button to send a test request to your endpoint and validate the end-to-end connection. Check your external system's logs to confirm that the request was received with the expected authentication and payload.

### Save or activate {#save-activate}

* Click **[!UICONTROL Save as draft]** to save your progress without making the channel available.
* Click **[!UICONTROL Activate]** to make the channel available for use in channel configurations, campaigns, and journeys.

>[!IMPORTANT]
>
>After a channel is activated, only the following fields remain editable: **name**, **description**, **icon**, **throttling configuration**, and **retry configuration**. Endpoint URL, headers, query parameters, authentication, and payload structure are locked.
>
>An activated channel can be **archived** (hidden from all selection drop-downs while existing journeys and campaigns continue to function), but it cannot be **deleted**. Deletion is only possible while the channel is in Draft status.

## Step 2: Manage API credentials {#api-credentials}

When a custom channel is created with an authentication type other than **None**, an initial set of API credentials is automatically generated when the channel is activated. You can view and manage credentials from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL API credentials]**.

To create additional credentials for the same channel (for example, for different brands or use cases):

1. Click **[!UICONTROL Create API credentials]**.
1. Select the **[!UICONTROL Channel]** for which you are creating credentials. Only custom channels with a non-None authentication type appear in this list.
1. The **[!UICONTROL Authentication type]** field is read-only and reflects the authentication method defined for the channel.
1. Fill in the authentication-specific fields:
   * **Basic** – Username and password.
   * **API Key** – Key name, value, and location (query parameter or header).
   * **OAuth 2.0** – Client ID, client secret, and token endpoint.
   * **Custom** – The fields defined in the channel's authentication payload.
1. Click **[!UICONTROL Save]**.

Having multiple credentials for the same channel lets you attach different authentication values to different channel configurations without duplicating the channel definition.

## Step 3: Delegate a subdomain (optional) {#subdomain-delegation}

Custom channel subdomains enable link tracking within message payloads. They are distinct from email and SMS subdomains and maintained in their own inventory.

To delegate a subdomain for custom channels:

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Subdomains]**.
1. Select the **[!UICONTROL Custom channel]** tab.
1. Follow the subdomain delegation steps to configure your domain.

## Step 4: Create a channel configuration {#create-channel-config}

A channel configuration links your custom channel to a named, reusable preset that marketers select when building campaigns and journeys.

To create a channel configuration for a custom channel:

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel configurations]** and click **[!UICONTROL Create channel configuration]**.

1. Fill in the following fields:

   * **[!UICONTROL Name]** (required) – A unique, descriptive name visible to campaign and journey practitioners.
   * **[!UICONTROL Description]** – Optional.
   * **[!UICONTROL Access labels]** – Optional. Restrict access using data governance labels.
   * **[!UICONTROL Marketing actions]** – Assign the appropriate marketing actions to enforce consent and data governance policies.
   * **[!UICONTROL Channel]** (required) – Select one of your activated custom channels from the drop-down.
   * **[!UICONTROL Communication type]** (required) – **[!UICONTROL Marketing]** or **[!UICONTROL Transactional]**.

1. If the selected channel uses authentication (type is not **None**), the **[!UICONTROL API credentials]** field appears. Select the credentials to use for this configuration.

1. If the channel has headers or query parameters defined as **Variable**, the **[!UICONTROL Endpoint dynamic parameters]** section appears. Enter the value for each variable parameter. You can use the personalization editor to inject dynamic values (for example, a user identifier resolved from the profile).

1. If the channel has payload fields with the **[!UICONTROL Channel config]** checkbox enabled, those fields appear in the **[!UICONTROL Payload fields]** section. Configure a value for each field as appropriate for this configuration.

1. For Orchestrated Campaigns, complete the **[!UICONTROL Execution details]** section to map profile dimensions and specify the execution address.

1. Click **[!UICONTROL Submit]** to save and activate the channel configuration.

>[!CAUTION]
>
>If your organization uses approval policies, you may need to request approval before activating journeys or campaigns that use this channel configuration. [Learn more](../test-approve/gs-approval.md)

## Next steps {#next-steps}

Your custom channel is now fully configured. Marketers can start using it to build customer experiences:

* [Create custom channel experiences](create-custom-channel.md)
* [Test your custom channel](test-custom-channel.md)
* [Manage and monitor custom channels](manage-custom-channel.md)
