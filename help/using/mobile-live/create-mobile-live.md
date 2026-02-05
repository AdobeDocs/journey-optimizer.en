---
solution: Journey Optimizer
product: journey optimizer
title: Create a Live activity message
description: Learn how to create a Live activity in Journey Optimizer
topic: Content Management
role: User
level: Beginner
hide: yes
hidefromtoc: yes
exl-id: 9864a136-e129-4279-bb09-081b72f584df
---
# Create a Live activity {#create-mobile-live}

>[!BEGINSHADEBOX]

* [Get started with Live activity](get-started-mobile-live.md)
* [Live activity configuration](mobile-live-configuration.md)
* [Live Activity integration with Adobe Experience Platform Mobile SDK](mobile-live-configuration-sdk.md)
* **[Create a Live activity](create-mobile-live.md)**
* [Frequently asked questions](mobile-live-faq.md)
* [Live activity campaign report](../reports/campaign-global-report-cja-activity.md)

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

1. Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 

1. Once configured, click **[!UICONTROL Review to activate]**, then click **[!UICONTROL Activate]**.

1. After the campaign is activated, use the provided **cURL request** as a template to trigger Live Activity start, update, or end events. Update the sample payload with your specific data before execution.

    Ensure that you also copy the **[!UICONTROL Campaign ID]** identifiers to include in your payload.

    ➡️ Refer to the [API Triggered Campaigns Documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging/) for authentication requirements, including OAuth tokens and API keys.

    ![](assets/create-live-3.png)

    +++ Example of an Individual Payload

    Note that most of the fields from the following payload example are mandatory, only `requestId`, `dismissal-date` and `alert` are optional.

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

After designing your Live activity, you can track measuring the impact of your Live activity with [built-in reports](../reports/campaign-global-report-cja-activity.md).
