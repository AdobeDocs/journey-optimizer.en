---
title: List ranking formulas
description: Ranking formulas allow you to define the functions for scoring, which is used to rank items.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 8b07be08-b37c-4535-82d8-3304340cbcad
---
# List ranking formulas {#list-ranking-formulas}

A ranking formula consists of a ranking function which defines how it should rank. 

You can view a list of all ranking formulas by performing a single GET request to the Offer Library API.

**API format**

```http
GET /{ENDPOINT_PATH}/ranking-formulas?{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{QUERY_PARAMS}` | exdFunction. | `property=exdFunction%3D%3Dtrue` |

## Using query parameters {#using-query-parameters}

You can use query parameters to page and filter results when listing resources.

### Paging {#paging}

The most common query parameters for paging include:

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `property` | An optional property filter: <ul><li>The properties are grouped by AND operation.</li><li>Parameters can be repeated like so: property={PROPERTY_EXPR}[&property={PROPERTY_EXPR2}...] or property={PROPERTY_EXPR1}[,{PROPERTY_EXPR2}...]</li><li>Property expressions are in format `[!]field[op]value`, with `op` in `[==,!=,<=,>=,<,>,~]`, supporting regular expressions.</li></ul> | `property=name!=abc&property=id~.*1234.*&property=description equivalent with property=name!=abc,id~.*1234.*,description.` |
| `orderBy` | Sort results by a specific property. Adding a - before name (orderby=-name) will sort items by name in descending order (Z-A). Path expressions are in the form of dot separated paths. This parameter can be repeated like so: `orderby=field1[,-fields2,field3,...]` | `orderby=id`,`-name` |
| `limit` | Limit the number of entities returned. | `limit=5` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/ranking-formulas?property=exdFunction%3D%3Dtrue&limit=2' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns a list of ranking formulas that you have access to. 

```json
{
    "results": [
        {
            "created": "2024-08-08T23:45:15.380Z",
            "modified": "2024-10-22T18:15:05.909Z",
            "etag": 36,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/ranking-function"
            ],
            "createdBy": "71486D7B5F4011980A494030@AdobeID",
            "lastModifiedBy": "71486D7B5F4011980A494030@AdobeID",
            "id": "dps:ranking-function:1947f5372cc4ed74",
            "name": "[Do not delete] - Cypress e2e - edit",
            "description": "some description",
            "returnType": {
                "type": "INTEGER"
            },
            "exdFunction": true,
            "expression": {
                "type": "PQL",
                "format": "pql/text",
                "value": "42 = 11"
            }
        },
        {
            "created": "2024-05-03T13:06:22.361Z",
            "modified": "2024-10-18T22:47:35.396Z",
            "etag": 2,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/ranking-function;version=0.3"
            ],
            "createdBy": "FD62391F5B44DF970A494124@AdobeID",
            "lastModifiedBy": "6F8A6FF05F4011C40A494005@AdobeID",
            "id": "xcore:ranking-function:18ca80c5b15c5e11",
            "name": "doc test exd",
            "description": "",
            "returnType": {
                "type": "INTEGER"
            },
            "exdFunction": true,
            "expression": {
                "type": "PQL",
                "format": "pql/text",
                "value": "false"
            }
        }
    ],
    "count": 2,
    "total": 50,
    "_links": {
        "self": {
            "href": "/ranking-formulas?orderby=-modified&limit=2",
            "type": "application/json"
        },
        "next": {
            "href": "/ranking-formulas?orderby=-modified&limit=2&start=2024-10-18T22:22:35.048Z",
            "type": "application/json"
        }
    }
}
```
