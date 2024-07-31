---
title: List item collections
xx description: Collections are subsets of offers based on predefined conditions defined by a marketer, such as category of the offer.
xx feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---

# List item collections {#list-decision-items}

A selection strategy consists of a collection associated with an eligibility constraint and a ranking method to determine the offers to be shown when selected in a [decision policy](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/experience-decisioning/create-decision).

You can view a list of all selection strategies by performing a single GET request to the Offer Library API.

**API format**

```http
GET /{ENDPOINT_PATH}/selection-strategies?{QUERY_PARAMS}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{QUERY_PARAMS}` | Optional query parameters to filter results by. | `limit=2` |

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
curl -X GET 'https://platform.adobe.io/data/core/dps/selection-strategies?limit=2' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns a list of selection strategies that you have access to. 

```json
{
    "results": [
        {
            "created": "2024-02-08T03:01:50.924Z",
            "modified": "2024-02-16T23:03:03.019Z",
            "etag": 4,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/selection-strategy;version=0.2"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "selectionStrategy1234",
            "name": "Selection Strategy One",
            "description": "Selection Strategy",
            "rank": {
                "priority": 1,
                "order": {
                    "orderEvaluationType": "static"
                }
            },
            "profileConstraint": {
                "profileConstraintType": "eligibilityRule",
                "eligibilityRule": "offerRule1234"
            },
            "optionSelection": {
                "filter": "itemCollection1234",
            }
        },
        {
            "created": "2024-01-11T11:12:06.775Z",
            "modified": "2024-01-15T14:36:02.994Z",
            "etag": 2,
            "schemas": [
                "https://ns.adobe.com/experience/offer-management/selection-strategy;version=0.1"
            ],
            "createdBy": "{CREATED_BY}",
            "lastModifiedBy": "{MODIFIED_BY}",
            "id": "selectionStrategy5678",
            "name": "Selection Strategy Two",
            "rank": {
                "priority": 1,
                "order": {
                    "orderEvaluationType": "scoringFunction",
                    "function": "rankingFormula5678"
                }
            },
            "profileConstraint": {
                "profileConstraintType": "none"
            "optionSelection": {
                "filter": "itemCollection5678"
            }
        }
    ],
    "count": 2,
    "total": 166,
    "_links": {
        "self": {
            "href": "/selection-strategies?orderby=-modified&limit=2",
            "type": "application/json"
        },
        "next": {
            "href": "/selection-strategies?orderby=-modified&limit=2&start=2024-06-04T23:37:33.980Z",
            "type": "application/json"
        }
    }
}
```