---
solution: Journey Optimizer
product: journey optimizer
title: Landing page use cases
description: Discover the most common use cases with landing pages in Journey Optimizer
feature: Landing Pages, Subscriptions
topic: Content Management
role: User
level: Intermediate
keywords: landing, landing page, use case
exl-id: 8c00d783-54a3-45d9-bd8f-4dc58804d922
---
# Landing page use cases {#lp-use-cases}

Below are some examples of how you can use [!DNL Journey Optimizer] landing pages to have your customers opt in/out from receiving some or all of your communications.

## Subscribe to a service {#subscription-to-a-service}

One of the most common use cases consists in inviting your customers to [subscribe to a service](subscription-list.md) (such as a newsletter or an event) through a landing page. The main steps are presented on the graph below:

![](assets/lp_subscription-uc.png)

For example, let's say you organize an event next month and you want to launch an event registration campaign<!--to keep your customers that are interested updated on that event-->. To do this, you're going to send an email including a link to a landing page that will enable your recipients to register for this event. The users who register will be added to the subscription list that you created for this purpose.

### Set up a landing page {#set-up-lp}

1. Create the event registration's subscription list, which will store the registered users. Learn how to create a subscription list [here](subscription-list.md#define-subscription-list).

    ![](assets/lp_subscription-uc-list.png)

1. [Create a landing page](create-lp.md) to enable your recipients to register for your event.

    ![](assets/lp_create-lp-details.png)

