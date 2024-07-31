---
title: Delete an item collection
description: Decision items are subsets of offers based on predefined conditions defined by a marketer, such as category of the offer.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---

# Delete an item collection {#delete-decision-item}

It may occasionally be necessary to remove (DELETE) an item collection. This is done by performing a DELETE request to the Offer Library API using the id of the item collection you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/item-collections/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete.| `itemCollections1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/item-collections/itemCollections1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the item collection. You should receive an HTTP status 404 (Not Found) because the item collection has been removed.
