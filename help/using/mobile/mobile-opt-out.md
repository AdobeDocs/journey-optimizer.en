---
solution: Journey Optimizer
product: journey optimizer
title: Opt-out management for Mobile messages
description: Learn how to manage opt-out with SMS/RCS/MMS messages
feature: SMS
topic: Content Management
role: User
level: Intermediate
exl-id: 59ea67d9-e90c-4ad0-afb9-d0e0fd868855
TQID: https://experienceleague.adobe.com/mQVaZ8jb-hBBPxDnztkayDEI4vj0KvMTREI0KxOgAf0
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
subfeature_v2:
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Opt-out management for Mobile messages {#sms-opt-out}
 
In accordance with the industry standards and regulations, all SMS marketing messages must contain a way for the recipients to easily unsubscribe. [Learn more about privacy & opt-out management](../privacy/opt-out.md)

>[!IMPORTANT]
>
>Mobile message communications may be subject to various legal compliance requirements depending on their nature, the location from where you are sending your Mobile messages, and the location of your recipients. While Adobe Journey Optimizer handles messages on short codes, long codes, and toll-free numbers as detailed below, consult your legal counsel to ensure that your Mobile messaging communications conform to all applicable legal compliance requirements.
>

## Native inbound keywords {#sms-native-keywords}

>[!NOTE]
>
> Only Sinch and Infobip support Native keywords when used with Journey Optimizer.

By default, Adobe Journey Optimizer handles the following standard English-language reply messages for Short codes, Toll-Free and Long Code messages:

* **Opt-Out**: STOP, QUIT, CANCEL, END, UNSUBSCRIBE, NO.
* **Opt-In**: SUBSCRIBE, YES, UNSTOP, START, CONTINUE, RESUME, BEGIN.
* **Help**: HELP.

These keywords typically trigger an automatic standard reply from your third party provider. You can confirm this directly with your provider or via their documentation site.

When using Infobip, ensure that the Forwarding action is set to Pull configuration.

No steps are required to ensure that SMS opt-out capabilities are working in Adobe Journey Optimizer as the keyword responses STOP, UNSTOP, START, QUIT, CANCEL, END, and UNSUBSCRIBE are automatically recognized. Profiles opt-out statuses are updated in real time in Adobe Journey Optimizer.

If you define custom opt-out keywords in your SMS API credentials, they override the default inbound keywords listed above. To keep the default keywords, such as STOP, QUIT, CANCEL, END, and UNSUBSCRIBE, functional, include them explicitly along with your custom keywords in the Opt-Out Keywords field of your SMS configuration. Otherwise, only your custom keywords are recognized, and the default keywords no longer trigger opt-out actions.

Note that if a customer responds STOP to a Mobile message, the provider blocks all subsequent SMS from that specific sender ID (short code or long number), including transactional messages. To ensure uninterrupted delivery of transactional SMS, use a separate sender ID that has not been previously opted out.


>[!NOTE]
>
>If you plan to use two-way SMS (reply with STOP, QUIT, etc.), ensure that you have first sent at least one one-way SMS to establish the phone number to profile mapping. Expired or misconfigured provider credentials will prevent inbound keywords from updating the user profile, resulting in missing or delayed opt-out records. Inbound responses are stored in the _AJO Inbound Activity Event Dataset_ system dataset. [Learn more](../data/get-started-datasets.md#system-datasets)


## Blocklists {#sms-blocklists}

In addition to Adobe Journey Optimizer stopping the send based on the opt-out status (for direct integrations with Twilio, Infobip, or Sinch), most SMS gateway providers also maintain a blocklist ensuring you that an SMS message is not delivered to an individual who has chosen to opt out. If you are using a provider other than Sinch or Twilio, and sending an SMS via [custom channel](../building-journeys/using-custom-actions.md), you need to confirm this with your provider. 


## Short Codes {#short-codes}

By default, opt-in or help keywords for short code numbers are not handled by Adobe Journey Optimizer. To ensure compliance with industry regulations and rules for opt-out handling, it's essential to verify that your short code adheres to all guidelines. 

However, Journey Optimizer does support global opt-outs based on incoming keywords with different sender-IDs.

## Alphanumeric Sender ID {#alphanumeric}

Alphanumeric Sender IDs are for one-way messaging only, and are unable to receive inbound messages. As a result, Adobe Journey Optimizer's SMS STOP, START, HELP keywords are not applicable for Alpha Sender IDs. You must provide other instructions, such as writing to the Support team, calling a Support phone line, or texting another phone number or code to allow users to opt out from messages sent via Alphanumeric Sender ID.

## Video {#video-sms}

* The video below helps you learn how to configure double opt-in for SMS.

    +++ See video

    >[!VIDEO](https://video.tv.adobe.com/v/3427129/?learn=on)

    +++
