---
title: Lookup a ranking formula
description: Ranking formulas allow you to define the functions for scoring, which is used to rank items.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: f048b2d1-d26b-4987-8acb-3558df506ec2
---
# Lookup a  {#list-ranking-formula}

You can look up specific ranking formula by making a GET request to the Offer Library API that includes the ID in the request path.

**API format**

```http
GET /{ENDPOINT_PATH}/ranking-formulas/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The ID of the entity you wish to look up. | `rankingFormula1234` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/ranking-formulas/rankingFormula1234' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the details of the ranking formula.

```json
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
}
```
