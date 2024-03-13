---
title: List placements
description: Placements are containers that are used to showcase your offers.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 52fbf683-d86f-43c6-be1a-c06141b64b16
---
# List placements {#list-placements}

Placements are containers that are used to showcase your offers. A placement helps ensure that the right offer content shows up in the right location within your message. When you add content to an offer, you will be asked to select a placement in which that content can be shown.

You can view a list of all placements within a container by performing a single GET request to the [!DNL Offer Library] API.

**API format**

```http
GET /{ENDPOINT_PATH}/{CONTAINER_ID}/queries/core/search?schema={SCHEMA_PLACEMENT}&{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the placements are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |
| `SCHEMA_PLACEMENT}` | Defines the schema associated with placements. | `https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=2` |

## Using query parameters {#using-query-parameters}

You can use query parameters to page and filter results when listing resources.

### Paging {#paging}

The most common query parameters for paging include:

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `q` | An optional query string to search for in selected fields. The query string should be lowercase and can be surrounded by double quotes to prevent it from being tokenized and to escape special characters. The characters `+ - = && \|\| > < ! ( ) { } [ ] ^ \" ~ * ? : \ /` have special meaning and should be escaped with a backslash when appearing in the query string. | Website JSON |
| `qop` | Applies AND or OR operator to values in q query string param. | `AND` / `OR` |
| `field` | Optional list of fields to limit the search to. This param can be repeated like so: field=field1[,field=field2,…] and (path expressions are in the form of dot separated paths such as _instance.xdm:name) | `_instance.xdm:name` |
| `orderBy` | Sort results by a specific property. Adding a `-` before title (`orderby=-title`) will sort items by title in descending order (Z-A). | `-repo:createdDate` |
| `limit` | Limit the number of placements returned. | `limit=5` |

**Request**

```shell
curl -X GET \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?schema=https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4&limit=2' \
  -H 'Accept: *,application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns a list of placements that are present within the container you have access to.

```json

{
    "containerId": "e0bd8463-0913-4ca1-bd84-6309134ca1f6",
    "schemaNs": "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4",
    "requestTime": "2023-10-21T19:48:51.843067Z",
    "_embedded": {
    "results": [
        {
                "instanceId": "0feb6a80-0f32-11eb-8110-e17787c335b5",
            "schemas": [
                    "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4"
            ],
                "productContexts": [
                    "acp"
                ],
                "repo:etag": 2,
                "repo:createdDate": "2023-10-15T22:02:05.480449Z",
                "repo:lastModifiedDate": "2023-10-15T22:13:00.278175Z",
                "repo:createdBy": "{CREATED_BY}",
                "repo:lastModifiedBy": "{MODIFIED_BY}",
                "repo:createdByClientId": "{CREATED_CLIENT_ID}",
                "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}",
                "_instance": {
                    "xdm:name": "New placement name",
                    "xdm:componentType": "https://ns.adobe.com/experience/offer-management/content-component-html",
                    "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                    "xdm:description": "Updated placement description",
                    "@id": "xcore:offer-placement:12466ef35fc5baa0"
                },
                "_links": {
                    "self": {
                        "name": "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4#0feb6a80-0f32-11eb-8110-e17787c335b5",
                        "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/0feb6a80-0f32-11eb-8110-e17787c335b5",
                        "@type": "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4"
                    }
            }
        },
        {
                "instanceId": "269192b0-f8f2-11ea-8723-916b9fbadc53",
            "schemas": [
                    "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4"
                ],
                "productContexts": [
                    "acp"
            ],
                "repo:etag": 1,
                "repo:createdDate": "2023-09-17T14:29:10.107121Z",
                "repo:lastModifiedDate": "2023-09-17T14:29:10.107121Z",
                "repo:createdBy": "{CREATED_BY}",
                "repo:lastModifiedBy": "{MODIFIED_BY}",
                "repo:createdByClientId": "{CREATED_CLIENT_ID}",
                "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}",
                "_instance": {
                    "xdm:componentType": "https://ns.adobe.com/experience/offer-management/content-component-html",
                    "xdm:name": "demo placement",
                    "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                    "@id": "xcore:offer-placement:1221fac4e7340521"
                },
                "_links": {
                    "self": {
                        "name": "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4#269192b0-f8f2-11ea-8723-916b9fbadc53",
                        "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/269192b0-f8f2-11ea-8723-916b9fbadc53",
                        "@type": "https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4"
            }
                },
                "sandboxName": "ode-prod-va7-edge-testing"
        }
    ],
        "total": 17,
        "count": 2
    },
    "_links": {
        "self": {
            "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?schema=https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4&limit=2",
            "@type": "https://ns.adobe.com/experience/xcore/hal/results"
        },
        "next": {
            "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?start=269192b0-f8f2-11ea-8723-916b9fbadc53&orderby=instanceId&schema=https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4&limit=2",
            "@type": "https://ns.adobe.com/experience/xcore/hal/results"
        }
    }
}
```
