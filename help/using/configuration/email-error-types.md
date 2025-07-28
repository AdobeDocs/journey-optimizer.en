---
solution: Journey Optimizer
product: journey optimizer
title: Email error types
description: Access the list of all possible email errors upon sending deliveries with Journey Optimizer.
feature: Deliverability, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: retries, bounce, soft, ignored, hard, optimizer, error
hide: yes
hidefromtoc: yes
---

# Email error types {#email-error-types}

Possible reasons for a delivery failure are multiple. The table below details all the errors that could happen upon sending email deliveries with [!DNL Journey Optimizer], together with their description and error type.

These errors can be found in the [AJO Message Feedback Event Dataset](../data/datasets-query-examples.md#message-feedback-event-dataset) which contains the message delivery logs, including information on all message delivery from [!DNL Journey Optimizer], and feedback records from the email ISPs on bounces.

| Error label | Error type | Technical value | Description |
| --- | --- | --- | --- |
| **Undetermined** |  Ignored | 1 | Unable to classify the SMTP bounce message received from the ISP. |
| **Invalid Recipient** | Hard Bounce | 10 | The recipient's address is not valid. |
| **Recipient Refused** | Hard Bounce | 15 | The recipient's ISP has refused the message, and the ISP may block the sender if the recipient is not suppressed. |
| **Soft Bounce** | Soft Bounce | 20 | The message experienced a temporary failure. It may succeed in future retries. |
| **DNS Failure** | Soft Bounce | 21 |  The message delivery experienced a temporary DNS failure. It may succeed in future retries. |
| **Mailbox Full** | Soft Bounce | 22 | The message experienced temporary delivery failure as the recipient's mailbox was full. |
| **Too Large** | Ignored | 23 | The message experienced a temporary delivery failure because the message size exceeded the recipient's limit. |
| **Timeout** | Ignored | 24 | The message delivery failed either because the message validity expired, or it took too long to send to the ISP. |
| **Admin Failure** | Admin | 25 | The delivery failed due to some policy configuration in the email-sending infrastructure. |
| **Generic Bounce: NO RCPT** | Ignored | 30 | The message could not be delivered because the recipient was not identified. |
| **Generic Bounce** | Ignored | 40 | The message experienced a temporary delivery failure for unspecified reasons. |
| **Mail Block** | Ignored | 50 | The delivery experienced temporary failure due to high volume or rate limits by the ISP. |
| **Spam Block** | Ignored | 51 | The delivery experienced temporary failure because the ISP considered the sender's domains or IPs a known spam source. |
| **Spam Content** | Ignored | 52 | The delivery experienced a temporary failure because the ISP classified the email's content as spam. |
| **Relaying Denied** | Soft Bounce | 54 | The message could not be accepted as the destination domain is not allow-listed for relaying. |
| **Auto-Reply** | Ignored | 60 | These messages are discarded by [!DNL Journey Optimizer] when received unless forwarding is enabled. |
| **Transient Failure** | Ignored | 70 | The delivery will be retried at a throttled rate or might be deferred in case of suspension. |
| **Challenge-Response** | Soft Bounce | 100 | The delivery might fail permanently as [!DNL Journey Optimizer] doesn't support a challenge-response authentication mechanism. |
