---
solution: Journey Optimizer
product: journey optimizer
title: Create a Live activity message
description: Learn how to create a Live activity in Journey Optimizer
topic: Content Management
role: User
level: Beginner
exl-id: 9864a136-e129-4279-bb09-081b72f584df
TQID: https://experienceleague.adobe.com/orXAhry8onHXUejP5pzOyHdKbAcD8fiDmvRk-s74xLo
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
  - id: ed2fba79-65cb-4680-96d2-2ad5d851714d
    internal-label: Live activities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
---
# Create a Live activity {#create-mobile-live}

>[!BEGINSHADEBOX]

**On this page:** Build an API-triggered campaign in Journey Optimizer so you can remotely start, update, and end Live activities for individual users or audiences.

>[!ENDSHADEBOX]

After configuring your mobile configuration and implement your Adobe Experience Platform mobile SDK, you can start creating your Live activity in Journey Optimizer:

1. Access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**.

1. Select the **API triggered** campaign type.

    * Select **API-triggered Marketing** for audience-based campaigns

    * Select **API-triggered Transactional** for individual campaigns.

    >[!IMPORTANT]
    >
    > Note that for **API-triggered Transactional**, **[!UICONTROL High Throughput]** option should not be enabled.

    ![](assets/create-live-1.png)

1. From the **[!UICONTROL Properties]** section, edit your Campaign's **[!UICONTROL Title]** and **[!UICONTROL Description]**.

1. In the **[!UICONTROL Actions]** section, choose **[!UICONTROL Live activity]** and select or create a new configuration.

    Learn more about Live activity configuration on [this page](mobile-live-configuration.md).

    ![](assets/create-live-2.png)

1. Click **[!UICONTROL Create experiment]** to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. [Learn more](../content-management/content-experiment.md)

1. From the **[!UICONTROL Audience]** tab, choose your **[!UICONTROL Identity type]** [Learn more](../audience/about-audiences.md).

    >[!NOTE]
    >
    >For **API-triggered Marketing** campaigns, you can select an existing audience that acts as the first segmentation before checking APNs channelID subscription from the API payload.

1. Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 

1. Once configured, click **[!UICONTROL Review to activate]**, then click **[!UICONTROL Activate]**.

1. After the campaign is activated, use the provided **cURL request** as a template to trigger Live activity start, update, or end events. Update the sample payload with your specific data before execution.

    Ensure that you also copy the **[!UICONTROL Campaign ID]** identifiers to include in your payload.

    ➡️ Refer to the [API Triggered Campaigns Documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging) for authentication requirements, including OAuth tokens and API keys.

    ![](assets/create-live-3.png)

    +++ Example of a Payload for Unitary use cases (API-triggered Transactional campaign)

    This payload example is for individual campaigns using **API-triggered Transactional** campaign type. Note that most of the fields from the following payload example are mandatory, only `requestId`, `dismissal-date` and `alert` are optional.

    ```json
    {
        "requestId": "your-request-id",
        "campaignId": "your-campaign-id",
        "recipients": [
    {
        "type": "aep",
        "userId": "testemail@gmail.com",
        "namespace": "email",
        "context": {
         "requestPayload": {
        "aps": {
        "content-available": 1,
        "timestamp": 1756984054,              // current epoch time
        "dismissal-date": 1756984084,         // optional – auto remove when event="end"
        "event": "update",                    // start | update | end
    
        // Fields from FoodDeliveryLiveActivityAttributes
        "content-state": {
          "orderStatus": "Delivered"
        },
    
        "attributes-type": "FoodDeliveryLiveActivityAttributes",
        "attributes": {
          "restaurantName": "Pizza",
          "liveActivityData": {
            "liveActivityID": "orderId1"       // customer reference ID
          }
        },
    
        "alert": {
          "title": "Order Delivered!",
          "body": "Your pizza has arrived."
        }
      }
    }
    }
    }
    ]
    }
    ```

    +++

    +++ Example of a Payload for Broadcast use cases (API-triggered Marketing campaign)

    This payload example is for audience-based campaigns using **API-triggered Marketing** campaign type.

    ```json
    {
        "requestId": "123400000",
        "campaignId": "d32e6f6c-56df-4a98-a2c0-6db6008f8f32",
        "audience": {
            "id": "508f9416-52d0-4898-ba47-08baaa22e9c7"
        },
        "context": {
            "requestPayload": {
                "aps": {
                    "input-push-channel": "V+8UslywEfAAAOq9SbTrLg==",  //apns-channel-id
                    "content-available": 1,
                    "timestamp": 1770808339,
                    "event": "update",   // start | update | end
                    
                    // Fields from GameScoreLiveActivityAttributes
                    "content-state": {
                        "homeTeamScore": 33,
                        "awayTeamScore": 49,
                        "statusText": "Wingdom keeps scoring!"
                    },
                    "attributes-type": "GameScoreLiveActivityAttributes",
                    "attributes": {
                        "liveActivityData": {
                            "channelID": "V+8UslywEfAAAOq9SbTrLg=="   //apns-channel-id, must match the "input-push-channel" value
                        }
                    },
                    "alert": {
                        "title": "This is the title for game",
                        "body": "This is the body for body"
                    }
                }
            }
        }
    }
    ```

    +++

