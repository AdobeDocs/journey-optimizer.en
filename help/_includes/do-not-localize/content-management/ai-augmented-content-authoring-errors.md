---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page explains the cause and the fix for the errors and warnings that [!DNL Adobe Journey Optimizer] returns when you validate or publish the content of an email, push, mobile message (SMS), in-app, or direct mail message, grouped by theme.

**Intents:**

* Identify what a content error code such as `CJMMAS-2000-422` means.
* Tell a warning (status 200) from an error that blocks saving or publishing.
* Find the cause and the fix of an error for email, push, mobile message (SMS), in-app, or direct mail content.
* Find the cause and the fix of a permission, lifecycle, channel configuration, decision policy, or expression template error.

**Glossary:**

* **Content errors:** errors and warnings returned when you validate or publish message content. Prefixes: **CJMMAS** and **CJMRT**.
* **Error code** format: prefix, error number, HTTP status. Example: `CJMMAS-2000-422`.
* **Warning:** a code with the status 200. Warnings do not block saving or publishing.
* **Channel configuration** *(product-specific)*: the configuration a message needs for its channel. The error messages call it "preset" or "surface".
* **Extraction file:** the file defined for a direct mail message. Its errors are in the **Direct mail** section.
* **Expression template:** the template saved as an expression fragment or template. Its errors are in the **Expression templates** section.

**Guardrails:**

* **Email size:** the content larger than the recommended size can truncate the email in some email clients (Gmail clips an email above 100 KB). The message `CJMMAS-2003-200` gives the recommended size in `{sizeLimit}`, and the message `CJMMAS-2060-422` gives the limit in `{sizeLimit}`.
* **Push payload:** the payload of the push notification is larger than the limit (4 KB) for `CJMMAS-2009-422` and `CJMMAS-2010-422`.
* **Direct mail:** an extraction file can have up to 50 columns. Each column needs a unique label.
* **Expression template size:** the template is larger than 200 KB (`CJMMAS-2038-422`; the message says "has exceeded the limit of 200 KB").
* **Decisions in a message:** a message cannot have more than the number of decisions given in `{maxLength}` (`CJMRT-030014-422`).
* **Channel configuration field length:** a field longer than the maximum length shown in the message returns `CJMRT-030007-400`.
* **Published messages:** a published message cannot be set back to Draft (`CJMMAS-1053-400`) or updated directly (`CJMMAS-1054-400`). A new version can only be created from a message in the published state (`CJMMAS-1060-400`).

**Terminology:**

* Canonical name: Content authoring errors — variants: content errors.
* Prefixes: **CJMMAS**, **CJMRT**, and **JOMAL** (used in the Message lifecycle and saving, and the Permissions sections).
* Error messages quote the terms "preset" and "surface"; the page uses "channel configuration" for the same configuration in the fix. Mobile message: the channel, with SMS as a variant; the messages and the page section title keep the wording "SMS" and "In-App".
* Acronym: AEM = Adobe Experience Manager.
* **Do not confuse:** a warning (status 200, does not block saving or publishing) and an error with another status such as 400, 403, 409, or 422. For example, `CJMMAS-2001-200` is a warning and `CJMMAS-2020-422` is an error, although both concern the opt-out link.
* **Do not confuse:** `403` (forbidden) and `401` (unauthorized).

**FAQ:**

**What do the CJMMAS and CJMRT prefixes mean?**
Content errors use the prefixes **CJMMAS** and **CJMRT**, followed by an error number and an HTTP status.

**Does a code ending in 200 block publishing?**
No. Codes with the status 200 are warnings: they do not block saving or publishing.

**The subject line error appears (`CJMMAS-2000-422`, `CJMMAS-2061-422`). What do I do?**
`CJMMAS-2000-422`: the subject line is missing, so enter a subject. `CJMMAS-2061-422`: the subject contains a line break, so remove it so that the subject is on a single line.

**The opt-out link error appears. What do I do?**
Marketing emails must include an opt-out link in every variant and language. For `CJMMAS-2001-200` (warning), add the link. For `CJMMAS-2020-422`, replace the empty link with the real link. For `CJMMAS-2047-200` (warning), replace each # placeholder with the real link. For `CJMMAS-2051-422`, add the OptOutLevel tag to the one-click opt-out. Transactional emails do not need an opt-out link (`CJMMAS-2001-200`).

