---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer troubleshooting articles
description: Journey Optimizer troubleshooting articles
feature: Get Started
role: User
level: Intermediate
exl-id: f8acb987-5c6e-4545-93b9-fdfc0d74db57
---
# Troubleshooting articles {#ajo-troubleshooting}

The following is a list of troubleshooting articles for Adobe Journey Optimizer. Each troubleshooting section provides answers to frequently asked questions and solutions to problems.

See also the [Adobe Experience Platform FAQ and Troubleshooting documentation](https://experienceleague.adobe.com/en/docs/experience-platform/landing/troubleshooting){target="_blank"}.

## Email channel {#ajo-troubleshooting-email}

+++ How to prevent email formatting issues in Adobe Journey Optimizer using themes?

In Adobe Journey Optimizer (AJO), modifying the default CSS blocks in the email header can lead to unexpected formatting issues—especially after removing content fragments. These issues are more noticeable on mobile devices and may result in layout shifts or styling inconsistencies. To prevent this, use the Themes feature to apply custom CSS safely without altering system generated CSS styles.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-27252){target="_blank"} to learn how to resolve this issue.

Learn more about email formatting [on this page](../email/get-started-email-design.md).

+++


+++ Why are fragments with editable fields not working?

In Adobe Journey Optimizer, fragments with editable fields may fail to load correctly or duplicate unexpectedly when added to templates. The problem typically affects specific fragments across environments.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26908){target="_blank"} to learn how to resolve this issue.

Learn more about customizable fragments [on this page](../content-management/customizable-fragments.md).

+++

+++ Why are HTML fragments not displaying correctly in emails?

HTML fragments may fail to render properly in emails, often appearing as **fragment IDs** rather than actual content. Unlike visual fragments, HTML fragments require careful configuration. To resolve this, follow best practices for using both **visual and HTML expression fragments** in your email campaigns.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25441){target="_blank"} to learn how to resolve this issue.

Learn more about HTML fragments [on this page](../content-management/fragments.md).

+++

+++ Why are email templates and content disappearing from unpublished journeys?

When editing email templates in an unpublished journey, the content and templates of certain emails may unexpectedly disappear. This can cause rework and delays. To reduce the risk of this issue, avoid simultaneous edits, limit the number of open tabs, and save changes frequently.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26738){target="_blank"} to learn how to resolve this issue.

Learn more about templates [on this page](../email/use-email-templates.md).

+++

+++ Why is the Email Preheader field not displaying in 'Code your own' mode? 

In **'Code your own'** mode under the **Edit Email Body** feature, the Preheader input field does not appear. To include preheader text, users must **manually code the preheader** within their custom HTML content.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26174){target="_blank"} to learn how to solve this issue.

Learn more about Email preheader configuration [on this page](../email/header-parameters.md).

+++

+++ Why is there a discrepancy in link behavior when using an HTML component in email templates?  

When adding an **HTML component** to an email template, links may behave differently depending on the **email client**, **viewing mode**, or **device/browser**. For example, anchor links can function differently in **Outlook's side-by-side view** compared to full-screen view. Be aware of these variations when designing email templates and test across multiple clients and devices.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26221){target="_blank"} to learn how to solve this issue.

See also Email design best practices [on this page](../email/get-started-email-design.md).

+++


+++ How to prevent missing email tracking links in reporting?

Missing link tracking in Adobe Journey Optimizer occurs when email URLs use dynamic variables and don't start with http, or when logic statements are placed in the URL field. To resolve this, ensure all URLs begin with http, avoid using logic in the URL field, and move complex personalization logic to the HTML content or pre-processed attributes.


Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26932){target="_blank"} to learn how to resolve this issue.

Learn more about email tracking [on this page](../email/message-tracking.md).

+++

+++ How do I resolve a Mail Exchanger error when setting up API-triggered transactional email campaigns? 

If you encounter a Mail Exchanger (MX) error while creating a channel configuration for an API-triggered transactional email campaign in Adobe Journey Optimizer, it may be due to **DNS misconfigurations** or **DMARC policy limitations**. To resolve this, ensure that your DNS is correctly configured and verify that your domain complies with **Domain-based Message Authentication, Reporting, and Conformance (DMARC)** requirements.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26200){target="_blank"} to learn how to resolve this issue.

Learn more about email DMARC policies [on this page](../configuration/dmarc-record-update.md).

See also [API-triggered campaigns documentation](../campaigns/api-triggered-campaigns.md).
+++

## Push channel {#ajo-troubleshooting-push}

+++ Can a profile have multiple push tokens in Adobe Journey Optimizer?

