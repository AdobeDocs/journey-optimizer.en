---
title: Update ranking formulas
description: Ranking formulas allow you to define the functions for scoring, which is used to rank items.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---
# Update a ranking formula {#update-ranking-formula}

You can modify or update a ranking formula by making a PUT request to the Offer Library API.

For more information on JSON PUT, including available operations, see the official [JSON PUT documentation](http://jsonpatch.com/).

**Accept and Content-Type headers**

The following table shows the valid values which comprise the Content-Type fields in the request header:

| Header name | Value | 
| --------- | ----------- |
| Content-Type | `application/json` |

**API format**

```http
PUT /{ENDPOINT_PATH}/ranking-formulas/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The ID of the entity you wish to update. | `rankingFormula1234` |

**Request**

```shell
curl -X PATCH 'https://platform.adobe.io/data/core/dps/ranking-formulas/rankingFormula1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "name": "[UPDATED] Test Ranking Function DPS",
    "description": "Ranking  function description",
    "isPure": true,
    "exdFunction": true,
    "returnType": {
        "type": "integer"
    },
    "expression": {
        "type": "PQL",
        "format": "pql/text",
        "value": "if(offer.rank.priority.isNotNull(), offer.rank.priority, 0) * if(offer.tags.intersects(boosted.tags), 2, 1)"
    },
    "definedOn": {
        "offer": {
            "schema": {
                "altId": "_experience.offer-management.personalized-offer",
                "version": "0"
            }
        },
        "boosted": {
            "schema": {
                "altId": "_xdm.context.foo",
                "version": "0"
            }
        }
    }
}'
```

| Parameter | Description |
| --------- | ----------- |
| `value` | The new value you want to update your parameter with. |
| `path` | The path of the parameter to be updated. |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, `remove`, `copy`, and `test`. |

**Response**

A successful response returns the updated details of the ranking formula, including the ID.

```json

{
    "etag": 2,
    "createdBy": "{CREATED_BY}",
    "lastModifiedBy": "{MODIFIED_BY}",
    "id": "{ID}",
    "sandboxId": "{SANDBOX_ID}",
    "createdDate": "2023-05-31T15:09:11.771Z",
    "lastModifiedDate": "2023-05-31T15:09:11.771Z",
    "createdByClientId": "{CREATED_CLIENT_ID}",
    "lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```