**Why is my published message not editable (`CJMMAS-1054-400`)?**
A published message cannot be updated directly. Create a new version of the campaign, edit the draft version, then activate it.

**I get a Forbidden error. What do I do?**
Your role lacks the permission named in the message (write, read, publish, or delete; `CJMMAS-1028-403`, `1029-403`, `1030-403`, `1042-403`). Ask your administrator to add the permission to your role.

**The save fails because the item was updated elsewhere (`JOMAL-1101-409`). What do I do?**
Someone else, or another browser tab, saved a newer version. Refresh the page to load the latest version, then reapply your changes and save again.

**Troubleshooting:**

* **Email content.** Causes and fixes:
  * Subject line missing (`CJMMAS-2000-422`): enter a subject.
  * Line break in the subject (`CJMMAS-2061-422`): remove it so that the subject is on a single line.
  * Opt-out link not present in the body (`CJMMAS-2001-200`, warning): add it; transactional emails do not need it.
  * Opt-out link null or empty (`CJMMAS-2020-422`): replace the empty link with the real link in every variant and language of a marketing email.
  * Opt-out links with a # placeholder and no actual link (`CJMMAS-2047-200`, warning): replace each # placeholder with the real link.
  * OptOutLevel tag missing from the one-click opt-out (`CJMMAS-2051-422`): add the OptOutLevel tag.
  * Empty link in the body (`CJMMAS-2002-200`, warning): add the destination, or remove the link.
  * Empty email version (`CJMMAS-2005-422`): open **[!UICONTROL Edit content]** and design the email content in the Email Designer. Empty HTML body (`CJMMAS-2052-422`): add the HTML content. Empty content template body (`CJMMAS-2053-200`, warning): add content to the template.
  * Size above the recommended size (`CJMMAS-2003-200`, warning): enable the **[!UICONTROL Optimize HTML size]** option, remove unused elements, simplify the structure, or move content into fragments. Size above the size limit named in the message (`CJMMAS-2060-422`): remove unused elements, simplify the structure, or move content into fragments.
  * AMP version present with an empty HTML version (`CJMMAS-2007-422`): add an HTML version, or remove the AMP version.
  * Text version empty (`CJMMAS-2008-200`, warning): add a text version, or let it sync with the HTML.
  * Potential spam risk (`CJMMAS-2071-200`, warning): open the spam report and fix the issues, especially if the score is above 2.
  * HTML not valid (`CJMMAS-2072-400`): check and correct the HTML.
  * Personalization attribute not correct (`CJMMAS-2400-400`): check the attribute against the personalization syntax and correct it.
  * Syntax error in a personalization expression (`CJMMAS-6101-422`): fix the expression in the personalization editor.
* **Push notifications.**
  * Empty push version (`CJMMAS-2004-422`): add the content, or remove the push channel.
  * iOS or Android payload above the limit (4 KB) (`CJMMAS-2009-422`, `CJMMAS-2010-422`): reduce the text, images, and emojis.
  * Button with no URI on iOS or Android (`CJMMAS-2016-422`, `CJMMAS-2018-422`): enter a deep link or a web URL for the button at the index named in the message.
  * On-click URI not valid for the platform named in the message (`CJMMAS-2022-422`): enter a valid deep link or web URL.
  * Media URI not valid for the platform named in the message (`CJMMAS-2023-422`): enter a valid media URL, or select an asset from [!DNL Adobe Experience Manager Assets].
* **SMS and in-app messages.**
  * Empty SMS (mobile message) version (`CJMMAS-2028-422`) or in-app version (`CJMMAS-2024-422`): add the content, or remove the channel.
  * In-app message larger than the limit named in the message (`CJMMAS-2025-200`, warning): reduce the size of images and content.
* **Direct mail.**
  * Empty file structure (`CJMMAS-2041-422`): click **[!UICONTROL Add]** to create the columns to extract.
  * File structure larger than the limit named in the message (`CJMMAS-2042-422`): an extraction file can have up to 50 columns, so remove columns until the file structure is within the limit.
  * Empty column labels (`CJMMAS-2043-422`): select each column with an empty label and specify a **[!UICONTROL Label]** in the **[!UICONTROL Formatting]** pane.
  * Repeated column label (`CJMMAS-2044-422`): change the **[!UICONTROL Label]** of the repeated columns in the **[!UICONTROL Formatting]** pane so that each label is unique.
  * Notes larger than the limit named in the message (`CJMMAS-2045-422`): shorten the notes.
  * Sort label that does not exist (`CJMMAS-2046-422`): select an existing column and toggle on its **[!UICONTROL Sort by]** option.
