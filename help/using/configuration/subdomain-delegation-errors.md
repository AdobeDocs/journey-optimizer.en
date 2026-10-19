---
solution: Journey Optimizer
product: journey optimizer
title: Subdomain delegation and DNS errors
description: Learn what common errors mean when you delegate subdomains, set up DNS records, and configure email channels in Adobe Journey Optimizer, and how to fix them
feature: Subdomains, Deliverability
topic: Administration
role: Admin
level: Experienced
keywords: error, troubleshooting, subdomain, delegation, DNS, DMARC, seed list
---
# Subdomain delegation and DNS errors {#subdomain-delegation-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you delegate a subdomain, create DNS records, create a channel configuration, or manage seed lists.

>[!ENDSHADEBOX]

Delegation errors use the prefix **CJMRT**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Subdomain delegation {#delegation}

These errors occur when you delegate a subdomain to Adobe.

See also [Get started with subdomain delegation](about-subdomain-delegation.md) and [Subdomain validation](delegate-subdomain.md#subdomain-validation).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080601-400** | Root level domain should not be delegated. | Delegate a subdomain (for example marketing.example.com), not the root domain. [Learn more](delegate-subdomain.md) |
| **CJMRT-080602-400** | Domain Name Server (DNS) has not been delegated to Adobe. Please delegate it and try again. | The subdomain is not delegated to Adobe yet. Add the name server records displayed in Journey Optimizer at your DNS provider. Allow 24 to 48 hours for DNS propagation, then try again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080603-400** | Domain has been delegated to wrong server names. Please restart the DNS delegation process with Adobe. | The subdomain points to name servers that are not the Adobe name servers. Correct the records at your DNS provider with the name servers displayed in Journey Optimizer, then restart the delegation. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080604-400** | Domain provided is invalid. Please check with domain registrar. | The domain is not valid. Check the domain name with your domain registrar. [Learn more](delegate-subdomain.md) |
| **CJMRT-080609-409** | The subdomain {subdomain} already exists. | This subdomain already exists. Use a different subdomain, or select the existing one. [Learn more](delegate-subdomain.md#access-delegated-subdomains) |
| **CJMRT-080616-403** | A domain delegation operation is already in progress. Please wait until that is completed, and try again. | Another delegation is in progress. Wait until the other subdomain leaves the **[!UICONTROL Processing]** status, then submit again. [Learn more](delegate-subdomain.md#guardrails) |

## DNS records {#dns}

These errors occur when a DNS record that Adobe checks during delegation is missing or not correct.

See also [Subdomain validation](delegate-subdomain.md#subdomain-validation) and [Channel configuration failure reasons](channel-surfaces.md#channel-config-failure).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080605-400** | Please create all required records and then try again | A required DNS record is missing. Create all the records listed in Journey Optimizer at your DNS provider, then try again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080606-400**, **080607-400** | Multiple ownership validation record found. Please remove extra validation record and try again.<br/>Ownership validation record not matching. Please check validation record and try again. | The ownership validation record is duplicated or does not match. Keep a single ownership validation record, with the value displayed in Journey Optimizer. [Learn more](delegate-subdomain.md#subdomain-validation) |
| **CJMRT-080608-400** | The Google verification record already exists. | A Google verification TXT record already exists for this subdomain. You do not need to add it again. [Learn more](google-txt.md) |
| **CJMRT-080610-400** | Please create forward dns first and then try again | Create the forward DNS record first, then try again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080612-400** | The MX record for the subdomain of {emailField} is missing. Please configure it and try again. | The MX record of the subdomain is missing. Add it at your DNS provider, then try again. [Learn more](channel-surfaces.md#channel-config-failure) |
| **CJMRT-080617-404** | This subdomain {subdomain} does not have any active DMARC record. It is recommended to add it. | The subdomain has no active DMARC record. Add one to comply with the Google and Yahoo sender requirements. [Learn more](dmarc-record.md) |
| **CJMRT-080618-404** | DMARC delegation record does not exist. Please create it and try again. | The DMARC delegation record does not exist. Create it at your DNS provider, then try again. [Learn more](dmarc-record.md) |

## Web and landing page subdomains {#web-lp}

These errors occur when you set up a subdomain for the web channel or for landing pages.

See also [Set up landing page subdomains](../landing-pages/lp-subdomains.md) and [Set up web subdomains](../web/web-delegated-subdomains.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080611-404** | There is no default web subdomain configured. Please configure a web subdomain, so the web assets used are published with the desired domain. | Set a default web subdomain. Select a delegated subdomain and use the **[!UICONTROL Set as default]** option. [Learn more](../web/web-delegated-subdomains.md) |
| **CJMRT-080613-400**, **080614-400** | The selected delegated subdomain cannot be used for assets publishing as the CDN domain has not been configured. Contact your Adobe representative to have your configuration updated.<br/>The selected subdomain is not email delegated. In order to use it as a web subdomain, it needs to be first delegated and have a CDN domain configured. | The subdomain cannot be used to publish web assets: it must first be delegated for email and have a CDN domain configured. Delegate it, then contact your Adobe representative to configure the CDN domain. [Learn more](../web/web-delegated-subdomains.md) |
| **CJMRT-080615-400** | You cannot use a custom prefix with the email delegated subdomain. Please provide a valid prefix and try again. | A custom prefix cannot be used with an email-delegated subdomain. Enter a valid prefix. [Learn more](../landing-pages/lp-subdomains.md) |
| **CJMRT-080631-409** | An email subdomain is already delegated for this subdomain. | An email subdomain is already delegated for this subdomain. Select it as an existing subdomain instead of delegating it again. [Learn more](../landing-pages/lp-subdomains.md) |
| **CJMRT-080632-400** | When delegating a landing page subdomain via 'Add your own domain', only the CNAME delegation type is allowed. | When you delegate a landing page subdomain with **[!UICONTROL Add your own domain]**, only CNAME delegation is available. Select CNAME. [Learn more](../landing-pages/lp-subdomains.md) |

## Channel configurations and IP pools {#config}

These errors occur when you create or edit an email channel configuration.

See also [Channel configuration failure reasons](channel-surfaces.md#channel-config-failure).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080101-403** | You cannot create an Email surface while the selected IP pool is under edition (Processing status) and has never been associated with the selected subdomain. Save the surface as draft and wait until the IP pool has the Success status to resume Email surface creation using the selected IP pool. | The IP pool is still being edited (**[!UICONTROL Processing]** status) and was never associated with this subdomain. Save the channel configuration as a draft, then wait until the IP pool has the **[!UICONTROL Success]** status. An update can take up to 3 hours. [Learn more](ip-pools.md) |
| **CJMRT-080102-403** | Once a surface has been created, new profile attributes cannot be added when editing this surface. | Profile attributes cannot be added to a channel configuration after it is created. Create a new channel configuration with the attributes you need. [Learn more](channel-surfaces.md#edit-channel-surface) |

## Seed lists {#seed}

These errors occur when you create or delete a seed list.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080801-403** | The seed list with name: {name} cannot be deleted as it is associated with at least one channel surface. Please update the surface(s) and try again. | The seed list is used by at least one channel configuration. Update those channel configurations to remove the seed list, then delete it. [Learn more](seed-lists.md) |
| **CJMRT-080802-409**, **080803-400** | The seedlist with the name {name} already exists. Please use a different seedlist name and try again.<br/>Please enter a valid seed address. | Use a seed list name that does not exist yet, and a valid seed email address. [Learn more](seed-lists.md#create-seed-list) |

## Related topics {#related}

* [Get started with subdomain delegation](about-subdomain-delegation.md)
* [Delegate a subdomain](delegate-subdomain.md)
* [Set up a DMARC record](dmarc-record.md)
* [Create IP pools](ip-pools.md)
* [Set up channel configurations](channel-surfaces.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-subdomain-delegation-errors.md}}
