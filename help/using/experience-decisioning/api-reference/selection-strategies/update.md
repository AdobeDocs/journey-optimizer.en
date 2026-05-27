---
title: Update selection strategies
description: Selection strategies consist of collections associated with constraints and ranking methods to determine offers.
feature: API, Collections, Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 060f8c5f-4750-44dc-83aa-630afbc180eb
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/zQ3pwcP7MPdwGKxOLwKfkBo54zW0HkNqTts179HRfnQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
---
# Update a selection strategy {#update-selection-strategy}

You can modify or update a selection strategy by making a PATCH request to the Offer Library API.

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](https://jsonpatch.com/).

**API format**

```http
PATCH /{ENDPOINT_PATH}/selection-strategies/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to update. | `selectionStrategy1234` |

**Request**

```shell
curl -X PATCH 'https://platform.adobe.io/data/core/dps/selection-strategies/selectionStrategy1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '[
    {
        "op": "replace",
        "path": "/name",
        "value": "Updated selection strategy"
    },
    {
        "op": "replace",
        "path": "/description",
        "value": "Updated selection strategy description"
    }
]'
```

| Parameter | Description |
| --------- | ----------- |
| `value` | The new value you want to update your parameter with. |
| `path` | The path of the parameter to be updated. |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, `remove`, `copy` and `test`. |

**Response**

A successful response returns the updated details of the selection strategy, including the id.

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
