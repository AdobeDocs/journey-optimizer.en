---
solution: Journey Optimizer
product: journey optimizer
title: AJO Message Export schema
description: Learn about the fields available in the AJO Message Export Dataset
feature: Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: export, messages, dataset, schema, emails, SMS

---
# AJO Message Export schema {#ajo-message-export-schema}

When **Message Export** is enabled on an Email or SMS channel configuration, sent message content is written to the **AJO Message Export Dataset** in [!DNL Adobe Experience Platform].

This section lists the fields available in the exported dataset.

## Dataset fields

+++ _experience

**Field:** `_experience`  
**Type:** object

+++

+++ _experience > customerJourneyManagement

**Field:** `customerJourneyManagement`  
**Type:** object

+++

+++ _experience > customerJourneyManagement > messageDeliveryMetadata

**Field:** `messageDeliveryMetadata`  
**Type:** object

+++

+++ _experience > customerJourneyManagement > messageDeliveryMetadata > emailMetadata

**Field:** `emailMetadata`  
**Type:** object

* recipient

  **Field:** `recipient`  
  **Type:** object

  * bcc

    **Field:** `bcc`  
    **Type:** array of strings

  * cc

    **Field:** `cc`  
    **Type:** array of strings

  * email

    **Field:** `email`  
    **Type:** string

  * name

    **Field:** `name`  
    **Type:** string

* sender

  **Field:** `sender`  
  **Type:** object

  * email

    **Field:** `email`  
    **Type:** string

  * errorEmail

    **Field:** `errorEmail`  
    **Type:** string

  * name

    **Field:** `name`  
    **Type:** string

  * replyToEmail

    **Field:** `replyToEmail`  
    **Type:** string

  * replyToName

    **Field:** `replyToName`  
    **Type:** string

+++

+++ _experience > customerJourneyManagement > messageDeliveryMetadata > smsMetadata

**Field:** `smsMetadata`  
**Type:** object

* recipient

  **Field:** `recipient`  
  **Type:** object

  * number

    **Field:** `number`  
    **Type:** string

* sender

  **Field:** `sender`  
  **Type:** object

  * numbers

    **Field:** `numbers`  
    **Type:** array of strings

+++

+++ _experience > customerJourneyManagement > messageExecution

**Field:** `messageExecution`  
**Type:** object

* audience

  **Field:** `audience`  
  **Type:** object

  * id

    **Field:** `id`  
    **Type:** string

  * type

    **Field:** `type`  
    **Type:** string

* fragmentPublicationIDs

  **Field:** `fragmentPublicationIDs`  
  **Type:** array of strings

* metadata

  **Field:** `metadata`  
  **Type:** map

  * [Map Key]

    **Type:** string

* parentSourceMeta

  **Field:** `parentSourceMeta`  
  **Type:** object

  * sourceActionID

    **Field:** `sourceActionID`  
    **Type:** string

  * sourceID

    **Field:** `sourceID`  
    **Type:** string

  * sourceType

    **Field:** `sourceType`  
    **Type:** string

  * sourceVersionID

    **Field:** `sourceVersionID`  
    **Type:** string

* batchInstanceID

  **Field:** `batchInstanceID`  
  **Type:** string

* campaignActionID

  **Field:** `campaignActionID`  
  **Type:** string

* campaignID

  **Field:** `campaignID`  
  **Type:** string

* campaignVersionID

  **Field:** `campaignVersionID`  
  **Type:** string

* journeyActionID

  **Field:** `journeyActionID`  
  **Type:** string

* journeyVersionID

  **Field:** `journeyVersionID`  
  **Type:** string

* journeyVersionInstanceID

  **Field:** `journeyVersionInstanceID`  
  **Type:** string

* journeyVersionNodeID

  **Field:** `journeyVersionNodeID`  
  **Type:** string

* messageExecutionID

  **Field:** `messageExecutionID`  
  **Type:** string

* messageID

  **Field:** `messageID`  
  **Type:** string

* messagePublicationID

  **Field:** `messagePublicationID`  
  **Type:** string

* messageType

  **Field:** `messageType`  
  **Type:** string

* waveID

  **Field:** `waveID`  
  **Type:** string

+++

+++ _experience > customerJourneyManagement > messageProfile

**Field:** `messageProfile`  
**Type:** object

* channel

  **Field:** `channel`  
  **Type:** object

  * contentTypes

    **Field:** `contentTypes`  
    **Type:** array of strings

  * locationTypes

    **Field:** `locationTypes`  
    **Type:** array of strings

  * metricTypes

    **Field:** `metricTypes`  
    **Type:** array of strings

  * _id

    **Field:** `_id`  
    **Type:** string

  * _type

    **Field:** `_type`  
    **Type:** string

  * mediaAction

    **Field:** `mediaAction`  
    **Type:** string

  * mediaType

    **Field:** `mediaType`  
    **Type:** string

  * mode

    **Field:** `mode`  
    **Type:** string

  * referringSource

    **Field:** `referringSource`  
    **Type:** string

  * typeAtSource

    **Field:** `typeAtSource`  
    **Type:** string

* isSendTimeOptimized

  **Field:** `isSendTimeOptimized`  
  **Type:** boolean

* isTestExecution

  **Field:** `isTestExecution`  
  **Type:** boolean

* messageProfileID

  **Field:** `messageProfileID`  
  **Type:** string

* messageProfileTrackingID

  **Field:** `messageProfileTrackingID`  
  **Type:** string

* requestID

  **Field:** `requestID`  
  **Type:** string

* secondaryDimensionID

  **Field:** `secondaryDimensionID`  
  **Type:** string

* secondaryDimensionName

  **Field:** `secondaryDimensionName`  
  **Type:** string

* variant

  **Field:** `variant`  
  **Type:** string

+++

+++ _experience > customerJourneyManagement > messageRenderedContent

**Field:** `messageRenderedContent`  
**Type:** object

* emailContent

  **Field:** `emailContent`  
  **Type:** object

  * html

    **Field:** `html`  
    **Type:** string

  * subject

    **Field:** `subject`  
    **Type:** string

  * text

    **Field:** `text`  
    **Type:** string

* smsContent

  **Field:** `smsContent`  
  **Type:** object

  * media

    **Field:** `media`  
    **Type:** string

  * message

    **Field:** `message`  
    **Type:** string

  * title

    **Field:** `title`  
    **Type:** string

+++

+++ identityMap

**Field:** `identityMap`  
**Type:** map

* [Map Key]

  **Type:** array of objects

  * authenticatedState

    **Field:** `authenticatedState`  
    **Type:** string

  * id

    **Field:** `id`  
    **Type:** string

  * primary

    **Field:** `primary`  
    **Type:** boolean

+++

+++ eventType

**Field:** `eventType`  
**Type:** string

+++

+++ producedBy

**Field:** `producedBy`  
**Type:** string

+++

+++ timestamp

**Field:** `timestamp`  
**Type:** dateTime

+++

<!--
## Schema reference

![](assets/ajo-message-export-schema.png)-->

