---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what the errors returned when you delegate a subdomain, create DNS records, set up web or landing page subdomains, create a channel configuration, or manage seed lists mean, and how to fix each family of errors.

**Intents:**

* Find the cause and the fix for a CJMRT error returned during subdomain delegation
* Identify which DNS record (name server, ownership validation, MX, DMARC, forward DNS, Google verification) is missing or not correct
* Fix errors when setting a subdomain for the web channel or for landing pages
* Fix errors when creating or editing an email channel configuration with an IP pool
* Fix errors when creating or deleting a seed list

**Glossary:**

* **CJMRT**: Prefix of the delegation error codes; an error code is the prefix, an error number, and an HTTP status (for example CJMRT-080602-400) *(product-specific)*
* **Delegated subdomain**: Subdomain delegated to Adobe by adding at your DNS provider the name server records displayed in Journey Optimizer *(product-specific)*
* **Ownership validation record**: DNS record with the value displayed in Journey Optimizer; only one must exist *(product-specific)*
* **Channel configuration**: Configuration of a channel; the error messages call it a surface or channel surface *(product-specific)*
* **IP pool**: Pool selected in an email channel configuration; the page names the statuses **[!UICONTROL Processing]** and **[!UICONTROL Success]** *(product-specific)*

**Guardrails:**

* A subdomain is delegated, not the root domain (CJMRT-080601-400).
* Allow 24 to 48 hours for DNS propagation after the name server records are added (CJMRT-080602-400).
* Only one delegation operation can be in progress at a time. Wait until the other subdomain leaves the **[!UICONTROL Processing]** status (CJMRT-080616-403).
* An email-delegated subdomain cannot be used with a custom prefix (CJMRT-080615-400).
* When you delegate a landing page subdomain with **[!UICONTROL Add your own domain]**, only CNAME delegation is available (CJMRT-080632-400).
* A subdomain used to publish web assets must first be delegated for email and have a CDN domain configured. Contact your Adobe representative to configure the CDN domain (CJMRT-080613-400, 080614-400).
* An update of an IP pool can take up to 3 hours (CJMRT-080101-403).
* Profile attributes cannot be added to a channel configuration after it is created (CJMRT-080102-403).

**Terminology:**

* Canonical name: Subdomain delegation — variants: DNS delegation (as in the error messages)
* Do not confuse: "CJMRT-080617-404" (no active DMARC record, a recommendation to add one) ≠ "CJMRT-080618-404" (the DMARC delegation record does not exist, create it then try again)

**FAQ:**

* **Q: How is an error code structured?** — The prefix **CJMRT**, followed by an error number and an HTTP status, for example CJMRT-080602-400.
* **Q: Why does Journey Optimizer say the subdomain is not delegated to Adobe?** — CJMRT-080602-400: the subdomain is not delegated yet. Add the name server records displayed in Journey Optimizer at your DNS provider, allow 24 to 48 hours for DNS propagation, then try again.
* **Q: Why was the domain delegated to wrong server names?** — CJMRT-080603-400: the subdomain points to name servers that are not the Adobe name servers. Correct the records at your DNS provider with the name servers displayed in Journey Optimizer, then restart the delegation.
* **Q: Why can I not delegate a subdomain while another delegation is running?** — CJMRT-080616-403: another delegation is in progress. Wait until the other subdomain leaves the **[!UICONTROL Processing]** status, then submit again.
* **Q: Why can I not create an email channel configuration with my IP pool?** — CJMRT-080101-403: the IP pool is under edition (**[!UICONTROL Processing]** status) and has never been associated with the selected subdomain. Save the channel configuration as a draft, then wait until the IP pool has the **[!UICONTROL Success]** status.
* **Q: Why can I not delete a seed list?** — CJMRT-080801-403: the seed list is associated with at least one channel configuration. Update those channel configurations to remove the seed list, then delete it.

**Troubleshooting:**

* **Subdomain delegation**: CJMRT-080601-400 ("Root level domain should not be delegated."): delegate a subdomain, for example marketing.example.com. CJMRT-080604-400 ("Domain provided is invalid. Please check with domain registrar."): check the domain name with your domain registrar. CJMRT-080609-409 ("The subdomain {subdomain} already exists."): use a different subdomain, or select the existing one.
* **DNS records**: errors when a DNS record that Adobe checks during delegation is missing or not correct.
  * CJMRT-080605-400 ("Please create all required records and then try again"): create all the records listed in Journey Optimizer at your DNS provider.
  * CJMRT-080606-400 ("Multiple ownership validation record found. Please remove extra validation record and try again."): more than one ownership validation record was found. Remove the extra record and keep a single one.
  * CJMRT-080607-400 ("Ownership validation record not matching. Please check validation record and try again."): the ownership validation record does not match. Use the value displayed in Journey Optimizer.
  * CJMRT-080608-400 ("The Google verification record already exists."): a Google verification TXT record already exists for this subdomain; you do not need to add it again.
  * CJMRT-080610-400 ("Please create forward dns first and then try again"): create the forward DNS record first.
  * CJMRT-080612-400: the MX record of the subdomain is missing. Add it at your DNS provider.
  * CJMRT-080617-404 ("This subdomain {subdomain} does not have any active DMARC record. It is recommended to add it."): add a DMARC record to comply with the Google and Yahoo sender requirements.
  * CJMRT-080618-404 ("DMARC delegation record does not exist. Please create it and try again."): create it at your DNS provider.
* **Web and landing page subdomains**: CJMRT-080611-404 (no default web subdomain configured): select a delegated subdomain and use the **[!UICONTROL Set as default]** option. CJMRT-080613-400 (the CDN domain is not configured for this delegated subdomain): contact your Adobe representative to configure the CDN domain. CJMRT-080614-400 (the subdomain is not delegated for email): delegate it first, then contact your Adobe representative to configure the CDN domain. CJMRT-080631-409 ("An email subdomain is already delegated for this subdomain."): select it as an existing subdomain instead of delegating it again.
* **Channel configurations and IP pools**: CJMRT-080101-403 and CJMRT-080102-403: see FAQ and Guardrails. For 080102-403, create a new channel configuration with the attributes you need.
* **Seed lists**: CJMRT-080802-409 ("The seedlist with the name {name} already exists. Please use a different seedlist name and try again."): use a seed list name that does not exist yet. CJMRT-080803-400 ("Please enter a valid seed address."): use a valid seed email address.

**Related pages:**

* Subdomain delegation basics: Get started with subdomain delegation (configuration/about-subdomain-delegation.md)
* Subdomain validation and delegation steps: Delegate a subdomain (configuration/delegate-subdomain.md)
* DMARC record: Set up a DMARC record (configuration/dmarc-record.md)
* Google verification record: Add a Google TXT record to a subdomain (configuration/google-txt.md)
* IP pools: Create IP pools (configuration/ip-pools.md)
* Channel configuration failure reasons and editing: Set up channel configurations (configuration/channel-surfaces.md)
* Seed lists: Seed lists (configuration/seed-lists.md)
* Landing page subdomains: Set up landing page subdomains (landing-pages/lp-subdomains.md)
* Web subdomains: Set up web subdomains (web/web-delegated-subdomains.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: 4148f260 -->
