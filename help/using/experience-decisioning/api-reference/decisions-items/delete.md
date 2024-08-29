---
title: Delete a decision item
description: Decision items are marketing offers that you can create and organize into collections and catalogs.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 0fd608e0-df71-4e2d-8304-d7d5561c7c7a
---
# Delete a decision item {#delete-decision-item}

To remove a decision item, perform a DELETE request to the Offer Library API with the ID of the decision item you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/offer-items/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete.| `offerItem1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/offer-items/offerItem1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-H 'x-schema-id: {SCHEMA_ID}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the decision item. You should receive an HTTP status 404 (Not Found) because the decision item has been removed.
