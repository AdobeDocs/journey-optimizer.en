---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: delete placements
description: Placements are containers that are used to showcase your offers.
feature: Decision Management, API
topic: Integrations
role: Developer
level: Experienced
exl-id: ca7af3b0-62cd-44ac-8856-b3d1ec15f284
version: Journey Orchestration
---
# Delete a placement {#delete-placement}

It may occasionally be necessary to remove (DELETE) a placement. This is done by performing a DELETE request to the [!DNL Offer Library] API using the id of the placement you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/placements/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The instance id of the placement you wish to update. | `offerPlacement1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/placements/offerPlacement1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the placement and should receive an HTTP status 404 (Not Found) because the placement has been removed.
