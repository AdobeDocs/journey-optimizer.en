---
solution: Journey Optimizer
product: journey optimizer
title: Get started with message archiving
description: Learn about BCC and Message Export options for archiving sent messages in Journey Optimizer
feature: Channel Configuration
topic: Administration
role: Admin
level: Experienced
---
# Get started with message archiving {#message-archiving}

>[!BEGINSHADEBOX]

**On this page:** Compare the two options for retaining sent message content from Adobe Journey Optimizer: BCC email and Message Export. Learn how they differ from mirror pages and the Entity Dataset.

>[!ENDSHADEBOX]

Regulations such as HIPAA require that [!DNL Journey Optimizer] provide a way to archive messages sent to individuals. If your customers raise a claim, they should be able to obtain a copy of the sent message for verification purposes.

[!DNL Journey Optimizer] provides two options to support message archiving in your own systems: **BCC email** and **Message Export**.

## Choose an archiving option {#archiving-options}

* **BCC email (Email channel):** Sends a blind copy of each email to the mailbox configured in the channel configuration. Your organization is responsible for retaining and managing the copies in the mailbox or an external archiving system. BCC usage counts against your licensed message volume. [Learn how to archive emails using BCC](archiving-support.md#bcc-email).

* **Message Export (Email and Mobile channels):** Writes sent message content and related metadata to the AJO Message Export Dataset in Adobe Experience Platform for export to your own storage. Requires the Message Export add-on. Dataset records are retained for **seven calendar days from ingestion** and must be exported during that period for longer-term retention. Messages sent before Message Export is enabled cannot be backfilled. [Learn how to export message content](message-export.md).

These options help you retain sent content, but do not replace your organization's archival or compliance solution. Your organization is responsible for configuring external storage, managing retention and access, and assessing whether the solution meets its requirements.

>[!NOTE]
>
>[!DNL Journey Optimizer] does not provide a managed archiving service for Mobile. Use Message Export to retain sent Mobile content, or work with your SMS provider (Sinch, Infobip, or Twilio) for vendor-managed archiving.

## Related capabilities {#not-archiving-options}

The following capabilities serve different purposes and should not be used as substitutes for archiving the exact personalized message sent to an individual:

* **Mirror pages** provide an online version of an email so recipients can view it in a browser. They are available for **90 days** after the email is sent, then expire. A mirror page is a temporary viewing capability, not an archiving option. [Learn more about mirror pages](../email/message-tracking.md#mirror-page).

* **Entity Dataset** contains non-personalized message templates and related metadata. Its `Template` field describes the format and structure of a message, not the exact personalized content received by an individual. Personalized data is not exported through this field. Exporting this dataset can help retain templates and metadata, but is not equivalent to archiving sent messages. [Learn more about the Entity Dataset](../data/datasets-query-examples.md#entity-dataset).

## Identify the right option for your requirement {#compare-options}

Use the table below to identify the right option for your requirement. BCC email and Message Export support archiving sent content in your own systems; mirror pages and the Entity Dataset serve other purposes.

| Requirement | Recommended capability | Archiving option? | Important distinction |
| --- | --- | --- | --- |
| Keep a hidden copy of outbound email messages | [BCC email](archiving-support.md#bcc-email) | Yes | Sends a copy to a configured mailbox; does not expose a mirror page URL or create a queryable Experience Platform field. |
| Export sent email or Mobile content to an external system | [Message Export](message-export.md) | Yes | Writes sent content and metadata to the AJO Message Export Dataset for downstream export; does not generate a mirror page URL. |
| Display the online version of an email to the recipient | [Mirror page link](../email/message-tracking.md#mirror-page) | No - temporary online viewing | Generated as part of the sent email and expires after 90 days; not a supported post-send URL retrieval API or an archiving solution. |
| Store non-personalized message templates or related metadata | [Entity Dataset](../data/datasets-query-examples.md#entity-dataset) | No - templates and metadata only | Does not provide the exact personalized content received by an individual. |

## Frequently asked questions {#faq}

+++ Can I retrieve a mirror page URL after an email is sent?

Not currently, through a documented public API or an Adobe Experience Platform dataset field. The [mirror page URL](../email/message-tracking.md#mirror-page) is generated as part of the message delivery process. If you need to retain or inspect sent content, use [Message Export](message-export.md) or [BCC archiving](archiving-support.md#bcc-email).

+++

+++ Is the mirror page URL available in the Entity Dataset or other tracking datasets?

No. The [Entity Dataset](../data/datasets-query-examples.md#entity-dataset) provides message template and metadata information, but it should not be used as a source for the exact personalized content received by a recipient.

+++

+++ Can Message Export be used to reconstruct a mirror page URL?

No. [Message Export](message-export.md) provides sent message content and metadata for downstream export, archival, compliance, or customer-care use. It does not generate or return a [mirror page URL](../email/message-tracking.md#mirror-page).

+++

+++ Which option should I use if I need to see the exact message sent to a customer?

Use [Message Export](message-export.md) when you need structured sent-message content and metadata in an external system. Use [BCC](archiving-support.md#bcc-email) when you only need a hidden copy of an outbound email retained in a mailbox. Neither option retrieves the original mirror page URL.

+++
