---
title: Update exd placement
description: Exd placement consist of collections associated with constraints and ranking methods to determine offers.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---
# Update an exd placement {#update-exd-placement}

You can modify or update a placement by making a PUT request to the Offer Library API.

For more information on JSON PUT, including available operations, see the official JSON PUT documentation.

**Accept and Content-Type headers**

The following table shows the valid values which comprise the Content-Type fields in the request header:

| Parameter | Description |
| --------- | ----------- |
| Content-Type | `application/json` |

**API format**

```http
PUT /{ENDPOINT_PATH}/exd-placements/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to update. | `placement1234` |

**Request**

```shell
curl --location --request PUT 'https://platform-stage.adobe.io/data/core/dps/exd-placements/dps:exd-placement:19aca09b0a456e57' \
--H 'Content-Type: application/json' \
--H 'x-gw-ims-org-id: {IMS_ORG}' \
--H 'x-sandbox-name: {SANDBOX_NAME}' \
--H 'x-api-key: {API_KEY}' \
--H 'Authorization: Bearer {ACCESS_TOKEN}' \
--X '{
  "id":"dps:exd-placement:19aca09b0a456e57",
  "description": "Keyboard application",
  "status":"archived"
}'
```

| Parameter | Description |
| --------- | ----------- |
| `value` | The new value you want to update your parameter with. |
| `path` | The path of the parameter to be updated. |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, `remove`, `copy`, and `test`. |

**Response**

A successful response returns the updated details of the exd placement, including the ID.

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
