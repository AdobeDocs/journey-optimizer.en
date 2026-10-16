---
solution: Journey Optimizer
product: Journey Optimizer
title: Troubleshooting overview
description: Find the right troubleshooting resource for Adobe Journey Optimizer, including the troubleshooting FAQ, the journey troubleshooting guides, and the pages that explain each family of error codes
hide: true
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
---
# Troubleshooting overview {#section-overview}

Use this section to find the cause of a problem and how to fix it. It brings together the troubleshooting FAQ, the guides for journeys, and one page for each family of error codes. Start from the type of resource you need, or from the error code that you received.

## Troubleshooting FAQ {#faq}

The [troubleshooting FAQ](../using/start/troubleshooting.md) answers frequent questions across [!DNL Journey Optimizer], such as fragments, email content and tracking, and the count of engageable profiles.

## Troubleshoot journeys {#journeys-guides}

| If you need to | Go to |
| --- | --- |
| Find and fix the errors that block the test or the publication of a journey | [Troubleshoot journey errors](../using/building-journeys/troubleshooting.md) |
| Understand a journey validation error code | [Journey validation errors](../using/building-journeys/journey-validation-errors.md) |
| Find out why profiles do not enter or progress through a live journey | [Troubleshoot journey execution](../using/building-journeys/troubleshooting-execution.md) |
| Debug an inbound action that does not display or continues after a profile exits | [Troubleshoot inbound actions](../using/building-journeys/troubleshooting-inbound.md) |
| Check that a custom action and its API call work | [Troubleshoot custom actions](../using/action/troubleshoot-custom-action.md) |

## Troubleshoot error codes {#error-codes}

Each page groups the errors of one feature, with the exact error message, the cause, and how to fix it. Use the family of the error code to open the right page, or go directly to the section that matches where the error occurs.

### Read an error code {#read-error-code}

An error code has a prefix that identifies the service, an error number, and an HTTP status. For example, `AJOJAS-2030-400` is a journey validation error (prefix AJOJAS), number 2030, status 400. A code with the status 200 is a warning: it does not block saving or publishing.

For the structure of error codes and the steps to take before you contact support, see the [error codes reference](../using/building-journeys/error-codes-reference.md).

### Find your error by family {#find-error}

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

Journeys

Prefix AJOJAS. Errors raised when you validate, test or publish a journey.

