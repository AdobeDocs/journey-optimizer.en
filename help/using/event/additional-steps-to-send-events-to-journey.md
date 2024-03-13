---
solution: Journey Optimizer
product: journey optimizer
title: Additional steps to send events to a journey
description: Learn additional steps to send events to a journey
feature: Journeys, Events
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Intermediate, Experienced
keywords: steps, configuration, journey, events, stream, API
exl-id: e0144151-6c54-4656-9650-b544d8e7be16
---
# Additional steps to send events {#additional-steps-to-send-events}

To configure events to be sent to **[!UICONTROL Streaming Ingestion APIs]** and to be used in [!DNL Journey Optimizer], you need to follow these steps:

1. Get the inlet URL from Adobe Experience Platform APIs. Learn more in [Streaming Ingestion APIs overview](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/overview.html){target="_blank"}.
1. Copy the payload from the payload preview in the **[!UICONTROL Event]** menu. Learn more in [this page](../event/about-creating.md#define-the-payload-fields).

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
