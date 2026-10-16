---
solution: Journey Optimizer
product: Journey Optimizer
title: Errors by feature area
description: Find the page that explains an Adobe Journey Optimizer error code, with its cause and fix, from the error code prefix or the feature
hide: true
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
---
# Errors by feature area {#section-overview}

>[!BEGINSHADEBOX]

**Purpose:** Find the cause and the fix of an error returned by [!DNL Adobe Journey Optimizer]  
**Primary users:** Campaign managers, journey designers, content creators, and administrators  
**Key outcome:** Resolve an error without contacting support

>[!ENDSHADEBOX]

Each page of this section groups the errors of one feature, with the exact error message, the cause, and how to fix it. Use the error code prefix or the feature to find the right page.

## Read an error code {#read-error-code}

An error code has a prefix that identifies the service, an error number, and an HTTP status. For example, `AJOJAS-2030-400` is a journey validation error (prefix AJOJAS), number 2030, status 400. A code with the status 200 is a warning: it does not block saving or publishing.

For the structure of error codes and the steps to take before you contact support, see the [error codes reference](../using/building-journeys/error-codes-reference.md).

## Find your error {#find-error}

| Error code prefix | Feature | Page |
| --- | --- | --- |
| AJOJAS | Journeys: validation before test or publication | [Journey validation errors](../using/building-journeys/journey-validation-errors.md) |
| CJMCMP | Action and API-triggered campaigns | [Campaign errors](../using/campaigns/campaign-errors.md) |
| CJMOC | Orchestrated campaigns | [Orchestrated campaign errors](../using/orchestrated/orchestrated-campaign-errors.md) |
| CJMDMS | Relational schemas and datasets | [Relational schema and dataset errors](../using/orchestrated/relational-schema-errors.md) |
| CJMRT 17xxxx | Audience composition | [Audience composition errors](../using/audience/audience-composition-errors.md) |
| CJMMAS 2xxx, CJMRT 030xxx | Content of emails, push notifications, SMS, in-app messages, and direct mail | [Content authoring errors](../using/content-management/content-authoring-errors.md) |
| CJMMAS 11xx to 17xx and 81xx, AJOCBS, AJOAGS | Fragments, AEM content fragments, and AEM assets | [Fragments and AEM content errors](../using/content-management/fragments-errors.md) |
| CJMMAS 51xx, CJMRT 0809xx, AJOCTO | Multilingual content and translation | [Multilingual content errors](../using/content-management/multilingual-errors.md) |
| CJMMAS 3xxx, 107x, and 130x | Landing pages | [Landing page errors](../using/landing-pages/landing-page-errors.md) |
| CJMPTS, AJOTDS, CJMSAS | Proofs, previews, and simulated users | [Proof and simulation errors](../using/content-management/proof-simulation-errors.md) |
| CJMRT 0806xx and 0808xx | Subdomain delegation, DNS records, and seed lists | [Subdomain delegation and DNS errors](../using/configuration/subdomain-delegation-errors.md) |
| CJMRT 18xxxx | IP warmup plans | [IP warmup plan errors](../using/configuration/ip-warmup-plan-errors.md) |
| CJMIAS, CJMRPS, CJMRT 0817xx | Inbound actions, reporting datasets, and custom channel credentials | [Custom channel, inbound action, and reporting dataset errors](../using/configuration/channel-reporting-errors.md) |

## If your error is not listed {#not-listed}

* Check the other troubleshooting guides: [Troubleshoot journey errors](../using/building-journeys/troubleshooting.md), [Troubleshoot journey execution](../using/building-journeys/troubleshooting-execution.md), and [Troubleshoot inbound actions](../using/building-journeys/troubleshooting-inbound.md).
* Look for the code in the [error codes reference](../using/building-journeys/error-codes-reference.md).
* If the error persists, [contact Adobe Support](../using/start/user-interface.md#support-ticket-guidelines) with the complete error code and the request ID.
