---
solution: Journey Optimizer
product: journey optimizer
title: Archiving support in Journey Optimizer
description: Learn how to archive messages
feature: Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: archive, messages, HIPAA, BCC, emails
exl-id: 186a5044-80d5-4633-a7a7-133e155c5e9f
---
# Support for archiving {#archiving-support}

## How to archive messages {#about-archiving}

Regulations such as HIPAA require that [!DNL Journey Optimizer] should provide a way to archive messages sent to individuals. Indeed, if your customers raise a claim, they should have the ability to get a copy of the sent message for verification purpose.

* For the email channel, [!DNL Journey Optimizer] provides a built-in BCC email capability. [Learn more](#bcc-email)

* Additionnaly, for all channels, you can use the 'Template' field in the **Entity Dataset**, which contains the details of the non-personalized message templates. Export the dataset with this field to save metadata such as: who sent the message, to whom and when. Note that personalized data is not exported - only the template (format and structure of the message) is taken into account. [Learn more](../data/datasets-query-examples.md#entity-dataset)

>[!NOTE]
>
>[!DNL Journey Optimizer] does not own support for SMS archival requirement. For dedicated archival support, work with your SMS vendor (Sinch, Infobip, or Twilio).

## How to use BCC for emails {#bcc-email}

>[!CONTEXTUALHELP]
>id="ajo_admin_preset_bcc"
>title="Define a BCC email address"
>abstract="You can keep a copy of sent emails by sending them to a BCC inbox. Enter the email address of your choice so that every email sent is blind-copied to this BCC address. Note that the BCC address domain must be different from any subdomain delegated to Adobe. This feature is optional."

You can send blind carbon copy (BCC) of an email sent by [!DNL Journey Optimizer] to a dedicated BCC address. This optional feature allows you to retain copies of email communications you send to your users for compliance and/or archival purposes. The BCC address is not visible to other recipients of the message.

### Enable BCC email {#enable-bcc}

To enable the **[!UICONTROL BCC email]** option, enter the email address of your choice in the dedicated field of the [channel configuration](channel-surfaces.md) (i.e. message preset). You can specify any external address in correct format, except an email address defined on a subdomain delegated to Adobe. For example, if you delegated the *marketing.luma.com* subdomain to Adobe, any address like *abc@marketing.luma.com* is prohibited.

>[!CAUTION]
>
>You can only define one BCC email address. Make sure the BCC address has enough reception capacity to store all the emails that are sent using the current channel configuration.
>
>More recommendations are listed in [this section](#bcc-recommendations-limitations).

>[!NOTE]
>
>If you have purchased the Healthcare Shield add-on offering, you must ensure that your BCC addresse's ISP supports the TLS 1.2 protocol.

![](assets/preset-bcc.png)

Once configuration is done, all email messages based on this configuration are blind-copied to the BCC email address you entered. From there, messages can be processed and archived using an external system.

>[!CAUTION]
>
>Your BCC feature usage is counted against the number of messages you are licensed for. Hence, only enable it in the configurations used for critical communications that you wish to archive. Check your contract for licensed volumes.

The BCC email address setting is immediately saved and processed at the configuration level. When you create a new message using this configuration, the BCC email address is automatically displayed.

![](assets/preset-bcc-in-msg.png)

However, the BCC address gets picked up for sending communications following the logic described [here](../email/email-settings.md).

### Recommendations and limitations {#bcc-recommendations-limitations}

* To ensure your privacy compliance, BCC emails must be processed by an archiving system capable of storing securely personally identifiable information (PII).

* As messages can contain sensitive or private data, such as personally identifiable information (PII), make sure the BCC address is correct, and secure the access to messages.

* Your inbox used for BCC should be properly managed for space and delivery. If the inbox returns bounces, some emails may not be received and therefore will fail to get archived.

* Messages may be delivered to the BCC email address before the target recipients. BCC messages can also been sent even though the original messages may have [bounced](../reports/suppression-list.md#delivery-failures).

    <!--OR: Only successfully sent emails are taken in account. [Bounces](../reports/suppression-list.md#delivery-failures) are not. TO CHECK -->

* Do not open or click through the emails sent to the BCC address as it is taken into account in the total opens and clicks from the send analysis, which could cause some miscalculations in [reports](../reports/global-report.md). 

* Do not mark messages as spam in the BCC inbox, as it will impact all the other emails sent to this address.

>[!CAUTION]
>
>Do not click the unsubscribe link in the emails sent to the BCC address as you will immediately unsubscribe the corresponding recipients.

### GDPR compliance {#gdpr-compliance}

Regulations such as GDPR state that Data Subjects should be able to modify their consent at any time. Because the BCC emails you are sending with Journey Optimizer include securely personally identifiable information (PII), you must edit the **[!UICONTROL CJM Email BCC Feedback Event Schema]** to be able to manage these PII in compliance with GDPR and similar regulations.

To do this, follow the steps below.

1. Go to **[!UICONTROL Data management]** > **[!UICONTROL Schemas]** > **[!UICONTROL Browse]** and select **[!UICONTROL CJM Email BCC Feedback Event Schema]**.

    ![](assets/preset-bcc-schema.png)

1. Click to expand **[!UICONTROL _experience]**, **[!UICONTROL customerJourneyManagment]** then **[!UICONTROL secondaryRecipientDetail]**.

1. Select **[!UICONTROL originalRecipientAddress]**.

1. In the **[!UICONTROL Field properties]** on the right, scroll down to the **[!UICONTROL Identity]** checkbox.

1. Select it and also select **[!UICONTROL Primary identity]**.

1. Select a namespace from the drop-down list.

    ![](assets/preset-bcc-schema-identity.png)

1. Click **[!UICONTROL Apply]**.

>[!NOTE]
>
>Learn more on managing Privacy and the applicable regulations in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/privacy/home.html){target="_blank"}.

### BCC reporting data {#bcc-reporting}

Reporting as such on BCC is not available in the journey and message reports. However, information is stored on a system dataset called **[!UICONTROL AJO BCC Feedback Event Dataset]**. You can run queries against this dataset to find useful information for debugging purpose for example.

To access this dataset through the user interface, select **[!UICONTROL Data management]** > **[!UICONTROL Datasets]** > **[!UICONTROL Browse]**. Learn more on how to access datasets in [this section](../data/get-started-datasets.md#access-datasets).

<!--![](assets/preset-bcc-dataset.png)-->

To run queries against this dataset, you can use the Query Editor provided by the [Adobe Experience Platform Query Service](https://experienceleague.adobe.com/docs/experience-platform/query/api/getting-started.html){target="_blank"}. To access it, select **[!UICONTROL Data management]** > **[!UICONTROL Queries]** and click **[!UICONTROL Create query]**. [Learn more](../data/get-started-queries.md)

![](assets/preset-bcc-queries.png)

Depending on what information you are looking for, you can run the following queries.

1. For all the other queries below, you will need the journey action ID. Run this query to fetch all action IDs associated with a particular journey version ID within the last 2 days:

    ```
    SELECT
    DISTINCT
    CAST(TIMESTAMP AS DATE) AS EventTime,
    _experience.journeyOrchestration.stepEvents.journeyVersionID,
    _experience.journeyOrchestration.stepEvents.actionName, 
    _experience.journeyOrchestration.stepEvents.actionID 
    FROM journey_step_events 
    WHERE 
    _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey version id>' AND 
    _experience.journeyOrchestration.stepEvents.actionID is not NULL AND 
    TIMESTAMP > NOW() - INTERVAL '2' DAY 
    ORDER BY EventTime DESC;
    ```

    >[!NOTE]
    >
    >To get the `<journey version id>`parameter, select the corresponding [journey version](../building-journeys/journey.md#journey-versions) from the **[!UICONTROL Journey management]** > **[!UICONTROL Journeys]** menu. The journey version ID is displayed at the end of the URL displayed in your web browser.
    >
    >![](assets/preset-bcc-action-id.png)

1. Run this query to fetch all message feedback events (especially feedback status) generated for a particular message targeted to a specific user within the last 2 days:

    ```
    SELECT  
    _experience.customerJourneyManagement.messageExecution.journeyVersionID AS JourneyVersionID, 
    _experience.customerJourneyManagement.messageExecution.journeyActionID AS JourneyActionID, 
    timestamp AS EventTime, 
    _experience.customerJourneyManagement.emailChannelContext.address AS RecipientAddress, 
    _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackStatus AS FeedbackStatus,
    CASE _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackStatus
        WHEN 'sent' THEN 'Sent'
        WHEN 'delay' THEN 'Retry'
        WHEN 'out_of_band' THEN 'Bounce' 
        WHEN 'bounce' THEN 'Bounce'
    END AS FeedbackStatusCategory
    FROM cjm_message_feedback_event_dataset 
    WHERE  
        timestamp > now() - INTERVAL '2' day  AND
        _experience.customerJourneyManagement.messageExecution.journeyVersionID = '<journey version id>' AND 
        _experience.customerJourneyManagement.messageExecution.journeyActionID = '<journey action id>' AND  
        _experience.customerJourneyManagement.emailChannelContext.address = '<recipient email address>'
        ORDER BY EventTime DESC;
    ```

    >[!NOTE]
    >
    >To get the `<journey action id>` parameter, run the first query described above using the journey version id. The `<recipient email address>` parameter is the targeted or actual recipient's email address.

1. Run this query to fetch all BCC message feedback events generated for a particular message targeted to a specific user within the last 2 days:

    ```
    SELECT   
    _experience.customerJourneyManagement.messageExecution.journeyVersionID AS JourneyVersionID, 
    _experience.customerJourneyManagement.messageExecution.journeyActionID AS JourneyActionID, 
    _experience.customerJourneyManagement.emailChannelContext.address AS BccEmailAddress,
    timestamp AS EventTime, 
    _experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress AS RecipientAddress, 
    _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackStatus AS FeedbackStatus,
    CASE _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackStatus
                WHEN 'sent' THEN 'Sent'
                WHEN 'delay' THEN 'Retry'
                WHEN 'out_of_band' THEN 'Bounce' 
                WHEN 'bounce' THEN 'Bounce'
            END AS FeedbackStatusCategory 
    FROM ajo_bcc_feedback_event_dataset  
    WHERE  
    timestamp > now() - INTERVAL '2' day  AND
    _experience.customerJourneyManagement.messageExecution.journeyVersionID = '<journey version id>' AND 
    _experience.customerJourneyManagement.messageExecution.journeyActionID = '<journeyaction id>' AND 
    _experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress = '<recipient email address>'
    ORDER BY EventTime DESC;
    ```

1. Run this query to fetch all recipient addresses who have not received the message whereas its BCC entry exists within the last 30 days:

   ```
    SELECT
        DISTINCT 
    bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress AS RecipientAddressesNotRecievedMessage
    FROM ajo_bcc_feedback_event_dataset bcc
    LEFT JOIN cjm_message_feedback_event_dataset mfe
    ON 
   bcc._experience.customerJourneyManagement.messageExecution.journeyVersionID =
            mfe._experience.customerJourneyManagement.messageExecution.journeyVersionID AND    bcc._experience.customerJourneyManagement.messageExecution.journeyActionID = mfe._experience.customerJourneyManagement.messageExecution.journeyActionID AND 
   bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress = mfe._experience.customerJourneyManagement.emailChannelContext.address AND
   mfe._experience.customerJourneyManagement.messageExecution.journeyVersionID = '<journey version id>' AND 
   mfe._experience.customerJourneyManagement.messageExecution.journeyActionID = '<journey action id>' AND
   mfe.timestamp > now() - INTERVAL '30' DAY AND
   mfe._experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus IN ('bounce', 'out_of_band') 
    WHERE bcc.timestamp > now() - INTERVAL '30' DAY;
   ```

### Use message header to reconcile BCC copy and sent email information {#bcc-header}

When your email BCC copies are archived on an external system for example, you can retrieve the information on the corresponding sent emails using a header included in the message.

Every email message now contains a header called `x-message-profile-id`. This header's value is different for each profile: it is unique to each sent email and to its corresponding BCC email copy.

The `x-message-profile-id` header is also stored in the following system datasets: [AJO Message Feedback Event Dataset](../data/datasets-query-examples.md#message-feedback-event-dataset) (sent emails) and [AJO BCC Feedback Event Dataset](#bcc-reporting) (BCC copies). You can query these datasets to reconcile the BCC copy and the corresponding actual email.

* To access these datasets through the user interface, select **[!UICONTROL Data management]** > **[!UICONTROL Datasets]** > **[!UICONTROL Browse]**. Learn more on how to access datasets in [this section](../data/get-started-datasets.md#access-datasets).

* Use the Query Editor provided by the [Adobe Experience Platform Query Service](https://experienceleague.adobe.com/docs/experience-platform/query/api/getting-started.html){target="_blank"}. To access it, select **[!UICONTROL Data management]** > **[!UICONTROL Queries]** and click **[!UICONTROL Create query]**. [Learn more](../data/get-started-queries.md)

Below are a few sample queries you can run to retrieve information corresponding to your BCC copies.

**Query 1**

To get the BCC event stitched with the corresponding feedback event for the actual email with the campaign action details:

```
SELECT
  mfe.timestamp as OriginalRecipientFeedbackEventTime,
  mfe._experience.customerJourneyManagement.emailChannelContext.address AS OriginalRecipientEmailAddress,
  mfe._experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus AS OriginalRecipientMessageFeedbackStatus,
  mfe._experience.customerJourneyManagement.messageExecution.campaignID AS CampaignID,
  mfe._experience.customerJourneyManagement.messageExecution.campaignActionID AS CampaignActionID,
  mfe._experience.customerJourneyManagement.messageExecution.batchInstanceID AS BatchInstanceID,
  mfe._experience.customerJourneyManagement.messageExecution.messageID AS MessageID AS MessageID
FROM ajo_bcc_feedback_event_dataset bcc
LEFT JOIN cjm_message_feedback_event_dataset mfe
ON bcc._experience.customerJourneyManagement.messageProfile.messageProfileID =
    mfe._experience.customerJourneyManagement.messageProfile.messageProfileID AND 
    mfe.timestamp > now() - INTERVAL '30' day
WHERE 
  bcc.timestamp > now() - INTERVAL '30' DAY AND 
  bcc._experience.customerJourneyManagement.messageProfile.messageProfileID = 'x-message-profile-id'
ORDER BY timestamp DESC;
```

**Query 2**

To get the BCC event stitched with the corresponding feedback event for the actual email with the journey action details:

```
SELECT
  mfe.timestamp as OriginalRecipientFeedbackEventTime,
  mfe._experience.customerJourneyManagement.emailChannelContext.address AS OriginalRecipientEmailAddress,
  mfe._experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus AS OriginalRecipientMessageFeedbackStatus,
  mfe._experience.customerJourneyManagement.messageExecution.journeyVersionID AS JourneyVersionID,
  mfe._experience.customerJourneyManagement.messageExecution.journeyVersionInstanceID AS JourneyVersionInstanceID,
  mfe._experience.customerJourneyManagement.messageExecution.batchInstanceID AS BatchInstanceID,
  mfe._experience.customerJourneyManagement.messageExecution.messageID AS MessageID AS MessageID
FROM ajo_bcc_feedback_event_dataset bcc
LEFT JOIN cjm_message_feedback_event_dataset mfe
ON bcc._experience.customerJourneyManagement.messageProfile.messageProfileID =
    mfe._experience.customerJourneyManagement.messageProfile.messageProfileID AND 
    mfe.timestamp > now() - INTERVAL '30' day
WHERE 
  bcc.timestamp > now() - INTERVAL '30' DAY AND 
  bcc._experience.customerJourneyManagement.messageProfile.messageProfileID = 'x-message-profile-id'
ORDER BY timestamp DESC;
```