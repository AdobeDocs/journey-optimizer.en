---
solution: Journey Optimizer
product: journey optimizer
title: Vendor Integration
description: Use Adobe Journey Optimizer Integrations with any external platform that exposes a valid API, plus engineering-tested vendor patterns for confidence when you design your setup.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
keywords: integration, vendor, third-party
---

# Vendor integration {#vendor-integration}

You can use **Integrations** in Adobe Journey Optimizer to call **external systems over HTTP** when each system exposes an **API endpoint** that suits your use case and is compatible with how Integrations issues requests and consumes responses. For complete workflow, see [Work with Integrations](external-sources.md).

The list of third-party solutions described is illustrative, not exhaustive. Other platforms may be used where they satisfy product requirements. The sections that follow are intended as reference patterns to support implementation of comparable integrations.


## Operational guardrails {#operational-guardrails}

Apply the following when you configure any integration in this guide or a similar vendor:

* **Response format:** Integrations map fields from **JSON** responses. Design calls so the API returns JSON suitable for mapping at authoring time.
* **Payload and fields:** Request and map only the attributes you need. Smaller responses reduce latency and limit exposure of sensitive data.
* **Endpoint shape:** Prefer stable, **single-resource** retrieval (for example one entry, product, or member) over broad list or pagination endpoints when the product expects targeted lookups. See [Limitations & exclusions](#limitations-exclusions) and [Work with Integrations](external-sources.md).
* **Volume and reliability:** Respect the vendor's **rate limits**; configure **timeout**, **retry**, and **cache** policy for your channel (for example batch email vs transactional sends) and validate under load.
* **Security:** Store and rotate tokens, API keys, and OAuth credentials according to your organization's policies. Do not embed secrets in message content.

## Limitations & exclusions {#limitations-exclusions}

The third-party solutions in this guide are **illustrative**, not exhaustive. Vendor APIs, hosts, rate limits, and JSON response shapes change—confirm endpoints, authentication, and field mapping with the vendor's current documentation and your subscription. Patterns here assume **read-oriented** calls suitable for personalization; write-back, batch exports, or non-JSON responses may be out of scope unless noted.

## Quick navigation {#quick-navigation}

Use these grouped links to jump to a **category** or a **vendor** pattern:

* **Content and CMS:** [Contentful](#contentful), [Sitecore](#sitecore), [Salsify](#salsify), [Contentstack](#contentstack), [Akeneo](#akeneo), [Magnolia](#magnolia)
* **Loyalty and rewards:** [Voucherify](#voucherify), [Talon.One](#talon-one), [Antavo](#antavo), [Salesforce Loyalty](#salesforce-loyalty), [Capillary](#capillary)
* **Templates and messaging:** [Stensul](#stensul), [Marigold](#marigold), [Adobe Target Recommendations](#adobe-target-recommendations)
* **Data, weather, and operations:** [AccuWeather](#accuweather), [ShipStation](#shipstation), [RevenueCat](#revenuecat), [Databricks](#databricks)
* **Reviews, consent, and social:** [Bynder](#bynder), [Trustpilot](#trustpilot), [Bazaarvoice](#bazaarvoice), [OneTrust](#onetrust), [Meta](#meta), [Aprimo](#aprimo), [Epsilon (Epsilon3)](#epsilon)


## Content and CMS {#content-and-cms}

### Contentful {#contentful}

>[!BEGINSHADEBOX]

For Contentful, the following prerequisites apply:

* Contentful space with Delivery API access and a read-oriented API key.
* Clear content types and field IDs; admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Broad listing or paginated Contentful APIs are a poor fit for this pattern; prefer retrieval calls that target a specific entry or asset.
* Write-back or two-way synchronization is outside the scope of this example.

>[!ENDSHADEBOX]

Contentful is a headless CMS for structured entries and assets over REST or GraphQL, so Journey Optimizer can pull content at send or open time.

Typical use cases include localized hero blocks, alt text, and CTAs in email, as well as product or promo entries in dynamic modules. Another common pattern is retrieving a specific entry by ID for personalized messaging.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Contentful Content Delivery API (CDA) URL: `https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}`

1. Select HTTP method: GET.

1. Add authentication header: 

  Authorization: Bearer <CONTENTFUL_DELIVERY_TOKEN>

1. Add path variables if required (e.g., entry ID, locale).

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select required fields for personalization.

1. Configure timeout and caching as needed.

1. Test connection and activate.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields (align with the [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/){target="_blank"} for your space and environment):

| Field | Value |
| -- | -- |
| **URL** | `https://cdn.contentful.com/spaces/{{spaceID}}/entries/environments/{{environment_id}}` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |
| **HTTP method** | `GET` |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `spaceID` | `spaceID` | `<YOUR_SPACE_ID>` |
| `environment_id` | `environment_id` | `<YOUR_ENV_ID>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | `access_token` | `<YOUR_API_KEY>` | Query Parameter |

+++

### Sitecore {#sitecore}

>[!BEGINSHADEBOX]

For Sitecore, the following prerequisites apply:

* Tenant URL and credentials (bearer or token per your API surface).
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Hostnames and paths vary by Sitecore product. Use only endpoints your tenant exposes.
* OAuth access tokens, refresh, and lifetimes must follow Sitecore security policy.

>[!ENDSHADEBOX]

Sitecore Content Hub and related cloud APIs support DAM-style download and metadata flows; the example pattern below centers on a download order by ID.

Typical use cases include asset or download metadata in email content and alignment with DAM workflows managed in Sitecore.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Configure **GET** on your download-order path, set authorization headers per Sitecore, map `id` from context, paste sample JSON, map fields, and tune timeouts for asset latency.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Content Hub API (example: download order by ID). Example URL pattern:

1. `https://xmapps-api.sitecorecloud.io/api/v1/downloadorders/{id}`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Use the following fields when you configure this sample call in Journey Optimizer. Confirm hostname and API version for your product (Content Hub, XM Cloud, and so on) in [Sitecore documentation](https://doc.sitecore.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://xmapps-api.sitecorecloud.io/api/v1/downloadorders/{{id}}` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `id` | `id` | `<id_of_download_order>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| Authorization | Authorization | Constant | Bearer `<token>` | Yes (on) |
| If-Modified-Since | If-Modified-Since | Variable | 2019-08-24T14:15:22Z | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | X-Auth-Token | `<token>` | Header |

+++

### Salsify {#salsify}

>[!BEGINSHADEBOX]

For Salsify, the following prerequisites apply:

* API token and organization context; product IDs resolvable from profile or context.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Very large catalogs: avoid bulk list endpoints if Integrations expects per-entity retrieval.
* Attribute visibility can be limited by Salsify role permissions.

>[!ENDSHADEBOX]

Salsify is a PIM with APIs for products, channels, and digital assets.

Typical use cases include product attributes or media URLs in email and messaging aligned with syndicated catalog data.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Prefer single-product retrieval over bulk catalog calls, set bearer auth, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Salsify Product API. Example URL pattern:

1. `https://api.salsify.com/v1/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Some older references reused a download-order style path for Salsify; your tenant may instead use `https://app.salsify.com/api/v1/orgs/{org_id}/products/{salsify_id}` or similar. Confirm in [Salsify developers](https://developers.salsify.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://app.salsify.com/api/v1/orgs/{{org_id}}/products/{{salsify_id}}` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `org_id` | `org_id` | `<org_id>` |
| `salsify_id` | `salsify_id` | `<salsify_id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default param) | Content-Type | Constant | application/json | Yes (on) |
| Authorization | Authorization | Constant | `Bearer <YOUR_TOKEN_HERE>` | Yes (on) |
| If-Modified-Since | If-Modified-Since | Variable | 2019-08-24T14:15:22Z | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | `apiKey` | `<your_api_key>` | Header |

+++

### Contentstack {#contentstack}

>[!BEGINSHADEBOX]

For Contentstack, the following prerequisites apply:

* Stack API key, delivery token, environment name, and content type UIDs.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* This pattern uses REST JSON for field mapping; GraphQL delivery follows a different integration path.
* Use production-appropriate delivery tokens; preview and published flows are not interchangeable.

>[!ENDSHADEBOX]

Contentstack is a headless CMS; REST delivery is typical for JSON field mapping in Journey Optimizer.

A typical use case is using entries for banners or promos with parameters that include locale.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Add both `api_key` and `access_token` headers as Contentstack requires, include the `environment` query parameter, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Content Delivery API. Example URL pattern:

1. `https://cdn.contentstack.io/v3/content_types/{content_type_uid}/entries/{entry_uid}`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields. See [Contentstack Content Delivery API](https://www.contentstack.com/docs/developers/apis/content-delivery-api/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://cdn.contentstack.io/v3/content_types/{{content_type_uid}}/entries/{{entry_uid}}` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |
| Headers | No extra headers needed. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `content_type_uid` | Content Type UID | `<your_content_type_uid>` |
| `entry_uid` | Entry UID | `<your_entry_uid>` |

**Authentication**

| Key name | Key value | Add to |
| --- | --- | --- |
| `api_key` | `<YOUR_STACK_API_KEY>` | Header |
| `access_token` | `<YOUR_DELIVERY_TOKEN>` | Header |

Contentstack expects **both** keys as headers for delivery requests.

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `environment` | Environment Name | Variable | `<your_environment_name>` | Yes (on) |

+++

### Akeneo {#akeneo}

>[!BEGINSHADEBOX]

For Akeneo, the following prerequisites apply:

* PIM base URL and OAuth client; product UUID or identifier strategy.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* PIM responses can be large. Map only the attributes required for personalization.
* Write operations are outside the scope of typical read-only personalization examples.

>[!ENDSHADEBOX]

Akeneo PIM exposes REST APIs for products, attributes, and media.

Typical use cases include governed product data in email modules and attributes for a given channel in journeys.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use **GET** with bearer token, request only needed attribute options in query flags, paste sample JSON, map a minimal attribute set, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Akeneo REST API. Example URL pattern:

1. `https://{pim-host}/api/rest/v1/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example pattern: `https://{pim-host}/api/rest/v1/products-uuid/{uuid}` with `Accept: application/json`. See [Akeneo API](https://api.akeneo.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://{{your-akeneo-domain}}.com/api/rest/v1/products-uuid/{{uuidProduct}}` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `uuidProduct` | UUID | `<product_uuid>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Authorization | Authorization | Constant | `Bearer <YOUR_TOKEN>` | Yes (on) |
| Accept | Accept | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `with_attribute_options` | Include Attribute Options | Variable | false | No (off) |
| `with_quality_scores` | Include Quality Scores | Variable | false | No (off) |
| `with_completenesses` | Include Completenesses | Variable | false | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | `Bearer <YOUR_ACCESS_TOKEN>` | Header |

+++

### Magnolia {#magnolia}

>[!BEGINSHADEBOX]

For Magnolia, the following prerequisites apply:

* Instance URL and token or basic auth; workspace and paths for delivery.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* REST delivery URLs depend on installed Magnolia modules and configuration.

>[!ENDSHADEBOX]

Magnolia offers headless and REST delivery endpoints depending on deployment.

A typical use case is delivering content nodes or fragments for marketing modules.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use the public delivery URL pattern your modules expose, authenticate per Magnolia guidance (anonymous delivery vs token for protected content), paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Magnolia REST (delivery). Example URL pattern:

1. `https://{author-or-public}/.rest/delivery/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example pattern: `https://{domain}/magnoliaAuthor/.rest/delivery/...` or public delivery tours-style URLs. Your paths depend on installed modules. See [Magnolia documentation](https://docs.magnolia-cms.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `http://{{your-domain}}/magnoliaAuthor/.rest/delivery/<myEndpoint>/travel/@nodes` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type | Content-Type | Constant | application/json | Yes (on) |
| Accept | Accept | Constant | application/json | Yes (on) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | `<bearer_token>` | Header |

Note: Delivery API is to use the rest-anonymous role for content that doesn't require a login. For secure access to protected data, a more robust method like API tokens or OAuth 2.0 is preferred

+++


## Loyalty and rewards {#loyalty-and-rewards}

### Voucherify {#voucherify}

>[!BEGINSHADEBOX]

For Voucherify, the following prerequisites apply:

* Application ID and secret (per region/cluster); clarity on which loyalty or campaign endpoints you call.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Avoid exposing internal promotion or campaign identifiers in customer-facing errors or message content.
* Application-level rate limits apply. Configure retries and caching per Voucherify guidance.

>[!ENDSHADEBOX]

Voucherify provides promotions and loyalty REST APIs (campaigns, vouchers, loyalty programs).

Typical use cases include reading loyalty or promotion state for offers in content and showing tier or balance where appropriate.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Set base URL for your cluster, add required headers (`X-APP-ID`, `X-APP-TOKEN`), constrain list endpoints with filters or IDs, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Loyalty / REST APIs. Example URL pattern:

1. Per Voucherify OpenAPI base URL for your region

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields. Full reference: [Voucherify API](https://docs.voucherify.io/reference/introduction){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://{{cluster}}.voucherify.io/v1/loyalties/{{campaignId}}/members` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `cluster` | `cluster` | `<your_cluster>` |
| `campaignId` | `campaignId` | `<loyalty_campaign_Id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| X-APP-ID | X-APP-ID | Constant | `<YOUR-APP-ID>` | Yes (on) |
| X-Voucherify-Channel | X-Voucherify-Channel | Constant | Voucherify Documentation | No (off) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `limit` | `limit` | Variable | 10 | No (off) |
| `page` | `page` | Variable | 1 | No (off) |
| `customer` | `customer` | Variable | `<customer_identifier>` | No (off) |
| `created_at` | `created_at` | Variable | `<iso8601_date>` | No (off) |
| `updated_at` | `updated_at` | Variable | `<iso8601_date>` | No (off) |
| `order` | `order` | Variable | `<sort_field>` | No (off) |
| `code` | `code` | Variable | `<loyalty_card_code>` | No (off) |
| `ids` | `ids` | Variable | `<array_of_ids>` | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | X-APP-TOKEN | `<YOUR-APP-TOKEN>` | Header |

+++

### Talon.One {#talon-one}

>[!BEGINSHADEBOX]

For Talon.One, the following prerequisites apply:

* API key and deployment-specific base URL; identifiers for application or campaign scope.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Session-heavy flows may require careful mapping to the Integrations request model.
* Observe Talon.One rate limits and idempotency guidance.

>[!ENDSHADEBOX]

Talon.One is a promotion and loyalty rules engine with REST APIs for sessions, effects, and profiles.

Typical use cases include promotions at cart or profile level in personalized content and loyalty progress or rewards display.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use **GET** on the profile or achievement path you need, set `Authorization: ApiKey-v1 <key>` as documented, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Talon.One Integration API. Example URL pattern:

1. `https://{your-domain}.talon.one/v1/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

| Field | Value |
| --- | --- |
| **URL** | `https://{{your-deployment}}.talon.one/v1/customer_profiles/{{integrationId}}/achievements/{{achievementId}}` |
| **HTTP method** | `GET` |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `your-deployment` | `your-deployment` | `<your_deployment>` |
| `integrationId` | `integrationId` | `<integrationId>` |
| `achievementId` | `achievementId` | `<achievementId>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `progressStatus` | `progressStatus` | Variable | inprogress / completed / expired | No (off) |
| `startDate` | `startDate` | Variable | 2024-05-29T15:04:05+07:00 | No (off) |
| `endDate` | `endDate` | Variable | 2024-05-29T15:04:05+07:00 | No (off) |
| `pageSize` | `pageSize` | Variable | `<default_page_size>` | No (off) |
| `skip` | `skip` | Variable | `<items_to_skip>` | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | ApiKey-v1 `<YOUR_API_KEY>` | Header |

+++

### Antavo {#antavo}

>[!BEGINSHADEBOX]

For Antavo, the following prerequisites apply:

* Stack URL and API credentials; program or shop identifiers as required.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Customer PII must be handled under Antavo agreements and your privacy policies.
* Confirm API versions and stable endpoints with Antavo for your environment.

>[!ENDSHADEBOX]

Antavo is an enterprise loyalty platform with REST APIs for members, rewards, and events.

Typical use cases include points, tier, or rewards in email or push and offers driven by loyalty state.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Configure **GET** with the vendor's authentication (for example API key in query), avoid exposing PII against policy, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Antavo Enterprise API. Example URL pattern:

1. Per Antavo stack base URL documented in your tenant

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields use the **staging** host; production uses your Antavo stack hostname. See [Antavo documentation](https://antavo.com/docs/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://api.staging.antavo.com/customers/{{customer_id}}/activities/offers` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `customer_id` | `customer_id` | `<customer_id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| Accept | Accept | Constant | application/json | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | `api_key` | `<YOUR_API_KEY>` | Query parameter |

+++

### Salesforce Loyalty {#salesforce-loyalty}

>[!BEGINSHADEBOX]

For Salesforce Loyalty, the following prerequisites apply:

* Salesforce instance, connected app or integration user, and OAuth appropriate to your org.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Salesforce API limits and OAuth token refresh must be designed into your integration.
* Field-level security and sharing rules govern which fields appear in API responses.

>[!ENDSHADEBOX]

Salesforce Loyalty Management exposes REST APIs on the Salesforce platform for members, programs, and transactions.

Typical use cases include surfacing tier, points, or benefits in journeys and aligning messaging with CRM and loyalty data.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use the loyalty integration endpoint your team approves, complete Salesforce OAuth, paste sample JSON, map fields, respect composite API limits, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Salesforce Loyalty Management REST. Example URL pattern:

1. `https://{instance}.salesforce.com/services/data/vXX.X/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Use the Loyalty Management **member profile** GET operation documented for your org's API version; paths include program and member identifiers. See [Salesforce developers](https://developer.salesforce.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://{{your-instance}}.my.salesforce.com/services/data/{{version}}/connect/loyalty/management/members` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `your-instance` | `your-instance` | `<your_instance>` |
| `version` | `version` | `version` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| Accept | Accept | Constant | application/json | No (off) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `membershipNumber` | `membershipNumber` | Variable | `<membership_number>` | No (off) * |
| `membershipId` | `membershipId` | Variable | `<membership_id>` | No (off) * |
| `posMemId` | `posMemId` | Variable | `<pos_mem_id>` | No (off) * |

\* At least one of the three is required.

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | `<access_token>` | Header |

+++

### Capillary {#capillary}

>[!BEGINSHADEBOX]

For Capillary, the following prerequisites apply:

* API host and authentication (often signed requests; follow Capillary docs).
* Program identifiers for your endpoint.

The following limitations and exclusions apply:

* Authentication schemes and regional hosts vary by deployment. Confirm with Capillary for your stack.

>[!ENDSHADEBOX]

Capillary provides loyalty and engagement APIs common in retail stacks.

Typical use cases include points, tier, or offers inside personalized journeys.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Configure headers such as `CAP-API-ACCESS-TOKEN` as required, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Capillary APIs. Example URL pattern:

1. Per Capillary integration guide for your region

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example: `https://ushc.intouch.capillarytech.com/api/v3/rewards/{reward_id}` (host varies by region). Validate the host and auth scheme with [Capillary](https://capillarytech.com/){target="_blank"}.


| Field | Value |
| --- | --- |
| **URL** | `https://ushc.intouch.capillarytech.com/api/v3/rewards/{{reward_id}}` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `reward_id` | Reward ID | `<your_reward_id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type | Content-Type | Constant | application/json | Yes (on) |
| CAP-API-ACCESS-TOKEN | Access Token | Constant | `<YOUR_ACCESS_TOKEN>` | Yes (on) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | CAP-API-ACCESS-TOKEN | `<YOUR_ACCESS_TOKEN>` | Header |

+++


## Templates and messaging {#templates-and-messaging}

### Stensul {#stensul}

>[!BEGINSHADEBOX]

For Stensul, the following prerequisites apply:

* Stensul account with API access and published templates with defined tokens.
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* In-place WYSIWYG editing of Stensul templates inside Journey Optimizer is not covered here.
* Large or complex HTML in template payloads may require security review and sanitization.

>[!ENDSHADEBOX]

Stensul is an email creation platform for approved templates; Journey Optimizer can consume template metadata and structured regions through its API.

Typical use cases include importing approved templates and mapping regions to profile attributes, and reusing governed blocks for scalable campaign builds.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name.

1. Configure the endpoint using the Stensul Templates API URL (example pattern): `https://api.stensul.com/v1/templates/{template_id}`

1. Configure authentication (API key or OAuth per Stensul API documentation).

1. Define path variables (e.g., template ID).

1. Paste a sample JSON response for field detection.

1. Map required template fields to Journey Optimizer personalization fields.

1. Test connection and activate.

### Marigold {#marigold}

>[!BEGINSHADEBOX]

For Marigold, the following prerequisites apply:

* Base URL and credentials from your contract; least-privilege API user when possible.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Endpoints vary by Marigold product. Validate with Marigold support for your deployment.
* Personal data in responses must comply with your DPA and retention policies.

>[!ENDSHADEBOX]

Marigold exposes loyalty and engagement APIs; hosts differ by geography (EU vs US module hostnames).

A typical use case is enriching messages with loyalty or preference data from Marigold programs.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Point to the Marigold host for your region, set authentication (the sample below uses `X-Api-Key` with key and secret), paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Marigold REST API (endpoint per your integration guide). Example URL pattern:

1. Use the base URL and path provided in your Marigold API documentation

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

1. Marigold uses 2 endpoints based on the geographical area for which the customer instance is active:

1. Europe: https://{{customername}}.module.slgnt.eu
   USA: https://{{customername}}.module.slgnt.us

The table below lists example values for this integration request.

+++ Sample integration fields

Base host depends on region (for example `https://{{customername}}.module.slgnt.eu` or `https://{{customername}}.module.slgnt.us`). Confirm paths with Marigold for your deployment.

| Field | Value |
| --- | --- |
| **URL** | `https://{{customername}}.module.slgnt.{{locale}}/Portal/Api/organizations/{{organization}}/content/{{api_name}}` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `customername` | `customername` | `<your_name>` |
| `locale` | `locale` | `eu` / `us` |
| `organization` | `organization` | `<your_organization>` |
| `api_name` | `api_name` | `<api_name>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | X-Api-Key | `<apiKey>:<apiSecret>` | Header |

+++

### Adobe Target Recommendations {#adobe-target-recommendations}

>[!BEGINSHADEBOX]

For Adobe Target Recommendations, the following prerequisites apply:

* Target with Recommendations; IMS org and supported authentication.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Recommendation and delivery APIs require specific parameters (for example mbox or product identifiers). Follow Adobe Target documentation.
* Tune latency and caching for your send volume and use case.

>[!ENDSHADEBOX]

Adobe Target includes Recommendations and delivery APIs for server-side or integrated experiences, subject to entitlements.

Typical use cases include injecting recommendations into experiences you author in Journey Optimizer and aligning keys with profile or Experience Platform context.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Delivery calls are often **POST** with a JSON body. Configure OAuth per [Target authentication](https://experienceleague.adobe.com/en/docs/target-dev/developer/api/configure-authentication){target="_blank"}, paste a sample response, map fields, test under expected volume.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Target Recommendations / delivery APIs (per Adobe documentation for your integration pattern). Example URL pattern:

1. See Adobe Target Recommendations API documentation for your use case

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

| Field | Value |
| --- | --- |
| **URL** | `https://{{client}}.tt.omtrdc.net/rest/v1/delivery` |
| Policy | Configure policy level details as per your need. |
| **HTTP method** | `POST` |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `client` | `client` | `<client_name>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| client | client | Variable | `<customer_client_code>` | Yes (on) |
| sessionId | sessionId | Variable | ` <session_identifier>` | Yes (on) |

**Authentication**

Refer to [Target authentication configuration](https://experienceleague.adobe.com/en/docs/target-dev/developer/api/configure-authentication) and add JSON to Payload.

**Request Payload** 

```Sample Request Payload JSON
{
  "id": {
    "tntId": "<YOUR_TENANT_ID>"
  },
  "context": {
    "channel": "web",
    "address": {
      "url": "https://example.com/store.html"
    },
    "screen": {
      "width": 1200,
      "height": 1400
    }
  },
  "experienceCloud": {
    "analytics": {
      "logging": "server_side",
      "supplementalDataId": "<supDataId>",
      "trackingServer": "sstats.adobe.com"
    }
  },
  "execute": {
    "pageLoad": {
      "parameters": {
        "pageType": "checkout",
        "preferredCurrency": "$"
      }
    },
    "mboxes": [
      {
        "index": 1,
        "name": "orderConfirmPage"
      }
    ]
  },
  "prefetch": {
    "views": [
      {
        "parameters": {
          "ad": "view"
        }
      }
    ],
    "mboxes": {
      "index": 1,
      "name": "SummerOffer"
    }
  }
}

```

+++


## Data, weather, and operations {#data-weather-and-operations}

### AccuWeather {#accuweather}

>[!BEGINSHADEBOX]

For AccuWeather, the following prerequisites apply:

* API subscription and key; location key or a city search flow.
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Confirm the JSON response shape for your AccuWeather subscription tier; Integrations maps fields from JSON responses.
* Observe AccuWeather rate limits and recommended caching.
* Resolving `locationKey` often requires a separate geolocation or city-search request before forecast calls.

>[!ENDSHADEBOX]

AccuWeather exposes forecast and location REST APIs so messages can include weather-aware snippets.

Typical use cases include short forecasts in email or push and tailoring content using forecast values tied to profile or context.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use **GET** unless your subscription requires otherwise, attach the `apiKey` query parameter (or as documented), map `locationKey` and other variables from profile/context, paste sample JSON, map fields, then test.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Daily Forecasts API. Example URL pattern:

1. `https://dataservice.accuweather.com/forecasts/v1/daily/{days}day/{locationKey}`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++Sample integration fields

Sample integration fields. Details and tiers are described in [AccuWeather APIs](https://developer.accuweather.com/apis){target="_blank"}. You often resolve `locationKey` with a separate locations search call (for example `.../locations/v1/cities/search?q={{cityName}}`).

| Field | Value |
| --- | --- |
| **URL** | `https://dataservice.accuweather.com/forecasts/v1/daily/{{days}}day/{{locationKey}}` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `days` | `days` | `15` |
| `locationKey` | `locationKey` | `<desired_location_key>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `format` | `format` | Variable | json | No (off) |
| `language` | `language` | Variable | en-US | No (off) |
| `details` | `details` | Variable | False | No (off) |
| `metric` | `metric` | Variable | False | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | `apiKey` | `<YOUR_API_KEY>` | Query parameter |

+++

### ShipStation {#shipstation}

>[!BEGINSHADEBOX]

For ShipStation, the following prerequisites apply:

* API key and secret (Basic auth per ShipStation docs).
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Do not expose ShipStation API keys in message content; keep credentials in the integration configuration only.
* Paginated list endpoints may be a poor fit for Integrations; prefer single-resource GETs when possible.

>[!ENDSHADEBOX]

ShipStation offers shipping and order APIs for carriers, labels, and tracking.

Typical use cases include order status, tracking links, or delivery ETAs in transactional messages.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Target the resource you need (orders vs shipments), authenticate per [ShipStation API](https://www.shipstation.com/docs/api/){target="_blank"}, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the ShipStation REST API. Example URL pattern:

1. `https://ssapi.shipstation.com/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

The following **Get Timer** example illustrates one ShipStation automation timing call. Use the exact path and auth from your ShipStation integration guide when reproducing it in Journey Optimizer.

| Field | Value |
| --- | --- |
| **URL** | `https://dashboard.sendtric.com/api/v1/timers/{{id}}` |
| **HTTP method** | `POST` |
| **Policy** | Configure policy level details as per your need. |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | apiKey | `<your_api_key>` | Header |

**Requet payload**

```Sample Request Payload

{
    "external_batch_id": "se-28529731",
    "batch_notes": "This is my batch",
    "shipment_ids": [
      "se-28529731"
    ],
    "rate_ids": [
      "se-28529731"
    ]
}
```

+++

### RevenueCat {#revenuecat}

>[!BEGINSHADEBOX]

For RevenueCat, the following prerequisites apply:

* Secret API key and app identifiers; stable mapping between profiles and RevenueCat customer IDs.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Protect secret API keys and follow your rotation policies.
* Subscription and entitlement data is sensitive. Meet privacy and consent requirements.

>[!ENDSHADEBOX]

RevenueCat provides subscription status and entitlements APIs for apps.

A typical use case is reflecting subscription state in lifecycle campaigns where policy allows.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Call the REST **GET** modeled below, authenticate with the secret key header, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the RevenueCat REST API. Example URL pattern:

1. `https://api.revenuecat.com/v1/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example pattern: use RevenueCat's **Get a Product** (or equivalent product/entitlement GET) from [RevenueCat docs](https://docs.revenuecat.com/){target="_blank"} with your project's base URL and version.

| Field | Value |
| --- | --- |
| **URL** | `https://api.revenuecat.com/projects/{{project_id}}/products/{{product_id}}` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `project_id` | `project_id` | `<project_id>` |
| `product_id` | `product_id` | `<product_id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `country` | `country` | Variable | `<iso_country_code>` | No (off) |
| `locale` | `locale` | Variable | `<locale_code>` | No (off) |
| `parentId` | `parentId` | Variable | `<parent_category_id>` | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | `Bearer <token>` | Header |

+++

### Databricks {#databricks}

>[!BEGINSHADEBOX]

For Databricks, the following prerequisites apply:

* Workspace host, token or OAuth per org policy; service principal with minimal scope.
* Admin access in Journey Optimizer.

>[!ENDSHADEBOX]

Databricks provides SQL and REST APIs over lakehouse data; earlier drafts combined statement execution guidance with a **jobs/get** sample.

A typical use case is using small, denormalized attributes from governed tables for personalization with strict least privilege.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Prefer narrow read paths; if you use **POST** statement execution, include the JSON body the API requires, paste a sample success response for mapping, test latency carefully, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Databricks SQL Statement Execution API. Example URL pattern:

1. `https://{workspace-host}/api/2.0/sql/statements/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++Sample integration fields

The **GET** job example below is illustrative; for SQL-driven personalization, prefer the [statement execution API](https://docs.databricks.com/api/workspace/statementexecution){target="_blank"} pattern your workspace supports.

| Field | Value |
| --- | --- |
| **URL** | `https://<databricks-instance>/api/2.0/jobs/get` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |
| Authentication | Oauth |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Accept | Accept | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `job_id` | `job_id` | Variable | `12` | Yes |

+++

## Reviews, consent, and social {#reviews-consent-and-social}

### Bynder {#bynder}

>[!BEGINSHADEBOX]

For Bynder, the following prerequisites apply:

* Portal domain and OAuth client (or approved token approach).
* Scopes for read-only access; admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Pagination and OAuth token refresh must follow Bynder's API rules.
* Large paginated responses: map only the fields required for personalization.

>[!ENDSHADEBOX]

Bynder is a DAM with REST APIs; integrations commonly use OAuth 2.0 for read-only metadata or asset URLs.

Typical use cases include pulling asset metadata or delivery URLs into messages and keeping creative approved in Bynder aligned with journeys.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Configure **GET** on the chosen endpoint (one common pattern is a users listing), complete OAuth per [Bynder](https://developer.bynder.com/){target="_blank"}, avoid pulling unnecessary pages of data, map fields, test, then activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Bynder API v4 (example: users listing pattern). Example URL pattern:

1. `https://{your-bynder-domain}/api/v4/users/`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields. See [Bynder API documentation](https://developer.bynder.com/){target="_blank"} for OAuth 2.0 payload details.

| Field | Value |
| --- | --- |
| **URL** | `https://{{your-bynder-domain}}/api/v4/users/` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `your-bynder-domain` | `your-bynder-domain` | `<your-bynder-domain>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| Authorization | Authorization | Constant | Bearer `<token>` | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `includeInActive` | `includeInActive` | Variable | False | No (off) |
| `limit` | `limit` | Variable | 100 | No (off) |
| `page` | `page` | Variable | 1 | No (off) |

**Authentication**

| Type | Payload |
| --- | --- |
| OAuth 2.0 | OAuth 2.0 payload (see Bynder documentation) |

```
{
    "type": "oauth2",
    "endpoint": {
        "uri": ""
    },
    "method": "get",
    "response": {
        "type": "json"
    },
    "request": {
        "header": [
            {
                "key": "client_id",
                "value": ""
            },
            {
                "key": "client_secret",
                "value": ""
            }
        ],
        "queryParams": [
            {
                "key": "grant_type",
                "value": ""
            },
            {
                "key": "scope",
                "value": ""
            }
        ],
        "payload": {
            "type": "json",
            "content": {}
        }
    },
    "credentialPaths": [
        "header.client_id",
        "header.client_secret",
        "queryParam.scope"
    ],
    "tokenPath": "message.token",
    "policy": {
        "timeoutInMilliseconds": 30000,
        "cache": {
            "enabled": true,
            "ttlInSeconds": 300
        },
        "retry": {
            "enabled": false
        }
    },
    "locationConfig": {
        "key": "x-token",
        "location": "query"
    }
}
```

+++

### Trustpilot {#trustpilot}

>[!BEGINSHADEBOX]

For Trustpilot, the following prerequisites apply:

* API key and approved use case; business identifiers for queries.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Use of Trustpilot data must comply with Trustpilot branding and data-use policies.
* Rate limits apply to review summary and related endpoints.

>[!ENDSHADEBOX]

Trustpilot provides APIs for business and review summary data where your use case and contract allow.

A typical use case is showing review counts or ratings in marketing content compliant with Trustpilot terms.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Configure **GET** with required query authentication, map identifiers from profile or context, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Trustpilot APIs. Example URL pattern:

1. `https://api.trustpilot.com/v1/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Use the categories listing operation from [Trustpilot developers](https://developers.trustpilot.com/){target="_blank"} for your integration pattern; parameters vary by resource.

| Field | Value |
| --- | --- |
| **URL** | `https://api.trustpilot.com/v1/categories` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `country` | `country` | Variable | `<iso_country_code>` | No (off) |
| `locale` | `locale` | Variable | `<locale_code>` | No (off) |
| `parentId` | `parentId` | Variable | `<parent_category_id>` | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | apiKey | `<your_api_key>` | Header |

+++

### Bazaarvoice {#bazaarvoice}

>[!BEGINSHADEBOX]

For Bazaarvoice, the following prerequisites apply:

* API passkey and client identifiers from your contract.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Display of ratings and reviews must follow Bazaarvoice content policies.
* Rate limits and caching rules apply per API key.

>[!ENDSHADEBOX]

Bazaarvoice provides ratings, reviews, and UGC APIs.

A typical use case is showing review summaries or ratings in email when policy allows.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use **GET** with `passkey` as a query parameter on the Conversations API, set `Accept: application/json`, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Bazaarvoice Conversations API. Example URL pattern:

1. `https://api.bazaarvoice.com/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example entry point: `https://api.bazaarvoice.com/data/products.json` with version and filter query parameters. See [Bazaarvoice developer](https://developer.bazaarvoice.com/){target="_blank"}.

| Field | Value |
| --- | --- |
| **URL** | `https://api.bazaarvoice.com/data/products.json` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Accept | Accept | Constant | application/json | Yes (on) |

**Authentication**

| Type | Key value | Location |
| --- | --- | --- |
| passkey | `<YOUR_ACCESS_TOKEN>` | Query parameter |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `apiversion` | apiversionNumber | Constant | 5.4 | Yes (on) |
| `filter` | `filter` | Variable | Id:47950830 | No (off) |
| `stats` | `stats` | Variable | all | No (off) |

+++

### OneTrust {#onetrust}

>[!BEGINSHADEBOX]

For OneTrust, the following prerequisites apply:

* API credentials and regional base URL; legal approval for fields used in messaging.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Consent and preference data are highly regulated. Coordinate with privacy and legal teams.
* API paths and payloads differ by OneTrust product. Use documentation for your subscription.

>[!ENDSHADEBOX]

OneTrust exposes privacy and consent APIs (product-specific URLs and schemas).

A typical use case is reading consent or preference signals for conditional content where architecture and legal review allow.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use the published schema or preference-center path your subscription documents, complete OAuth if required, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the OneTrust API. Example URL pattern:

1. Per OneTrust developer portal base URL

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

| Field | Value |
| --- | --- |
| **URL** | `https://customer.my.onetrust.com/api/consentmanager/v2/preferencecenters/{{preferencecenterid}}/schema` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |
| **Authentication** | Oauth |

**Path parameters**

| Parameter | Name | Value |
| --- | --- | --- |
| `preferencecenterid` | `preferencecenterid` | `<pref-id>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Accept | Accept | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `state` | `state` | constant | PUBLISHED | Yes |

+++

#### Preference center schema (published)

Example pattern (fragment): `https://{tenant}.my.onetrust.com/api/consentmanager/v2/preferencecenters/{preferencecenterid}/schema?state=PUBLISHED`. Confirm the exact path in [OneTrust Developer](https://developer.onetrust.com/){target="_blank"}.

### Meta {#meta}

>[!BEGINSHADEBOX]

For Meta, the following prerequisites apply:

* System user or app token with correct permissions; Business Manager alignment.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Short-lived access tokens require a renewal or long-lived strategy suited to server-side integrations.
* Comply with Meta Platform Terms; do not log tokens or other secrets in message payloads.

>[!ENDSHADEBOX]

Meta Graph and Marketing APIs expose catalog and campaign objects for authorized business integrations.

A typical use case is enriching content with attributes from Meta where tokens and policies allow.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Graph calls are often **GET** with a versioned path; handle token expiry, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Meta Graph API. Example URL pattern:

1. `https://graph.facebook.com/vXX.X/...`
1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Sample integration fields. See [Graph API](https://developers.facebook.com/docs/graph-api){target="_blank"} for versioning and access tokens.

| Field | Value |
| --- | --- |
| **URL** | `https://graph.facebook.com/{{API_VERSION}}/{{PRODUCT_CATALOG_ID}}/products` |
| **HTTP method** | `GET` |
| Response Payload | Select and configure the desired response fields for use during authoring, based on the API response. |
| Policy | Configure policy level details as per your need. |
| Authentication | Oauth |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `API_VERSION` | `API_VERSION` | `v19.0` |
| `PRODUCT_CATALOG_ID` | `PRODUCT_CATALOG_ID` | `12345` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Accept | Accept | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `fields` | `fields` | Variable | id | No |
| `filter` | `filter` | Variable | — | No |

+++

### Aprimo {#aprimo}

>[!BEGINSHADEBOX]

For Aprimo, the following prerequisites apply:

* Tenant URL and credentials (OAuth or API key per your setup).
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Aprimo field-level security must align with the attributes you map in Journey Optimizer.
* Large HAL or JSON payloads: restrict mapped fields to the minimum required set.

>[!ENDSHADEBOX]

Aprimo combines marketing operations and DAM APIs for records, assets, and metadata.

Typical use cases include approved record or asset fields in dynamic content and governed DAM workflows in regulated industries.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Use **GET** on the record path you need, send required headers such as `API-VERSION`, paste sample JSON (HAL or JSON as returned), map a minimal field set, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Aprimo DAM / Records API. Example URL pattern:

1. Per Aprimo API base URL and resource path for your tenant

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

| Field | Value |
| --- | --- |
| **URL** | `https://productstrategy1.dam.aprimo.com/api/core/record/{{recordID}}` |
| **HTTP method** | `GET` |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `recordId` | `recordId` | `<record_identifier>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |
| API-VERSION | API-VERSION | Constant | 1 | Yes (on) |
| Accept | Accept | Constant | application/hal+json OR application/json | No (off) |
| select-record | select-record | Variable | `<selection_type>` | No (off) |
| select-record-fields | select-record-fields | Variable | `<field_list>` | No (off) |
| select-field | select-field | Variable | `<field_selection>` | No (off) |

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | Authorization | Bearer `<token>` | Header |

+++

### Epsilon (Epsilon3) {#epsilon}

>[!BEGINSHADEBOX]

For Epsilon (Epsilon3), the following prerequisites apply:

* Credentials and endpoints from Epsilon; admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Endpoints and hosts are customer-specific. Do not deploy without documentation from your Epsilon account team.

>[!ENDSHADEBOX]

Epsilon exposes APIs per enterprise agreement; base URLs and auth come from your account team (the Events API example below is illustrative).

A typical use case is exposing loyalty or offer attributes through supported JSON APIs.

Use the procedure below to configure this integration in Journey Optimizer. See **Sample integration fields** for example request details, and confirm those values with the vendor documentation for your environment.

1. Follow [Work with Integrations](external-sources.md). Do not guess public URLs. Use the specification from Epsilon, paste sample JSON, map fields, test, activate.

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name without spaces.

1. Configure the endpoint using the Epsilon API (per your integration specification). Example URL pattern:

1. Provided by Epsilon for your program

1. Select the HTTP method shown in the configuration table (typically GET unless noted otherwise).

1. Configure authentication (headers, query parameters, or OAuth) exactly as specified in the table and in the vendor documentation.

1. Define path, query, and header parameters, and map variables to profile or contextual data where needed.

1. Paste a sample JSON response so fields can be detected and mapped.

1. Select the fields required for personalization in the response payload mapping.

1. Configure timeout, retry, and caching policies based on expected volume.

1. Test the connection, then activate the integration.

The table below lists example values for this integration request.

+++ Sample integration fields

Example pattern: `https://{your-instance}.epsilon3.io/api/v1/planning/events` with `start` and `end` query parameters and header-based API key. Confirm with Epsilon before production.

| Field | Value |
| --- | --- |
| **URL** | `https://{{your-instance}}.epsilon3.io/api/v1/planning/events` |
| **HTTP method** | `GET` |
| **Policy** | Configure policy level details as per your need. |
| **Response payload** | Select and configure the desired response fields for use during authoring, based on the API response. |

**Path parameters**

| Path parameter | Name | Default value |
| --- | --- | --- |
| `your-instance` | `your-instance` | `<your_instance>` |

**Headers**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| Content-Type (default) | Content-Type | Constant | application/json | Yes (on) |

**Query parameters**

| Parameter | Name | Type | Value | Mandatory |
| --- | --- | --- | --- | --- |
| `start` | `start` | Variable | 2019-08-24T14:15:22Z | Yes (on) * |
| `end` | `end` | Variable | 2019-08-24T14:15:22Z | Yes (on) * |
| `eventType` | `eventType` | Variable | scheduled / unscheduled | No (off) |
| `exclude_recurrences` | `exclude_recurrences` | Variable | true / false | No (off) |

\* Optional for `eventType` = `unscheduled`, and for `exclude_recurrences` = `true`.

**Authentication**

| Type | API key name | API key value | Location |
| --- | --- | --- | --- |
| API Key | `<your_username>` | `<EPSILON3_API_KEY>` | Header |

+++

