---
title: List personalized offers
description: A personalized offer is a customizable marketing message based on eligibility rules and constraints.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 45d51918-1106-4b6b-b383-8ab4d9a4f7af
---

# List personalized offers {#list-personalized-offers}

A personalized offer is a customizable marketing message based on eligibility rules and constraints.

You can view a list of all personalized offers by performing a single GET request to the [!DNL Offer Library] API.

**API format**

```http
GET /{ENDPOINT_PATH}/offers?offer-type=personalized&{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` |The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=2` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/offers?offer-type=personalized&limit=2' \
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
| `limit` | Limit the number of placements returned. | `limit=5` |

**Response**

A successful response returns a list of personalized offers that are present along with those that you have access to.

```json
{
    "results": [
        {
            "created": "2023-05-15T14:35:16.781+00:00",
            "modified": "2023-05-15T14:38:26.691+00:00",
            "etag": 2,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.15"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "personalizedOffer1234",
            "name": "Test personalized offer with frequency constraint",
            "status": "draft",
            "representations": [
                {
                    "channel": "https://ns.adobe.com/xdm/channel-types/web",
                    "placement": "offerPlacement1234",
                    "components": [
                        {
                            "type": "html",
                            "format": "text/html",
                            "language": [
                                "en-us"
                            ],
                            "content": "Hello You qualify for our Discount of 60%"
                        }
                    ]
                }
            ],
            "selectionConstraint": {
                "startDate": "2022-07-27T05:00:00.000+00:00",
                "endDate": "2023-07-29T05:00:00.000+00:00",
                "profileConstraintType": "none"
            },
            "rank": {
                "priority": 0
            },
            "cappingConstraint": {},
            "frequencyCappingConstraints": [
                {
                    "enabled": false,
                    "limit": 1,
                    "startDate": "2023-05-15T14:25:49.622+00:00",
                    "endDate": "2023-05-25T14:25:49.622+00:00",
                    "scope": "global",
                    "entity": "offer",
                    "repeat": {
                        "enabled": false,
                        "unit": "month",
                        "unitCount": 1
                    }
                }
            ]
        }
    ],
    "count": 1,
    "total": 1,
    "_links": {
        "self": {
            "href": "/offers?offer-type=personalized&href={SELF_HREF}",
            "type": "application/json"
        }
    }
}
```

Perform pagination if multiple personalized offers are missing from the response.

**Response**

```json
{
    "results": [...],
    "count": 2,
    "total": 43,
    "_links": {
        "self": {
        "href": "/offers?orderby=-modified&limit=2&offer-type=PERSONALIZED",
        "type": "application/json"
        },
        "next": {
        "href": "/offers?orderby=-modified&limit=2&start={TIMESTAMP}&offer-type=PERSONALIZED",
        "type": "application/json"
        }
    }
    }
```

| Metric  | Description |
|---------|-------------|
| `total` | The number of personalized offers. |
| `count` | The number of offers returned in this response. |

Retrieve the endpont from `_links.next.href` such as `/offers?orderby=-modified&limit=2&start={TIMESTAMP}&offer-type=PERSONALIZED` and append it to the API.

**API Format**

```http
GET /{ENDPOINT_PATH}/offers?orderby=-modified&limit=2&start={TIMESTAMP}&offer-type=PERSONALIZED
```

```json
{
    "results": [...],
    "count": 2,
    "total": 43,
    "_links": {
        "self": {...},
        "next": {
        "href": "/offers?orderby=-modified&limit=2&start={TIMESTAMP}&offer-type=PERSONALIZED",
        "type": "application/json"
        }
    }
}
```

Similarly, if you are not on the first page and need to retrieve the previous page of personalized offers, use the `href` value from `_links.prev`. Make a request to the URL to fetch the previous set of results, as shown in the example below.

**Response**

```json
{
    "results": [...],
    "count": 2,
    "total": 43,
    "_links": {
        "self": {...},
        "next": {...},
        "prev": {
        "href": "/offers?orderby=-modified&limit=2&start={TIMESTAMP}&offer-type=PERSONALIZED",
        "type": "application/json"
        }
    }
}
```