---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Explains how to add an email to a journey or a campaign in Journey Optimizer, override values of the email channel configuration at the action level, define the subject line and content, check alerts, optimize the HTML size, and preview the email before sending.

**Intents:**

* Add an email to a journey (an Action activity with the Email channel selected) or to a campaign (Email selected as your action).
* Override specific values inherited from the selected email channel configuration directly at the action level, including with contextual data.
* Define the email content: the subject line, the sender information, and the email body using the Email Designer, with decision policies if you toggle Enable decisioning.
* Check the warnings and errors displayed when key settings are missing.
* Optimize the HTML size of the email and test the impact of the optimization when sending proofs.
* Preview the content with Simulate content, and validate its quality, before activating the journey or campaign.

**Glossary:**

* **Action activity** *(product-specific)*: in a journey, the activity dragged and dropped from the Actions section of the palette. Email is selected as the action type, and the Label identifies the action in the journey canvas.
* **Email configuration**: the configuration that you select or create for the email. The From name, From email and BCC fields shown in the Header section are configured in it.
* **Message category**: Marketing or Transactional. It is defined at the channel configuration level and when creating the message from a journey or a campaign.
* **Override email channel configuration**: toggle you enable after selecting the email configuration. It lets you change only specific fields of the values inherited from the selected channel configuration, directly at the action level, without creating a new channel configuration. The configured value displays under each override field; to keep the configured value for a setting, leave that field empty.
* **Contextual data**: available for the override fields because the action runs in a journey or campaign execution context, as opposed to channel configuration, which is defined at setup time. You can use it to personalize the override fields, in addition to profile attributes and helper functions.
* **Email header override fields**: From name, From email prefix, Reply to name, and Reply to email. Overriding them allows sender details to reflect information such as the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address.
* **Delivery address** (execution address override): when several email addresses are available for a given profile, Journey Optimizer uses the execution field set in the general settings or in the channel configuration to determine which email address to use from the profile service in priority. The override defines a different value at the action level than the one set globally.
* **List-unsubscribe override fields**: Mailto (unsubscribe) and One-click unsubscribe URL. They let you replace the unsubscribe address and one-click unsubscribe URL set at the channel configuration level. The one-click List unsubscribe URL is an unsubscribe link or button displayed next to the email sender information; it lets recipients instantly opt out of your mailing lists with a single click.
* **Enable decisioning**: toggle to use if you want to add decision policies in your email.
* **Decision policies** *(product-specific)*: containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.
* **Email Designer**: accessed with the Edit email body button, to start building your content.
* **Code Editor**: button available if you are in a campaign, to code your own content in plain HTML using the pop-up window that displays. Content already created or imported through the Email Designer displays in HTML.
* **Alerts**: displayed in the interface (on top right of the screen) when key settings are missing. Two types of alerts can happen: warnings and errors. Warnings refer to recommendations and best practices.
* **Optimize HTML size**: option that compresses the email HTML version during the publishing process by removing unnecessary whitespace and indentation. Keeping the HTML size small helps you avoid email clipping, improve email load time, and improve deliverability and reduce bandwidth usage. The optimization is email-client safe: it preserves MSO/Outlook conditional comments and does not alter your actual content, images, or videos.
* **Email clipping**: some clients such as Gmail truncate messages larger than ~100 KB, preventing recipients from viewing the full content.
* **Simulate content**: preview option to test content variations with sample input data or AI auto-generation.
* **Simulate content (AEP profiles)**: option selected from the dropdown after Simulate content, to preview with test profiles, send proofs, and check email rendering.
* **Send proof**: button used to send a proof to your test recipients. When you select the Optimize HTML size option for the proof, the proof is sent with the reduced HTML size to your test recipients. This setting is independent from the email editor: the proof reflects whatever you select in the proof, regardless of whether the option is enabled or disabled in the email itself. The optimization details of the proof, including the original HTML size, the optimized HTML size, and the size reduction percentage, are displayed in a pop-up window.
* **Content quality validation**: validates your content quality to assess readability, effectiveness, and content cohesiveness.
* **Tracking section**: contains the dedicated options to track the behavior of your recipients through email openings and/or interactions. Make sure these options are enabled in the journey's Action activity with the Email channel selected or in the email campaign.