When implementing push notifications in Journey Optimizer, a single profile can indeed have multiple push tokens associated with different devices. During a push notification campaign, Journey Optimizer is designed to manage these tokens and ensure that the targeted profile can be reached across all associated devices.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26738){target="_blank"} to learn more about push token management.

Learn more about push configuration [on this page](../push/push-configuration.md).

+++

+++ Why does clicking on a push message not redirect me to the configured web URL?  

If push messages are not redirecting to the intended web URL, it may be due to incorrect click action configuration or disabled push notification settings. Ensure that the **click action** for the push message is correctly set and that **automatic display and tracking** of push notifications are enabled to resolve this issue.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26226){target="_blank"} to learn more about this issue.

Learn more about push configuration [on this page](../push/push-configuration.md).

+++


## SMS channel {#ajo-troubleshooting-sms}

+++ Why are my transactional SMS not delivered even though consent is set to `marketing.sms.value=y`?

If a recipient responds **STOP** to an SMS, all future messages from that short number are blocked — including transactional messages. To guarantee uninterrupted delivery of transactional SMS, configure and send them through a **separate short number** that recipients have not previously opted out from.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26258){target="_blank"} to learn more about this issue.

Learn more about SMS opt-out configuration [on this page](../sms/sms-opt-out.md).

+++

## In-app channel

+++ Why can't I report on the In-app channel in Customer Journey Analytics?

Difficulties reporting on the **In-app channel** in Adobe Customer Journey Analytics often arise from misconfigured **data views**, **datasets**, or **schema updates**. Ensure these configurations are correctly applied to resolve the issue.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26206){target="_blank"} to learn more about this issue.

Learn more how to integrate Journey Optimizer analytics data in Customer Journey Analytics [on this page](https://experienceleague.adobe.com/en/docs/analytics-platform/using/integrations/ajo?lang=en#automatically-configure-journey-optimizer-integration){target="_blank"}.

See also the [Journey Optimizer All-time reports documentation](../reports/report-gs-cja.md)

+++


## Data management {#ajo-troubleshooting-data-management}

+++ How do Time-to-Live (TTL) settings apply to Profile and Data Lake datasets when you create a new sandbox?

Organizations provisioning new sandboxes in Adobe Journey Optimizer have raised questions about how Time-to-Live (TTL) settings apply to Profile and Data Lake datasets. This article clarifies that TTL settings do not affect existing sandboxes and are automatically applied only to newly provisioned ones.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26135){target="_blank"} to learn how to handle TTL.

Learn more about dataset Time-to-live [on this page](../data/datasets-ttl.md).

+++


## Profiles and Audience management {#ajo-troubleshooting-audiences}

+++ How to resolve audience count discrepancies?

The number of processed entries in the **Read Audience** feature of Adobe Journey Optimizer can be lower than the expected audience count. This issue often arises due to incorrect namespace configurations, leading to profiles being excluded from journeys. The resolution involves checking and correcting namespace configurations, reviewing relevant documentation, and adjusting priorities to ensure smoother operations in Adobe Journey Optimizer.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26135){target="_blank"} to learn how to resolve this issue.

See also [this article about outdated audience counts](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26166){target="_blank"}.

Learn more about the **Read Audience** activity in journeys [on this page](../building-journeys/read-audience.md).

+++

+++ Why are profile updates failing?

In Adobe Journey Optimizer, certain field values may not update correctly after running through an **Update Profile** activity in a journey. In some cases, updated fields can disappear or revert to their previous state. To address this, check for conflicting rules or conditions, review permissions settings, use a unique dataset for the **Update Profile** activity, and ensure no other ingestion process is writing to the same profile at the same time.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26352){target="_blank"} to learn steps to resolve this issue.

Learn more about the **Update Profile** activity in journeys [on this page](../building-journeys/update-profiles.md).

See also the [Adobe Experience Platform documentation about Data ingestion](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/tutorials/ingest-batch-data?lang=en#dataset-activity){target="_blank"}.

+++

+++ Why is there a mismatch in profile count entering a journey vs. in the associated audience?

The discrepancy can happen when the journey uses a previous day's profile snapshot if the current day's snapshot is not available at the time of journey execution. 

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26253){target="_blank"} to learn steps to resolve this issue.

Learn more in [this Journey Optimizer Community post](https://experienceleaguecommunities.adobe.com/t5/real-time-customer-data-platform/profile-snapshot-and-segment-qualification-troubleshooting/ba-p/698998){target="_blank"}.

See also the [Adobe Experience Platform Schedules API documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/api/schedules?lang=en){target="_blank"} to check when your daily job is scheduled.

+++


+++ How to resolve audience population issues?

Audience population problems can occur when components or resources are missing, often due to entitlement, provisioning, or permission misconfigurations. To fix these issues, start by verifying entitlements, ensuring correct provisioning, and reviewing permissions. If the problem persists, escalate the case and coordinate with support teams for a complete resolution.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26333){target="_blank"} to learn steps to resolve this issue.

