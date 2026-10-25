---
solution: Journey Optimizer
product: Journey Optimizer
title: Troubleshooting overview
description: Find the right troubleshooting resource for Adobe Journey Optimizer, including the troubleshooting FAQ, the journey troubleshooting guides, and the pages that explain each family of error codes
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
---
# Troubleshooting overview {#section-overview}

Use this section to find the cause of a problem and how to fix it. It brings together the troubleshooting FAQ, the guides for journeys, and one page for each family of error codes. Start from the type of resource you need, or from the error code that you received.

## Troubleshooting FAQ {#faq}

The [troubleshooting FAQ](../using/start/troubleshooting.md) answers frequent questions across [!DNL Journey Optimizer], such as fragments, email content and tracking, and the count of engageable profiles.

## Troubleshoot journeys {#journeys-guides}

* [Troubleshoot journey errors](../using/building-journeys/troubleshooting.md): find and fix the errors that block the test or the publication of a journey.
* [Journey validation errors](../using/building-journeys/journey-validation-errors.md): understand a journey validation error code.
* [Troubleshoot journey execution](../using/building-journeys/troubleshooting-execution.md): find out why profiles do not enter or progress through a live journey.
* [Troubleshoot inbound actions](../using/building-journeys/troubleshooting-inbound.md): debug an inbound action that does not display or continues after a profile exits.
* [Troubleshoot custom actions](../using/action/troubleshoot-custom-action.md): check that a custom action and its API call work.

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

Errors raised when you validate, test or publish a journey.

