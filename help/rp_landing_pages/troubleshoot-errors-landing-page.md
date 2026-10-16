---
solution: Journey Optimizer
product: Journey Optimizer
title: Troubleshoot error codes
description: Find the page that explains an Adobe Journey Optimizer error code, with its cause and fix, from the family of the error code or the feature
hide: true
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
---
# Troubleshoot error codes {#section-overview}

Find the cause and the fix of an error returned by [!DNL Adobe Journey Optimizer]. Each page groups the errors of one feature, with the exact error message, the cause, and how to fix it. Use the family of the error code to open the right page, or go directly to the section that matches where the error occurs.

## Read an error code {#read-error-code}

An error code has a prefix that identifies the service, an error number, and an HTTP status. For example, `AJOJAS-2030-400` is a journey validation error (prefix AJOJAS), number 2030, status 400. A code with the status 200 is a warning: it does not block saving or publishing.

For the structure of error codes and the steps to take before you contact support, see the [error codes reference](../using/building-journeys/error-codes-reference.md).

## Find your error by family {#find-error}

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

Journeys

Prefix AJOJAS. Errors raised when you validate, test or publish a journey.

* [Journey validation errors](../using/building-journeys/journey-validation-errors.md)
    * [Journey structure](../using/building-journeys/journey-validation-errors.md#structure)
    * [Action activities](../using/building-journeys/journey-validation-errors.md#actions)
    * [Events and reactions](../using/building-journeys/journey-validation-errors.md#events)
    * [License package limits (Select)](../using/building-journeys/journey-validation-errors.md#select-package)
    * [Versions, test mode, and size](../using/building-journeys/journey-validation-errors.md#versions)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

Campaigns and audiences

Prefixes CJMCMP, CJMOC, CJMDMS and CJMRT 15xxxx and 17xxxx. Errors on Action, API-triggered and Orchestrated campaigns, on relational schemas and datasets, and on audience composition.

* [Campaign errors](../using/campaigns/campaign-errors.md)
    * [Audience](../using/campaigns/campaign-errors.md#audience)
    * [Schedule and approval](../using/campaigns/campaign-errors.md#schedule)
    * [Rapid delivery](../using/campaigns/campaign-errors.md#rapid)
* [Orchestrated campaign errors](../using/orchestrated/orchestrated-campaign-errors.md)
    * [Campaign status and lifecycle](../using/orchestrated/orchestrated-campaign-errors.md#status)
    * [Activities](../using/orchestrated/orchestrated-campaign-errors.md#activities)
    * [Signals and chained campaigns](../using/orchestrated/orchestrated-campaign-errors.md#signal)
* [Relational schema and dataset errors](../using/orchestrated/relational-schema-errors.md)
    * [Files and formats](../using/orchestrated/relational-schema-errors.md#files)
    * [Primary key and version descriptor](../using/orchestrated/relational-schema-errors.md#keys)
    * [Relationships](../using/orchestrated/relational-schema-errors.md#relationships)
* [Audience composition errors](../using/audience/audience-composition-errors.md)
    * [Enrichment](../using/audience/audience-composition-errors.md#enrichment)
    * [Publication, limits, and permissions](../using/audience/audience-composition-errors.md#publication)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/pencil-alt.svg)

Content authoring and personalization

Prefixes CJMMAS 10xx and 2xxx, CJMRT 030xxx, CJMTL, JOMAL, CJMPTS, AJOTDS and CJMSAS. Errors on the content of messages, on expressions and helpers, and on proofs and simulated users.

* [Content authoring errors](../using/content-management/content-authoring-errors.md)
    * [Email content](../using/content-management/content-authoring-errors.md#email)
    * [Push notifications](../using/content-management/content-authoring-errors.md#push)
    * [Message lifecycle and saving](../using/content-management/content-authoring-errors.md#lifecycle)
    * [Permissions](../using/content-management/content-authoring-errors.md#permissions)
* [Personalization errors](../using/personalization/personalization-errors.md)
    * [Variables and paths](../using/personalization/personalization-errors.md#variables)
    * [Helpers](../using/personalization/personalization-errors.md#helpers)
    * [URL parameter encryption keys](../using/personalization/personalization-errors.md#encryption)
* [Proof and simulation errors](../using/content-management/proof-simulation-errors.md)
    * [Proofs and previews](../using/content-management/proof-simulation-errors.md#proofs)
    * [Simulated users](../using/content-management/proof-simulation-errors.md#simulated-users)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/file-alt.svg)

Fragments, multilingual content and landing pages

Prefixes CJMMAS 11xx to 17xx, 3xxx, 51xx and 81xx, AJOCBS, AJOAGS, AJOCTO and CJMRT 0809xx. Errors on fragments and AEM content, translation, and landing pages.

* [Fragments and AEM content errors](../using/content-management/fragments-errors.md)
    * [Publishing fragments](../using/content-management/fragments-errors.md#publication)
    * [AEM content fragments](../using/content-management/fragments-errors.md#aem-fragments)
    * [AEM assets](../using/content-management/fragments-errors.md#aem-assets)
* [Multilingual content errors](../using/content-management/multilingual-errors.md)
    * [Language settings](../using/content-management/multilingual-errors.md#language-settings)
    * [Translation projects](../using/content-management/multilingual-errors.md#translation-project)
* [Landing page errors](../using/landing-pages/landing-page-errors.md)
    * [Publication and status](../using/landing-pages/landing-page-errors.md#publication)
    * [Forms and subscription lists](../using/landing-pages/landing-page-errors.md#forms)
    * [Expiration](../using/landing-pages/landing-page-errors.md#expiration)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

Deliverability setup

Prefixes CJMRT 0806xx, 0808xx and 18xxxx. Errors on subdomain delegation, DNS records, seed lists and IP warmup plans.

* [Subdomain delegation and DNS errors](../using/configuration/subdomain-delegation-errors.md)
    * [Subdomain delegation](../using/configuration/subdomain-delegation-errors.md#delegation)
    * [DNS records](../using/configuration/subdomain-delegation-errors.md#dns)
    * [Seed lists](../using/configuration/subdomain-delegation-errors.md#seed)
* [IP warmup plan errors](../using/configuration/ip-warmup-plan-errors.md)
    * [Plan file](../using/configuration/ip-warmup-plan-errors.md#file)
    * [Runs and activation](../using/configuration/ip-warmup-plan-errors.md#runs)
    * [Run failures](../using/configuration/ip-warmup-plan-errors.md#failures)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Custom channels, inbound actions and reporting

Prefixes CJMIAS, CJMRPS and CJMRT 0817xx. Errors on custom channel credentials, inbound actions and reporting datasets.

* [Custom channel, inbound action, and reporting dataset errors](../using/configuration/channel-reporting-errors.md)
    * [Custom channels](../using/configuration/channel-reporting-errors.md#custom-channel)
    * [Inbound actions](../using/configuration/channel-reporting-errors.md#inbound)
    * [Reporting datasets](../using/configuration/channel-reporting-errors.md#reporting)
:::

::::

## Error code prefixes by feature {#prefixes}

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

## If your error is not listed {#not-listed}

* Check the other troubleshooting guides: [Troubleshoot journey errors](../using/building-journeys/troubleshooting.md), [Troubleshoot journey execution](../using/building-journeys/troubleshooting-execution.md), and [Troubleshoot inbound actions](../using/building-journeys/troubleshooting-inbound.md).
* Look for the code in the [error codes reference](../using/building-journeys/error-codes-reference.md).
* If the error persists, [contact Adobe Support](../using/start/user-interface.md#support-ticket-guidelines) with the complete error code and the request ID.