1. Configure the registration [primary landing page](create-lp.md#configure-primary-page).

1. When designing the [landing page content](design-lp.md), select the subscription list that you created to update it with the profiles who select the registration checkbox.

    ![](assets/lp_subscription-uc-lp-list.png)

1. Create a 'thank you' page that will be displayed to your recipients once they submit the registration form. Learn how to configure landing subpages [here](create-lp.md#configure-subpages).

    ![](assets/lp_subscription-uc-thanks.png)

1. [Publish](create-lp.md#publish) the landing page.

1. In a [journey](../building-journeys/journey.md), add an **Email** activity to drive traffic to the registration landing page.

    ![](assets/lp_subscription-uc-journey.png)

1. [Design the email](../email/get-started-email-design.md) to announce that registration is now open for your event.

1. [Insert a link](../email/message-tracking.md#insert-links) into your message content. Select **[!UICONTROL Landing page]** as the **[!UICONTROL Link type]** and choose the [landing page](create-lp.md#configure-primary-page) that you created for registration.

    ![](assets/lp_subscription-uc-link.png)

    >[!NOTE]
    >
    >To be able to send your message, make sure the landing page you select is not expired yet. Learn how to update the expiry date [in this section](create-lp.md#configure-primary-page).

    Once they receive the email, if your recipients click the link to the landing page, they will be directed to the 'thank you' page and they will be added to the subscription list.

### Send a confirmation email {#send-confirmation-email}

Additionally, you can send a confirmation email to the recipients who registered for your event. To do so, follow the steps below.

1. Create another [journey](../building-journeys/journey.md). You can do it directly from the landing page by clicking the **[!UICONTROL Create journey]** button. [Learn more](create-lp.md#configure-primary-page)

    ![](assets/lp_subscription-uc-create-journey.png)

1. Unfold the **[!UICONTROL Events]** category and drop an **[!UICONTROL Audience Qualification]** activity into your canvas. [Learn more](../building-journeys/audience-qualification-events.md)

1. Click in the **[!UICONTROL Audience]** field and select the subscription list that you created.

    ![](assets/lp_subscription-uc-confirm-journey.png)

1. Add a confirmation email of your choice and send it through the journey.

    ![](assets/lp_subscription-uc-confirm-email.png)

All the users who registered for your event will receive the confirmation email.

<!--The event registration's subscription list tracks the profiles who registered and you can send them targeted event updates.-->

## Opt-out landing page {#opt-out}

To enable your recipients to unsubscribe from your communications, you can include a link to an opt-out landing page into your emails.

>[!NOTE]
>
>Learn more on managing your recipients' consent and why this is important in [this section](../privacy/opt-out.md).

### Opt-out management {#opt-out-management}

Providing the capability to recipients to unsubscribe from receiving communications from a brand is a legal requirement. Learn more about the applicable legislation in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/privacy/regulations/overview.html#regulations){target="_blank"}.

Therefore, you must always include an **unsubscribe link** in every email sent out to recipients:

* Upon clicking this link, the recipients will be directed to a landing page including a button to confirm opting out.
* Upon clicking the opt-out button, the profile data will be updated with this information.

### Configure email opt-out {#configure-opt-out}

To enable the recipients of an email to unsubscribe from your communications through a landing page, follow the steps below:

1. Create your landing page. [Learn more](create-lp.md)

1. Define the primary page. [Learn more](create-lp.md#configure-primary-page)

1. [Design](design-lp.md) the primary page content: use the landing page-specific **[!UICONTROL Form]** component, define an **[!UICONTROL Opt-out]** checkbox and choose to update **[!UICONTROL Channel (email)]**: the profile that checks the opt-out box on your landing page will be opted out from all your communications.

    ![](assets/lp_opt-out-primary-lp.png)

    <!--You can also build your own landing page and host it on the third-party system of your choice.-->

1. Add a confirmation [subpage](create-lp.md#configure-subpages) that will be displayed to the users who submit the form.

    ![](assets/lp_opt-out-subpage.png)

    >[!NOTE]
    >
    >Make sure you reference the subpage in the primary page's **[!UICONTROL Call to action]** section of the **[!UICONTROL Form]** component. [Learn more](design-lp.md)

1. Once you configured and defined the content of your pages, [publish](create-lp.md#publish) the landing page.

1. [Create an email message](../email/get-started-email-design.md) in a journey.

1. Select text in your content and [insert a link](../email/message-tracking.md#insert-links) using the contextual toolbar. You can also use a link on a button.

1. Select **[!UICONTROL Landing page]** from the **[!UICONTROL Link type]** drop-down list and select the [landing page](create-lp.md#configure-primary-page) that you created for opting out.

    ![](assets/lp_opt-out-landing-page.png)

    >[!NOTE]
    >
    >To be able to send your message, make sure the landing page you select is not expired yet. Learn how to update the expiry date [in this section](create-lp.md#configure-primary-page).

1. Publish and run the journey. [Learn more](../building-journeys/journey.md).

1. Once the message is received, if a recipient clicks the unsubscribe link in the email, your landing page is displayed.

    ![](assets/lp_opt-out-submit-form.png)

    If the recipient checks the box and submits the form:

    * The opted-out recipient is redirected to the confirmation message screen.

    * The profile data is updated and will not receive communications from your brand unless subscribed again.

To check that the corresponding profile's choice has been updated, go to Experience Platform and access the profile by selecting an identity namespace and a corresponding identity value. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.

![](assets/lp_opt-out-profile-choice.png)

In the **[!UICONTROL Attributes]** tab, you can see that the value for **[!UICONTROL choice]** has changed to **[!UICONTROL no]**.

The opt-out information is stored in the **Consent Service Dataset**. [Learn more on datasets](../data/get-started-datasets.md)

>[!NOTE]
>
>If the merge method for your default [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"} **[!UICONTROL Profiles]** merge policy is **[!UICONTROL Dataset Precedence]**, make sure to enable the **[!UICONTROL AJO Consent Service Dataset]** and to prioritize it in the merge policy. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html#dataset-precedence-profile){target="_blank"}
>
>Even if no batches have been added to this dataset, it will still contain the opt-in/opt-out information.



**See also:**

* [One-click opt-out](../email/email-opt-out.md#one-click-opt-out-link)
* [Opt-out link in the email header](../email/email-opt-out.md#unsubscribe-header)

<!--

### Other ways to opt out

You can also enable your recipients to unsubscribe whithout using landing pages.

* **One-click opt-out**

    You can add a one-click opt-out link into your email content. This will enable your recipients to quickly unsubscribe from your communications, without being redirected to a landing page where they need to confirm opting out. [Learn more](../privacy/opt-out.md#one-click-opt-out-link)

* **Unsubscribe link in header**

    If the recipients' email client supports displaying an unsubscribe link in the email header, emails sent with [!DNL Journey Optimizer] automatically include this link. [Learn more](../privacy/opt-out.md#unsubscribe-header)

////////


## Leverage landing page submission event {#leverage-lp-event}

You can use information that was submitted on a landing page to send communications to your customers. For example, if a user subscribes to a given subscription list, you can leverage that information to send an email recommending other subscription lists to that user.

To do this, you need to create an event containing the landing page submission information and use it in a journey. Follow the steps below.

1. Go to **[!UICONTROL Administration]** > **[!UICONTROL Configurations]**, and in the **[!UICONTROL Events]** section, select **[!UICONTROL Manage]**.

    ![](assets/lp_subscription-uc-configurations.png)

1. The list of events displays. Select **[!UICONTROL Create Event]**.

    ![](assets/lp_subscription-uc-create-event.png)

1. The event configuration pane opens on the right side of the screen. Configure a rule-based unitary event. [Learn more](../event/about-creating.md)

1. Define the schema: select **[!UICONTROL AJO Email Tracking Experience Event Schema v.1]** (available by default in [!DNL Journey Optimizer]).

    ![](assets/lp_subscription-uc-event-schema.png)

1. In the **[!UICONTROL Fields]** section, select the following elements:

    * **[!UICONTROL _experience]** > **[!UICONTROL customerJourneyManagement]** > **[!UICONTROL messageInteraction]** > **[!UICONTROL Interaction Type]**
    
    * **[!UICONTROL _experience]** > **[!UICONTROL customerJourneyManagement]** > **[!UICONTROL messageInteraction]** > **[!UICONTROL Landing Page Details]** > **[!UICONTROL Landing Page ID]**

    ![](assets/lp_subscription-uc-event-fields.png)

1. Click inside the **[!UICONTROL Event ID condition]** field. Using the simple expression editor, define the condition for the **[!UICONTROL Interaction Type]** and **[!UICONTROL Landing Page ID]** fields. This will be used by the system to identify the events that will trigger your journey.

    ![](assets/lp_subscription-uc-event-id-condition.png)

    >[!NOTE]
    >
    >To find the landing page ID, you can insert the landing page as a link into an email and select the source code from the contextual toolbar to display the landing page information.
    >
    >![](assets/lp_subscription-uc-lp-id.png)

1. Save your changes.

1. Create a [journey](../building-journeys/journey.md). You can do it directly from the landing page by clicking the **[!UICONTROL Create journey]** button. Learn more [here](create-lp.md#configure-primary-page)

    ![](assets/lp_subscription-uc-event-create-journey.png)

1. In the journey, unfold the **[!UICONTROL Events]** category and drop the event that you created into the canvas. Learn more [here](../building-journeys/audience-qualification-events.md)

    ![](assets/lp_subscription-uc-journey-event.png)

1. Unfold the **[!UICONTROL Actions]** category and drop an email action into the canvas.

    ![](assets/lp_subscription-uc-journey-email.png)

///How do you use the information from the event to send an email to the users? -->
