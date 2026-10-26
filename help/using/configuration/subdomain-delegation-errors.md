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

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Subdomain delegation {#delegation}

These errors occur when you delegate a subdomain to Adobe.

See also [Get started with subdomain delegation](about-subdomain-delegation.md) and [Subdomain validation](delegate-subdomain.md#subdomain-validation).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080601-400** | Root level domain should not be delegated. | Enter a subdomain of your domain, for example marketing.example.com, as the name of the subdomain to delegate. [Learn more](delegate-subdomain.md) |
| **CJMRT-080602-400** | Domain Name Server (DNS) has not been delegated to Adobe. Please delegate it and try again. | Add the name server records displayed in the **[!UICONTROL DNS record]** section at your DNS provider. Allow 24 to 48 hours for DNS propagation, then delegate the subdomain again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080603-400** | Domain has been delegated to wrong server names. Please restart the DNS delegation process with Adobe. | At your DNS provider, replace the name server records of the subdomain with the ones displayed in [!DNL Journey Optimizer], then restart the delegation. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080604-400** | Domain provided is invalid. Please check with domain registrar. | Check the domain name with your domain registrar, then enter the subdomain name again. [Learn more](delegate-subdomain.md) |
| **CJMRT-080609-409** | The subdomain {subdomain} already exists. | Enter a different subdomain name, or select the existing subdomain in the **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL Subdomains]** list. [Learn more](delegate-subdomain.md#access-delegated-subdomains) |
| **CJMRT-080616-403** | A domain delegation operation is already in progress. Please wait until that is completed, and try again. | In the **[!UICONTROL Subdomains]** list, wait until the other subdomain leaves the **[!UICONTROL Processing]** status, then submit again. [Learn more](delegate-subdomain.md#guardrails) |

## DNS records {#dns}

These errors occur when a DNS record that Adobe checks during delegation is missing or not correct.

See also [Subdomain validation](delegate-subdomain.md#subdomain-validation) and [Channel configuration failure reasons](channel-surfaces.md#channel-config-failure).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080605-400** | Please create all required records and then try again | Create all the records listed in the **[!UICONTROL DNS record]** section at your DNS provider, then submit the subdomain again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080606-400** | Multiple ownership validation record found. Please remove extra validation record and try again. | At your DNS provider, delete the extra ownership validation record so that only one remains. [Learn more](delegate-subdomain.md#subdomain-validation) |
| **CJMRT-080607-400** | Ownership validation record not matching. Please check validation record and try again. | At your DNS provider, replace the ownership validation record with the value displayed in [!DNL Journey Optimizer]. [Learn more](delegate-subdomain.md#subdomain-validation) |
| **CJMRT-080608-400** | The Google verification record already exists. | Keep the existing record. To change it, open the subdomain, clear the **[!UICONTROL Google txt record]** field and save, then reopen the subdomain, enter the new verification code and save again. [Learn more](google-txt.md) |
| **CJMRT-080610-400** | Please create forward dns first and then try again | Create the forward DNS record at your DNS provider first, then submit the subdomain again. [Learn more](delegate-subdomain.md#set-up-subdomain) |
| **CJMRT-080612-400** | The MX record for the subdomain of {emailField} is missing. Please configure it and try again. | Add the MX record of the subdomain at your DNS provider, then create the channel configuration again. If the error persists, contact Adobe Customer Care. [Learn more](channel-surfaces.md#channel-config-failure) |
| **CJMRT-080617-404** | This subdomain {subdomain} does not have any active DMARC record. It is recommended to add it. | Set up a DMARC record for the subdomain in the **[!UICONTROL DMARC record]** section to comply with the Google and Yahoo sender requirements. [Learn more](dmarc-record.md) |
| **CJMRT-080618-404** | DMARC delegation record does not exist. Please create it and try again. | Create the DMARC delegation record at your DNS provider, allow time for DNS propagation (up to 48 hours), then try again. [Learn more](dmarc-record.md) |

## Web and landing page subdomains {#web-lp}

These errors occur when you set up a subdomain for the web channel or for landing pages.

See also [Set up landing page subdomains](../landing-pages/lp-subdomains.md) and [Set up web subdomains](../web/web-delegated-subdomains.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080611-404** | There is no default web subdomain configured. Please configure a web subdomain, so the web assets used are published with the desired domain. | In the web subdomains list, select **[!UICONTROL More actions]** > **[!UICONTROL Set as default]** next to a delegated subdomain in the **[!UICONTROL Success]** status. [Learn more](../web/web-delegated-subdomains.md) |
| **CJMRT-080613-400** | The selected delegated subdomain cannot be used for assets publishing as the CDN domain has not been configured. Contact your Adobe representative to have your configuration updated. | Contact your Adobe representative to have the CDN domain configured for this delegated subdomain. [Learn more](../web/web-delegated-subdomains.md) |
| **CJMRT-080614-400** | The selected subdomain is not email delegated. In order to use it as a web subdomain, it needs to be first delegated and have a CDN domain configured. | Delegate the subdomain for email first, then contact your Adobe representative to configure its CDN domain. [Learn more](../web/web-delegated-subdomains.md) |
| **CJMRT-080615-400** | You cannot use a custom prefix with the email delegated subdomain. Please provide a valid prefix and try again. | Enter a prefix that uses only alpha-numeric characters and hyphens, and is not a reserved prefix such as `cdn` or `data`. [Learn more](../landing-pages/lp-subdomains.md) |
| **CJMRT-080631-409** | An email subdomain is already delegated for this subdomain. | Select the existing subdomain with the **[!UICONTROL Use delegated domain]** configuration type instead of delegating it again. [Learn more](../landing-pages/lp-subdomains.md) |
| **CJMRT-080632-400** | When delegating a landing page subdomain via 'Add your own domain', only the CNAME delegation type is allowed. | In the **[!UICONTROL Configuration type]** section, select the CNAME delegation type. [Learn more](../landing-pages/lp-subdomains.md) |

## Channel configurations and IP pools {#config}

These errors occur when you create or edit an email channel configuration.

See also [Channel configuration failure reasons](channel-surfaces.md#channel-config-failure).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080101-403** | You cannot create an Email surface while the selected IP pool is under edition (Processing status) and has never been associated with the selected subdomain. Save the surface as draft and wait until the IP pool has the Success status to resume Email surface creation using the selected IP pool. | Save the channel configuration as a draft, then resume its creation once the IP pool has the **[!UICONTROL Success]** status. An update can take up to 3 hours. [Learn more](ip-pools.md) |
| **CJMRT-080102-403** | Once a surface has been created, new profile attributes cannot be added when editing this surface. | Create a new channel configuration that includes the attributes you need. [Learn more](channel-surfaces.md#edit-channel-surface) |

## Seed lists {#seed}

These errors occur when you create or delete a seed list.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-080801-403** | The seed list with name: {name} cannot be deleted as it is associated with at least one channel surface. Please update the surface(s) and try again. | Remove the seed list from the channel configurations that use it, and from any active campaign or journey that uses it, then delete it. [Learn more](seed-lists.md) |
| **CJMRT-080802-409** | The seedlist with the name {name} already exists. Please use a different seedlist name and try again. | Enter a seed list name that is not used yet. Names must begin with a letter and include only alpha-numeric characters or the special characters `_`, `.` and `-`. [Learn more](seed-lists.md#create-seed-list) |
| **CJMRT-080803-400** | Please enter a valid seed address. | Correct the seed addresses so that each one is a valid email address, whether you enter them manually or import a CSV file. [Learn more](seed-lists.md#create-seed-list) |

## Related topics {#related}

* [Get started with subdomain delegation](about-subdomain-delegation.md)
* [Delegate a subdomain](delegate-subdomain.md)
* [Set up a DMARC record](dmarc-record.md)
* [Create IP pools](ip-pools.md)
* [Set up channel configurations](channel-surfaces.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-subdomain-delegation-errors.md}}
