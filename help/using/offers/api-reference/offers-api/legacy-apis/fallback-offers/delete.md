---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Delete a fallback offer
description: A fallback offer is sent to customers if they are not eligible for other offers
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: 5e97a1fd-7542-4c9a-8234-21c1fa419671
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/AwEMmVSJOAsd0uD45JftZ0PqavVLuIXMpOTqNUeDNmg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: ed0d8d0e-04b9-4326-be72-a0fbca265377
    internal-label: Integrations
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Delete a fallback offer {#delete-fallback-offer}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../../../../experience-decisioning/gs-experience-decisioning.md)


It may occasionally be necessary to remove (DELETE) a fallback offer. Only fallback offers that you create in the tenant container may be deleted. This is done by performing a DELETE request to the [!DNL Offer Library] API using the $id of the fallback offer you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/{CONTAINER_ID}/instances/{INSTANCE_ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the fallback offers are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |
| `{INSTANCE_ID}` | The instance id of the fallback offer. | `b3966680-13ec-11eb-9c20-8323709cfc65` |

**Request**

```shell
curl -X DELETE \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/b3966680-13ec-11eb-9c20-8323709cfc65' \
  -H 'Accept: application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 202 (No Content) and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the fallback offer. You will need to include an Accept header in the request, but should receive an HTTP status 404 (Not Found) because the fallback offer has been removed from the container.
