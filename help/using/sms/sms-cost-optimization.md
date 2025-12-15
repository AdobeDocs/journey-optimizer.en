---
solution: Journey Optimizer
product: journey optimizer
title: SMS best practices for cost optimization
description: Learn how to optimize SMS message costs by managing character limits, encoding, and personalization in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Intermediate
---
# Best practices for SMS cost optimization {#sms-cost-optimization}

SMS messages are typically billed by providers based on a 160-character limit per message. Sending SMS messages can incur additional costs if messages are split into multiple parts. 

Follow these guidelines to optimize your messaging strategy and reduce expenses.

## Keep messages short {#keep-messages-short}

Journey Optimizer allows up to 1,500 characters in an SMS message body. A warning appears when you exceed this limit, and messages beyond this threshold will trigger an error.

Most SMS providers support GSM 7-bit encoding, where a single SMS can contain up to 160 characters. Messages exceeding this length are automatically split into multiple SMS parts (concatenation):

* **Less than 160 characters**: 1 SMS part
* **161-306 characters**: 2 SMS parts
* **307-459 characters**: 3 SMS parts

**To minimize costs**, aim to keep messages under 160 characters so they are billed as a single SMS part.

For example, a 1,600-character message could consume 10 SMS credits, even though it appears as a single message in Journey Optimizer.

## Avoid special characters that increase length {#avoid-special-characters}

Certain characters—such as `| ^ € { } [ ] ~ \` are counted as two characters in GSM encoding. Including these characters can cause your message to exceed the **160-character limit** more quickly.

## Prevent UCS-2 encoding {#prevent-ucs2-encoding}

If the message includes non-GSM characters, such as Chinese or Arabic text, trademark symbols, or hard returns from rich-formatting tools, the message will be encoded by the provider using UCS-2, which supports only 70 characters per SMS. 

Using UCS-2 encoding may increase the character count and, consequently, affect message billing with your service provider. 

For example, a 200-character Unicode message will be delivered in 3 SMS parts. 

## Authoring best practices {#authoring-best-practices}

Compose the final SMS message directly within Journey Optimizer or paste it from plain-text applications.

Avoid using rich-text applications, as they may introduce hidden characters or line breaks that trigger UCS-2 encoding, potentially increasing both the number of SMS parts and associated costs.

## Check character count before sending {#check-character-count}

Use plain-text applications or Journey Optimizer **[!UICONTROL Simulate content]** menu to verify character counts.

While Journey Optimizer displays a character count, including spaces, during content simulation, note that:

* It does **not** include characters generated through dynamic personalization or certain special characters.

* The **x/1500 count** serves as a visual indicator of the technical payload limit, not the per-message limit, for example, the 160-character GSM 7-bit limit.

* Adobe supports UTF-8 encoding in the editor, which differs from GSM-7-bit encoding.

## Understanding reporting {#understanding-reporting}

**Journey Optimizer reporting** counts the full message as one send, regardless of SMS parts. 

**Provider reporting** reflects the actual number of SMS message parts used for delivery and should be referenced to confirm billing and any potential overages. If Adobe is your SMS provider via Sinch, you will receive this billing report separately on a monthly basis.

## Personalization considerations {#personalization-considerations}

Dynamic personalization may increase the length of a message. For instance, substituting a variable with a long first name can add additional characters.

## Additional resources {#additional-resources}

Review supported characters and encoding rules in [Sinch Character Support Guide](https://developers.sinch.com/docs/sms/resources/message-info/character-support/)

