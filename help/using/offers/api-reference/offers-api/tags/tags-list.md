---
title: List collection qualifiers
description: Collection qualifiers allow you to better organize and sort through your offers.
feature: Decision Management, API
topic: Integrations
role: Developer
level: Experienced
exl-id: 8cee44ed-5569-416c-b463-e75fb20d4c9c
version: Journey Orchestration
---

# List collection qualifiers {#list-tags}

Collection qualifiers (previously known as "tags") allow you to better organize and sort through your offers. For example, you could label your Black Friday offers with the "Black Friday" collection qualifier. You can then use the search functionality in the Offer Library to easily locate all of the offers with that collection qualifier.

Collection qualifiers can also be used to group offers together into collections.

You can view a list of all collection qualifiers within a container by performing a single GET request to the Offer Library API.

**API format**

```http
GET /{ENDPOINT_PATH}/tags?{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=2` |

## Paging {#paging}

The most common query parameters for paging include:

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `property` | An optional property filter: <ul><li>The properties are grouped by AND operation.</li><li>Parameters can be repeated like so: property={PROPERTY_EXPR}[&property={PROPERTY_EXPR2}...] or property={PROPERTY_EXPR1}[,{PROPERTY_EXPR2}...]</li><li>Property expressions are in format `[!]field[op]value`, with `op` in `[==,!=,<=,>=,<,>,~]`, supporting regular expressions.</li></ul> | `property=name!=abc&property=id~.*1234.*&property=description equivalent with property=name!=abc,id~.*1234.*,description.` |
| `orderBy` | Sort results by a specific property. Adding a - before name (orderby=-name) will sort items by name in descending order (Z-A). Path expressions are in the form of dot separated paths. This parameter can be repeated like so: `orderby=field1[,-fields2,field3,...]` | `orderby=id`,`-name` |
| `limit` | Limit the number of placements returned. | `limit=5` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/tags?limit=2' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns a list of collection qualifiers that are present within the container you have access to.

```json
{
    "results": [
        {
            "created": "2022-09-16T19:00:02.070+00:00",
            "modified": "2022-09-16T19:00:02.070+00:00",
            "etag": 1,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/tag;version=0.1"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "tag1234",
            "name": "Sneakers"
        },
        {
            "created": "2022-09-16T19:55:02.168+00:00",
            "modified": "2022-09-16T19:55:02.168+00:00",
            "etag": 1,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/tag;version=0.1"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "tag5678",
            "name": "Black Friday"
        }
    ],
    "count": 2,
    "total": 5,
    "_links": {
        "self": {
            "href": "/tags?href={SELF_HREF}&limit=2",
            "type": "application/json"
        },
        "next": {
            "href": "/tags?href={NEXT_HREF}&limit=2",
            "type": "application/json"
        }
    }
}
```