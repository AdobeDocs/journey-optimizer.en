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
| **CJMRT-080902-409** | A language setting with the name {name} already exists. Please enter a unique language setting name and try again. | Enter a unique name for the language setting. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080904-400** | Language settings have duplicate locale values. Please ensure each locale has a unique mapping. | Remove the duplicate locale so that each locale appears once in the language setting. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080905-400** | Only one locale has been defined in the language settings. You must have at least two locales configured. | Add a locale so that the language setting has at least two. To change an active language setting, duplicate it first, then edit the copy. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080906-400** | You have reached the locale limit. You can add up to {localeLimit} locales in the language settings. | Remove the locales you do not need to stay within 50 locales. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080907-400** | There are no profile preferences available for the selected locale. At least one profile preference per locale is required. | Select at least one profile language preference attribute for each locale. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080908-400** | You cannot map more than {profilePreferencesLimit} profile preferences to a single locale. Please reduce the number of profile preferences selected. | Reduce the number of attributes mapped to the locale to the limit given in the message. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080909-400** | Profile preferences attribute XDM path does not exist. Verify the path and try again. | Select an existing attribute from the **[!UICONTROL Profile language preference attributes]** menu. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080910-400** | There are duplicate locale values in the profile preferences. Please ensure locale values are unique. | Make each locale value unique in the profile language preference attributes. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080903-403** | This language setting cannot be deleted as it is attached to a campaign or journey. | Remove the language setting from the campaigns and journeys that use it, then delete it. [Learn more](multilingual-manual.md#language-settings) |

## Translation projects {#translation-project}

These errors occur when a language setting is linked to a translation project that is missing, not active, or not in sync.

See also [Create a translation project](multilingual-automated.md#translation-project).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080911-400** | This Language Setting is being configured for Manual Translation. The translation project ID is only required when using Translation Project. | Leave the translation project empty in this language setting. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5111-400** | The translation project ID is missing in the given language setting. | Click **[!UICONTROL Edit]** in the **[!UICONTROL Translation project]** field of the language setting and choose a translation project. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5108-400** | The type of the language setting must be 'Translation Project'. | Select a language setting of the **[!UICONTROL Translation project]** type. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5109-400** | The type of the language setting must be 'Manual Translation'. | Select a language setting of the **[!UICONTROL Manual Translation]** type. [Learn more](multilingual-automated.md#language-settings) |
| **AJOCTO-5110-400** | The language setting must be 'Active'. | Activate the language setting, or select an active language setting. [Learn more](multilingual-manual.md#language-settings) |
| **CJMRT-080912-400** | The selected translation project is not active. Please select an active translation project to create this setting. | Choose an active translation project in the **[!UICONTROL Translation project]** field to create the setting. [Learn more](multilingual-automated.md#translation-project) |
| **AJOCTO-5112-400** | The translation project associated with the language setting must be 'Active'. | Choose an active translation project in the **[!UICONTROL Translation project]** field of the language setting. [Learn more](multilingual-automated.md#translation-project) |
| **CJMRT-080914-400** | Translation project with given ID not found. Please provide a valid ID to create a language setting. | Choose an existing translation project in the **[!UICONTROL Translation project]** field of the language setting. [Learn more](multilingual-automated.md#translation-project) |
| **CJMRT-080913-400** | The locales in the translation project do not match with those in the language setting. Please ensure they are the same. | Make the locales of the translation project and of the language setting the same, keep the same primary variant, then try again. [Learn more](multilingual-automated.md#translation-project) |
| **AJOCTO-5113-400** | The language setting is out of sync with the associated translation project. Please sync them up and try again. | Sync the locales and the primary variant of the language setting with its translation project, then try again. [Learn more](multilingual-automated.md#translation-project) |
| **AJOCTO-5127-400** | The target locale of the translation job does not match the locale of the language setting. Please sync them up and try again. | Make the locales of the translation project match those of the language setting, then try again. [Learn more](multilingual-automated.md#translation-project) |
| **AJOCTO-5136-400** | The primary variant of the language setting has changed as it no longer matches the source locale of the translation job. Please sync them up and try again. | Keep the same primary variant in the language setting and in the translation project, then try again. [Learn more](multilingual-automated.md#translation-project) |

## Translation jobs {#jobs}

These errors occur when you create, cancel, or run a translation job from a campaign or a journey.

See also [Review your translation project](multilingual-automated.md#review-translation-project).

| Error code | Message | How to fix |
|---|---|---|
| **AJOCTO-5107-409** | The translation job cannot be created as the latest translation job of the given entity ID is already in 'In Progress' state. | Wait until the translation job in progress completes, then create a new job. [Learn more](multilingual-automated.md#review-translation-project) |
| **AJOCTO-5106-400** | The translation job cannot be cancelled as it has already been completed, failed, or cancelled. | Follow the status of the translation in your translation project. To translate changed content again, create a new translation project and resend it for translation. [Learn more](multilingual-automated.md#review-translation-project) |
| **AJOCTO-5138-400** | The translation job cannot be cancelled as the translation task creation is still in progress. Please try again later. | Wait until the translation tasks are created, then cancel the job again. [Learn more](multilingual-automated.md#review-translation-project) |
| **AJOCTO-5128-404** | Cannot find primary variant. Please check and try again. | Create the content of the primary variant before you create the translation job. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5115-400** | The translation job failed as the subject is missing in the email variant. | Add the subject to the email variant, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5116-400** | The translation job failed as the HTML body is missing in the email variant. | Add the HTML body to the email variant, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5117-400** | The translation job failed as the content is missing in the SMS variant. | Add the content to the SMS variant, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5118-400** | The translation job failed as the title is missing in the push variant. | Add the title to the push variant, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |
| **AJOCTO-5119-400** | The translation job failed as the push notification body or title is missing. Check the content of the push notification and try again. | Add the missing body or title to the push variant, then create the job again. [Learn more](multilingual-automated.md#create-multilingual-campaign) |

## Multilingual messages {#messages}

These errors and warnings occur when you save or publish a message that has several locales.

See also [Create multilingual content](multilingual-manual.md#create-multilingual-campaign).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-5101-422** | Primary variant is missing in the multilingual inline message. | Create the primary variant. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5102-422** | Multilingual inline message must have at least 2 variants. | Add variants so that the message has at least two. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5105-422** | The provided LanguageSetting must have at least two locales. | Add locales to the language setting of the message so that it has at least two. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5103-200** | Multilingual inline message has following missing variants: ''{missingVariants}''. | Author the variants named in the message, or accept that profiles in these locales receive the fallback variant (warning). [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5104-422** | The provided LanguageSetting has status: ''{status}''. Please provide a valid  | Select an active language setting for the message. [Learn more](multilingual-manual.md#language-settings) |
| **CJMMAS-5108-422** | Fallback variant ''{localeCode}'' has not been authored. Please author the fallback variant before continuing | Author the fallback variant before you continue. [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5106-200** | The provided LanguageSetting has an empty fallback variant. For email, push, and sms channels, the first locale ''{firstLocale}'' from the language setting will be used as the fallback variant. | Author the fallback variant (warning). [Learn more](multilingual-manual.md#create-multilingual-campaign) |
| **CJMMAS-5107-200** | The provided LanguageSetting has an empty fallback variant. Nothing will be delivered in case of fallback. | Author the fallback variant so that profiles who match no locale receive content (warning). [Learn more](multilingual-manual.md#create-multilingual-campaign) |

## Related topics {#related}

* [Get started with multilingual content](multilingual-gs.md)
* [Create a locale](multilingual-locale.md)
* [Create a language provider](multilingual-provider.md)
* [Create multilingual content with manual translation](multilingual-manual.md)
* [Create multilingual content with automated translation](multilingual-automated.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/content-management/ai-augmented-multilingual-errors.md}}
