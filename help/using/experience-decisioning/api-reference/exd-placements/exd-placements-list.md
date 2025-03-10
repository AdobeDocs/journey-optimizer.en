---
title: List exd placements
description: Exd placements consist of collections associated with constraints and ranking methods to determine offers.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---
# List exd placements {#list-exd-placements}

You can view a list of all exd placements by performing a single GET request to the Offer Library API.

**API format**

```http
GET /{ENDPOINT_PATH}/exd-placements?{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |

## Using query parameters {#using-query-parameters}

You can use query parameters to page and filter results when listing resources. You can filter by status, channel and channelConfiguration.

### Paging {#paging}

The most common query parameters for paging include:

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `property` | An optional property filter: <ul><li>The properties are grouped by AND operation.</li><li>Parameters can be repeated like so: property={PROPERTY_EXPR}[&property={PROPERTY_EXPR2}...] or property={PROPERTY_EXPR1}[,{PROPERTY_EXPR2}...]</li><li>Property expressions are in format `[!]field[op]value`, with `op` in `[==,!=,<=,>=,<,>,~]`, supporting regular expressions.</li></ul> | `property=name!=abc&property=id~.*1234.*&property=description equivalent with property=name!=abc,id~.*1234.*,description.` |
| `orderBy` | Sort results by a specific property. Adding a - before name (orderby=-name) will sort items by name in descending order (Z-A). Path expressions are in the form of dot separated paths. This parameter can be repeated like so: `orderby=field1[,-fields2,field3,...]` | `orderby=id`,`-name` |
| `limit` | Limit the number of entities returned. | `limit=5` |

**Request**

```shell
curl --location --request GET 'https://platform-stage.adobe.io/data/core/dps/exd-placements' \
--header 'Content-Type: application/json' \
--header 'x-gw-ims-org-id: {IMS_ORG}' \
--header 'x-sandbox-name: {SANDBOX_NAME}' \
--header 'x-api-key: {API_KEY}' \
--header 'Authorization: Bearer {ACCESS_TOKEN}' \
--data '{"query":"","variables":{}}'
```

**Response**

A successful response returns a list of Exd placements that you have access to. 

```json
{
    "results": [
        {
            "created": "2024-11-14T23:30:29.820Z",
            "modified": "2024-11-14T23:30:29.820Z",
            "etag": 1,
            "schemas": [
                "exd-placement"
            ],
            "createdBy": "14D546EA60B67E540A494010@658557135fa10b860a494019",
            "lastModifiedBy": "14D546EA60B67E540A494010@658557135fa10b860a494019",
            "id": "dps:exd-placement:19c61da45ed96159",
            "name": "testing-alfa",
            "description": "atest",
            "tags": [
                "35801d6b-6371-449d-9083-d895fc120569"
            ],
            "channel": "https://ns.adobe.com/xdm/channel-types/email",
            "channelConfiguration": "fb8e9621-a5e8-485f-9f3f-d040c601ebc4",
            "status": "active"
        },
        {
            "created": "2024-10-22T00:18:17.997Z",
            "modified": "2024-10-22T05:04:15.315Z",
            "etag": 2,
            "schemas": [
                ""
            ],
            "createdBy": "71486D7B5F4011980A494030@AdobeID",
            "lastModifiedBy": "71486D7B5F4011980A494030@AdobeID",
            "id": "dps::19a7426d533db126",
            "name": "Test Exd Placement capacitor",
            "description": "Wooden system",
            "status": "archived"
        }
    ],
    "count": 2,
    "total": 2,
    "_links": {
        "self": {
            "href": "/exd-placements?orderby=-modified&limit=50",
            "type": "application/json"
        }
    }
}
```