**Guardrails:**

* The subject line must not include line breaks.
* Errors prevent you from testing or activating the journey/campaign as long as they are not resolved. To be able to test or activate the journey/campaign using the email, you must resolve all error alerts.
* Marketing-type email messages must include an opt-out link, which is not required for transactional messages.
* For API-triggered campaigns, the context is generated from the API payload at runtime, so contextual attributes are not available in the personalization editor when defining the email action, and they must be entered manually. The expression path must match the API payload structure exactly, as no check is performed by Journey Optimizer.
* The HTML size optimization is not applied automatically: you must manually enable it in the Edit content screen. The HTML size reduction is only applied at publication time.
* Removal of non-essential HTML comments is also part of the optimization, but this capability has been temporarily disabled as of July 10, 2026.
* The reduction in email size depends on the original HTML structure of your email. If the content is already compact or the email payload is very large, the reduction may be minimal and may not fully prevent clipping in all cases.
* In multilingual emails, the Optimize HTML size setting is tracked at the email level, not per locale. Enabling it on any one locale applies it to all locales of that email at publish time, even locales where the checkbox still appears unchecked in the UI. To disable it, you must uncheck Optimize HTML size on every locale; leaving it enabled on even one locale is sufficient for the optimization to be applied across all locales.
* In a content experiment, the Optimize HTML size setting is managed independently for each treatment, as each treatment is considered a separate message.
* The sizes displayed in the View proofs pop-up reflect the size of your HTML template, where Handlebars expressions are evaluated at their minimum possible value, not the size of the final delivered email. At delivery time, dynamic expressions such as `{{#each}}` loops are resolved against the profile data of the recipient, which may significantly increase the actual email size.

**Applicability:**

