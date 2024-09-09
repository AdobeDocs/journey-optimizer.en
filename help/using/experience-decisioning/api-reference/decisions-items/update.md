---
title: Update a decision item
description: Decision items are marketing offers that you can create and organize into collections and catalogs.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: b924b7d0-bbed-409e-8173-0685fc41d7de
---
# Update a decision item {#update-decision-items}

You can modify or update a decision item by making a PATCH request to the Offer Library API.

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](http://jsonpatch.com/).

**API format**

```http
PATCH /{ENDPOINT_PATH}/offer-items/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to update. | `offerItem1234` |

**Request**

```shell
curl -X PATCH 'https://platform.adobe.io/data/core/dps/offer-items/offerItem1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-H 'x-schema-id: {SCHEMA_ID}' \
-d '[
    {
        "op": "replace",
        "path": "/_experience/decisioning/decisionitem/itemName",
        "value": "Updated offer item"
    },
    {
        "op": "replace",
        "path": "/_experience/decisioning/decisionitem/itemDescription",
        "value": "Updated offer item description"
    }
]'
```

| Parameter | Description |
| --------- | ----------- |
| `value` | The new value you want to update your parameter with. |
| `path` | The path of the parameter to be updated. |
| `op` | The type of operation to be performed. Operations include: `add`, `replace`, `remove`, `copy` and `test`. |

**Response**

A successful response returns the details of the updated item, including the id. You can use the id in later steps to update or delete your decision item.

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
