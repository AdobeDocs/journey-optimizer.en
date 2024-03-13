---
title: lookup fallback offers
description: A fallback offer is sent to customers if they are not eligible for other offers
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: e470d491-b30b-4d26-83a6-e5b34e49fe61
---
# Look up fallback offers {#look-up-fallback-offers}

You can look up specific fallback offers by making a GET request to the [!DNL Offer Library] API that includes either the fallback offer `@id` or the name of the fallback offer in the request path.

**API format**

```http
GET /{ENDPOINT_PATH}/{CONTAINER_ID}/queries/core/search?schema={SCHEMA_FALLBACK_OFFER}&{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the fallback offers are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |
| `{SCHEMA_FALLBACK_OFFER}` | Defines the schema associated with fallback offers. | `https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1` |
| `id` | A string used to match the `@id` property of the entities. The string is matched exactly. The parameters `id` and `name` cannot be used together. | `xcore:fallback-offer:122206064e0d98df` |
| `name` | A string used to match the xdm:name property of the entities. The string is matched exactly, with capitalization, but wild card characters can be used. The parameters `id` and `name` cannot be used together | `F1: Web fallback` |

**Request**

```shell
curl -X GET \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances?schema=https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1&id=xcore:fallback-offer:122206064e0d98df' \
  -H 'Accept: *,application/vnd.adobe.platform.xcore.hal+json; schema="https://ns.adobe.com/experience/xcore/hal/results"' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the details of the placement including information about your container ID, instance ID and, unique fallback offer `@id`.

```json
{
    "containerId": "e0bd8463-0913-4ca1-bd84-6309134ca1f6",
    "schemaNs": "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1",
    "requestTime": "2023-10-21T22:21:50.658080Z",
    "_embedded": {
        "results": [
            {
                "instanceId": "053bc610-f8f9-11ea-ad6e-775ad2c9b1a1",
    "schemas": [
                    "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.5"
                ],
                "productContexts": [
                    "acp"
    ],
                "repo:etag": 3,
                "repo:createdDate": "2023-09-17T15:18:20.657299Z",
                "repo:lastModifiedDate": "2023-10-02T02:34:48.034583Z",
                "repo:createdBy": "712B3670554A7AF17F000101@AdobeID",
                "repo:lastModifiedBy": "68D9EA8559BC2D810A495CC2@AdobeID",
                "repo:createdByClientId": "exc_app",
                "repo:lastModifiedByClientId": "exc_app",
                "_score": 0,
                "_instance": {
                    "xdm:name": "F1: Web fallback ",
                    "xdm:representations": [
                        {
                            "xdm:components": [
        {
                                    "xdm:content": "aaa",
                                    "@type": "https://ns.adobe.com/experience/offer-management/content-component-json",
                                    "dc:format": "application/json",
                                    "repo:name": "aa"
                                }
                            ],
                            "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                            "xdm:placement": "xcore:offer-placement:122201b2150d98c2"
                        },
                        {
                            "xdm:components": [
                                {
                                    "xdm:content": "bb",
                                    "@type": "https://ns.adobe.com/experience/offer-management/content-component-html",
                                    "dc:format": "text/html",
                                    "repo:name": "bb"
                                }
                            ],
                            "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                            "xdm:placement": "xcore:offer-placement:122201c34354a2b4"
                        },
                {
                            "xdm:components": [
                                {
                                    "xdm:deliveryURL": "https://mysite.com",
                                    "@type": "https://ns.adobe.com/experience/offer-management/content-component-imagelink",
                                    "dc:format": "image/png",
                                    "repo:name": "ll"
                                }
                            ],
                            "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                            "xdm:placement": "xcore:offer-placement:122207eddb05205a"
                        }
                    ],
                    "xdm:status": "approved",
                    "xdm:tags": [],
                    "@id": "xcore:fallback-offer:122206064e0d98df"
                },
                "_links": {
                    "self": {
                        "name": "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.5#053bc610-f8f9-11ea-ad6e-775ad2c9b1a1",
                        "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/053bc610-f8f9-11ea-ad6e-775ad2c9b1a1",
                        "@type": "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.5"
                    }
                },
                "sandboxName": "ode-prod-va7-edge-testing"
            }
        ],
        "total": 1,
        "count": 1
    },
    "_links": {
        "self": {
            "href": "/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances?schema=https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1&id=xcore:fallback-offer:122206064e0d98df",
            "@type": "https://ns.adobe.com/experience/xcore/hal/results"
                }
        }
}
```
