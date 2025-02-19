---
product: experience platform
solution: Experience Platform
title: Context data & Decisioning requests
description: Learn how to pass context data in Decisioning requests.
feature: Decision Management
role: Developer, Data Engineer
level: Experienced
---

# Context data & Decisioning requests {#context-data-decisioning}

This section guides you thgrough passing context data in Decisioning requests and using them in eligihbility rules. 

>[!BEGINSHADEBOX]

To go further, you can also leverage context into **ranking formulas** to boost your offers. Detailed examples of ranking formulas leveraging context data are available in [this section](../offers/ranking/create-ranking-formulas.md#context-data).

>[!ENDSHADEBOX]

## Pass context data in Decisioning requests

Context data in Decisioning requests is defined using the key: `xdm:ContextData`.

Context data attributes are not driven by XDM schema. You can pass any context data in JSON as part of the Decisioning request payload.

Here is a sample decisioning request with context data (see `xdm:ContextData`):

```
curl --location 'https://platform-stage.adobe.io/data/core/ods/decisions' \
--header 'Accept: application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-response;version=1.0"' \
--header 'Content-Type: application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-request;version=1.0"' \
--header 'Authorization: Bearer eyJhbGciOi....' \
--header 'x-api-key: {{api_key}}' \
--header 'x-gw-ims-org-id: {{ims_org}}' \
--header 'x-sandbox-name: {{sandbox_name}}' \
--header 'x-request-id: {{$guid}}' \
--data-raw '{
    "xdm:propositionRequests": [
        {
            "xdm:activityId": "dps:offer-activity:19978bf95ebfc8fb",
            "xdm:placementId": "dps:offer-placement:199772e1c90d50ac"
        }
    ],
    "xdm:profiles": [
        {
            "xdm:identityMap": {
                "Email": [
                    {
                        "xdm:id": "test@test.com",
                        "primary": true
                    }
                ]
            },
            "xdm:contextData": [
                {
                    "@type": "_xdm.context.additionalParameters;version=1",
                    "xdm:data": {
                        "xdm:channel": "mobile",
                        "xdm:language": "en",
                        "xdm:isThirdParty": true,
                        "xdm:mobileVersion": "3.0.5106",
                        "xdm:mobileVersionMajor": "3",
                        "xdm:mobileVersionMinor": "0",
                        "xdm:mobileVersionPatch": "125",
                        "xdm:deviceType": "iOS",
                        "xdm:features": [
                            "p1000",
                            "p1001"
                        ]
                    }
                }
            ]
        }
    ],
    "xdm:allowDuplicatePropositions": {
        "xdm:acrossActivities": true,
        "xdm:acrossPlacements": true
    },
    "xdm:responseFormat": {
        "xdm:includeContent": true,
        "xdm:includeMetadata": {
            "xdm:activity": [
                "name"
            ],
            "xdm:option": [
                "name"
            ],
            "xdm:placement": [
                "name"
            ]
        }
    }
}'
```

## Use context data in eligibility rules

Here are examples illustrating how to use context data passed in Decisioning requests in eligibility rules.

* Eligibile if the context data features contain a particular value:

    ```
    
    select contextData from @{_xdm.context.additionalParameters;version=1} where contextData.features AND (select personetic from contextData.features where personetic.contains("123"))

    ```

*  Eligible if the channel is non-empty and equal to mobile:

    ```

    select contextData from @{_xdm.context.additionalParameters;version=1} where !contextData.channel.isNull() AND contextData.channel!="" AND contextData.channel="mobile"

    ```
