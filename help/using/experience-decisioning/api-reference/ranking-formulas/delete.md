---
title: Delete a ranking formula
description: Ranking formulas allow you to define the functions for scoring, which is used to rank items.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 4ea50481-b1b9-4e0c-ad4e-c4139891bfdf
---
# Delete a ranking formula {#delete-selection-strategy}

It may occasionally be necessary to remove (DELETE) a ranking formula. This is done by performing a DELETE request to the Offer Library API using the ID of the ranking formula you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/ranking-formulas/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The ID of the entity you wish to delete.| `rankingFormula1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/ranking-formulas/rankingFormula1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the ranking formula. You should receive an HTTP status 404 (Not Found) because the ranking formula has been removed.