[View the error pages](../using/building-journeys/journey-validation-errors.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

Campaigns and audiences

Errors on Action, API-triggered and Orchestrated campaigns, on relational schemas and datasets, and on audience composition.

[View the error pages](../using/campaigns/campaign-errors.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/pencil-alt.svg)

Content authoring and personalization

Errors on the content of messages, on expressions and helpers, and on proofs and simulated users.

[View the error pages](../using/content-management/content-authoring-errors.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/file-alt.svg)

Fragments, multilingual content and landing pages

Errors on fragments and AEM content, translation, and landing pages.

[View the error pages](../using/content-management/fragments-errors.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

Deliverability setup

Errors on subdomain delegation, DNS records, seed lists and IP warmup plans.

[View the error pages](../using/configuration/subdomain-delegation-errors.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Custom channels, inbound actions and reporting

Errors on custom channel credentials, inbound actions and reporting datasets.

[View the error pages](../using/configuration/channel-reporting-errors.md)
:::

::::

### Error pages and sections by family {#pages}

Open a family to see its error pages, the prefixes of its error codes, and the sections of each page.

+++**Journeys**

These errors appear when you check, test or publish a journey. Go to the section that matches the activity or setting named in the message.

* [Journey validation errors](../using/building-journeys/journey-validation-errors.md): Journeys: validation before test or publication<br/>Prefixes: AJOJAS<br/>Sections: [Journey structure](../using/building-journeys/journey-validation-errors.md#structure) | [Action activities](../using/building-journeys/journey-validation-errors.md#actions) | [Events and reactions](../using/building-journeys/journey-validation-errors.md#events) | [License package limits (Select)](../using/building-journeys/journey-validation-errors.md#select-package) | [Versions, test mode, and size](../using/building-journeys/journey-validation-errors.md#versions)

+++

+++**Campaigns and audiences**

These errors appear when you set up, schedule or activate an Action, API-triggered or Orchestrated campaign, when you define a relational schema or a dataset, and when you build and publish an audience composition.

* [Campaign errors](../using/campaigns/campaign-errors.md): Action and API-triggered campaigns, including schedules<br/>Prefixes: CJMCMP, CJMRT 15xxxx<br/>Sections: [Audience](../using/campaigns/campaign-errors.md#audience) | [Schedule and approval](../using/campaigns/campaign-errors.md#schedule) | [Rapid delivery](../using/campaigns/campaign-errors.md#rapid)
* [Orchestrated campaign errors](../using/orchestrated/orchestrated-campaign-errors.md): Orchestrated campaigns<br/>Prefixes: CJMOC<br/>Sections: [Campaign status and lifecycle](../using/orchestrated/orchestrated-campaign-errors.md#status) | [Activities](../using/orchestrated/orchestrated-campaign-errors.md#activities) | [Signals and chained campaigns](../using/orchestrated/orchestrated-campaign-errors.md#signal)
* [Relational schema and dataset errors](../using/orchestrated/relational-schema-errors.md): Relational schemas and datasets<br/>Prefixes: CJMDMS<br/>Sections: [Files and formats](../using/orchestrated/relational-schema-errors.md#files) | [Primary key and version descriptor](../using/orchestrated/relational-schema-errors.md#keys) | [Relationships](../using/orchestrated/relational-schema-errors.md#relationships)
* [Audience composition errors](../using/audience/audience-composition-errors.md): Audience composition<br/>Prefixes: CJMRT 17xxxx<br/>Sections: [Enrichment](../using/audience/audience-composition-errors.md#enrichment) | [Publication, limits, and permissions](../using/audience/audience-composition-errors.md#publication)

+++

+++**Content authoring and personalization**

These errors appear when you validate or save the content of a message, when an expression or a helper cannot be resolved, and when you preview a message or use simulated users.

* [Content authoring errors](../using/content-management/content-authoring-errors.md): Content of emails, push notifications, SMS, in-app messages, and direct mail, including message lifecycle and permissions<br/>Prefixes: CJMMAS 10xx and 2xxx, CJMRT 030xxx, JOMAL<br/>Sections: [Email content](../using/content-management/content-authoring-errors.md#email) | [Push notifications](../using/content-management/content-authoring-errors.md#push) | [Message lifecycle and saving](../using/content-management/content-authoring-errors.md#lifecycle) | [Permissions](../using/content-management/content-authoring-errors.md#permissions)
* [Personalization errors](../using/personalization/personalization-errors.md): Personalization expressions, helpers, and URL encryption keys<br/>Prefixes: CJMTL, CJMRT 01xxxx, 07xxxx, 13xxxx, 0816xx<br/>Sections: [Variables and paths](../using/personalization/personalization-errors.md#variables) | [Helpers](../using/personalization/personalization-errors.md#helpers) | [URL parameter encryption keys](../using/personalization/personalization-errors.md#encryption)
* [Proof and simulation errors](../using/content-management/proof-simulation-errors.md): Proofs, previews, and simulated users<br/>Prefixes: CJMPTS, AJOTDS, CJMSAS<br/>Sections: [Proofs and previews](../using/content-management/proof-simulation-errors.md#proofs) | [Simulated users](../using/content-management/proof-simulation-errors.md#simulated-users)

+++

+++**Fragments, multilingual content and landing pages**

These errors appear when you publish a fragment or use AEM content, when you set up language settings and translations, and when you publish or edit a landing page.

* [Fragments and AEM content errors](../using/content-management/fragments-errors.md): Fragments, AEM content fragments, and AEM assets<br/>Prefixes: CJMMAS 11xx to 17xx and 81xx, AJOCBS, AJOAGS<br/>Sections: [Publishing fragments](../using/content-management/fragments-errors.md#publication) | [AEM content fragments](../using/content-management/fragments-errors.md#aem-fragments) | [AEM assets](../using/content-management/fragments-errors.md#aem-assets)
* [Multilingual content errors](../using/content-management/multilingual-errors.md): Multilingual content and translation<br/>Prefixes: CJMMAS 51xx, CJMRT 0809xx, AJOCTO<br/>Sections: [Language settings](../using/content-management/multilingual-errors.md#language-settings) | [Translation projects](../using/content-management/multilingual-errors.md#translation-project)
* [Landing page errors](../using/landing-pages/landing-page-errors.md): Landing pages<br/>Prefixes: CJMMAS 3xxx, 107x, and 130x<br/>Sections: [Publication and status](../using/landing-pages/landing-page-errors.md#publication) | [Forms and subscription lists](../using/landing-pages/landing-page-errors.md#forms) | [Expiration](../using/landing-pages/landing-page-errors.md#expiration)

+++

+++**Deliverability setup**

These errors appear when you delegate a subdomain, create DNS records or seed lists, and when you upload, activate or run an IP warmup plan.

* [Subdomain delegation and DNS errors](../using/configuration/subdomain-delegation-errors.md): Subdomain delegation, DNS records, and seed lists<br/>Prefixes: CJMRT 0806xx and 0808xx<br/>Sections: [Subdomain delegation](../using/configuration/subdomain-delegation-errors.md#delegation) | [DNS records](../using/configuration/subdomain-delegation-errors.md#dns) | [Seed lists](../using/configuration/subdomain-delegation-errors.md#seed)
* [IP warmup plan errors](../using/configuration/ip-warmup-plan-errors.md): IP warmup plans<br/>Prefixes: CJMRT 18xxxx<br/>Sections: [Plan file](../using/configuration/ip-warmup-plan-errors.md#file) | [Runs and activation](../using/configuration/ip-warmup-plan-errors.md#runs) | [Run failures](../using/configuration/ip-warmup-plan-errors.md#failures)

+++

+++**Custom channels, inbound actions and reporting**

These errors appear when you configure custom channel credentials, when an inbound action runs, and when you set up reporting datasets.

* [Custom channel, inbound action, and reporting dataset errors](../using/configuration/channel-reporting-errors.md): Inbound actions, reporting datasets, and custom channel credentials<br/>Prefixes: CJMIAS, CJMRPS, CJMRT 0817xx<br/>Sections: [Custom channels](../using/configuration/channel-reporting-errors.md#custom-channel) | [Inbound actions](../using/configuration/channel-reporting-errors.md#inbound) | [Reporting datasets](../using/configuration/channel-reporting-errors.md#reporting)

+++

## If your problem is not listed {#not-listed}

* Look for the error code in the [error codes reference](../using/building-journeys/error-codes-reference.md).
* Check the [troubleshooting FAQ](../using/start/troubleshooting.md) and the journey guides above.
* If the problem persists, [contact Adobe Support](../using/start/user-interface.md#support-ticket-guidelines) with the complete error code and the request ID.