Learn more about the **Update Profile** activity in journeys [on this page](../building-journeys/update-profiles.md).

See also the [Adobe Real-Time CDP Profile documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide?lang=en#profile-detail){target="_blank"}.

+++

+++ Why has the Engageable Profiles count increased significantly in a short period? 

The **Engageable Profiles** metric reflects the number of unique profiles engaged by journeys or campaigns over the past 12 months. A sudden increase may result from large audiences being targeted or changes in datasets. To manage this, review the **profile counting logic**, investigate journeys targeting large audiences, **filter audiences** at the journey level, reduce the **addressable audience size**, and monitor **dataset changes**.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26161){target="_blank"} to learn steps to resolve this issue.

Monitor your organization's license usage and engageable profiles using the [License Usage Dashboard](../audience/license-usage.md)

See also the [Adobe Experience Platform Query Service overview](https://experienceleague.adobe.com/en/docs/experience-platform/query/home?lang=en){target="_blank"}.

+++

+++ Why are emails sent to individuals outside the intended audience based on date functions?

Emails may be sent to recipients who **do not meet the specified audience criteria**. For example, members with redemption dates **before July 4th, 2025** may receive emails intended only for those after that date. This behavior can result from **misconfigured audience segmentation** or **unexpected changes in profile qualification logic**.  

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26173){target="_blank"} to learn steps to resolve this issue.

Learn more about date functions [on this page](../../rp_landing_pages/date-landing-page.md).

+++

+++ How do I resolve audience selection issues and Chrome errors when saving journeys?

Adding audiences to journey conditions may sometimes cause **application crashes** or display an **Aw Snap error** in Chrome, including errors when saving journeys. These issues are often related to **Chromium services**. To resolve them, apply a **browser update** or use an appropriate **workaround**.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26145){target="_blank"} to learn steps to resolve this issue.

+++

## Journeys {#ajo-troubleshooting-journeys}

For Journeys, refer to the following troubleshooting sections:

* [Troubleshoot errors before testing your journey](../building-journeys/troubleshooting.md) 
* [Troubleshoot inbound actions in journeys](../building-journeys/troubleshooting-inbound.md) 
* [Troubleshoot your live journey execution](../building-journeys/troubleshooting-execution.md) 
* [Troubleshoot custom actions](../action/troubleshoot-custom-action.md)


+++ Why are expressions lost when creating a new journey version?  

When creating a new version of a journey, **expressions in specific steps** may be lost, causing errors and requiring manual re-entry. To resolve this, **duplicate the journey**, test for reproducibility, **avoid browser reloads**, and use the **updated canvas** for older journeys.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26152){target="_blank"} to learn steps to resolve this issue.

Learn how to duplicate a journey [on this page](../building-journeys/journey-ui.md#duplicate-a-journey).
 
+++

+++ Why do profiles exit journeys prematurely? 

Profiles may exit a journey unexpectedly without passing through a designated node when the **condition checking feedback status** of sent messages is misconfigured. To resolve this, review the **condition logic**, implement **alternative logic**, or consult with your **implementation team**.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26127){target="_blank"} to learn steps to resolve this issue.

See also [Journey design guidelines](../building-journeys/using-the-journey-designer.md).

+++


+++ Why are profiles exiting journeys unexpectedly?

Profiles may exit a journey unexpectedly when **event capping** occurs, causing some profiles to be discarded if the number of events processed exceeds system capacity. To reduce profile exits, understand the **system limits**, monitor for **event spikes**, and optimize **data flow** to prevent exceeding thresholds.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26018){target="_blank"} to learn steps to resolve this issue.

See also [Journey guardrails](../start/guardrails.md#journey-guardrails).

+++


+++ Why is my event not triggering the intended journey?  

Events may fail to trigger a journey even if all criteria are met when they are **created through query services** rather than being streamed to the **Data Collection Core Service (DCCS)**. To resolve this, review the event configuration, ensure events are **streamed directly to DCCS**, and verify functionality using **test mode**.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26031){target="_blank"} to learn steps to resolve this issue.

Learn more about events [on this page](../event/about-events.md).