* Legacy native channel activities (Email, Push, Mobile message, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes; no migration is required.

**Terminology:**

* Canonical names: Email Designer; Code Editor; Override email channel configuration; Optimize HTML size; Enable decisioning; Simulate content; Simulate content (AEP profiles); Send proof.
* Canonical name: Adobe Experience Platform — Acronym: AEP (used in the label Simulate content (AEP profiles)).
* Do not confuse: "Simulate content" ≠ "Simulate content (AEP profiles)": the page names them as two simulation methods to preview the content.

**FAQ:**

* **How do I add an email to a journey or a campaign?** In a journey, add an Action activity with the Email channel selected. In a campaign, select Email as your action when you create the campaign.
* **Can I change only some values of the email channel configuration?** Yes. After selecting the email configuration, enable Override email channel configuration to change only specific fields without creating a new channel configuration. Leave a field empty to keep its configured value.
* **Is the subject line mandatory?** Yes. The subject line is mandatory, and it must not include line breaks.
* **Do I have to resolve alerts before I test or activate?** You must resolve all error alerts to test or activate the journey/campaign using the email. Warnings refer to recommendations and best practices.
* **Is the HTML size optimization applied automatically?** No. You must manually enable it in the Edit content screen, and the HTML size reduction is only applied at publication time.
* **How do I disable HTML size optimization in a multilingual email?** You must uncheck Optimize HTML size on every locale. Leaving it enabled on even one locale is sufficient for the optimization to be applied across all locales.

**Troubleshooting:**

* `The opt-out link is not present in the email body` (warning): adding an unsubscription link into your email body is a best practice.
* `Text version of HTML is empty` (warning): do not forget to define a text version of your email body, as it will be used when HTML content cannot be displayed.
* `Empty link is present in email body` (warning): check that all the links in your email are correct.
* `Email size has exceeded the limit of 100KB` (warning): for optimal delivery, make sure the size of your email does not exceed 100KB. To reduce the HTML size, use the Optimize HTML size option.
* `The subject line is missing` (error): the email subject line is mandatory.
* `The email version of the message is empty` (error): this error is displayed when the email content has not been configured.
* `configuration doesn't exist` (error): you cannot use your message if the configuration you have selected is deleted after the message creation. If this error occurs, select another configuration in the message Properties.

**Examples:**

* Overriding the email header fields: a customer visits one of your stores, discusses selected items with a relationship manager, and shares their email address. A few days later, you can send a personalized follow-up email and override the sender name and email address so the message appears to come from that same relationship manager, creating a more consistent and relevant experience.

**Related pages:**

* To learn more about the Action activity: Action activity (building-journeys/journey-action.md)
* To create, configure and publish a journey, or to complete the configuration of your journey and activate it: Create your first journey (building-journeys/journey-gs.md)
* To complete your journey flow by adding actions or events: Get started with journey activities (building-journeys/about-journey-activities.md)
* In a journey, to apply capping rules by selecting a rule set in the Business rules drop-down list: Work with rule sets (conflict-prioritization/channel-capping.md)
* In a journey, to use the Send time optimization option to predict the best time to send the message: Send time optimization (building-journeys/send-time-optimization.md)
* To create a campaign and select Email as your action, or to complete the configuration of your campaign and activate it: Create a campaign (campaigns/create-campaign.md)
* To create, configure and activate a campaign: Get started with campaigns (campaigns/get-started-with-campaigns.md)
* To complete the audience step of an email campaign: audience (audience/about-audiences.md)
* To complete the schedule step of an email campaign: schedule (campaigns/campaign-schedule.md)
* To select or create the email configuration, or to find the execution field set in the channel configuration: Configure email settings (email/email-settings.md)
* To learn about channel configurations: Set up channel configurations (configuration/channel-surfaces.md)
* To learn more about the email header override fields: Learn more on header parameters (email/header-parameters.md)
* To find the execution field set in the general settings: general settings (configuration/primary-email-addresses.md)
* For the one-click unsubscribe URL of the list-unsubscribe override fields: List unsubscribe (email/list-unsubscribe.md)
* To personalize the override fields using contextual data, or to configure and personalize the subject line with the personalization editor: personalize (personalization/personalization-build-expressions.md)
* For the contextual data syntax in API-triggered campaigns: Learn more on contextual data syntax (campaigns/api-triggered-campaign-content.md)
* To configure the email content with the Edit content button, access the Email Designer, or design the email content: Design emails (email/get-started-email-design.md)
* To add a decision policy in an email: Learn how to add a decision policy in an email (experience-decisioning/create-decision.md)
* To configure the unsubscription link of the email body: Manage opt-out (privacy/opt-out.md)
* To create the text version of the email body: Manage the text version of an email (email/text-version-email.md)
* To manage content and links in the email: Design content from scratch in Journey Optimizer (email/content-from-scratch.md)
* When working with multilingual email variants: multilingual email variants (content-management/multilingual-gs.md)
* When running a content experiment: content experiment (content-management/content-experiment.md)
* To simulate content variations: Learn how to simulate content variations (test-approve/simulate-sample-input.md)
* To validate the quality of your content: Learn more about content quality validation (content-management/brands-score.md)
* To select test profiles and preview your content: Content Management (content-management/preview-test.md)
* To send proofs: Send email proofs (content-management/proofs.md)
* If your email content returns an error code: Content authoring errors (content-management/content-authoring-errors.md)

**Personas:**

* **marketer:** Can add an email to a journey with an Action activity with the Email channel selected. Can add an email to a campaign by selecting Email as the action. Can enable Override email channel configuration to change only specific fields without creating a new channel configuration. Can override From name, From email prefix, Reply to name, Reply to email, Delivery address, Mailto (unsubscribe), and One-click unsubscribe URL. Can add a subject line for the message. Can select Edit email body to access the Email Designer. Can check the warnings and errors displayed when key settings are missing. Can enable Optimize HTML size to reduce the size of the email HTML during the publishing process. The page states that you must resolve all error alerts to test or activate the journey/campaign using the email. Where: "Add an email action".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Drag and drop an Action activity from the Actions section of the palette into your journey.
* **Success check:** If you do not see the button that displays alerts on the top right of the screen, no alert has been detected.

+++

<!-- ai-section-version: 1 | source-hash: d10b54dc -->
