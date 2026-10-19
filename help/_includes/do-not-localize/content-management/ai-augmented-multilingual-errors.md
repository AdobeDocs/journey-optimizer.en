---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors and warnings that [!DNL Adobe Journey Optimizer] returns when you create language settings, link them to translation projects, run translation jobs, or save multilingual messages, with the cause and the fix of each.

**Intents:**

* Find the cause and the fix of an error returned when creating, editing, or deleting a language setting
* Fix errors caused by a translation project that is missing, not active, or not in sync with a language setting
* Fix errors returned when creating or cancelling a translation job
* Fix errors and warnings returned when saving or publishing a message that has several locales
* Recognize which error prefix belongs to which part of multilingual content

**Glossary:**

* **Error code**: Prefix, error number, and HTTP status, for example CJMRT-080902-409 *(product-specific)*
* **CJMRT**: Error prefix for language settings *(product-specific)*
* **AJOCTO**: Error prefix for translation jobs *(product-specific)*
* **CJMMAS**: Error prefix for messages *(product-specific)*
* **Language setting**: Configuration that lists the locales of multilingual content; its type is **[!UICONTROL Translation project]** or **[!UICONTROL Manual Translation]**, and it can be active *(product-specific)*
* **Translation project**: Project linked to a language setting of the **[!UICONTROL Translation project]** type; it must exist, be active, and have the same locales as the language setting *(product-specific)*
* **Translation job**: Job created from a campaign or a journey to translate content; it can be In Progress, completed, failed, or cancelled *(product-specific)*
* **Primary variant**: The variant that must exist before a translation job is created *(product-specific)*
* **Fallback variant**: The variant that profiles who match no locale receive *(product-specific)*
* **[!UICONTROL Profile language preference attributes]**: Menu in which one or more profile attributes are selected for each locale *(product-specific)*

**Guardrails:**

* A language setting can have up to 50 locales (hard limit). Error CJMRT-080906-400 is returned when the limit is reached, and its message gives the limit.
* A language setting needs at least two locales, and a multilingual message needs at least two variants.
* A locale can appear only once in a language setting.
* At least one profile language preference attribute is required for each locale. The number of attributes that can be mapped to one locale is limited to the value given in the message of CJMRT-080908-400.
* A language setting cannot be deleted while a campaign or a journey uses it (CJMRT-080903-403).
* To change an active language setting, duplicate it first, then edit the copy (CJMRT-080905-400).
* A translation project is needed only for a language setting of the **[!UICONTROL Translation project]** type; leave it empty for manual translation.
* A translation job cannot be created while the latest translation job of the same entity is In Progress (AJOCTO-5107-409).
* A translation job cannot be cancelled when it is already completed, failed, or cancelled, or while its tasks are still being created.

**Applicability:**

* Language settings errors (CJMRT): apply when you create, edit, or delete a language setting.
* Translation project errors: apply when a language setting is linked to a translation project.
* Translation job errors (AJOCTO): apply when you create, cancel, or run a translation job from a campaign or a journey. Missing-content errors are documented for email variants (subject, HTML body), SMS variants (content), and push variants (title, body).
* Message errors and warnings (CJMMAS): apply when you save or publish a message that has several locales.

**Terminology:**

* Canonical name: Multilingual content errors — variants: language setting errors, translation job errors, multilingual message errors
* Do not confuse: error codes ending in -200 (warnings, for example CJMMAS-5103-200, CJMMAS-5106-200, CJMMAS-5107-200) ≠ error codes ending in -400, -403, -404, -409, or -422
* Do not confuse: language setting type **[!UICONTROL Translation project]** ≠ language setting type **[!UICONTROL Manual Translation]**
* Do not confuse: CJMRT (language settings) ≠ AJOCTO (translation jobs) ≠ CJMMAS (messages)

**FAQ:**

