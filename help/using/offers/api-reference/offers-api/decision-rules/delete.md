---
title: Delete decision rules
description: Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 52f4803b-9e9a-4ad0-ae24-de652006763d
---
# Delete a decision rule {#delete-decision-rule}

It may occasionally be necessary to remove (DELETE) a decision rule. This is done by performing a DELETE request to the [!DNL Offer Library] API using the `id` of the decision rule you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/offer-rules/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete. | `offerRule1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/offer-rules/offerRule1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the decision rule and should receive an HTTP status 404 (Not Found) because the decision rule has been removed.
