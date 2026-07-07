---
solution: Journey Optimizer
product: journey optimizer
title: CNIL guidance on email tracking pixels
description: Learn about CNIL's updated guidance on email tracking pixels and the Adobe Journey Optimizer controls that can support your compliance efforts.
feature: Privacy, Consent Management
topic: Content Management
role: User
level: Intermediate
keywords: CNIL, tracking, pixel, email, consent, opt-out, privacy
---

# Understanding CNIL's updated guidance on email tracking pixels {#cnil-pixel-tracking}

>[!BEGINSHADEBOX]

**On this page:** Learn about CNIL's April 2026 recommendation on email tracking pixels and discover the Adobe Journey Optimizer controls—open tracking toggles, link-level tracking, consent management, opt-out mechanisms, and suppression—that can support your compliance efforts.

>[!ENDSHADEBOX]

>[!NOTE]
>
>This page is for informational purposes only. It is not legal advice and does not warrant your compliance with applicable law. The Adobe Journey Optimizer product capabilities described below are building blocks that, configured and operated appropriately, may support a compliant implementation. Each customer is responsible for determining and complying with their obligations under applicable law.

## Overview {#overview}

On April 14, 2026, the *Commission Nationale de l'Informatique et des Libertés* (CNIL), France's data protection authority, published a [recommendation on the use of tracking pixels within emails](https://www.cnil.fr/sites/default/files/2026-04/recommandation-pixels_de_suivi.pdf). The guidance clarifies when consent is required and highlights the importance of proper consent practices for email pixel tracking. This policy could impact sending practices for any entity delivering emails to subscribers based in France.

CNIL provided a three-month period from the date of the recommendation for companies to inform their email recipients ("users") of the presence of the tracking pixels, their purpose, and users' right to opt-out. During this transition period, customers are expected to notify users about pixel tracking and provide an opt-out if necessary. CNIL is expected to begin enforcement activities after July 14, 2026.

As CNIL and other regulators clarify guidance on tracking pixels and related issues, Adobe will continue to monitor updates and inform customers of the technical capabilities of Adobe products that support email marketing, including Adobe Journey Optimizer.

Adobe Journey Optimizer provides controls that can help customers manage open tracking at the delivery level. Customers are responsible for determining their own compliance obligations under applicable CNIL guidance and other laws, but these capabilities may support customer compliance efforts.

## What is an email tracking pixel {#tracking-pixel}

An email tracking pixel is a 1x1 transparent image embedded in the HTML of an email. When the recipient's email client loads that image, the pixel pings a server that records data such as a timestamp, device type, email client, and sometimes an IP address for approximate location. That log is then tied to a recipient's record, allowing marketers to see whether an email is opened.

## Customer Support {#support}

Customers seeking assistance implementing the changes described above may engage with their existing Adobe ecosystem. For technical questions about the Adobe capabilities referenced, contact your Customer Success Manager or technical account manager.

## Adobe Journey Optimizer functionality related to email tracking {#ajo-functionality}

Adobe Journey Optimizer provides several native controls to help customers address elements of the CNIL guidance. The sections below describe the relevant product capabilities.

### Email type classification {#email-type}

In Adobe Journey Optimizer, every email channel configuration is classified as either Marketing or Transactional. This classification determines whether subscriber consent is required before sending.

* **Marketing emails**: Promotional communications sent to opted-in subscribers. User consent is required. These emails respect suppression and opt-out preferences automatically.
* **Transactional emails**: Non-commercial communications (e.g., order confirmations, password resets). These can be sent to profiles who have unsubscribed from marketing communications, subject to applicable law.

The email type is set at the channel configuration level. When authoring an email in a journey or campaign, authors must select a channel configuration whose email type matches the nature of the communication. This classification informs which consent checks are applied before delivery.

### Open tracking controls {#open-tracking}

Adobe Journey Optimizer enables marketers to control open tracking (i.e., the 1x1 pixel) at the individual message level. When creating an email in a journey or campaign, two tracking options are available in the message properties panel:

* **[!UICONTROL Email opens]**: Controls whether the open-tracking pixel is included in the email. This option is enabled by default.
* **[!UICONTROL Click on email]**: Controls whether link clicks are tracked. This option is also enabled by default.

To disable open tracking for a specific email, uncheck the **[!UICONTROL Email opens]** option when creating your message. When disabled, the option prevents open tracking data from being collected for that delivery. For organizations sending to French subscribers, review open tracking settings for all active journeys and campaigns before the enforcement date.

<!-- EDITORIAL NOTE – ENGINEERING CONFIRMATION NEEDED before publish:
Clarify whether unchecking "Email opens" fully removes the 1x1 tracking pixel from the delivered HTML, or whether the pixel is still present in the HTML but open data is suppressed at the data processing layer only. The current wording ("prevents open tracking data from being collected") is intentionally neutral. If the pixel is removed: update to state this explicitly. If the pixel remains but data is not processed: reword to make that distinction clear, to avoid misleading customers seeking CNIL compliance. -->

[Learn how to track your messages](../email/message-tracking.md)

### Link-level tracking management {#link-tracking}

Beyond the per-message open tracking toggle, Adobe Journey Optimizer's Email Designer provides granular control over which URLs are tracked. Using the Links panel in the Email Designer, authors can view all tracked URLs in a message and set the tracking mode for each link individually.

Available tracking modes for each link include:

* **Tracked**: Activates tracking on this URL.
* **Opt out**: Designates this URL as an opt-out or unsubscription URL.
* **Mirror page**: Designates this URL as a mirror page link.
* **Never**: Tracking is never activated for this URL, regardless of message-level settings.

Setting specific links to **Never** can help ensure that certain URLs are not tracked even when message-level tracking is enabled.

### Consent capture and management {#consent-management}

Adobe Journey Optimizer handles consent through the Adobe Experience Platform (AEP) Consent and Preferences schema. Consent preferences are stored at the profile level and automatically enforced during journey and campaign execution.

Key consent attributes relevant to email tracking include:

* **`consents.marketing.email.val`**: The primary email marketing consent field. A value of `y` indicates opt-in; `n` indicates opt-out. An empty value is treated as consent by default (this default can be changed at onboarding).

### Opt-out and withdrawal mechanisms {#opt-out}

Adobe Journey Optimizer offers multiple mechanisms for subscribers to opt out of communications and manage their preferences, all of which update the profile's consent attributes in Adobe Experience Platform.

**One-click unsubscribe (email header)**

When the **[!UICONTROL Enable List-Unsubscribe]** option is turned on in the email channel configuration, a one-click unsubscribe URL and mailto address are automatically added to the email header. Recipients can opt out directly from their email client without clicking into the email body. This option is enabled by default for new channel configurations.

**One-click opt-out (email body)**

Authors can insert a one-click opt-out link directly in the email content using the Email Designer. When a recipient clicks this link, their preference is updated immediately. The opt-out can be scoped at either:

* **Channel level**: Opts the profile out of all future email communications across the channel.
* **Identity level**: Opts out the specific email address used in the current message only.

**Preference center via AJO landing pages**

Adobe Journey Optimizer's native landing page capability enables organizations to build preference centers where subscribers can manage their communication and tracking preferences. When a subscriber submits a preference center form, their choices are written back to their AEP profile attributes in the Consent and Preferences field group.

For CNIL compliance scenarios, a preference center landing page can be linked from the email footer (distinct from the unsubscribe link) so that recipients can manage their tracking preferences independently of their subscription status.

### Consent processing and enforcement {#consent-enforcement}

When a recipient opts out through any of the above mechanisms, the following occurs:

* The profile's consent attribute (`consents.marketing.email.val`) is updated to `n` in Adobe Experience Platform.
* The profile is immediately excluded from future marketing email sends in journeys and campaigns.
* The opt-out information is stored in the AEP Consent Service Dataset.
* Journey Optimizer performs a consent check at the channel level before each send, ensuring opted-out profiles do not receive marketing communications.

### Consent policies {#consent-policies}

Organizations can create and enforce consent policies in Adobe Journey Optimizer to ensure that only profiles meeting specific consent criteria receive communications. Consent policies can be associated with channel configurations via marketing actions.

[Learn how to work with consent policies](../action/consent.md)

### Suppression list and re-solicitation {#suppression}

Adobe Journey Optimizer automatically manages a suppression list that includes email addresses resulting in hard bounces, soft bounces, or spam complaints. Profiles on the suppression list are excluded from future marketing sends.

The Journey Optimizer Suppression REST API provides additional programmatic control over outgoing messages, enabling organizations to manage suppression and allowlist behavior via API.

<!-- EDITORIAL NOTE – ENGINEERING CONFIRMATION NEEDED before publish:
AJO has no native equivalent of Campaign v8's "lastPixelRefusalDate" field or re-solicitation typology rule. If re-solicitation governance for pixel consent refusal is required, customers would likely need to: (a) create a custom XDM date field to capture the pixel refusal date, and (b) build an AEP audience that filters out profiles where that date falls within the last six months, then use that audience as a suppression filter in campaigns/journeys. Confirm with Engineering: (1) whether this guidance should be included in this article, and (2) whether any native AJO improvements are planned in this area. -->

### Reporting {#reporting}

Adobe Journey Optimizer's email reporting provides open and click metrics through Live reports and Customer Journey Analytics reports. When **[!UICONTROL Email opens]** tracking is disabled for a message, open data is not collected for that delivery; reporting will reflect clicks and other engagement signals only.

## Documentation references {#references}

For more information regarding email tracking and consent management in Adobe Journey Optimizer, see the documentation below.

| Topic | Documentation reference |
|-------|------------------------|
| Enable and disable open tracking | [Message tracking](../email/message-tracking.md) |
| Email opt-out management | [Email opt-out management](../email/email-opt-out.md) |
| List-Unsubscribe (email header) | [Configure List-Unsubscribe](../email/list-unsubscribe.md) |
| Preference center landing pages | [Landing page use cases](../landing-pages/lp-use-cases.md) |
| Consent and opt-out management | [Manage opt-out](opt-out.md) |
| Consent policies | [Work with consent policies](../action/consent.md) |
| Email channel configuration | [Configure email settings](../email/email-settings.md) |
| Suppression list | [Manage the suppression list](../configuration/manage-suppression-list.md) |
