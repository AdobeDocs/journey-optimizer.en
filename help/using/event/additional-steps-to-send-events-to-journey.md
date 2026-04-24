---
solution: Journey Optimizer
product: journey optimizer
title: Additional steps to send events to a journey
description: Learn additional steps to send events to a journey
feature: Journeys, Events
topic: Administration
role: Developer, Admin
level: Intermediate, Experienced
keywords: steps, configuration, journey, events, stream, API
exl-id: e0144151-6c54-4656-9650-b544d8e7be16
TQID: https://experienceleague.adobe.com/SiUXmerz2D-TYmIEXvaYk4usjRq67Y0v7V7sGVN-4vo
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: dd51b532-b93f-4bcf-8dbf-0d007f593aca
    internal-label: Data source configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Additional steps to send events {#additional-steps-to-send-events}

To configure events to be sent to **[!UICONTROL Streaming Ingestion APIs]** and to be used in [!DNL Journey Optimizer], you need to follow these steps:

1. Get the inlet URL from Adobe Experience Platform APIs. Learn more in [Streaming Ingestion APIs overview](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/overview.html){target="_blank"}.
1. Copy the payload from the payload preview in the **[!UICONTROL Event]** menu. Learn more on [this page](../event/about-creating.md#define-the-payload-fields).

>[!IMPORTANT]
>
>For event requirements and limitations (streaming, Query Service, batch ingestion), see [Journey guardrails - Events](../start/guardrails.md#events-g).

You then need to configure the data system that pushes events to Streaming Ingestion APIs using the payload you copied:

1. Set up a POST API call to the Streaming Ingestion APIs URL (called an inlet).
1. Use the payload you copied from [!DNL Journey Optimizer] in the body ("data section") of the API call to Streaming Ingestion APIs. See below for an example
1. Determine where to get all the variables present in the payload. Example: if the event is supposed to convey the address, the payload pasted will show "address": "string". "string" should be replaced by the variable that will automatically populate the right value, the email of the person to send a message to. Note that in the payload preview, in the **[!UICONTROL Header]** section, we autofill many values expected to facilitate your work.
1. Select "application/json" as a body type.
1. Pass your organization ID in the header using the key "x-gw-ims-org-id". For the value, use your organization ID ("XXX@AdobeOrg").

Here is an example of a Streaming Ingestion APIs event:

```
{
    "header": {
        "msgType": "xdmEntityCreate",
        "msgId": "c25585b9-252e-431d-b562-e73da70c04e7",
        "msgVersion": "1.0",
        "xactionId": "f5995abe-c49d-4848-9577-a7a4fc2996fb",
        "datasetId": "string - required if you want the data to land in a specific dataset - not mandatory",
        "imsOrgId": "XXX@AdobeOrg",
        "schemaRef": {
            "id": "XXX",
            "contentType": "application/vnd.adobe.xed-full+json;version=1"
        },
        "source": {
            "name": "Journeys"
        }
    },
    "body": {
        "xdmMeta": {
            "schemaRef": {
                "id": "XXX",
                "contentType": "application/vnd.adobe.xed-full+json;version=1"
            }
        },
        "xdmEntity": {
            "_instance_name": {
                "person": {
                    "firstName": "string",
                    "lastName": "string",
                    "gender": "string",
                    "birthYear": 10,
                    "emailAddress": "string"
                }
            },
            "identityMap": {
                "Email": [
                {
                    "id": "string"
                    }
                ]
            },
            "_id": "string",
            "timestamp": "2023-05-29T00:00:00.000Z",
            "_experience": {
                "campaign": {
                    "orchestration": {
                    "eventID": "XXX"
                    }
                }
            }
        }
    }
}
```

To facilitate the identification of the place where to paste the "data" part, you can use a JSON visualization tool such as [JSON formatter](https://jsonformatter.curiousconcept.com){target="_blank"}.

To troubleshoot Streaming Ingestion APIs, refer to [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/troubleshooting.html){target="_blank"}.