See also [Journey Event guardrails](../start/guardrails.md#events).

+++


+++ How do I resolve journey trigger issues after audience changes in Adobe Journey Optimizer? 

If a journey stops triggering after modifications to its associated audience — such as changes to the merge policy — you may experience interrupted flows. To resolve this, **duplicate and republish the journey** with the updated audience settings to ensure triggers function correctly.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26224){target="_blank"} to learn steps to resolve this issue.

Learn how to duplicate a journey [on this page](../building-journeys/journey-ui.md#duplicate-a-journey).

+++

+++ Why does a custom action calling an external third-party endpoint time out?

Timeout errors can occur when a **custom action** calls an external third-party endpoint. To resolve this, verify that the **endpoint is accessible**, check **server logs**, ensure there is **no blocking from Adobe**, update endpoint configurations as needed, and **test after updates**. Also, be mindful of **API call timeout specifications**.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26156){target="_blank"} to learn steps to resolve this issue.

Learn more about Journey Throttling API [on this page](../configuration/throttling.md).

See also the [Integration with external systems documentation](../configuration/external-systems.md).

+++

+++ What steps should you take if you encounter a 403 error with the message **invalid_access** or **No access to this dataId=XX granted** granted when publishing an audience from an arrow?

To resolve this error, ask your administrator to verify that your user profile has access to the required data views for audience publishing, then try publishing the audience again.

Refer to [the permissions documentation](../administration/permissions.md){target="_blank"} to learn steps to resolve this issue.

+++

## Rules {#ajo-troubleshooting-rules}

+++ Why is the Capping rules dropdown not working?

Issues with the **Capping rules dropdown** often occur when rule sets are **misconfigured** or **inaccessible**. Ensure that all rule sets are correctly configured and available to resolve the problem.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26204){target="_blank"} to learn more.

Learn how to apply capping rules [in this section](../conflict-prioritization/rule-sets.md).

+++

## Decisioning {#ajo-troubleshooting-decisioning}

+++ How do I resolve issues when creating offer collections?

Difficulties creating offer collections often occur when **catalogs have not been provisioned** for your organization. To resolve this, verify that all required catalogs are correctly provisioned before attempting to create offer collections.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26265){target="_blank"} to learn steps to resolve this issue.

Learn more about offer collections [on this page](../offers/offer-library/creating-collections.md).

+++

+++ Why am I unable to access Offer Decisioning?  

When integrating Adobe Target into an application using Adobe Journey Optimizer, the **Offer Decisioning** option may be inaccessible within the Datastream configuration. This typically occurs due to **permission settings** or **provisioning constraints**. To resolve the issue, verify user permissions and ensure the necessary provisioning is in place.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26175){target="_blank"} to learn steps to resolve this issue.

Learn more about required permissions for Offer Decisioning [on this page](../offers/get-started/starting-offer-decisioning.md#granting-acess-to-decision-management).

+++



## Multilingual {#ajo-troubleshooting-multilingual}

+++ How to resolve this issue `Message validation error (CJMMAS - 1069-500)`?

In Adobe Journey Optimizer, a Message Validation Error (CJMMAS - 1069-500) linked to the multilingual feature prevents journeys from being set to Test mode or Published. 

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26168){target="_blank"} to learn steps to resolve this issue.

Learn more about multilingual content [on this page](../content-management/multilingual-gs.md).

+++


## Configuration {#ajo-troubleshooting-config}

+++ How do I enable TLS v1.3 for Custom Actions?  

To maintain **data integrity and security** when connecting to third-party systems, ensure that Transport Layer Security (**TLS**) v1.3 is enabled for your custom actions. This helps protect communications and prevents potential security vulnerabilities.


Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26223){target="_blank"} to learn more.

Learn more about multilingual content [on this page](../action/about-custom-action-configuration.md).

+++

+++ Why am I unable to create a dashboard directly from a query in Adobe Journey Optimizer? 

In Adobe Journey Optimizer, dashboards cannot be created directly from queries. To build dashboards, use the available **dashboard creation functionalities** within Adobe Experience Platform, which allow you to visualize and analyze query data effectively.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26201){target="_blank"} to learn more.

+++

## APIs {#ajo-troubleshooting-apis}

+++ How do I resolve access issues with the Query Service API?  

Access errors when using the **Query Service API** via Postman or similar tools are usually caused by **insufficient permissions**. To resolve this, verify user permissions, check API credentials, and provide detailed information to support if needed.

Refer to [this troubleshooting article](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26196){target="_blank"} to learn more.

See also the [Manage API credentials documentation](https://experienceleague.adobe.com/en/docs/experience-platform/access-control/abac/permissions-ui/permissions?lang=en#manage-api-credentials-for-role){target="_blank"}.

+++
