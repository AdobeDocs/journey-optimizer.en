---
title: Update selection strategies
description: Selection strategies consist of collections associated with constraints and ranking methods to determine offers.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---

# Update a selection strategy {#update-selection-strategy}

You can modify or update a selection strategy by making a PATCH request to the Offer Library API.

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](http://jsonpatch.com/).

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