* **Message lifecycle and saving.**
  * Set back to Draft (`CJMMAS-1053-400`): a published message cannot be set back to Draft; create a new version of the campaign to change it.
  * Published message update (`CJMMAS-1054-400`): create a new version of the campaign, edit the draft version, then activate it.
  * Version creation from a message that is not published (`CJMMAS-1060-400`): a new version can only be created from a message in the published state; activate the campaign first, or edit the draft directly.
  * Approval status change (`CJMMAS-1077-400`): request approval, or ask the reviewer to approve or request changes.
  * Save conflict (`JOMAL-1101-409`): refresh the page to load the latest version, then reapply your changes and save again.
  * Malformed tracking links (`JOMAL-1102-400`): correct the links in the HTML, for example a missing or unclosed href, then save again.
* **Permissions.**
  * Missing write, read, publish, or delete permission (`CJMMAS-1028-403`, `CJMMAS-1029-403`, `CJMMAS-1030-403`, `CJMMAS-1042-403`): ask your administrator to add the permission to your role.
  * No permission to simulate content (`CJMMAS-1094-403`) or to manage content (`CJMMAS-1095-403`), or no access to the template: ask your administrator to update your permissions or the template access.
  * User not authorized, or operation forbidden (`JOMAL-1003-403`, `JOMAL-1203-403`): ask your administrator to check your role and your access to the item.
  * Unauthorized user (`JOMAL-1001-401`, `JOMAL-1201-401`): sign in again. If the error persists, ask your administrator to check your access to the sandbox.
  * Message belonging to another organization (`CJMMAS-1001-400`): sign in to the organization that owns the message.
* **Channel configurations and access.**
  * No channel configuration, or not found, for the channel of the message (`CJMMAS-2006-422`): select a channel configuration in the message.
  * No email, push, SMS, or web channel configuration in the message (`CJMMAS-2012-422`, `CJMMAS-2013-422`, `CJMMAS-2027-200` warning, `CJMMAS-2030-422`): select a channel configuration for that channel in the message.
  * Push channel configuration with no app (`CJMMAS-2014-422`): select an app in the configuration.
  * Email channel configuration with an empty execution list (`CJMMAS-2015-422`): complete the execution list in the configuration.
  * Channel configuration ID not valid (`CJMMAS-1034-400`) or selected channel configuration not valid (`CJMMAS-1064-400`): select a valid channel configuration, then try again.
  * Landing page with no channel configuration (`CJMMAS-1068-400`): select a channel configuration in the landing page, then try again.
  * No permission on the AEM repositories used in the content (`CJMMAS-2036-403`): ask your administrator for access to the repositories named in the message.
* **Decision policies and channel configuration fields.**
  * Empty mandatory field of the channel configuration (`CJMRT-030002-400`): open the channel configuration and fill in all mandatory fields.
  * Field longer than the maximum length shown in the message (`CJMRT-030007-400`): shorten the value.
  * Link with no URL (`CJMRT-030008-400`): add the URL, or remove the link.
  * Too many decisions (`CJMRT-030014-422`): reduce the number of decision policies in the message.
  * Decision policy that does not exist (`CJMRT-030015-422`): select a decision policy that exists.
  * Decision policy that does not belong to this campaign (`CJMRT-030017-422`): select a decision policy that belongs to the campaign.
  * Content with a decision policy saved as a fragment (`CJMRT-030018-422`): remove the decision policy, then save the fragment.
* **Expression templates.**
  * Malformed template (`CJMMAS-2037-422`): fix the syntax.
  * Empty expression content (`CJMMAS-2059-422`): add content to the expression template.
  * Template larger than 200 KB (`CJMMAS-2038-422`): reduce its size.

**Related pages:**

* Opt-out links: Email opt-out management (email/email-opt-out.md)
* Email checks: Content checks (email/content-check.md)
* Spam score and issues: Email spam report (content-management/spam-report.md)
* Limits and guardrails: Guardrails and limitations (start/guardrails.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: da514c77 -->
