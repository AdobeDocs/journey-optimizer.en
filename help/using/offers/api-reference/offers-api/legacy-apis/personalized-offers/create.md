---
title: Create a personalized offer
description: A personalized offer is a customizable marketing message based on eligibility rules and constraints.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 234bee17-c830-4bc0-b258-182804df4cb3
---
# Create a personalized offer {#create-personalized-offer}

A personalized offer is a customizable marketing message based on eligibility rules and constraints.

You can create a personalized offer by making a POST request to the [!DNL Offer Library] API, while providing your container ID.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1` |
| Content-Type | `application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5"` |

**API format**

```http
POST /{ENDPOINT_PATH}/{CONTAINER_ID}/instances
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the personalized offers are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |

**Request**

```shell
curl -X POST \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances' \
  -H 'Accept: application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1' \
  -H 'Content-Type: application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.5"' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
        "xdm:name": "Sale offer",
        "xdm:status": "draft",
        "xdm:representations": [
        {
                "xdm:components": [
                {
                        "dc:language": [
                            "en"
                    ],
                        "@type": "https://ns.adobe.com/experience/offer-management/content-component-html",
                        "dc:format": "text/html"
                }
                ],
                "xdm:placement": "xcore:offer-placement:124e0be5699743d3"
        }
    ],
        "xdm:selectionConstraint": {
            "xdm:startDate": "2023-10-01T16:00:00Z",
            "xdm:endDate": "2021-12-13T16:00:00Z",
            "xdm:eligibilityRule": "xcore:eligibility-rule:124e0faf5b8ee89b"
        },
        "xdm:rank": {
            "xdm:priority": 1
    },
        "xdm:cappingConstraint": {
            "xdm:globalCap": 150
    },
        "xdm:tags": [
            "xcore:tag:124e147572cd7866"
    ]
}'
```

**Response**

A successful response returns information on the newly created personalized offer, including its unique instance ID and placement `@id`. You can use the instance ID in later steps to update or delete your personalized offer.

```json
{
    "instanceId": "0f4bc230-13df-11eb-bc55-c11be7252432",
    "@id": "xcore:personalized-offer:124e181c8b0d7878",
    "repo:etag": 1,
    "repo:createdDate": "2023-10-21T20:50:32.018624Z",
    "repo:lastModifiedDate": "2023-10-21T20:50:32.018624Z",
    "repo:createdBy": "{CREATED_BY}",
    "repo:lastModifiedBy": "{MODIFIED_BY}",
    "repo:createdByClientId": "{CREATED_CLIENT_ID}",
    "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```

## Limitations {#limitations}

Offer representations and some offer constraints are currently not supported with the mobile [!DNL Experience Edge] workflows, for example `Capping`. The `Capping` field value specifies the number of times an offer can be presented across all users. For more details, see [Offer eligibility rules and constraints documentation](../../../../offer-library/creating-personalized-offers.md).
