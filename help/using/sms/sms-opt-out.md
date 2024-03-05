---
solution: Journey Optimizer
product: journey optimizer
title: Opt-out management for text messages
description: Learn how to manage opt-out with SMS/MMS messages
feature: SMS
topic: Content Management
role: User
level: Intermediate
exl-id: 59ea67d9-e90c-4ad0-afb9-d0e0fd868855
---
# Opt-out management for text messages {#sms-opt-out}

In accordance with the industry standards and regulations, all SMS marketing messages must contain a way for the recipients to easily unsubscribe. [Learn more on privacy & opt-out management](../privacy/opt-out.md)

>[!IMPORTANT]
>
>Text message communications may be subject to various legal compliance requirements depending on its nature, the location from where you are sending your text messages, and the location of your recipients. While Adobe Journey Optimizer handles the messages on Short-codes, Long codes and Toll-free numbers as detailed below, consult your legal counsel to ensure that your text messaging communications conform to all applicable legal compliance requirements.
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

No steps are required to ensure that SMS opt-out capabilities are working in Adobe Journey Optimizer as the keyword responses STOP, UNSTOP, START, QUIT, CANCEL, END, and UNSUBSCRIBE are automatically recognized. Profiles opt-out statuses are updated in real time in Adobe Journey Optimizer.


## Blocklists {#sms-blocklists}

In addition to Adobe Journey Optimizer stopping the send based on the opt-out status (for direct integrations with Twilio or Sinch), most SMS gateway providers also maintain a blocklist ensuring you that an SMS message is not delivered to an individual who has chosen to opt out. If you are using a provider other than Sinch or Twilio, and sending an SMS via [custom channel](../building-journeys/using-custom-actions.md), you need to confirm this with your provider. 


## Short Codes {#short-codes}

By default, opt-in or help keywords for short code numbers are not handled by Adobe Journey Optimizer. To ensure compliance with industry regulations and rules for opt-out handling, it's essential to verify that your short code adheres to all guidelines. 

However, Journey Optimizer does support global opt-outs based on incoming keywords with different sender-IDs.

## Alphanumeric Sender ID {#alphanumeric}

Alphanumeric Sender IDs are for one-way messaging only, and are unable to receive inbound messages. As a result, Adobe Journey Optimizer's SMS STOP, START, HELP keywords are not applicable for Alpha Sender IDs. You must provide other instructions, such as writing to the Support team, calling a Support phone line, or texting another phone number or code to allow users to opt out from messages sent via Alphanumeric Sender ID.

## Video {#video-sms}

* The video below shows how native inbound keyword support (START, STOP and UNSTOP) works for SMS.

    +++ See video

    >[!VIDEO](https://video.tv.adobe.com/v/344026?quality=12)

    +++

* The video below helps you learn how to configure double opt-in for SMS.

    +++ See video

    >[!VIDEO](https://video.tv.adobe.com/v/3427129/?learn=on)

    +++
