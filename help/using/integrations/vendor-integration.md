---
solution: Journey Optimizer
product: journey optimizer
title: Vendor Integration Documentation
description: Use Adobe Journey Optimizer Integrations with any external platform that exposes a valid API—plus engineering-tested vendor patterns for confidence when you design your setup.
feature: Integrations
topic: Content Management
role: User
level: Intermediate
keywords: integration, vendor, third-party
---

# Vendor integration documentation {#vendor-integration}

You can use **Integrations** in Adobe Journey Optimizer to call **external systems over HTTP** when each system exposes an **API endpoint** that suits your use case and is compatible with how Integrations issues requests and consumes responses. For complete workflow, see [Work with Integrations](external-sources.md).

The list of third-party solutions described is illustrative, not exhaustive. Other platforms may be used where they satisfy product requirements. The sections that follow are intended as reference patterns to support implementation of comparable integrations.


## Operational guardrails {#operational-guardrails}

Apply the following when you configure any integration in this guide or a similar vendor:

* **Response format:** Integrations map fields from **JSON** responses. Design calls so the API returns JSON suitable for mapping at authoring time.
* **Payload and fields:** Request and map only the attributes you need. Smaller responses reduce latency and limit exposure of sensitive data.
* **Endpoint shape:** Prefer stable, **single-resource** retrieval (for example one entry, product, or member) over broad list or pagination endpoints when the product expects targeted lookups. See [Limitations & exclusions](#limitations-exclusions) and [Work with Integrations](external-sources.md).
* **Volume and reliability:** Respect the vendor's **rate limits**; configure **timeout**, **retry**, and **cache** policy for your channel (for example batch email vs transactional sends) and validate under load.
* **Security:** Store and rotate tokens, API keys, and OAuth credentials according to your organization's policies. Do not embed secrets in message content.

## Quick navigation {#quick-navigation}

Use these grouped links to jump to the relevant vendor pattern quickly:

* **Content and CMS:** [Contentful](#contentful), [Sitecore](#sitecore), [Salsify](#salsify), [Contentstack](#contentstack), [Akeneo](#akeneo), [Magnolia](#magnolia)
* **Loyalty and rewards:** [Voucherify](#voucherify), [Talon.One](#talon-one), [Antavo](#antavo), [Salesforce Loyalty](#salesforce-loyalty), [Capillary](#capillary)
* **Templates and messaging:** [Stensul](#stensul), [Marigold](#marigold), [Adobe Target Recommendations](#adobe-target-recommendations)
* **Data, weather, and operations:** [AccuWeather](#accuweather), [ShipStation](#shipstation), [RevenueCat](#revenuecat), [Databricks](#databricks)
* **Reviews, consent, and social:** [Bynder](#bynder), [Trustpilot](#trustpilot), [Bazaarvoice](#bazaarvoice), [OneTrust](#onetrust), [Meta](#meta), [Aprimo](#aprimo), [Epsilon (Epsilon3)](#epsilon)

## Contentful {#contentful}

Contentful is a headless CMS for structured entries and assets over REST or GraphQL, so Journey Optimizer can pull content at send or open time.

The following use cases are common:

* Localized hero blocks, alt text, and CTAs in email.
* Product or promo entries in dynamic modules.
* Entry-by-ID retrieval for personalized messaging.

The following prerequisites apply:

* Contentful space with Delivery API access and a read-oriented API key.
* Clear content types and field IDs; admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Broad listing or paginated Contentful APIs are a poor fit for this pattern—prefer retrieval calls that target a specific entry or asset.
* Write-back or two-way synchronization is outside the scope of this example.

### Configuration steps

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

+++ Sample integration fields

Sample integration fields (align with the [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/){target="_blank"} for your space and environment):

| Field | Value |
| --- | --- |
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

## Stensul {#stensul}

Stensul is an email creation platform for approved templates; Journey Optimizer can consume template metadata and structured regions through its API.

The following use cases are common:

* Import approved templates and map regions to profile attributes.
* Reuse governed blocks for scalable campaign builds.

The following prerequisites apply:

* Stensul account with API access and published templates with defined tokens.
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* In-place WYSIWYG editing of Stensul templates inside Journey Optimizer is not covered here.
* Large or complex HTML in template payloads may require security review and sanitization.

### Configuration steps

1. In Journey Optimizer, go to Configurations > Manage, then select Create Integration.

1. Enter an integration name.

1. Configure the endpoint using the Stensul Templates API URL (example pattern): `https://api.stensul.com/v1/templates/{template_id}`

1. Configure authentication (API key or OAuth per Stensul API documentation).

1. Define path variables (e.g., template ID).

1. Paste a sample JSON response for field detection.

1. Map required template fields to Journey Optimizer personalization fields.

1. Test connection and activate.

## AccuWeather {#accuweather}

AccuWeather exposes forecast and location REST APIs so messages can include weather-aware snippets.

The following use cases are common:

* Short forecasts in email or push.
* Tailoring based on forecast values tied to profile or context.

The following prerequisites apply:

* API subscription and key; location key or a city search flow.
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Confirm the JSON response shape for your AccuWeather subscription tier; Integrations maps fields from JSON responses.
* Observe AccuWeather rate limits and recommended caching.
* Resolving `locationKey` often requires a separate geolocation or city-search request before forecast calls.

### Configuration steps

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

## Sitecore {#sitecore}

Sitecore Content Hub and related cloud APIs support DAM-style download and metadata flows; the example pattern below centers on a download order by ID.

The following use cases are common:

* Asset or download metadata in email content.
* Alignment with DAM workflows managed in Sitecore.

The following prerequisites apply:

* Tenant URL and credentials (bearer or token per your API surface).
* Admin access in Journey Optimizer to create integrations.

The following limitations and exclusions apply:

* Hostnames and paths vary by Sitecore product—use only endpoints your tenant exposes.
* OAuth access tokens, refresh, and lifetimes must follow Sitecore security policy.

### Configuration steps

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

## Bynder {#bynder}

Bynder is a DAM with REST APIs; integrations commonly use OAuth 2.0 for read-only metadata or asset URLs.

The following use cases are common:

* Pull asset metadata or delivery URLs into messages.
* Keep creative approved in Bynder aligned with journeys.

The following prerequisites apply:

* Portal domain and OAuth client (or approved token approach).
* Scopes for read-only access; admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Pagination and OAuth token refresh must follow Bynder's API rules.
* Large paginated responses: map only the fields required for personalization.

### Configuration steps

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

## Voucherify {#voucherify}

Voucherify provides promotions and loyalty REST APIs (campaigns, vouchers, loyalty programs).

The following use cases are common:

* Read loyalty or promotion state for offers in content.
* Show tier or balance where appropriate.

The following prerequisites apply:

* Application ID and secret (per region/cluster); clarity on which loyalty or campaign endpoints you call.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Avoid exposing internal promotion or campaign identifiers in customer-facing errors or message content.
* Application-level rate limits apply—configure retries and caching per Voucherify guidance.

### Configuration steps

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

## Marigold {#marigold}

Marigold exposes loyalty and engagement APIs; hosts differ by geography (EU vs US module hostnames).

The following use cases are common:

* Enrich messages with loyalty or preference data from Marigold programs.

The following prerequisites apply:

* Base URL and credentials from your contract; least-privilege API user when possible.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Endpoints vary by Marigold product—validate with Marigold support for your deployment.
* Personal data in responses must comply with your DPA and retention policies.

### Configuration steps

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

1. Europe – https://{{customername}}.module.slgnt.eu
   USA – https://{{customername}}.module.slgnt.us

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

## Adobe Target Recommendations {#adobe-target-recommendations}

Adobe Target includes Recommendations and delivery APIs for server-side or integrated experiences, subject to entitlements.

The following use cases are common:

* Inject recommendations into Journey Optimizer-authored experiences.
* Align keys with profile or Experience Platform context.

The following prerequisites apply:

* Target with Recommendations; IMS org and supported authentication.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Recommendation and delivery APIs require specific parameters (for example mbox or product identifiers)—follow Adobe Target documentation.
* Tune latency and caching for your send volume and use case.

### Configuration steps

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

## Aprimo {#aprimo}

Aprimo combines marketing operations and DAM APIs for records, assets, and metadata.

The following use cases are common:

* Approved record or asset fields in dynamic content.
* Governed DAM workflows in regulated industries.

The following prerequisites apply:

* Tenant URL and credentials (OAuth or API key per your setup).
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Aprimo field-level security must align with the attributes you map in Journey Optimizer.
* Large HAL or JSON payloads: restrict mapped fields to the minimum required set.

### Configuration steps

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

## Talon.One {#talon-one}

Talon.One is a promotion and loyalty rules engine with REST APIs for sessions, effects, and profiles.

The following use cases are common:

* Cart- or profile-level promotions in personalized content.
* Loyalty progress or rewards display.

The following prerequisites apply:

* API key and deployment-specific base URL; identifiers for application or campaign scope.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Session-heavy flows may require careful mapping to the Integrations request model.
* Observe Talon.One rate limits and idempotency guidance.

### Configuration steps

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

## Antavo {#antavo}

Antavo is an enterprise loyalty platform with REST APIs for members, rewards, and events.

The following use cases are common:

* Points, tier, or rewards in email or push.
* Offers driven by loyalty state.

The following prerequisites apply:

* Stack URL and API credentials; program or shop identifiers as required.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Customer PII must be handled under Antavo agreements and your privacy policies.
* Confirm API versions and stable endpoints with Antavo for your environment.

### Configuration steps

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

## Salesforce Loyalty {#salesforce-loyalty}

Salesforce Loyalty Management exposes REST APIs on the Salesforce platform for members, programs, and transactions.

The following use cases are common:

* Surface tier, points, or benefits in journeys.
* Align messaging with CRM and loyalty data.

The following prerequisites apply:

* Salesforce instance, connected app or integration user, and OAuth appropriate to your org.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Salesforce API limits and OAuth token refresh must be designed into your integration.
* Field-level security and sharing rules govern which fields appear in API responses.

### Configuration steps

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

## Epsilon (Epsilon3) {#epsilon}

Epsilon exposes APIs per enterprise agreement; base URLs and auth come from your account team (the Events API example below is illustrative).

The following use cases are common:

* Loyalty or offer attributes when exposed through supported JSON APIs.

The following prerequisites apply:

* Credentials and endpoints from Epsilon; admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Endpoints and hosts are customer-specific—do not deploy without documentation from your Epsilon account team.

### Configuration steps

1. Follow [Work with Integrations](external-sources.md). Do not guess public URLs—use the specification from Epsilon, paste sample JSON, map fields, test, activate.

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

## Trustpilot {#trustpilot}

Trustpilot provides APIs for business and review summary data where your use case and contract allow.

The following use cases are common:

* Review counts or ratings in marketing content compliant with Trustpilot terms.

The following prerequisites apply:

* API key and approved use case; business identifiers for queries.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Use of Trustpilot data must comply with Trustpilot branding and data-use policies.
* Rate limits apply to review summary and related endpoints.

### Configuration steps

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

## ShipStation {#shipstation}

ShipStation offers shipping and order APIs for carriers, labels, and tracking.

The following use cases are common:

* Order status, tracking links, or delivery ETAs in transactional messages.

The following prerequisites apply:

* API key and secret (Basic auth per ShipStation docs).
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Do not expose ShipStation API keys in message content; keep credentials in the integration configuration only.
* Paginated list endpoints may be a poor fit for Integrations—prefer single-resource GETs when possible.

### Configuration steps

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

+++ Sample integration fields

The following **Get Timer** example illustrates one ShipStation automation timing call—use the exact path and auth from your ShipStation integration guide when reproducing it in Journey Optimizer.

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

## RevenueCat {#revenuecat}

RevenueCat provides subscription status and entitlements APIs for apps.

The following use cases are common:

* Reflect subscription state in lifecycle campaigns where policy allows.

The following prerequisites apply:

* Secret API key and app identifiers; stable mapping between profiles and RevenueCat customer IDs.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Protect secret API keys and follow your rotation policies.
* Subscription and entitlement data is sensitive—meet privacy and consent requirements.

### Configuration steps

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

## Salsify {#salsify}

Salsify is a PIM with APIs for products, channels, and digital assets.

The following use cases are common:

* Product attributes or media URLs in email.
* Messaging aligned with syndicated catalog data.

The following prerequisites apply:

* API token and organization context; product IDs resolvable from profile or context.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Very large catalogs: avoid bulk list endpoints if Integrations expects per-entity retrieval.
* Attribute visibility can be limited by Salsify role permissions.

### Configuration steps

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

## Contentstack {#contentstack}

Contentstack is a headless CMS; REST delivery is typical for JSON field mapping in Journey Optimizer.

The following use cases are common:

* Entries for banners or promos with locale-aware parameters.

The following prerequisites apply:

* Stack API key, delivery token, environment name, and content type UIDs.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* This pattern uses REST JSON for field mapping; GraphQL delivery follows a different integration path.
* Use production-appropriate delivery tokens; preview and published flows are not interchangeable.

### Configuration steps

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

## Capillary {#capillary}

Capillary provides loyalty and engagement APIs common in retail stacks.

The following use cases are common:

* Points, tier, or offers inside personalized journeys.

The following prerequisites apply:

* API host and authentication (often signed requests—follow Capillary docs).
* Program identifiers for your endpoint.

The following limitations and exclusions apply:

* Authentication schemes and regional hosts vary by deployment—confirm with Capillary for your stack.

### Configuration steps

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

## Akeneo {#akeneo}

Akeneo PIM exposes REST APIs for products, attributes, and media.

The following use cases are common:

* Governed product data in email modules.
* Channel-specific attributes in journeys.

The following prerequisites apply:

* PIM base URL and OAuth client; product UUID or identifier strategy.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* PIM responses can be large—map only the attributes required for personalization.
* Write operations are outside the scope of typical read-only personalization examples.

### Configuration steps

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

## Magnolia {#magnolia}

Magnolia offers headless and REST delivery endpoints depending on deployment.

The following use cases are common:

* Content nodes or fragments for marketing modules.

The following prerequisites apply:

* Instance URL and token or basic auth; workspace and paths for delivery.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* REST delivery URLs depend on installed Magnolia modules and configuration.

### Configuration steps

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

+++ Sample integration fields

Example pattern: `https://{domain}/magnoliaAuthor/.rest/delivery/...` or public delivery tours-style URLs—your paths depend on installed modules. See [Magnolia documentation](https://docs.magnolia-cms.com/){target="_blank"}.

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

## Bazaarvoice {#bazaarvoice}

Bazaarvoice provides ratings, reviews, and UGC APIs.

The following use cases are common:

* Review summaries or ratings in email when policy allows.

The following prerequisites apply:

* API passkey and client identifiers from your contract.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Display of ratings and reviews must follow Bazaarvoice content policies.
* Rate limits and caching rules apply per API key.

### Configuration steps

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

## OneTrust {#onetrust}

OneTrust exposes privacy and consent APIs (product-specific URLs and schemas).

The following use cases are common:

* Read consent or preference signals for conditional content where architecture and legal review allow.

The following prerequisites apply:

* API credentials and regional base URL; legal approval for fields used in messaging.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Consent and preference data are highly regulated—coordinate with privacy and legal teams.
* API paths and payloads differ by OneTrust product—use documentation for your subscription.

### Configuration steps

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

### Preference center schema (published)

Example pattern (fragment): `https://{tenant}.my.onetrust.com/api/consentmanager/v2/preferencecenters/{preferencecenterid}/schema?state=PUBLISHED`. Confirm the exact path in [OneTrust Developer](https://developer.onetrust.com/){target="_blank"}.

## Meta {#meta}

Meta Graph and Marketing APIs expose catalog and campaign objects for authorized business integrations.

The following use cases are common:

* Enrich content with attributes from Meta where tokens and policies allow.

The following prerequisites apply:

* System user or app token with correct permissions; Business Manager alignment.
* Admin access in Journey Optimizer.

The following limitations and exclusions apply:

* Short-lived access tokens require a renewal or long-lived strategy suited to server-side integrations.
* Comply with Meta Platform Terms; do not log tokens or other secrets in message payloads.

### Configuration steps

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

## Databricks {#databricks}

Databricks provides SQL and REST APIs over lakehouse data; earlier drafts combined statement execution guidance with a **jobs/get** sample.

The following use cases are common:

* Small, denormalized attributes from governed tables for personalization (strict least privilege).

The following prerequisites apply:

* Workspace host, token or OAuth per org policy; service principal with minimal scope.
* Admin access in Journey Optimizer.

### Configuration steps

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
