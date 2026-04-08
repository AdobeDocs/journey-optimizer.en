---
solution: Journey Optimizer
product: journey optimizer
title: Create a Live activity message
description: Learn how to create a Live activity in Journey Optimizer
topic: Content Management
role: User
level: Beginner
exl-id: 9864a136-e129-4279-bb09-081b72f584df
---
# Create a Live activity {#create-mobile-live}

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

    ➡️ Refer to the [API Triggered Campaigns Documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging/) for authentication requirements, including OAuth tokens and API keys.

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

## How-to video

Discover how to configure iOS Live activities with Adobe Journey Optimizer to deliver rich, real-time updates on the iPhone Lock Screen and Dynamic Island.

>[!VIDEO](https://video.tv.adobe.com/v/3479864)
