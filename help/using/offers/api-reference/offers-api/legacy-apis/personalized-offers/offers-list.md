---
title: List personalized offers
description: A personalized offer is a customizable marketing message based on eligibility rules and constraints.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 50f4119f-c730-4883-867e-eac83793dced
---
# List personalized offers {#list-personalized-offers}

A personalized offer is a customizable marketing message based on eligibility rules and constraints.

You can view a list of all personalized offers within a container by performing a single GET request to the [!DNL Offer Library] API.

**API format**

```http
GET /{ENDPOINT_PATH}/{CONTAINER_ID}/queries/core/search?schema={SCHEMA_PERSONALIZED_OFFER}&{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the personalized offers are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |
| `{SCHEMA_PERSONALIZED_OFFER}` | Defines the schema associated with personalized offers. | `https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=1` |

**Request**

```shell
curl -X GET \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?schema=https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5&limit=1' \
  -H 'Accept: *,application/vnd.adobe.platform.xcore.hal+json; schema="https://ns.adobe.com/experience/xcore/hal/results"' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

## Using query parameters {#using-query-parameters}

You can use query parameters to page and filter results when listing resources.

### Paging {#paging}

The most common query parameters for paging include:

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `q` | An optional query string to search for in selected fields. The query string should be lowercase and can be surrounded by double quotes to prevent it from being tokenized and to escape special characters. The characters `+ - = && \|\| > < ! ( ) { } [ ] ^ \" ~ * ? : \ /` have special meaning and should be escaped with a backslash when appearing in the query string. | `discounted offers` |
| `qop` | Applies AND or OR operator to values in q query string param. | `AND` / `OR` |
| `field` | Optional list of fields to limit the search to. This param can be repeated like so: field=field1[,field=field2,…] and (path expressions are in the form of dot separated paths such as _instance.xdm:name) | `_instance.xdm:name` |
| `orderBy` | Sort results by a specific property. Adding a `-` before title (`orderby=-title`) will sort items by title in descending order (Z-A). | `-repo:createdDate` |
| `limit` | Limit the number of personalized offers returned. | `limit=5` |

**Response**

A successful response returns a list of personalized offers that are present within the container you have access to.

```json
{
    "containerId": "e0bd8463-0913-4ca1-bd84-6309134ca1f6",
    "schemaNs": "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5",
    "requestTime": "2023-10-22T20:36:50.408105Z",
    "_embedded": {
    "results": [
        {
                "instanceId": "2cdb4d10-149e-11eb-b1a9-a779d2fe8690",
            "schemas": [
                    "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5"
            ],
                "productContexts": [
                    "acp"
                ],
                "repo:etag": 2,
                "repo:createdDate": "2023-10-22T19:38:35.489354Z",
                "repo:lastModifiedDate": "2023-10-22T19:45:43.839088Z",
                "repo:createdBy": "{CREATED_BY}",
                "repo:lastModifiedBy": "{MODIFIED_BY}",
                "repo:createdByClientId": "{CREATED_CLIENT_ID}",
                "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}",
                "_instance": {
                    "xdm:name": "Checking Advanced",
                    "xdm:representations": [
                        {
                            "xdm:components": [
                                {
                                    "dc:format": "image/png",
                                    "repo:id": "urn:aaid:sc:US:7db21be9-89ee-472a-b2c9-91f7a39ada51",
                                    "repo:resolveURL": "https://platform-cs-va6.adobe.io/content/storage/id/urn:aaid:sc:US:7db21be9-89ee-472a-b2c9-91f7a39ada51/:rendition;size=300",
                                    "repo:name": "mobile-check-deposit.png",
                                    "dc:language": [
                                        "en-us"
                                    ],
                                    "@type": "https://ns.adobe.com/experience/offer-management/content-component-imagelink",
                                    "xdm:deliveryURL": ""
                                }
                            ],
                            "xdm:channel": "https://ns.adobe.com/xdm/channel-types/offline",
                            "xdm:placement": "xcore:offer-placement:124f4e33724bb15f"
                        },
                {
                            "xdm:components": [
                        {
                                    "dc:format": "text/html",
                                    "repo:name": "my content",
                                    "dc:language": [
                                "en-us"
                            ],
                                    "xdm:content": "{\n\"foo\": \"bar\"\n}",
                                    "@type": "https://ns.adobe.com/experience/offer-management/content-component-html"
                        }
                            ],
                            "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                            "xdm:placement": "xcore:offer-placement:124e0be5699743d3"
                }
            ],
                    "xdm:rank": {
                        "xdm:priority": 10
                    },
                    "xdm:characteristics": {
                        "PROD": "checking",
                        "offer_code": "CHECK200",
                        "region": "NA"
            },
                    "xdm:selectionConstraint": {
                        "xdm:startDate": "2023-10-22T07:00:00.000Z",
                        "xdm:endDate": "2023-12-31T08:00:00.000Z",
                        "xdm:eligibilityRule": "xcore:eligibility-rule:124f4f57259caba5"
            },
                    "xdm:status": "draft",
                    "xdm:cappingConstraint": {
                        "xdm:globalCap": 1000
                    },
                    "xdm:tags": [
                        "xcore:tag:124f4e5c8a00cd92",
                        "xcore:tag:1229cf47455177b1"
                    ],
                    "@id": "xcore:personalized-offer:124f513c290bb16e"
                },
                "_links": {
                    "self": {
                        "name": "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5#2cdb4d10-149e-11eb-b1a9-a779d2fe8690",
                        "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/2cdb4d10-149e-11eb-b1a9-a779d2fe8690",
                        "@type": "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5"
                    }
                },
                "sandboxName": "ode-prod-va7-edge-testing"
        }
    ],
        "total": 15,
        "count": 1
    },
    "_links": {
        "self": {
            "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?schema=https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5&orderby=-repo:createdDate&limit=1",
            "@type": "https://ns.adobe.com/experience/xcore/hal/results"
        },
        "next": {
            "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/queries/core/search?start=1603395515489%2C2cdb4d10-149e-11eb-b1a9-a779d2fe8690&schema=https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5&orderby=-repo%3AcreatedDate%2CinstanceId&limit=1",
            "@type": "https://ns.adobe.com/experience/xcore/hal/results"
        }
    }
}
```
