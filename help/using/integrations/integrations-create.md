---
solution: Journey Optimizer
product: journey optimizer
title: Create Standard integrations
description: Integrate external integrations into the channel authoring process to enrich content with personalized and dynamic information
feature: Integrations
topic: Content Management
role: User
level: Beginner
keywords: integration
---
# Work with Standard integrations {#external-sources}

>[!BEGINSHADEBOX]

**On this page:** Learn how administrators configure, test, and activate external integrations that connect Adobe Journey Optimizer to third-party APIs, so marketers can use them to build personalized, dynamic content in outbound channels.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
> This integration feature is restricted to outbound channels (Email, SMS, and Push) and supports pulling JSON or HTML.

A **[!UICONTROL Standard]** integration connects Journey Optimizer directly to a third-party API so you can pull external data or content into your outbound channels for personalization.

You can also link a [Browsing integration](integrations-browsing.md) to a Standard integration's parameter so the value marketers select is automatically passed to the API call.

## Create Standard integrations {#configure}

As an administrator, you can set up external integrations by following these steps:

### Set up the integration and request

Start by creating the integration and defining how it calls the external API.

1. Navigate to the **[!UICONTROL Configurations]** section in the left menu and click **[!UICONTROL Manage]** from the **[!UICONTROL Integrations]** card.
    
    Then, click **[!UICONTROL Create Integration]** to start a new configuration.

    ![Integrations card with the Create Integration button in the Configurations section](assets/external-integration-config-1.png){zoomable="yes"}

1. Optionally, paste a **cURL** command to auto-fill the URL, HTTP method, headers, and query parameters.

1. Provide a **[!UICONTROL Name]** and **[!UICONTROL Description]** for your integration. 

    >[!NOTE]
    >
    >**[!UICONTROL Name]** field cannot contain spaces.

1. Enter the API endpoint **[!UICONTROL URL]**. 

    For path variables, wrap a label in double curly braces in the URL, for example, `https://api.example.com/v1/products/{{productId}}`, then set each placeholder in **[!UICONTROL Path Parameter]**.

1. Select **[!UICONTROL Enable browsing]** to link an active Browsing integration, so its response fields can be mapped to variables in headers, query and path parameters, and the payload. 

    ➡️ See [Create Browsing integrations](integrations-browsing.md)

    ![Enable browsing option linking a Browsing integration to a Standard integration parameter](assets/external-integration-config-12.png){zoomable="yes"}

1. Configure the **[!UICONTROL Path Parameter]** with **[!UICONTROL Name]** and **[!UICONTROL Default value]** for every placeholder you added in the URL.

    Note that the **[!UICONTROL Name]** is a marketer-facing label in the editor only, it is not sent on the API request.

    ![Path Parameter configuration with Name and Default value fields for each placeholder](assets/external-integration-config-2.png){zoomable="yes"}

1. Select the **[!UICONTROL HTTP Method]** between GET and POST.

1. Click **[!UICONTROL Add Header]** and/or **[!UICONTROL Add Query Parameters]** as needed for your integration. For each parameter, provide the following details:

    * **[!UICONTROL Parameter]**: The actual header or query parameter name as expected by the API.

    * **[!UICONTROL Name]**: A marketer-friendly label for this parameter, authors select it when mapping values in campaigns.

    * **[!UICONTROL Type]**: Choose **Constant** for a fixed value or **Variable** for dynamic input.

    * **[!UICONTROL Value]**: Enter the value directly for constants, or select a variable mapping.

    * **[!UICONTROL Mandatory]**: Specify whether this parameter is required. For mandatory **[!UICONTROL Variable]** parameters, if no value is resolved at runtime and no default is provided, request generation fails with an error and the outbound API call is not made.

    ![Header and query parameter configuration with Parameter, Name, Type, Value, and Mandatory fields](assets/external-integration-config-3.png){zoomable="yes"}

With the request defined, you are ready to configure authentication, policy, and the response payload.

### Configure authentication, policy, and response

After defining the request, configure how it authenticates and behaves, and shape the response used for personalization.

1. Choose an **[!UICONTROL Authentication Type]**:

    * **[!UICONTROL No Authentication]**: For open APIs that do not require any credentials.

    * **[!UICONTROL API key]**: Authenticate requests using a static API key. Enter your **[!UICONTROL API Key Name ​]**, **[!UICONTROL API Key Value ​]** and specify your **[!UICONTROL Location]**.

    * **[!UICONTROL Basic Auth]**: Use standard HTTP Basic Authentication. Enter **[!UICONTROL Username]** and **[!UICONTROL Password]**.

    * **[!UICONTROL OAuth 2.0]**: Authenticate using the OAuth 2.0 protocol. Click the ![edit](assets/do-not-localize/Smock_Edit_18_N.svg) icon to configure or update the **[!UICONTROL Payload]**.

    ![Authentication Type options including No Authentication, API key, Basic Auth, and OAuth 2.0](assets/external-integration-config-4.png){zoomable="yes"}

