---
solution: Journey Optimizer
product: journey optimizer
title: Multilingual content errors
description: Learn what common errors mean when you create language settings, translation projects, and multilingual content in Adobe Journey Optimizer, and how to fix them
feature: Multilingual Content
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, multilingual, language settings, translation, locale
hide: true
---
# Multilingual content errors {#multilingual-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you create language settings, link them to translation projects, run translation jobs, or save multilingual messages.

>[!ENDSHADEBOX]

Multilingual errors use the prefixes **CJMRT** (language settings), **AJOCTO** (translation jobs), and **CJMMAS** (messages), followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Language settings {#language-settings}

These errors occur when you create, edit, or delete a language setting.

See also [Create language settings](multilingual-manual.md#language-settings).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080902-409** | A language setting with the name {name} already exists. Please enter a unique language setting name and try again. | A language setting with this name already exists. Enter a unique name. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080904-400** | Language settings have duplicate locale values. Please ensure each locale has a unique mapping. | A locale can appear only once in a language setting. Remove the duplicate locale. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080905-400** | Only one locale has been defined in the language settings. You must have at least two locales configured. | A language setting needs at least two locales. Add a locale. To change an active language setting, duplicate it first, then edit the copy. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080906-400** | You have reached the locale limit. You can add up to {localeLimit} locales in the language settings. | A language setting can have up to 50 locales. Remove the locales you do not need. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080907-400** | There are no profile preferences available for the selected locale. At least one profile preference per locale is required. | No profile language preference attribute is selected for a locale. Select at least one attribute for each locale. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080908-400** | You cannot map more than {profilePreferencesLimit} profile preferences to a single locale. Please reduce the number of profile preferences selected. | Too many profile language preference attributes are mapped to one locale. Reduce the number of attributes to the limit given in the message. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080909-400** | Profile preferences attribute XDM path does not exist. Verify the path and try again. | A selected profile language preference attribute does not exist in the profile schema. Select an existing attribute from the **[!UICONTROL Profile language preference attributes]** menu. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080910-400** | There are duplicate locale values in the profile preferences. Please ensure locale values are unique. | The same locale value appears more than once in the profile language preference attributes. Make each locale value unique. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080903-403** | This language setting cannot be deleted as it is attached to a campaign or journey. | The language setting is used by a campaign or a journey. Remove it from the campaigns and journeys that use it, then delete it. [Learn more](multilingual-manual.md#language-settings) |

## Translation projects {#translation-project}

These errors occur when a language setting is linked to a translation project that is missing, not active, or not in sync.

See also [Create a translation project](multilingual-automated.md#translation-project).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080911-400**, **AJOCTO-5111-400** | This Language Setting is being configured for Manual Translation. The translation project ID is only required when using Translation Project.<br/>The translation project ID is missing in the given language setting. | A translation project is needed only for a language setting of the **[!UICONTROL Translation Project]** type. Add the project to such a setting, and leave it empty for manual translation. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5108-400**, **AJOCTO-5109-400** | The type of the language setting must be 'Translation Project'.<br/>The type of the language setting must be 'Manual Translation'. | The operation needs a language setting of another type. Select a language setting of the type named in the message. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5110-400** | The language setting must be 'Active'. | The language setting must be active. Activate it, or select an active language setting. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080912-400**, **AJOCTO-5112-400** | The selected translation project is not active. Please select an active translation project to create this setting.<br/>The translation project associated with the language setting must be 'Active'. | The translation project is not active. Select an active translation project. [Learn more](multilingual-automated.md#translation-project) |
| **CJMRT-080914-400** | Translation project with given ID not found. Please provide a valid ID to create a language setting. | The translation project cannot be found. Select an existing translation project. [Learn more](multilingual-automated.md#translation-project) |
| **CJMRT-080913-400**, **AJOCTO-5113-400**, **AJOCTO-5127-400**, **AJOCTO-5136-400** | The locales in the translation project do not match with those in the language setting. Please ensure they are the same.<br/>The language setting is out of sync with the associated translation project. Please sync them up and try again.<br/>The target locale of the translation job does not match the locale of the language setting. Please sync them up and try again.<br/>The primary variant of the language setting has changed as it no longer matches the source locale of the translation job. Please sync them up and try again. | The language setting and the translation project are not in sync: their locales, or the primary variant, do not match. Make the locales of the translation project match those of the language setting, keep the same primary variant, then try again. [Learn more](multilingual-automated.md#translation-project) |

## Translation jobs {#jobs}

These errors occur when you create, cancel, or run a translation job from a campaign or a journey.

See also [Review your translation project](multilingual-automated.md#review-translation-project).

| Error code | Message | How to fix |
|---|---|---|
| **AJOCTO-5107-409** | The translation job cannot be created as the latest translation job of the given entity ID is already in 'In Progress' state. | A translation job is already in progress for this content. Wait until it completes, then create a new job. [Learn more](multilingual-automated.md#review-translation-project) |
| **AJOCTO-5106-400**, **AJOCTO-5138-400** | The translation job cannot be cancelled as it has already been completed, failed, or cancelled.<br/>The translation job cannot be cancelled as the translation task creation is still in progress. Please try again later. | The job cannot be cancelled: it is already completed, failed, or cancelled, or its tasks are still being created. In the second case, wait and try again. [Learn more](multilingual-automated.md#review-translation-project) |
| **AJOCTO-5128-404** | Cannot find primary variant. Please check and try again. | The primary variant cannot be found. Create the content of the primary variant before you create the translation job. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5115-400**, **AJOCTO-5116-400** | The translation job failed as the subject is missing in the email variant.<br/>The translation job failed as the HTML body is missing in the email variant. | The email variant to translate has no subject or no HTML body. Add the missing content, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5117-400**, **AJOCTO-5118-400**, **AJOCTO-5119-400** | The translation job failed as the content is missing in the SMS variant.<br/>The translation job failed as the title is missing in the push variant.<br/>The translation job failed as the push notification body or title is missing. Check the content of the push notification and try again. | The SMS or push variant to translate has no content, no title, or no message. Add the missing content, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |

## Multilingual messages {#messages}

These errors and warnings occur when you save or publish a message that has several locales.

See also [Create multilingual content](multilingual-manual.md#create-multilingual-campaign).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-5101-422** | Primary variant is missing in the multilingual inline message. | The message has no primary variant. Create the primary variant. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5102-422**, **CJMMAS-5105-422** | Multilingual inline message must have at least 2 variants.<br/>The provided LanguageSetting must have at least two locales. | A multilingual message needs at least two variants, and its language setting at least two locales. Add the missing variants or locales. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5103-200** | Multilingual inline message has following missing variants: ''{missingVariants}''. | Some variants of the message are missing (warning). Author the variants named in the message, or accept that profiles in these locales receive the fallback variant. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5104-422** | The provided LanguageSetting has status: ''{status}''. Please provide a valid  | The language setting of the message is not active. Select an active language setting. [Learn more](multilingual-manual.md#language-settings) |
| **CJMMAS-5108-422** | Fallback variant ''{localeCode}'' has not been authored. Please author the fallback variant before continuing | The fallback variant is not authored. Author the fallback variant before you continue. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5106-200**, **CJMMAS-5107-200** | The provided LanguageSetting has an empty fallback variant. For email, push, and sms channels, the first locale ''{firstLocale}'' from the language setting will be used as the fallback variant.<br/>The provided LanguageSetting has an empty fallback variant. Nothing will be delivered in case of fallback. | The fallback variant is empty (warning). Author it so that profiles who match no locale receive content. [Learn more](multilingual-manual.md#create-multilingual-campaign) |

## Related topics {#related}

* [Get started with multilingual content](multilingual-gs.md)
* [Create a locale](multilingual-locale.md)
* [Create a language provider](multilingual-provider.md)
* [Create multilingual content with manual translation](multilingual-manual.md)
* [Create multilingual content with automated translation](multilingual-automated.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)
