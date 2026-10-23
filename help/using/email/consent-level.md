---
solution: Journey Optimizer
product: journey optimizer
title: Choose a consent level for opt-outs
description: Learn the difference between the channel and identity consent levels and how to choose the right one when recipients unsubscribe
feature: Email Design, Consent Management
topic: Content Management
role: User
level: Intermediate
keywords: opt-out, consent level, channel, identity, unsubscribe, email
---
# Choose a consent level for opt-outs {#consent-level}

>[!BEGINSHADEBOX]

**On this page:** Learn what the **Channel** and **Identity** consent levels mean, how they affect profiles with several email addresses, and how to choose between them.

>[!ENDSHADEBOX]

When a recipient unsubscribes, [!DNL Journey Optimizer] must decide where to record the opt-out on the profile. The **[!UICONTROL Consent level]** setting controls this choice. It is available when you configure:

* The [List-Unsubscribe header](list-unsubscribe.md#enable-list-unsubscribe) in an email channel configuration.
* A [one-click opt-out link](email-opt-out.md#one-click-opt-out) in the email content.

## Channel and identity {#channel-vs-identity}

* **[!UICONTROL Channel]**: The opt-out is recorded for the email channel on the whole profile. It applies to every email address (identity) associated with that profile, whichever address received the message.
* **[!UICONTROL Identity]**: The opt-out is recorded only for the email address (identity) that received the message. Other email addresses on the same profile are not affected. This is the default level if nothing else is configured.

The identity is the email address the message was sent to, as stored in the profile's identity namespace. Profiles can hold several email addresses, for example when [Experience Platform identity graph](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/identity-graph-viewer){target="_blank"} links a personal and a work address to the same person.

## Example {#consent-level-example}

Alice has one profile with two email addresses: **alice@personalmail.com** and **alice.smith@bigcorp.com**. She receives a marketing email at her personal address and clicks the unsubscribe link.

| Consent level | What is recorded | Result |
|---|---|---|
| **[!UICONTROL Channel]** | An email opt-out on Alice's profile | Alice no longer receives marketing emails at either address. |
| **[!UICONTROL Identity]** | An opt-out for alice@personalmail.com only | alice@personalmail.com is suppressed. alice.smith@bigcorp.com continues to receive emails. |

## Which level should I choose? {#choose-consent-level}

* Choose **[!UICONTROL Identity]** when profiles can carry several addresses collected over time, such as personal and work addresses, household members, or progressively collected data. An unsubscribe only silences the address that was used.
* Choose **[!UICONTROL Channel]** when unsubscribing must mean "stop emailing this person", whichever address is used. This suits cases where each profile realistically maps to a single working mailbox.

>[!NOTE]
>
>The consent level only applies to unsubscribe actions, such as List-Unsubscribe and one-click opt-out. It does not apply to spam complaints, which are handled by a separate mechanism.
