---
solution: Journey Optimizer
product: journey optimizer
title: Frequently asked questions about Integrations
description: Frequently asked questions about Journey Optimizer Integrations for external data and content in messages.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
keywords: integration, FAQ, external data, personalization
hide: true
---
# Frequently asked questions about Integrations {#vendor-integration-faq}

>[!BEGINSHADEBOX]

Table of content:

* [Work with Integrations](external-sources.md)
* [Get started with Vendors integration](vendor-integration-gs.md)
* [Available vendors](vendor-integration.md)
* **[FAQ](vendor-integration-faq.md)** 

>[!ENDSHADEBOX]

Below are frequently asked questions about **Integrations** in Adobe Journey Optimizer.


## Get started

+++ What do Integrations do in Journey Optimizer?

It connects external data sources into Journey Optimizer so you can pull content and data from third party systems into your campaigns and journeys, and personalize messages using that data.

➡️ [Learn more on the Integrations overview](external-sources.md)

+++

+++ Who configures Integrations, and who uses them in content?

Administrators create and activate the technical configuration (**[!UICONTROL Configurations]** > **[!UICONTROL Integrations]** > **[!UICONTROL Manage]** > **[!UICONTROL Create Integration]**). Marketers use **[!UICONTROL Add personalization]** in Text or HTML components, open **[!UICONTROL Integrations]**, choose an active integration, and map attributes.

➡️ [Learn more on administrator and marketer workflows](external-sources.md)

+++

+++ Where do I create or manage Integrations in the UI as an administrator?

Go to the **[!UICONTROL Configurations]** section in the left menu, open **[!UICONTROL Manage]** from the **[!UICONTROL Integrations]** card, then select **[!UICONTROL Create Integration]**.

➡️ [Learn more on creating an integration](external-sources.md#configure)

+++

+++ What are common use cases for Integrations?

Examples include rewards points from loyalty systems, product price information, recommendations from recommendation engines, and logistics updates such as delivery status.

➡️ [Learn more on example data from third party systems](external-sources.md)

➡️ [Learn more on vendor integration examples](vendor-integration.md)

+++

## Configuration

+++ How do I configure an integration at a high level as an administrator?

You provide a name and description, an API endpoint URL (optionally with path variables), path template values, **[!UICONTROL GET]** or **[!UICONTROL POST]**, optional headers and query parameters, an authentication method, policy settings (such as timeout and optional cache or retry), a sample JSON response to map fields, then run **[!UICONTROL Send test connection]** and **[!UICONTROL Activate]** when valid.

➡️ [Learn more on integration configuration](external-sources.md#configure)

+++

+++ Which authentication types are supported?

These authentication types are available: **[!UICONTROL No Authentication]**, **[!UICONTROL API key]**, **[!UICONTROL Basic Auth]**, and **[!UICONTROL OAuth 2.0]** (with payload configuration for OAuth where applicable).

➡️ [Learn more on authentication types](external-sources.md#configure)

+++

+++ What is the response payload step used for?

Paste a sample JSON response so the system can detect data types and you can choose which fields are exposed for personalization in messages. You can limit which fields are available to marketers during authoring.

➡️ [Learn more on response payload mapping](external-sources.md#configure)

+++

+++ How do marketers add an integration to a message?

In campaign or journey content, use **[!UICONTROL Add personalization]** on a Text or HTML component, go to **[!UICONTROL Integrations]**, select an integration, and save. With Pills mode in the personalization editor, you can map values to variables in the configuration (such as header or query parameters, or path variables in the URL).

➡️ [Learn more on personalization with Integrations](external-sources.md#personalization)

+++

## Capabilities and use cases

+++ Can I use Integrations in journeys and campaigns?

Yes. The feature is available for both journeys and campaigns for **outbound** channels (for example email, SMS, and push), within current product limits.

➡️ [Learn more on journeys and campaigns](external-sources.md#limitations)

+++

+++ Can I use Integrations in reusable fragments?

The Integrations feature is **not** supported in Fragments. Use integrations in campaign and journey message content where the product supports them.

➡️ [Learn more on Fragments and beta limits](external-sources.md#limitations)

+++

## Limitations

+++ Which channels support Integrations?

**Outbound** channels are supported (for example email, SMS, and push).

➡️ [Learn more on supported channels](external-sources.md#limitations)

+++

+++ Which API response formats are supported?

For API call responses, **JSON** is supported for field mapping. Raw binary image output and formats that are not JSON are not available for this workflow.

➡️ [Learn more on JSON and response formats](external-sources.md#limitations)

+++

+++ Which API patterns can I connect to?

**Retrieval** APIs that target specific content are supported. **Listing** APIs (broad list or pagination patterns) are not supported for this integration model.

➡️ [Learn more on retrieval versus listing APIs](external-sources.md#limitations)

+++

## Permissions and related capabilities

+++ What permissions do I need to configure Integrations?

Configuration is an administrator workflow under **[!UICONTROL Configurations]** > **[!UICONTROL Integrations]**. Exact permission names depend on your organization's Admin Console and Journey Optimizer product profiles. Confirm with your admin or Adobe representative.

➡️ [Learn more on where Integrations are configured](external-sources.md#configure)

+++

+++ Do Integrations replace Adobe Journey Optimizer connectors to Experience Platform Sources?

No. **Integrations** are for personalization fields in message content that you drive from APIs. **Sources** and other data ingestion capabilities serve different purposes (for example batch data ingestion and profile enrichment). Use each capability for its intended scope.

➡️ [Learn more on what Integrations are for](external-sources.md)

➡️ [Learn more on Experience Platform Sources](https://experienceleague.adobe.com/docs/experience-platform/sources/home.html){target="_blank"}

+++

## Troubleshooting

+++ Why does the test connection fail or stay invalid?

Verify the endpoint URL, HTTP method, path templates, headers and query parameters, authentication, and policy timeout. Use **[!UICONTROL Send test connection]** after adjustments. For payload issues, ensure the sample reflects valid JSON and that selected fields match what the API returns.

➡️ [Learn more on test connection and payload validation](external-sources.md#configure)

+++

+++ Why marketers do not see my integration in the picker?

Integrations must be **activated** after a successful test. Only active integrations appear when marketers open **[!UICONTROL Integrations]**. If the integration is still draft or inactive, complete activation first.

➡️ [Learn more on test connection and activation](external-sources.md#configure)

+++

## Third party vendors

+++ Which vendor examples are available, and who secures the API?

You can integrate with any third party platform that exposes a compatible API endpoint. **Illustrative** vendor patterns and configuration examples can help you model compatible APIs. Responsibility for securing endpoints lies with the third party platform and your team.

➡️ [Learn more on vendor integration procedures](vendor-integration.md)

+++
