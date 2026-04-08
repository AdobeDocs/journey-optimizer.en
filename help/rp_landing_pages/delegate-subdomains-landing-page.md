---
solution: Journey Optimizer
product: Journey Optimizer
title: Delegate email subdomains
description: Delegate email subdomains
redpen-status: CREATED_||_2025-08-11_21-07-51
exl-id: 7df9b8e2-136a-4ffc-9243-53c7be026d81
---
# Delegate email subdomains{#section-overview}

Delegating email subdomains is a core step in [channel configuration](../using/configuration/get-started-configuration.md)—required before you can send emails from Journey Optimizer. Subdomains let you isolate traffic types (e.g., marketing vs. transactional), protect your main domain's reputation, and speed up [IP warmup](../using/configuration/ip-warmup-gs.md). They work alongside [email channel configuration](../using/email/get-started-email-config.md) and [deliverability monitoring](../using/reports/deliverability.md) to ensure messages reach inboxes.

You can choose from several setup methods: **full delegation** (Adobe manages DNS), **CNAME setup**, or **custom delegation** (you own certificates and DNS). If you start with CNAME, you can later [migrate to custom delegation](../using/configuration/custom-subdomain-migration.md) for stricter security. This section also covers DMARC and PTR records, Google TXT records for Gmail, and IP pools. For broader deliverability guidance, see [Get started with deliverability](../using/reports/deliverability.md) and [Monitor email addresses](monitor-reputation-landing-page.md).

## Delegate Email Subdomains

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

Get Started with Subdomain Delegation

Learn the benefits, configuration methods, and considerations for delegating subdomains in Adobe Journey Optimizer.

[Start Delegating Subdomains](../using/configuration/about-subdomain-delegation.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

Delegate a Subdomain

Step-by-step guidance for delegating subdomains to Adobe, including full delegation and CNAME setup.

[Learn How to Delegate](../using/configuration/delegate-subdomain.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/screwdriver-wrench.svg)

Set Up a Custom Subdomain

Take full ownership of your subdomains with custom delegation—upload your own SSL certificates and maintain full control over domain configuration.

[Set up a custom subdomain](../using/configuration/delegate-custom-subdomain.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/chart-line.svg)

Migrate from CNAME to Custom Delegation

Migrate existing CNAME-configured subdomains to custom delegation to meet security policies and gain full control over certificates.

[Migrate your subdomain](../using/configuration/custom-subdomain-migration.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/shield-halved.svg)

Set Up DMARC Records

Configure DMARC records to enhance email security and deliverability for delegated subdomains.

[Set Up DMARC Now](../using/configuration/dmarc-record.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg)

Add a Google TXT Record

Verify subdomains for Gmail deliverability by adding Google TXT records in Adobe Journey Optimizer.

[Add Google TXT Records](../using/configuration/google-txt.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Access & Edit PTR Records

Manage PTR records for delegated subdomains, including editing and understanding update statuses.

[Edit PTR Records](../using/configuration/ptr-records.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

Create IP Pools

Group IP addresses for improved email deliverability and manage subdomain reputation effectively.

[Create IP Pools](../using/configuration/ip-pools.md)
:::

::::

## Additional resources

- **[Configure landing page subdomains](../using/landing-pages/lp-subdomains.md)** - Set up subdomains for landing pages and subscription forms.
- **[Configure web subdomains](../using/web/web-delegated-subdomains.md)** - Delegate subdomains for web experiences and tracking.
- **[Get started with channels configuration](../using/configuration/get-started-configuration.md)** - Overview of all channel setup steps, including subdomain delegation.
