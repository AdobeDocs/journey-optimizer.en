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
* **Published messages:** a published message cannot be set back to Draft (`CJMMAS-1053-400`) or updated directly (`CJMMAS-1054-400`). A new version can only be created from a published (Live) message (`CJMMAS-1060-400`).

**Terminology:**

* Canonical name: Content authoring errors — variants: content errors.
* Prefixes: **CJMMAS**, **CJMRT**, and **JOMAL** (used in the Message lifecycle and saving, and the Permissions sections).
* Error messages quote the terms "preset" and "surface"; the page uses "channel configuration" for the same configuration in the fix. Mobile message: the channel, with SMS as a variant; the messages and the page section title keep the wording "SMS" and "In-App".
* Acronym: AEM = Adobe Experience Manager.
* **Do not confuse:** a warning (status 200, does not block saving or publishing) and an error with another status such as 400, 403, 409, or 422. Some codes in the same row have different statuses: for example `CJMMAS-2001-200` (warning) and `CJMMAS-2020-422`.
* **Do not confuse:** `403` (permission) and `401` (session not valid or expired).

**FAQ:**

**What do the CJMMAS and CJMRT prefixes mean?**
Content errors use the prefixes **CJMMAS** and **CJMRT**, followed by an error number and an HTTP status.

**Does a code ending in 200 block publishing?**
No. Codes with the status 200 are warnings: they do not block saving or publishing.

**The subject line error appears (`CJMMAS-2000-422`, `CJMMAS-2061-422`). What do I do?**
The email needs a subject line, on a single line. Enter a subject and remove any line break.

**The opt-out link error appears. What do I do?**
Marketing emails must include an opt-out link in every variant and language. Add the link, replace any # placeholder with the real link, and for a one-click opt-out add the OptOutLevel tag. Transactional emails do not need it.

**Why is my published message not editable (`CJMMAS-1054-400`)?**
A published message cannot be updated directly. Create a new version of the campaign, edit the draft version, then activate it.

**I get a Forbidden error. What do I do?**
Your role lacks the permission named in the message (write, read, publish, or delete; `CJMMAS-1028-403`, `1029-403`, `1030-403`, `1042-403`). Ask your administrator to add the permission to your role.

**The save fails because the item was updated elsewhere (`JOMAL-1101-409`). What do I do?**
Someone else, or another browser tab, saved a newer version. Refresh the page to load the latest version, then reapply your changes and save again.

**Troubleshooting:**

* **Email content.** Causes and fixes:
  * Subject line: missing or on several lines (`CJMMAS-2000-422`, `2061-422`).
  * Opt-out link: missing, empty, or a # placeholder (`CJMMAS-2001-200`, `2020-422`, `2047-200`), or the OptOutLevel tag is missing for a one-click opt-out (`2051-422`).
  * Empty link in the body (`CJMMAS-2002-200`, warning): add the destination, or remove the link.
  * Empty email, HTML body, or content template (`CJMMAS-2005-422`, `2052-422`, `2053-200`): add the content.
  * Size above the recommended size (`CJMMAS-2003-200`, `2060-422`): remove unused elements, simplify the structure, or move content into fragments.
  * AMP version present with an empty HTML version (`CJMMAS-2007-422`): add an HTML version, or remove the AMP version.
  * Text version empty (`CJMMAS-2008-200`, warning): add a text version, or let it sync with the HTML.
  * Potential spam risk (`CJMMAS-2071-200`, warning): open the spam report and fix the issues, especially if the score is above 2.
  * HTML not valid, or syntax error in a personalization expression (`CJMMAS-2072-400`, `2400-400`, `6101-422`): check the HTML, and fix the expression in the personalization editor.
* **Push notifications.** Causes: an empty push version (`CJMMAS-2004-422`, add the content or remove the push channel), a payload above 4 KB (`2009-422`, `2010-422`, reduce the text, images, and emojis), a button with no URI (`2016-422`, `2018-422`, enter a deep link or a web URL), an on-click or media URI that is not valid (`2022-422`, `2023-422`).
* **SMS and in-app messages.** Causes: an empty SMS (mobile message) version (`CJMMAS-2028-422`) or in-app version (`2024-422`), for which you add the content or remove the channel; an in-app message larger than the limit named in the message (`2025-200`, warning), for which you reduce the size of images and content.
* **Direct mail.** Causes: empty file structure or larger than the limit named in the message (`CJMMAS-2041-422`, `2042-422`), empty or repeated column labels (`2043-422`, `2044-422`), notes larger than the limit named in the message, or a sort label that does not exist (`2045-422`, `2046-422`). Fix: add the columns to extract (up to 50), give each column a unique label, shorten the notes, and select an existing column for the sort.
* **Message lifecycle and saving.** Causes: set back to Draft (`CJMMAS-1053-400`), published message update (`1054-400`), version creation from a message that is not published (`1060-400`), approval status change (`1077-400`), save conflict (`JOMAL-1101-409`), malformed tracking links (`JOMAL-1102-400`). Fixes: create a new version of the campaign; activate the campaign first, or edit the draft directly; the approval status is set by the approval workflow, so request approval or ask the reviewer to approve or request changes; refresh and save again; correct the links in the HTML, for example a missing or unclosed href.
* **Permissions.** Causes: missing write, read, publish, or delete permission (`CJMMAS-1028-403`, `1029-403`, `1030-403`, `1042-403`); no permission to simulate or manage content, or to access the template (`1094-403`, `1095-403`); user not authorized (`JOMAL-1003-403`, `1203-403`); session not valid or expired (`JOMAL-1001-401`, `1201-401`); message belonging to another organization (`CJMMAS-1001-400`). Fixes: ask your administrator to add the permission, update your permissions or the template access, or check your role and the object access for the item; sign in again (if the error persists, ask your administrator to check your access to the sandbox); sign in to the organization that owns the message.
* **Channel configurations and access.** Causes: no channel configuration for the channel (`CJMMAS-2006-422`, `2012-422`, `2013-422`, `2027-200`, `2030-422`), an incomplete configuration (`2014-422`, `2015-422`: a push configuration needs an app, and an email configuration needs its execution list), a configuration that is not valid (`1034-400`, `1064-400`), a landing page with no channel configuration (`1068-400`), no permission on the AEM repositories used in the content (`2036-403`). Fix: select or complete a valid channel configuration; for the AEM repositories, ask your administrator for access to the repositories named in the message.
* **Decision policies and channel configuration fields.** Causes: an empty mandatory field (`CJMRT-030002-400`), a field that is too long (`030007-400`), a link with no URL (`030008-400`), too many decisions (`030014-422`), a decision policy that does not exist or does not belong to this campaign (`030015-422`, `030017-422`), content with a decision policy saved as a fragment (`030018-422`). Fix: fill in the mandatory fields, shorten the value, add the URL or remove the link, reduce the number of decision policies, select a decision policy that exists in the campaign, or remove the decision policy before saving the fragment.
* **Expression templates.** Causes: an empty or not valid template (`CJMMAS-2037-422`, `2059-422`), a template larger than 200 KB (`2038-422`). Fix: add content, fix the syntax, or reduce the size.

**Related pages:**

* Opt-out links: Email opt-out management (email/email-opt-out.md)
* Email checks: Content checks (email/content-check.md)
* Spam score and issues: Email spam report (content-management/spam-report.md)
* Limits and guardrails: Guardrails and limitations (start/guardrails.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: b64d60c4 -->
