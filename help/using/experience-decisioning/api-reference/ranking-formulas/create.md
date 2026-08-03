---
title: Create a ranking formula
description: Ranking formulas allow you to define the functions for scoring, which is used to rank items.
feature: API, Collections, Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 2eb3ca65-f9f2-4483-ac6a-7bd896b0e516
version: Journey Orchestration
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
---
# Create a ranking formula {#create-ranking-formula}

You can create a ranking formula by making a POST request to the Offer Library API.

**Accept and Content-Type headers**

The following table shows the valid values which comprise the Content-Type fields in the request header:

| Header name | Value |
| --------- | ----------- |
| Content-Type |application/json |

**API format**

```http
POST /{ENDPOINT_PATH}/ranking-formulas 
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |

**Request**

```shell
curl -X POST 'https://platform.adobe.io/data/core/dps/ranking-formulas' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "name": "Test Ranking Function DPS",
    "description": "Ranking  function description",
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

**Response**

A successful response returns the details of the newly created ranking formula including the `id`. You can use the `id` in later steps to update or delete your ranking formula.

```json
{
    "etag": 1,
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