[View the error pages](#journeys)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

Campaigns and audiences

Prefixes CJMCMP, CJMOC, CJMDMS and CJMRT 15xxxx and 17xxxx. Errors on Action, API-triggered and Orchestrated campaigns, on relational schemas and datasets, and on audience composition.

[View the error pages](#campaigns-and-audiences)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/pencil-alt.svg)

Content authoring and personalization

Prefixes CJMMAS 10xx and 2xxx, CJMRT 030xxx, CJMTL, JOMAL, CJMPTS, AJOTDS and CJMSAS. Errors on the content of messages, on expressions and helpers, and on proofs and simulated users.

[View the error pages](#content-authoring-and-personalization)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/file-alt.svg)

Fragments, multilingual content and landing pages

Prefixes CJMMAS 11xx to 17xx, 3xxx, 51xx and 81xx, AJOCBS, AJOAGS, AJOCTO and CJMRT 0809xx. Errors on fragments and AEM content, translation, and landing pages.

[View the error pages](#fragments-multilingual-content-and-landing-pages)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

Deliverability setup

Prefixes CJMRT 0806xx, 0808xx and 18xxxx. Errors on subdomain delegation, DNS records, seed lists and IP warmup plans.

[View the error pages](#deliverability-setup)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Custom channels, inbound actions and reporting

Prefixes CJMIAS, CJMRPS and CJMRT 0817xx. Errors on custom channel credentials, inbound actions and reporting datasets.

[View the error pages](#custom-channels-inbound-actions-and-reporting)
:::

::::

### Error pages and sections by family {#pages}

#### Journeys {#journeys}

These errors appear when you check, test or publish a journey. Go to the section that matches the activity or setting named in the message.

| Error page | Sections |
| --- | --- |
| [Journey validation errors](../using/building-journeys/journey-validation-errors.md) | [Journey structure](../using/building-journeys/journey-validation-errors.md#structure) \| [Action activities](../using/building-journeys/journey-validation-errors.md#actions) \| [Events and reactions](../using/building-journeys/journey-validation-errors.md#events) \| [License package limits (Select)](../using/building-journeys/journey-validation-errors.md#select-package) \| [Versions, test mode, and size](../using/building-journeys/journey-validation-errors.md#versions) |

#### Campaigns and audiences {#campaigns-and-audiences}

These errors appear when you set up, schedule or activate an Action, API-triggered or Orchestrated campaign, when you define a relational schema or a dataset, and when you build and publish an audience composition.

| Error page | Sections |
| --- | --- |
| [Campaign errors](../using/campaigns/campaign-errors.md) | [Audience](../using/campaigns/campaign-errors.md#audience) \| [Schedule and approval](../using/campaigns/campaign-errors.md#schedule) \| [Rapid delivery](../using/campaigns/campaign-errors.md#rapid) |
| [Orchestrated campaign errors](../using/orchestrated/orchestrated-campaign-errors.md) | [Campaign status and lifecycle](../using/orchestrated/orchestrated-campaign-errors.md#status) \| [Activities](../using/orchestrated/orchestrated-campaign-errors.md#activities) \| [Signals and chained campaigns](../using/orchestrated/orchestrated-campaign-errors.md#signal) |
| [Relational schema and dataset errors](../using/orchestrated/relational-schema-errors.md) | [Files and formats](../using/orchestrated/relational-schema-errors.md#files) \| [Primary key and version descriptor](../using/orchestrated/relational-schema-errors.md#keys) \| [Relationships](../using/orchestrated/relational-schema-errors.md#relationships) |
| [Audience composition errors](../using/audience/audience-composition-errors.md) | [Enrichment](../using/audience/audience-composition-errors.md#enrichment) \| [Publication, limits, and permissions](../using/audience/audience-composition-errors.md#publication) |

#### Content authoring and personalization {#content-authoring-and-personalization}

These errors appear when you validate or save the content of a message, when an expression or a helper cannot be resolved, and when you preview a message or use simulated users.

| Error page | Sections |
| --- | --- |
| [Content authoring errors](../using/content-management/content-authoring-errors.md) | [Email content](../using/content-management/content-authoring-errors.md#email) \| [Push notifications](../using/content-management/content-authoring-errors.md#push) \| [Message lifecycle and saving](../using/content-management/content-authoring-errors.md#lifecycle) \| [Permissions](../using/content-management/content-authoring-errors.md#permissions) |
| [Personalization errors](../using/personalization/personalization-errors.md) | [Variables and paths](../using/personalization/personalization-errors.md#variables) \| [Helpers](../using/personalization/personalization-errors.md#helpers) \| [URL parameter encryption keys](../using/personalization/personalization-errors.md#encryption) |
| [Proof and simulation errors](../using/content-management/proof-simulation-errors.md) | [Proofs and previews](../using/content-management/proof-simulation-errors.md#proofs) \| [Simulated users](../using/content-management/proof-simulation-errors.md#simulated-users) |

#### Fragments, multilingual content and landing pages {#fragments-multilingual-content-and-landing-pages}

These errors appear when you publish a fragment or use AEM content, when you set up language settings and translations, and when you publish or edit a landing page.

| Error page | Sections |
| --- | --- |
| [Fragments and AEM content errors](../using/content-management/fragments-errors.md) | [Publishing fragments](../using/content-management/fragments-errors.md#publication) \| [AEM content fragments](../using/content-management/fragments-errors.md#aem-fragments) \| [AEM assets](../using/content-management/fragments-errors.md#aem-assets) |
| [Multilingual content errors](../using/content-management/multilingual-errors.md) | [Language settings](../using/content-management/multilingual-errors.md#language-settings) \| [Translation projects](../using/content-management/multilingual-errors.md#translation-project) |
| [Landing page errors](../using/landing-pages/landing-page-errors.md) | [Publication and status](../using/landing-pages/landing-page-errors.md#publication) \| [Forms and subscription lists](../using/landing-pages/landing-page-errors.md#forms) \| [Expiration](../using/landing-pages/landing-page-errors.md#expiration) |

#### Deliverability setup {#deliverability-setup}

These errors appear when you delegate a subdomain, create DNS records or seed lists, and when you upload, activate or run an IP warmup plan.

| Error page | Sections |
| --- | --- |
| [Subdomain delegation and DNS errors](../using/configuration/subdomain-delegation-errors.md) | [Subdomain delegation](../using/configuration/subdomain-delegation-errors.md#delegation) \| [DNS records](../using/configuration/subdomain-delegation-errors.md#dns) \| [Seed lists](../using/configuration/subdomain-delegation-errors.md#seed) |
| [IP warmup plan errors](../using/configuration/ip-warmup-plan-errors.md) | [Plan file](../using/configuration/ip-warmup-plan-errors.md#file) \| [Runs and activation](../using/configuration/ip-warmup-plan-errors.md#runs) \| [Run failures](../using/configuration/ip-warmup-plan-errors.md#failures) |

#### Custom channels, inbound actions and reporting {#custom-channels-inbound-actions-and-reporting}

These errors appear when you configure custom channel credentials, when an inbound action runs, and when you set up reporting datasets.

| Error page | Sections |
| --- | --- |
| [Custom channel, inbound action, and reporting dataset errors](../using/configuration/channel-reporting-errors.md) | [Custom channels](../using/configuration/channel-reporting-errors.md#custom-channel) \| [Inbound actions](../using/configuration/channel-reporting-errors.md#inbound) \| [Reporting datasets](../using/configuration/channel-reporting-errors.md#reporting) |

### Error code prefixes by feature {#prefixes}

The prefix of an error code tells you which feature raised it. Use the table to open the page that explains the code.

| Error code prefix | Feature | Page |
| --- | --- | --- |
| AJOJAS | Journeys: validation before test or publication | [Journey validation errors](../using/building-journeys/journey-validation-errors.md) |
| CJMCMP, CJMRT 15xxxx | Action and API-triggered campaigns, including schedules | [Campaign errors](../using/campaigns/campaign-errors.md) |
| CJMOC | Orchestrated campaigns | [Orchestrated campaign errors](../using/orchestrated/orchestrated-campaign-errors.md) |
| CJMDMS | Relational schemas and datasets | [Relational schema and dataset errors](../using/orchestrated/relational-schema-errors.md) |
| CJMRT 17xxxx | Audience composition | [Audience composition errors](../using/audience/audience-composition-errors.md) |
| CJMMAS 10xx and 2xxx, CJMRT 030xxx, JOMAL | Content of emails, push notifications, SMS, in-app messages, and direct mail, including message lifecycle and permissions | [Content authoring errors](../using/content-management/content-authoring-errors.md) |
| CJMTL, CJMRT 01xxxx, 07xxxx, 13xxxx, 0816xx | Personalization expressions, helpers, and URL encryption keys | [Personalization errors](../using/personalization/personalization-errors.md) |
| CJMPTS, AJOTDS, CJMSAS | Proofs, previews, and simulated users | [Proof and simulation errors](../using/content-management/proof-simulation-errors.md) |
| CJMMAS 11xx to 17xx and 81xx, AJOCBS, AJOAGS | Fragments, AEM content fragments, and AEM assets | [Fragments and AEM content errors](../using/content-management/fragments-errors.md) |
| CJMMAS 51xx, CJMRT 0809xx, AJOCTO | Multilingual content and translation | [Multilingual content errors](../using/content-management/multilingual-errors.md) |
| CJMMAS 3xxx, 107x, and 130x | Landing pages | [Landing page errors](../using/landing-pages/landing-page-errors.md) |
| CJMRT 0806xx and 0808xx | Subdomain delegation, DNS records, and seed lists | [Subdomain delegation and DNS errors](../using/configuration/subdomain-delegation-errors.md) |
| CJMRT 18xxxx | IP warmup plans | [IP warmup plan errors](../using/configuration/ip-warmup-plan-errors.md) |
| CJMIAS, CJMRPS, CJMRT 0817xx | Inbound actions, reporting datasets, and custom channel credentials | [Custom channel, inbound action, and reporting dataset errors](../using/configuration/channel-reporting-errors.md) |

## If your problem is not listed {#not-listed}

* Look for the error code in the [error codes reference](../using/building-journeys/error-codes-reference.md).
* Check the [troubleshooting FAQ](../using/start/troubleshooting.md) and the journey guides above.
* If the problem persists, [contact Adobe Support](../using/start/user-interface.md#support-ticket-guidelines) with the complete error code and the request ID.
