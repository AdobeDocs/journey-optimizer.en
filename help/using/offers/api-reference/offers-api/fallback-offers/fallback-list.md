---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: List fallback offers
description: A fallback offer is sent to customers if they are not eligible for other offers
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: dd95c040-d905-4f5a-8cc5-58e39082e57e
version: Journey Orchestration
---
# List fallback offers {#list-fallback-offers}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)


A fallback offer is sent to customers if they are not eligible for other offers. The steps to create a fallback offer consist in creating one or several representations, like when creating an offer.

You can view a list of all fallback offers by performing a single GET request to the [!DNL Offer Library] API.

**API format**

```http
GET /{ENDPOINT_PATH}/offers?offer-type=fallback&{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=2` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/offers?offer-type=fallback&limit=2' \
-H 'Accept: *,application/json' \
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
| `property` | An optional property filter: <ul><li>The properties are grouped by AND operation.</li><li>Parameters can be repeated like so: property={PROPERTY_EXPR}[&property={PROPERTY_EXPR2}...] or property={PROPERTY_EXPR1}[,{PROPERTY_EXPR2}...]</li><li>Property expressions are in format `[!]field[op]value`, with `op` in `[==,!=,<=,>=,<,>,~]`, supporting regular expressions.</li></ul> | `property=name!=abc&property=id~.*1234.*&property=description equivalent with property=name!=abc,id~.*1234.*,description.` |
| `orderBy` | Sort results by a specific property. Adding a - before name (orderby=-name) will sort items by name in descending order (Z-A). Path expressions are in the form of dot separated paths. This parameter can be repeated like so: `orderby=field1[,-fields2,field3,...]` | `orderby=id`,`-name` |
| `limit` | Limit the number of entities returned. | `limit=5` |

**Response**

A successful response returns a list of fallback offers that you have access to.

```json
{
      "results": [
        {
            "created": "2023-06-08T14:04:41.011+00:00",
            "modified": "2023-06-08T14:04:41.011+00:00",
            "etag": 1,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.8"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "fallbackOffer1234",
            "name": "Fallback Offer Web",
            "description": "Fallback Offer Web Description",
            "status": "draft",
            "representations": [
                {
                    "channel": "https://ns.adobe.com/xdm/channel-types/web",
                    "placement": "offerPlacement5678",
                    "components": [
                        {
                            "type": "imagelink",
                            "format": "image/png",
                            "deliveryURL": "https://mysite.com"
                        }
                    ]
                }
            ]
        },
        {
            "created": "2022-10-07T11:23:55.885+00:00",
            "modified": "2022-10-07T11:23:55.885+00:00",
            "etag": 1,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.7"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "fallbackOffer5678",
            "name": "Fallback Offer email",
            "status": "approved",
            "representations": [
                {
                    "channel": "https://ns.adobe.com/xdm/channel-types/email",
                    "placement": "offerPlacement1234",
                    "components": [
                        {
                            "type": "component-text",
                            "format": "text/template",
                            "content": "Get free shipping!"
                        }
                    ]
                }
            ],
            "labels": [
                "core/C1"
            ]
        }
    ],
    "count": 2,
    "total": 3,
    "_links": {
        "self": {
            "href": "/offers?offer-type=fallback&href={SELF_HREF}&limit=2",
            "type": "application/json"
        },
        "next": {
            "href": "/offers?offer-type=fallback&href={NEXT_HREF}&limit=2",
            "type": "application/json"
        }
    }
}
```
