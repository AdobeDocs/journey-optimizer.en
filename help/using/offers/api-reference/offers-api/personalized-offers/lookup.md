---
title: Look up a personalized offer
description: A personalized offer is a customizable marketing message based on eligibility rules and constraints.
feature: Decision Management, API
topic: Integrations
role: Developer
level: Experienced
exl-id: 2e30b155-688b-432b-a703-d09de12ebdfd
version: Journey Orchestration
---
# Look up a personalized offer {#look-up-personalized-offer}

A personalized offer is a customizable marketing message based on eligibility rules and constraints.

You can look up specific personalized offers by making a GET request to the [!DNL Offer Library] API that includes the personalized offer id in the request path.

**API format**

```http
GET /{ENDPOINT_PATH}/offers/{ID}?offer-type=personalized
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The id of the entity you wish to look up. | `personalizedOffer1234` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/offers/personalizedOffer1234?offer-type=personalized' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the details of the personalized-offer including information about your unique personalized offer `id`.

```json
{
    "created": "2023-05-15T14:35:16.781+00:00",
    "modified": "2023-05-15T14:38:26.691+00:00",
    "etag": 2,
    "schemas": [
        "https://ns.adobe.com/experience/offer-management/personalized-offer;version=0.15"
    ],
    "createdBy": "{CREATED_BY}",
    "lastModifiedBy": "{MODIFIED_BY}",
    "id": "personalizedOffer1234",
    "name": "Test personalized offer with frequency constraint",
    "status": "draft",
    "representations": [
        {
            "channel": "https://ns.adobe.com/xdm/channel-types/web",
            "placement": "offerPlacement1234",
            "components": [
                {
                    "type": "html",
                    "format": "text/html",
                    "language": [
                        "en-us"
                    ],
                    "content": "Hello You qualify for our Discount of 60%"
                }
            ]
        }
    ],
    "selectionConstraint": {
        "startDate": "2022-07-27T05:00:00.000+00:00",
        "endDate": "2023-07-29T05:00:00.000+00:00",
        "profileConstraintType": "none"
    },
    "rank": {
        "priority": 0
    },
    "cappingConstraint": {},
    "frequencyCappingConstraints": [
        {
            "enabled": false,
            "limit": 1,
            "startDate": "2023-05-15T14:25:49.622+00:00",
            "endDate": "2023-05-25T14:25:49.622+00:00",
            "scope": "global",
            "entity": "offer",
            "repeat": {
                "enabled": false,
                "unit": "month",
                "unitCount": 1
            }
        }
    ]
}
```
