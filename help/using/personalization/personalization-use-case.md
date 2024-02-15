---
solution: Journey Optimizer
product: journey optimizer
title: Personalization use case&colon; order status notification
description: Learn how to personalize a message with profile, offer decision, and context information.
feature: Personalization
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor, use case, personalization
exl-id: 7d9c3d31-af57-4f41-aa23-6efa5b785260
---
# Personalization use case: order status notification {#personalization-use-case}

In this use case, you will see how to use multiple types of personalization in a single push notification message. Three types of personalization will be used:

* **Profile**: message personalization based on a profile field
* **Offer decision**: personalization based on decision management variables
* **Context**: personalization based on contextual data from the journey

The goal of this example is to push an event to [!DNL Journey Optimizer] every time a customer order is updated. A push notification is then sent to the customer with information on the order and a personalized offer.

For this use case, the following prerequisites are needed:

* configure an order event including the order number, status and item name. Refer to this [section](../event/about-events.md).
* create a decision, refer to this [section](../offers/offer-activities/create-offer-activities.md).

➡️ [Discover a similar use case in video](#video) 

## Step 1 - Create the journey {#create-journey}

1. Click the **[!UICONTROL Journeys]** menu and create a new journey.

   ![](assets/perso-uc4.png)

1. Add your entry event, and a **Push** action activity.

   ![](assets/perso-uc5.png)

1. Configure and design your push notification message. Refer to this [section](../push/create-push.md).

## Step 2 - Add personalization on profile {#add-perso}

1. In the **Push** activity, click **Edit content**.

1. Click the **Title** field.

   ![](assets/perso-uc2.png)

1. Enter the subject and add profile personalization. Use the search bar to find the profile's first name field. In the subject text, place the cursor where you want to insert the personalization field, and click the **+** icon. Click **Save**.

   ![](assets/perso-uc3.png)

## Step 3 - Add personalization on contextual data {#add-perso-contextual-data}

1. In the **Push** activity, click **Edit content** and click the **Title** field.

   ![](assets/perso-uc9.png)

1. Select the **Contextual attributes** menu. Contextual attributes are only available if a journey has passed contextual data to the message. Click **Journey Orchestration**. The following contextual information appears:

   * **Events**: this category regroups all fields from the event(s) placed before the channel action activity in the journey.
   * **Journey Properties**: the technical fields related to the journey for a given profile, for example the journey ID or the specific errors encountered. Learn more in [Journey Orchestration documentation](../building-journeys/expression/journey-properties.md).

   ![](assets/perso-uc10.png)

1. Expand the **Events** item, and look for the order number field related to your event. You can also use the search box. Click the **+** icon to insert the personalization field in the subject text. Click **Save**.

   ![](assets/perso-uc11.png)

1. Now click the **Body** field.

   ![](assets/perso-uc12.png)

1. Type the message and insert, from the **[!UICONTROL Contextual attributes]** menu, the order item name and the order progress. 

   ![](assets/perso-uc13.png)

1. From the left menu, select **Offer decisions** to insert a decisioning variable. Select the placement and click the **+** icon next to the decision to add it to the body.  

   ![](assets/perso-uc14.png)

1. Click validate to make sure that there are no errors, and click **Save**.

   ![](assets/perso-uc15.png)

## Step 4 - Test and publish the journey {#test-publish}

1. Click the **Test** button, then click **Trigger an event**.

   ![](assets/perso-uc17.png)

1. Enter the different values to pass in the test. Test mode only works with test profiles. The profile identifier needs to correspond to a test profile. Click **Send**.

   ![](assets/perso-uc18.png)

   The push notification is sent and displayed on the test profile's mobile phone.

    ![](assets/perso-uc19.png)

1. Verify that there is no error and publish the journey.

## How-to video {#video}

The video below shows a similar use case leveraging contextual data from a journey to personalize an email.

>[!VIDEO](https://video.tv.adobe.com/v/3425027?quality=12)
