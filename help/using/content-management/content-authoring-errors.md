---
solution: Journey Optimizer
product: journey optimizer
title: Content authoring errors
description: Learn what common errors mean when you validate email, push, SMS, in-app, and direct mail content in Adobe Journey Optimizer, and how to fix them
feature: Email, Push, SMS, In App, Direct Mail
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, content, email, push, SMS, in-app, direct mail, validation
---
# Content authoring errors {#content-authoring-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors and warnings that [!DNL Adobe Journey Optimizer] returns when you validate or publish the content of an email, push, SMS, in-app, or direct mail message.

>[!ENDSHADEBOX]

Content errors use the prefixes **CJMMAS** and **CJMRT**, followed by an error number and an HTTP status. Codes with the status 200 are warnings: they do not block saving or publishing. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Email content {#email}

These errors and warnings occur when you validate or publish the content of an email.

See also [Email opt-out management](../email/email-opt-out.md) and [Content checks](../email/content-check.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2000-422** | The subject line is missing. | The subject line is empty. Enter a subject. [Learn more](../email/create-email.md#define-email-content) |
| **CJMMAS-2061-422** | Line break in email subject is not allowed. Please remove the new line and try again. | The subject contains a line break. Remove it so that the subject is on a single line. [Learn more](../email/create-email.md#define-email-content) |
| **CJMMAS-2001-200** | The opt-out link is not present in the email body. | The email body has no opt-out link (warning). Marketing emails must include an opt-out link in every variant and language, so add it. Transactional emails do not need it. [Learn more](../email/email-opt-out.md#one-click-opt-out) |
| **CJMMAS-2020-422** | The opt-out link is null or empty in email body. | The opt-out link is null or empty. Marketing emails must include an opt-out link in every variant and language, so enter the real link. [Learn more](../email/email-opt-out.md#one-click-opt-out) |
| **CJMMAS-2047-200** | {count} opt-out links labeled {labelName} have a '#' placeholder and no actual link. Please add the required links. | Some opt-out links have a # placeholder and no actual link (warning). Replace each # placeholder with the real link. [Learn more](../email/email-opt-out.md#one-click-opt-out) |
| **CJMMAS-2051-422** | One click opt-out is missing the "OptOutLevel" tag. Please add this tag and try again. | The one-click opt-out is missing the OptOutLevel tag. Add the OptOutLevel tag to the one-click opt-out. [Learn more](../email/email-opt-out.md#one-click-opt-out) |
| **CJMMAS-2002-200** | Empty link is present in Email body. | The email body has an empty link (warning). Add the destination, or remove the link. [Learn more](../email/content-check.md) |
| **CJMMAS-2005-422** | The email version of the message is empty. | The email version of the message is empty. Add the email content. [Learn more](../email/create-email.md#define-email-content) |
| **CJMMAS-2052-422** | The HTML body is empty. Please check and try again. | The HTML body is empty. Add the HTML content. [Learn more](../email/create-email.md#define-email-content) |
| **CJMMAS-2053-200** | The content template body is empty. Please check and try again. | The content template body is empty (warning). Add content to the template. [Learn more](../email/create-email.md#define-email-content) |
| **CJMMAS-2003-200** | Your email size of {actualHtmlSize}KB exceeds the recommended size of {sizeLimit}KB by {percentIncrease}%, which may have adverse impact on email delivery and deliverability, including truncation of email in email clients. | The email is larger than the recommended size (warning), which can truncate it in some email clients (Gmail clips an email above 100 KB). Remove unused elements, simplify the structure, or move content into fragments. [Learn more](../email/create-email.md#optimize-html-size) |
| **CJMMAS-2060-422** | The {type} content with size {fragmentSize}KB has exceeded the limit of {sizeLimit}KB. Content may be clipped by some clients. Please update and try again. | The content is larger than the size limit named in the message, so some email clients may clip it (Gmail clips an email above 100 KB). Remove unused elements, simplify the structure, or move content into fragments. [Learn more](../email/create-email.md#optimize-html-size) |
| **CJMMAS-2007-422** | The HTML version cannot be empty when the AMP version is present. | An AMP version needs an HTML version. Add an HTML version, or remove the AMP version. [Learn more](../email/get-started-email-design.md) |
| **CJMMAS-2008-200** | Text version of HTML is empty. | The text version of the email is empty (warning). Add a text version, or let it sync with the HTML. [Learn more](../email/text-version-email.md) |
| **CJMMAS-2071-200** | A potential risk of spam was detected. Please review and address the identified issues before activating the campaign. | A potential spam risk was detected (warning). Open the spam report and fix the issues, especially if the score is above 2. [Learn more](spam-report.md) |
| **CJMMAS-2072-400** | The html body is not valid. Provide correct html body and try again. | The HTML is not valid. Check and correct the HTML. [Learn more](../personalization/personalization-syntax.md) |
| **CJMMAS-2400-400** | The HTML does not have correct personalization attributes. Provide correct attributes and try again. | The HTML has a personalization attribute that is not correct. Check the attribute against the personalization syntax and correct it. [Learn more](../personalization/personalization-syntax.md) |
| **CJMMAS-6101-422** | Content contains a syntax error in the personalization expression. | A personalization expression has a syntax error. Fix the expression in the personalization editor. [Learn more](../personalization/personalization-syntax.md) |

## Push notifications {#push}

These errors occur when you validate or publish a push notification.

See also [Design push notifications](../push/design-push.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2004-422** | The push version of the message is empty. | The push version of the message is empty. Add the content, or remove the push channel. [Learn more](../push/design-push.md#push-title-body) |
| **CJMMAS-2009-422** | Push iOS payload has exceeded limit of {sizeLimit}KB. | The iOS push payload is larger than the limit (4 KB). Reduce the text, images, and emojis. [Learn more](../push/send-push.md) |
| **CJMMAS-2010-422** | Push Android payload has exceeded limit of {sizeLimit}KB. | The Android push payload is larger than the limit (4 KB). Reduce the text, images, and emojis. [Learn more](../push/send-push.md) |
| **CJMMAS-2016-422** | Push iOS {buttonType} type's URI is null or empty for button index: {index} | A button of the iOS push notification has no URI. Enter a deep link or a web URL for the button at the index named in the message. [Learn more](../push/design-push.md#add-buttons-push) |
| **CJMMAS-2018-422** | Push Android {buttonType} type's URI is null or empty for button index: {index} | A button of the Android push notification has no URI. Enter a deep link or a web URL for the button at the index named in the message. [Learn more](../push/design-push.md#add-buttons-push) |
| **CJMMAS-2022-422** | Push - {platform} Platform on click behavior, invalid {linkType} URI. | The URI of the on-click action is not valid for the platform named in the message. Enter a valid deep link or web URL. [Learn more](../push/design-push.md#on-click-behavior) |
| **CJMMAS-2023-422** | Push - {platform} Platform Add Media, invalid {mediaType} URI. | The media URI is not valid for the platform named in the message. Enter a valid media URL, or select an asset from [!DNL Adobe Experience Manager Assets]. [Learn more](../push/design-push.md#add-media-push) |

## SMS and in-app messages {#sms-inapp}

These errors occur when you validate the content of a mobile message or an in-app message.

See also [Design mobile messages](../mobile/design-mobile.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2028-422** | The SMS version of the message is empty. | The SMS version of the message is empty. Add the message text, or remove the channel. [Learn more](../mobile/design-mobile.md) |
| **CJMMAS-2024-422** | The In-App version of the message is empty. | The in-app version of the message is empty. Add the content, or remove the channel. [Learn more](../in-app/design-in-app.md) |
| **CJMMAS-2025-200** | In-App size has exceeded the limit of {sizeLimit}KB. | The in-app message is larger than the limit named in the message (warning). Reduce the size of images and content. [Learn more](../start/guardrails.md#message-content-size) |

## Direct mail {#direct-mail}

These errors occur when you define the extraction file of a direct mail message.

See also [Create a direct mail message](../direct-mail/create-direct-mail.md#extraction-file).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2041-422** | The Direct mail file structure is empty. | The file structure is empty. Add the columns to extract. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |
| **CJMMAS-2042-422** | The Direct mail file structure size is greater than {sizeLimit}. | The file structure is larger than the limit named in the message. An extraction file can have up to 50 columns, so remove the extra columns. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |
| **CJMMAS-2043-422** | The Direct mail file structure {count} label(s) are empty. | Some columns of the file have an empty label. Enter a unique label for each empty column. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |
| **CJMMAS-2044-422** | The Direct mail file structure {labelName} label is repeated {count} times. | A label is used by several columns of the file. Rename the repeated columns so that each label is unique. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |
| **CJMMAS-2045-422** | The Direct mail notes size has exceeded the limit of {sizeLimit}KB. | The notes are larger than the limit named in the message. Shorten the notes. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |
| **CJMMAS-2046-422** | The Direct mail label, on which sorting is added, does not exist. | The label used for sorting does not exist. Select an existing column for the sort. [Learn more](../direct-mail/create-direct-mail.md#extraction-file) |

## Message lifecycle and saving {#lifecycle}

These errors occur when you edit, create a version of, approve, or save a message, and its state or the saved content does not allow the action.

See also [Manage campaigns](../campaigns/manage-campaigns.md) and [Review & approve a request](../test-approve/review-approve-request.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1053-400** | Message status change to Draft is not permitted. | A published message cannot be set back to Draft. Create a new version of the campaign to change it. [Learn more](../campaigns/manage-campaigns.md#edit-published-message) |
| **CJMMAS-1054-400** | Published message update is not permitted. | A published message cannot be updated directly. Create a new version of the campaign, edit the draft version, then activate it. [Learn more](../campaigns/manage-campaigns.md#edit-published-message) |
| **CJMMAS-1060-400** | Version Creation is not permitted. Message must be in published state. | A new version can only be created from a published (Live) message. Activate the campaign first, or edit the draft directly. [Learn more](../campaigns/manage-campaigns.md#edit-published-message) |
| **CJMMAS-1077-400** | Changing the message approval status is not allowed. | The approval status is set by the approval workflow, not by editing the message. Request approval, or ask the reviewer to approve or request changes. [Learn more](../test-approve/review-approve-request.md#approve) |
| **JOMAL-1101-409** | Save failed because this item was updated in another tab or by another user. Refresh to load the latest version before saving. | Someone else, or another browser tab, saved a newer version. Refresh the page to load the latest version, then reapply your changes and save again. [Learn more](../campaigns/manage-campaigns.md) |
| **JOMAL-1102-400** | Unable to patch HTML due to malformed tracking links. | The HTML contains a link that cannot be tracked, for example a missing or unclosed href. Correct the links in the HTML, then save again. [Learn more](../email/message-tracking.md#insert-links) |

## Permissions {#permissions}

These errors occur when your user does not have the permission required to work with a message, or when the message belongs to another organization or sandbox.

See also [Manage users & roles](../administration/permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1028-403** | Forbidden. You do not have write permission on messages. | Your role lacks the write permission on messages. Ask your administrator to add the permission to your role. [Learn more](../administration/high-low-permissions.md#campaign-capability) |
| **CJMMAS-1029-403** | Forbidden. You do not have read permission on messages. | Your role lacks the read permission on messages. Ask your administrator to add the permission to your role. [Learn more](../administration/high-low-permissions.md#campaign-capability) |
| **CJMMAS-1030-403** | Forbidden. You do not have publish permission on messages. | Your role lacks the publish permission on messages. Ask your administrator to add the permission to your role. [Learn more](../administration/high-low-permissions.md#campaign-capability) |
| **CJMMAS-1042-403** | Forbidden. You do not have delete permission on messages. | Your role lacks the delete permission on messages. Ask your administrator to add the permission to your role. [Learn more](../administration/high-low-permissions.md#campaign-capability) |
| **CJMMAS-1094-403** | You do not have permission to simulate content or access this template. Please contact your administrator to update your permissions. | Your role does not allow you to simulate this content, or you cannot access the template. Ask your administrator to update your permissions or the template access. [Learn more](../administration/permissions.md) |
| **CJMMAS-1095-403** | You do not have permission to manage content or access this template. Please contact your administrator to update your permissions. | Your role does not allow you to manage this content, or you cannot access the template. Ask your administrator to update your permissions or the template access. [Learn more](../administration/permissions.md) |
| **JOMAL-1003-403** | Forbidden. User is not authorized for request operation. | Your user is not allowed to perform this operation. Ask your administrator to check your role and the object access for the item. [Learn more](../administration/permissions.md) |
| **JOMAL-1203-403** | Requested operation is forbidden. | Your user is not allowed to perform this operation. Ask your administrator to check your role and the object access for the item. [Learn more](../administration/permissions.md) |
| **JOMAL-1001-401** | Unauthorized. User is not authorized for request operation. | Your session is not valid or has expired. Sign in again. If the error persists, ask your administrator to check your access to the sandbox. [Learn more](../administration/permissions.md) |
| **JOMAL-1201-401** | User is unauthorized. | Your session is not valid or has expired. Sign in again. If the error persists, ask your administrator to check your access to the sandbox. [Learn more](../administration/permissions.md) |
| **CJMMAS-1001-400** | Bad Request. Message belongs to different org. | The message belongs to another organization. Sign in to the organization that owns the message. [Learn more](../administration/permissions.md) |

## Channel configurations and access {#config}

These errors occur when the message has no usable channel configuration, or when your user cannot use the content.

See also [Set up channel configurations](../configuration/channel-surfaces.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2006-422** | Preset doesn't exist. | The message has no channel configuration, or the configuration is not found, for its channel. Select a channel configuration in the message. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2012-422** | Email preset is not defined. | The message has no email channel configuration. Select an email channel configuration in the message. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2013-422** | Push preset is not defined. | The message has no push channel configuration. Select a push channel configuration in the message. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2027-200** | The SMS surface is not defined. | The message has no SMS channel configuration (warning). Select an SMS channel configuration in the message. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2030-422** | The Web channel surface is not defined. | The message has no web channel configuration. Select a web channel configuration in the message. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2014-422** | App selection in the Push preset is empty. | The push channel configuration has no app. Select an app in the configuration. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2015-422** | Global preset email Execution list is empty. | The email channel configuration has an empty execution list. Complete the execution list in the configuration. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-1034-400** | Bad Request. Invalid Preset Id in request/message. | The request or message contains a channel configuration ID that is not valid. Select a valid channel configuration, then try again. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-1064-400** | Bad request. The selected preset is invalid. Select a valid preset and try again. | The channel configuration selected in the message is not valid. Select a valid channel configuration, then try again. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-1068-400** | Bad request. A preset has not been selected in the landing page. Select a preset and try again. | The landing page has no channel configuration. Select a channel configuration in the landing page, then try again. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMMAS-2036-403** | You do not have permission to use one or more AEM repositories referenced in the content: {deniedRepositoryIds}. | You do not have permission on the AEM repositories used in the content. Ask your administrator for access to the repositories named in the message. [Learn more](../integrations/assets.md) |

## Decision policies and channel configuration fields {#decisions}

These errors occur when a message is validated or published, and a decision policy or a channel configuration field is not valid.

See also [Decisioning guardrails and limitations](../experience-decisioning/decisioning-guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-030002-400** | Please enter details for all mandatory fields for {channel} surface. | A mandatory field of the channel configuration is empty. Open the channel configuration and fill in all mandatory fields. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMRT-030007-400** | Length of {fieldName} is {currentLength}. Please enter up to {maxLength} characters only for {fieldName}. | A field of the channel configuration is longer than the maximum length shown in the message. Shorten the value. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMRT-030008-400** | Invalid CLICK link without URL | A link of the message has no URL. Add the URL, or remove the link. [Learn more](../email/message-tracking.md) |
| **CJMRT-030014-422** | Your message cannot have more than {maxLength} decisions. Please reduce the number of decisions and try again. | The message uses more decision policies than allowed. Reduce the number of decision policies in the message. [Learn more](../experience-decisioning/decisioning-guardrails.md) |
| **CJMRT-030015-422** | The referenced decision ID does not exist: {invalidDecisionPolicyIds}. Please check if this decision exists or use another decision. | A decision policy used in the message does not exist. Select a decision policy that exists. [Learn more](../experience-decisioning/create-decision.md) |
| **CJMRT-030017-422** | The referenced decision ID {invalidDecisionPolicyIds} does not belong to enclosing campaign | A decision policy used in the message does not belong to this campaign. Select a decision policy that belongs to the campaign. [Learn more](../experience-decisioning/create-decision.md) |
| **CJMRT-030018-422** | This content cannot be saved as a fragment because it contains a decision policy. If you want to save it as a fragment, remove the decision policy. | Content that contains a decision policy cannot be saved as a fragment. Remove the decision policy, then save the fragment. [Learn more](create-fragments.md) |

## Expression templates {#expression}

These errors occur when you save an expression fragment or template.

See also [Use expression fragments](../personalization/use-expression-fragments.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-2037-422** | This expression template is malformed. Provide a valid template and try again. | The expression template is malformed. Fix the syntax. [Learn more](../personalization/personalization-syntax.md) |
| **CJMMAS-2059-422** | The Expression content is empty. Please check and try again. | The expression content is empty. Add content to the expression template. [Learn more](../personalization/personalization-syntax.md) |
| **CJMMAS-2038-422** | The expression template size has exceeded the limit of 200 KB. Reduce the template size and try again. | The expression template is larger than 200 KB. Reduce its size. [Learn more](../personalization/personalization-build-expressions.md) |

## Related topics {#related}

* [Content checks](../email/content-check.md)
* [Email opt-out management](../email/email-opt-out.md)
* [Email spam report](spam-report.md)
* [Guardrails and limitations](../start/guardrails.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/content-management/ai-augmented-content-authoring-errors.md}}
