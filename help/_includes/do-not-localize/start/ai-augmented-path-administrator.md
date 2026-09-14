---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is the System Administrator getting-started path, covering how to set up access and permissions, configure channels and messages, and enable additional governance capabilities so other teams can work in Journey Optimizer.

**Intents:**

* Set up access and permissions using sandboxes, roles, permissions, and object-level access control
* Configure channel settings and message presets for email, SMS, push, web push, and direct mail
* Delegate subdomains, create IP pools, and manage suppression and allowed lists
* Enable additional capabilities such as consent policies, data governance policies, IP warmup plans, and quiet hours
* Collaborate with data engineers, developers, and marketers

**Glossary:**

* **Sandbox**: An isolated virtual environment that partitions instances to separate data and journeys for different user groups *(product-specific)*
* **Role**: A set of unitary rights that allows users access to certain functionalities or objects in the interface *(product-specific)*
* **Permission**: A unitary right that defines the authorizations assigned to a role, gathered under capabilities such as Journey or Offers *(product-specific)*
* **Object-level access control (OLAC)**: An optional capability that applies access labels to objects such as journeys, campaigns, and channel configurations to control which users can access specific resources *(product-specific)*
* **Allowed list**: A list specifying the only email addresses or domains authorized to receive emails sent from a specific sandbox, which can prevent sending accidentally to real customer addresses in a testing environment *(product-specific)*

**Guardrails:**

* These capabilities can be managed by Product administrators that have access to the Permissions product.
* If you cannot see the Sandboxes or Channels menu, you need to update your permissions in the Permissions product.
* When accessing Journey Optimizer for the first time, you are provisioned a production sandbox and allocated a certain number of IPs depending on your contract.
* Users who need access to Assets Essentials must be added to the Assets Essentials Consumer Users or Assets Essentials Users roles.
* Message export is an add-on offering, enabled at the channel configuration level.
* Consent policies require that your organization has purchased Healthcare Shield or Privacy and Security Shield.

**Terminology:**

* Canonical name: System Administrator — variants: Product administrator, Administrator
* Acronym: OLAC = Object-level access control
* Implementation order: Administrator → Data Engineer → Developer → Marketer (the Administrator sets up the environment first)
* Do not confuse: "suppression list" (email addresses excluded from deliveries) ≠ "allowed list" (the only addresses or domains authorized to receive emails from a sandbox)

**FAQ:**

* **Q: What are the main responsibilities of a System Administrator here?** — Setting up user groups and permissions, creating and managing sandboxes, and configuring delivery channels and message presets.
* **Q: What do I get when I access Journey Optimizer for the first time?** — A production sandbox and a number of IPs allocated depending on your contract.
* **Q: Why can I not see the Sandboxes or Channels menu?** — You need to update your permissions in the Permissions product.
* **Q: What is the difference between the suppression list and the allowed list?** — The suppression list excludes addresses from deliveries to protect sending reputation, while the allowed list restricts sending to only the specified addresses or domains from a sandbox.
* **Q: What additional capabilities can I enable as the organization grows?** — Consent policies, data governance policies, IP warmup plans, and quiet hours.

+++

<!-- ai-section-version: 1 | source-hash: d3c8c8d7 -->