After designing your Live activity, you can track measuring the impact of your Live activity with [built-in reports](../reports/campaign-global-report-cja-activity.md).

>[!TIP]
>
>If your Live activity is not appearing or updating as expected, see [Troubleshoot Live activities](troubleshoot-mobile-live.md) for step-by-step debugging guidance.

## Add custom data with execution metadata {#metadata}

>[!AVAILABILITY]
>
> `executionMetadata` is available for both **API-triggered Transactional** and **API-triggered Marketing** campaigns.

Attach your own **custom data** to a profile, such as an order ID, loyalty tier, or region code, using the optional `executionMetadata` field. Journey Optimizer stores this data alongside the execution so you can retrieve it later from your **Live activity feedback dataset** and match delivery results to your own business records.

To send this data via the API, see the [Messaging API reference for the `executionMetadata` field](https://developer.adobe.com/journey-optimizer-apis/references/messaging#operation/postIMUnitaryMessageExecution!path=recipients/0/executionMetadata&t=request). To read the values back on the device, see the [Mobile SDK guide on receiving execution metadata from the API trigger](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/live-activities/tutorial#receiving-execution-metadata-from-the-api-trigger).

To add custom data with execution metadata:

* Add `executionMetadata` to a profile, next to `userId` and `namespace`. Only string keys and string values are accepted, convert any non-string value to a string before sending it.

* Values are recorded exactly as sent. `executionMetadata` does not support personalization expressions, so any `{{...}}` expression is treated as literal text rather than resolved. You should always send final, literal values.

* Each profile can carry up to **50 key/value pairs**, with a combined size limit of **2 KB** for all keys and values. Metadata exceeding this limit is discarded but the Live activity is still delivered. Limit the payload to the information required for reporting purposes.

+++ JSON example

In this example, `orderId`, `tier`, `restaurant`, and `region` are your own values. After the Live activity is triggered, you can read them back from the feedback dataset to link the delivery to your order record.

```json
{
    "requestId": "your-request-id",
    "campaignId": "your-campaign-id",
    "recipients": [
        {
            "type": "aep",
            "userId": "testemail@gmail.com",
            "namespace": "email",
            "executionMetadata": {
                "orderId": "A-123",
                "tier": "gold",
                "restaurant": "PizzaPlace",
                "region": "EU"
            },
            "context": {
                "requestPayload": {
                    "aps": {
                        "content-available": 1,
                        "timestamp": 1756984054,
                        "dismissal-date": 1756984084,
                        "event": "update",
                        "content-state": {
                            "orderStatus": "Delivered"
                        },
                        "attributes-type": "FoodDeliveryLiveActivityAttributes",
                        "attributes": {
                            "restaurantName": "PizzaPlace",
                            "liveActivityData": {
                                "liveActivityID": "orderId1"
                            }
                        },
                        "alert": {
                            "title": "Order Delivered!",
                            "body": "Your pizza has arrived."
                        }
                    }
                }
            }
        }
    ]
}
```

+++

## How-to video

Discover how to configure iOS Live activities with Adobe Journey Optimizer to deliver rich, real-time updates on the iPhone Lock Screen and Dynamic Island.

>[!VIDEO](https://video.tv.adobe.com/v/3479864)
