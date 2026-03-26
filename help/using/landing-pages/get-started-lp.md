---
solution: Journey Optimizer
product: journey optimizer
title: Get started with landing pages
description: Learn about landing pages in Journey Optimizer
feature: Landing Pages, Subscriptions
topic: Content Management
role: User
level: Beginner
keywords: landing, landing page, start, get start
exl-id: 0da96e32-52ad-4cc3-bac4-844b1f39ed16
---
# Get started with landing pages {#get-started-lp}

A landing page is a standalone web page that a user is directed to after clicking through from an email, a website, an ad, or any other digital location.

[!DNL Journey Optimizer] allows you to create and design landing pages to direct your users to online forms where they can opt in or opt out from receiving your communications or a specific service such as a newsletter.

➡️ [Learn more about configuring subscriptions and creating landing pages in this video](#video)

## When to use landing pages {#when-to-use}

Use landing pages when you want to:

* Let customers **opt in or opt out** of marketing communications or a specific service or newsletter from a link in an email or campaign—including subscription lists for targeted services. [Read more](lp-use-cases.md#subscription-to-a-service)
* **Collect consent** before sending communications and send a **confirmation email** upon opt-in or opt-out. [Read more](lp-use-cases.md#send-confirmation-email)
* **Capture or update profile data** using forms on **[!UICONTROL Data Capture]** landing pages—for progressive profiling, preferences, registrations, and similar scenarios. [Read more](#data-capture-lp)
* Redirect users to a **dedicated web form** without building an external page outside of [!DNL Journey Optimizer]
* Build **responsive landing pages** using [!DNL Journey Optimizer]'s content design capabilities

### Data capture with landing pages {#data-capture-lp}

**[!UICONTROL Data Capture]** landing pages let you embed published forms so visitors can submit attributes that are written to your [!DNL Adobe Experience Platform] dataset through the streaming connection configured in your form preset. [Learn how to create and embed forms in a landing page](lp-forms.md)

>[!NOTE]
>
>Data capture through landing page forms is supported for **known profiles** (existing profiles identified in [!DNL Adobe Experience Platform]). The landing page should be opened from a **personalized link** (for example from an email campaign) so the profile identity can be resolved when the page loads.

The following are example use cases:

1. **Progressive profile enrichment** — Collect additional attributes from known customers—such as phone number, date of birth, or location—through a personalized landing page to enrich their existing [!DNL Experience Platform] profile for segmentation and personalization.

2. **Preference center update** — Allow known subscribers to manage their communication preferences (channel, topic interests) via a landing page, with changes typically reflected in their [!DNL Experience Platform] profile within about 15 minutes.

3. **Event or webinar registration** — Capture event-specific data from known profiles on a registration page, update the profile with registration attributes, and trigger a confirmation journey.

4. **Loyalty or program enrollment** — Let existing customers enroll in loyalty programs or membership tiers by submitting additional details through a landing page, enriching the profile for downstream targeting.

5. **Competition or contest entry** — Let known customers enter competitions or sweepstakes via a landing page form; capture entry-specific details (answers, preferences, or declarations) and write them to the profile to support eligibility, winner selection, and follow-up journeys.

<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="create-lp.md">
<img alt="Lead" src="../assets/do-not-localize/lp-subscription.jpeg">
</a>
<div><a href="create-lp.md"><strong>Create landing pages</strong>
</div>
<p>
</td>
<td>
<a href="subscription-list.md">
<img alt="Infrequent" src="../assets/do-not-localize/lp-list.jpg">
</a>
<div>
<a href="subscription-list.md"><strong>Create subscription lists</strong></a>
</div>
<p></td>
<td>
<a href="lp-forms.md">
<img alt="Forms list for landing pages in Journey Optimizer" src="../assets/do-not-localize/lp-design.jpg">
</a>
<div>
<a href="lp-forms.md"><strong>Use forms in your landing pages</strong></a>
</div>
<p>
</td>
<td>
<a href="../reports/lp-report-live.md">
<img alt="Validation" src="../assets/do-not-localize/lp-reporting.jpg">
</a>
<div>
<a href="../reports/lp-report-live.md"><strong>Reporting</strong></a>
</div>
<p>
</td>
</tr></table>

## Before you start {#prerequisites}

Before creating a landing page, complete these setup steps:

1. **Configure a subdomain** — Set up a subdomain dedicated to hosting your landing pages. [Learn more](lp-subdomains.md)
1. **Create a landing page preset** — A preset defines the subdomain and other settings applied to your landing pages. [Learn more](lp-presets.md#lp-create-preset)
1. **Create a subscription list** (for subscription use cases) — Required if you want customers to subscribe to or unsubscribe from a specific service. [Learn more](subscription-list.md)
1. **Create a form** (for data capture use cases) — Required when you want to embed a form on a **[!UICONTROL Data Capture]** landing page and send submissions to [!DNL Experience Platform]. [Learn more](lp-forms.md)

## How it works {#how-it-works}

Creating and deploying a landing page follows this sequence:

1. **Create and configure your landing page** — Select a preset, set up the primary page, and add any required subpages. [Learn more](create-lp.md#create-landing-page)
1. **Design the page** — Build the page content and form using [!DNL Journey Optimizer]'s drag-and-drop editor. [Learn more](design-lp.md)
1. **Test and publish your landing page** — Preview the page, test form behavior, then publish to make it live. [Learn more](create-lp.md#test-landing-page)
1. **Link in a message or journey** — Add the landing page URL to an email, campaign, or journey action so customers can reach it. [Learn more](../email/message-tracking.md#insert-links)

## How-to video{#video}

The video below shows how to create a subscription list, set up landing pages to opt in to or opt out from a service, integrate the opt-in/opt-out option to a message and configure relevant journeys.

>[!VIDEO](https://video.tv.adobe.com/v/341280?quality=12&learn=on)
