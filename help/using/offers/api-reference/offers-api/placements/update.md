---
title: update a placement
description: Placements are containers that are used to showcase your offers.
feature: Offers
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 6990918c-e736-4f28-9ac6-9ac3101b069f
---
# Update a placement {#update-placement}

You can modify or update a placement by making a PATCH request to the [!DNL Offer Library] API.

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](http://jsonpatch.com/).

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1` |
| Content-Type | `application/vnd.adobe.platform.xcore.patch.hal+json; version=1; schema="https://ns.adobe.com/experience/offer-management/offer-placement;version=0.4"` |

**API format**

```http
PATCH /{ENDPOINT_PATH}/placements/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The id of the entity you wish to update. | `offerPlacement1234` |

**Request**

```shell
curl -X PATCH 'https://platform.adobe.io/data/core/dps/placements/offerPlacement1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '[
    {
        "op": "replace",
        "path": "/name",
        "value": "Updated placement"
    },
    {
        "op": "replace",
        "path": "/description",
        "value": "Updated placement description"
    }
]'
```

| Parameter | Description |
| --------- | ----------- |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, and `remove`. |
| `path` | The path of the parameter to be updated. |
| `value` | The new value you want to update your parameter with. |

**Response**

A successful response returns the updated details of the placement, including its unique instance ID and placement `@id`.

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
    "lastModifiedByClientId": "{MODIFIED_CLIENT_ID}""
}
```