1. Set  **[!UICONTROL Policy configuration]** such as **[!UICONTROL Timeout]** period for API requests and choose to enable throttling, cache and/or retry.

    >[!NOTE]
    >
    >With throttling enabled, supported rates are 50 to 5000 TPS. Limits apply to the **integration**, not each API endpoint.
    >
    >With retry enabled, other failures retry **three** times by default, with **200 ms**, **400 ms**, and **800 ms** between attempts.

1. For a **POST** method, configure the **[!UICONTROL Payload]** by choosing a **[!UICONTROL Body type]**:

    * **[!UICONTROL JSON]**: Click the ![edit](assets/do-not-localize/Smock_Edit_18_N.svg) icon and paste your JSON request payload. Map the variables you need to fulfill in the payload.

    * **[!UICONTROL GraphQL]**: Paste your GraphQL query. Journey Optimizer generates an **[!UICONTROL Operation name]** automatically and lets you map the corresponding query variables.

        ![GraphQL payload with generated operation name and query variable mapping](assets/external-integration-config-13.png){zoomable="yes"}

1. Choose the **[!UICONTROL Response type]** between **JSON** and **HTML**.

1. With the **[!UICONTROL Response payload]** field, you can decide which fields of the sample output needs to be used for message personalization. 

    Click the ![edit](assets/do-not-localize/Smock_Edit_18_N.svg) icon and paste a sample JSON response payload to automatically detect data types.

1. Choose the fields to expose for personalization and specify their corresponding data types.

    ![Response payload fields selected for personalization with detected data types](assets/external-integration-config-5.png){zoomable="yes"}

    >[!NOTE]
    >
    >The **[!UICONTROL Response payload]** configuration defines the expected response for authoring including any schema applied in that step. Marketers may reference only exposed fields, tokens for other paths fail validation in the editor.

Once authentication, policy, and response are configured, test your connection before activating.

## Test your connection {#connection}

**[!UICONTROL Send test connection]** validates the endpoint URL, authentication, and request structure against the target API prior to activation, which reduces the risk of runtime failures during message processing. 

1. When the URL, HTTP method, headers, and query parameters are defined, click **[!UICONTROL Send test connection]** to run a connectivity test and confirm the configuration.

1. In the **[!UICONTROL Send test connection]** dialog, enter default values for any **[!UICONTROL Variable]** placeholders in the URL path, headers, and query parameters.
    
    Those values are included in the test request. Journey Optimizer invokes the endpoint and reports whether the connection succeeded or failed.

    ![Send test connection dialog with default values for variable placeholders](assets/external-integration-config-11.png){zoomable="yes"}

1. If the test returns a successful response, select **[!UICONTROL Use as response payload]** to copy the response body into the **[!UICONTROL Response payload]** field, see step 10 under [Configure your Integration](#configure), where data types can be detected and fields can be selected for personalization.

    ![Successful test connection response with the Use as response payload option](assets/external-integration-config-10.png){zoomable="yes"}

1. If the test does not succeed, expand the **[!UICONTROL Error]** drop-down to review the failure details, update the integration configuration as needed, and run **[!UICONTROL Send test connection]** again.

    ![Test connection error details displayed in the Error drop-down](assets/external-integration-content-12.png){zoomable="yes"}

After the test succeeds, select **[!UICONTROL Activate]** in the integration configuration.

## Manage your integrations

After a successful test, activate the integration, then update or archive it as needed.

1. Once validated, click **[!UICONTROL Activate]**.

1. Access your newly created Integration to:

    * **Update**: Change **Authentication** details and **Policy configuration** only. Updates apply to live journeys and campaigns. Before you save changes, use the **[!UICONTROL Explore references]** menu to confirm where the integration is used.

    * **Archive**: Archive an Integration configuration.

        ![Update and Archive options for an integration configuration](assets/external-integration-config-7.png){zoomable="yes"}

1. After activation, click the ![advanced menu](assets/do-not-localize/Smock_More_18_N.svg) icon to access the **[!UICONTROL Explore references]** menu and to review usage for this configuration, including journeys and campaigns that depend on it.

    ![Explore references menu showing journeys and campaigns that use the integration](assets/external-integration-config-6.png){zoomable="yes"}

Once your integration is live, keep the following send-time behavior in mind.

## Send-time limits and behavior {#configure-send-time}

At send time, responses from the external API may be up to **4 MB** by default. Anything larger is treated as an integration error, and **retries are not attempted** when the failure is caused by response size. 

Calls honor the **throttling** rate you configured: Journey Optimizer schedules attempts up to that limit even when the external system is down or returning errors. If **cache** is enabled, only **successful** responses are stored and reused until the cache **TTL** you defined expires; failed responses are never cached.

Each queued message also carries a validity window (TTL). If processing falls behind and a message sits past that window, the system **discards** it and emits a **`MessageValidityExclusion`** event so stale work clears from the queue and resources stay available..

**See also**

* [Work with Browsing integrations](integrations-browsing.md)
* [Integrations troubleshooting FAQ](vendor-integration-faq.md#troubleshooting)
* [Monitoring & Troubleshooting](../../rp_landing_pages/troubleshoot-journey-landing-page.md)