* **Q: How is a multilingual error code structured?** — It is a prefix (CJMRT for language settings, AJOCTO for translation jobs, CJMMAS for messages), an error number, and an HTTP status. For the other error code prefixes, see the error codes reference.
* **Q: Which errors are warnings?** — CJMMAS-5103-200, CJMMAS-5106-200, and CJMMAS-5107-200 are described as warnings. They concern missing variants and an empty fallback variant.
* **Q: Why can I not delete a language setting?** — CJMRT-080903-403: the language setting is used by a campaign or a journey. Remove it from the campaigns and journeys that use it, then delete it.
* **Q: Why does a language setting fail to save with a locale error?** — Check the locale rules: at least two locales (CJMRT-080905-400), no duplicate locale (CJMRT-080904-400), up to 50 locales (CJMRT-080906-400), and at least one profile language preference attribute for each locale (CJMRT-080907-400).
* **Q: What do I do when the language setting and the translation project do not match?** — Errors CJMRT-080913-400, AJOCTO-5113-400, AJOCTO-5127-400, and AJOCTO-5136-400 mean they are not in sync, and each has its own fix. For CJMRT-080913-400, make the locales of the translation project and the language setting the same, keep the same primary variant, then try again. For AJOCTO-5113-400, sync the locales and the primary variant of the language setting with its translation project, then try again. For AJOCTO-5127-400, make the locales of the translation project match those of the language setting, then try again. For AJOCTO-5136-400, keep the same primary variant in both, then try again.
* **Q: Why is my translation job not created?** — Possible causes: a translation job is already In Progress for this content (AJOCTO-5107-409, wait until it completes), the primary variant cannot be found (AJOCTO-5128-404, create it first), or the variant to translate has missing content (AJOCTO-5115-400 to AJOCTO-5119-400, add the missing subject, HTML body, content, title, or body).
* **Q: What happens when the fallback variant is empty?** — CJMMAS-5106-200 and CJMMAS-5107-200 are warnings. For CJMMAS-5106-200, the first locale named in the message is used as the fallback variant for email, push, and SMS. For CJMMAS-5107-200, nothing is delivered in case of fallback. In both cases, author the fallback variant. CJMMAS-5108-422 is returned when the fallback variant has not been authored; author it before you continue.
* **Q: Which language setting status does a message need?** — An active one (CJMMAS-5104-422). Select an active language setting.

**Troubleshooting:**

* **CJMRT-080902-409** — "A language setting with the name {name} already exists. Please enter a unique language setting name and try again." Enter a unique name.
* **CJMRT-080909-400** — "Profile preferences attribute XDM path does not exist. Verify the path and try again." Select an existing attribute from the **[!UICONTROL Profile language preference attributes]** menu.
* **CJMRT-080911-400** — The language setting is for manual translation, which does not use a translation project. Leave the translation project empty.
* **AJOCTO-5111-400** — The language setting has no translation project. Click **[!UICONTROL Edit]** in the **[!UICONTROL Translation project]** field of the language setting and choose a translation project.
* **AJOCTO-5108-400**, **AJOCTO-5109-400** — "The type of the language setting must be 'Translation Project'." and "The type of the language setting must be 'Manual Translation'." Select a language setting of the **[!UICONTROL Translation project]** type (AJOCTO-5108-400) or the **[!UICONTROL Manual Translation]** type (AJOCTO-5109-400).
* **AJOCTO-5110-400** — "The language setting must be 'Active'." Activate it, or select an active language setting.
* **CJMRT-080912-400**, **AJOCTO-5112-400** — The translation project is not active. Choose an active translation project in the **[!UICONTROL Translation project]** field of the language setting.
* **CJMRT-080914-400** — "Translation project with given ID not found. Please provide a valid ID to create a language setting." Choose an existing translation project in the **[!UICONTROL Translation project]** field of the language setting.
* **CJMRT-080908-400**, **CJMRT-080910-400** — Reduce the number of attributes mapped to the locale to the limit given in the message (CJMRT-080908-400). Make each locale value unique in the profile language preference attributes (CJMRT-080910-400).
* **AJOCTO-5106-400**, **AJOCTO-5138-400** — The translation job cannot be cancelled. For AJOCTO-5106-400, follow the status of the translation in your translation project; to translate changed content again, create a new translation project and resend it for translation. For AJOCTO-5138-400, wait until the translation tasks are created, then cancel the job again.
* **CJMMAS-5101-422** — "Primary variant is missing in the multilingual inline message." Create the primary variant.
* **CJMMAS-5102-422** — A multilingual message needs at least two variants. Add the missing variants.
* **CJMMAS-5105-422** — The language setting of the message has fewer than two locales. Add the missing locales.
* **CJMMAS-5103-200** — Warning: some variants of the message are missing. Author the variants named in the message, or accept that profiles in these locales receive the fallback variant.

**Related pages:**

* Create language settings and multilingual content manually: Create multilingual content with manual translation (content-management/multilingual-manual.md)
* Translation projects and review of translation jobs: Create multilingual content with automated translation (content-management/multilingual-automated.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Overview of multilingual content: Get started with multilingual content (content-management/multilingual-gs.md)
* Locales: Create a locale (content-management/multilingual-locale.md)
* Language providers: Create a language provider (content-management/multilingual-provider.md)

+++

<!-- ai-section-version: 1 | source-hash: f2cdca50 -->
