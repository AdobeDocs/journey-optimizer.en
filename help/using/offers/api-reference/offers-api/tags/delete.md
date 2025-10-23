---
title: Delete collection qualifiers
description: Collection qualifiers allow you to better organize and sort through your offers.
feature: Decision Management, API
topic: Integrations
role: Developer
level: Experienced
exl-id: 335c1b80-f1f0-4fd0-add8-84b8cc5e2e00
---

# Delete a collection qualifier {#delete-tag}

It may occasionally be necessary to remove (DELETE) a collection qualifier (previously known as "tag"). This is done by performing a DELETE request to the Offer Library API using the id of the collection qualifier you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/tags/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The id of the entity you wish to delete. | `tag1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/tags/tag1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the collection qualifier. You should receive an HTTP status 404 (Not Found) because the collection qualifier has been removed.