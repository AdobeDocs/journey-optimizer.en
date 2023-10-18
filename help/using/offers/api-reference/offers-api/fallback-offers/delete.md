---
title: Delete a fallback offer
description: A fallback offer is sent to customers if they are not eligible for other offers
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 5c94842a-021c-4a3a-ad9c-ccc2af2c1526
---

# Delete a fallback offer {#delete-fallback-offer}

It may occasionally be necessary to remove (DELETE) a fallback offer. This is done by performing a DELETE request to the [!DNL Offer Library] API using the id of the fallback offer you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/offers/{ID}?offer-type=fallback
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The id of the entity you wish to delete. | `fallbackOffer1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/offers/fallbackOffer1234?offer-type=fallback' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the offer and should receive an HTTP status 404 (Not Found) because the fallback offer has been removed.
