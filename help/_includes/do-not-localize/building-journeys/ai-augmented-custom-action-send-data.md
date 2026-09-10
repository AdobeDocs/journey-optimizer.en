---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through a journey-based IP warming use case that gradually ramps up email delivery volume using a Profile cap condition to protect sender reputation.

**Intents:**

* Build an IP warming journey to gradually increase email send volume
* Configure a Profile cap condition to limit the number of recipients per delivery
* Add an Email action activity to the nominal journey path
* Remove the profile cap condition once IP warming is complete

**Glossary:**

* **IP warming**: The process of gradually increasing email send volume from a new IP address to establish sender reputation *(product-specific)*
* **Profile cap**: A condition type in Journey Optimizer that limits the maximum number of profiles that can take a specific journey path *(product-specific)*
* **Nominal path**: The primary branch of a journey that profiles follow when conditions are met *(product-specific)*

**Guardrails:**

* A Profile cap condition must be set on the Condition activity to control delivery volume during IP warming.
* Profiles exceeding the cap limit are routed to the alternate path.
* The journey must be recreated or modified after IP warming is complete to remove the cap condition.

**Terminology:**

* Canonical name: IP warming — Acronym: n/a — variants: IP warm-up, sender reputation warm-up
* Synonyms: "Profile cap" = "recipient limit condition"
* Do not confuse: "IP warming" ≠ "email authentication" (SPF/DKIM/DMARC setup is separate)

**FAQ:**

* **Q: Why do I need to warm up my IP?** — New IP addresses have no sending history, so mailbox providers may block or spam-folder messages until reputation is established.
* **Q: What happens to profiles that exceed the profile cap?** — They take the alternate path defined in the Condition activity.
* **Q: How do I increase the cap over time?** — Edit the Limit field in the Condition activity settings and gradually raise it up to your total subscriber count.
* **Q: When can I remove the profile cap condition?** — Once your IP has sufficient sending history and deliverability metrics are stable, you can remove the condition from the journey.

+++
