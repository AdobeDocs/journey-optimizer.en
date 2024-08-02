---
title: Delete a decision item
description: Decision items are marketing offers that you can create and organize into collections and catalogs.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---

# Delete a decision item {#delete-decision-item}

It may occasionally be necessary to remove (DELETE) a decision item. This is done by performing a DELETE request to the Offer Library API using the id of the decision item you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/offer-items/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete.| `offerCollection1234` |

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
