---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the implementation, visual authoring, delivery, and reporting prerequisites and guardrails required to access, author, deliver, and report on web experiences in Journey Optimizer.

**Intents:**

* Understand the supported implementation types for the web channel
* Install the browser extension required to author in the web designer
* Troubleshoot a website that fails to load in the web designer
* Define the Adobe Experience Platform settings needed for correct web delivery
* Configure datasets and field groups so web data appears in reporting
* Understand the Engageable Profiles cost implications of web campaigns

**Glossary:**

* **Client-side only implementation**: Implementation that adds modifications by implementing the Adobe Experience Platform Web SDK on your website *(product-specific)*
* **Hybrid mode**: Implementation that uses the AEP Edge Network Server API to request personalization server-side, with the response rendered client-side by the Web SDK *(product-specific)*
* **Adobe Experience Cloud Visual Editing Helper**: The browser extension required to open, author, and preview web pages reliably in the web designer *(product-specific)*
* **Active-On-Edge Merge Policy**: A merge policy option that must be enabled so inbound channels activate and publish inbound campaigns on the edge *(product-specific)*
* **Edge Delivery**: A view within Adobe Experience Platform Assurance used to troubleshoot delivery of web experiences *(product-specific)*
* **Engageable Profiles**: The count increased when web campaigns target new profiles not previously engaged on other channels, with possible cost implications *(product-specific)*

**Guardrails:**

* Server-side only implementation is not currently supported with the Web channel; use the Code-based experience channel instead.
* For client-side only implementation, the Adobe Experience Platform Web SDK version must be 2.16 or above.
* Google Chrome and Microsoft Edge are currently the only browsers that support authoring web pages in Journey Optimizer.
* To access the web designer, the Adobe Experience Cloud Visual Editing Helper browser extension must be installed.
* Third-party cookies must be allowed in your browser, otherwise the web page cannot be loaded inside the web designer.
* Some websites might not open reliably in the web designer if they have strict security policies, are in an iframe, or are internal (QA/stage sites not available to the outside world).
* For delivery, a datastream must be defined with the Adobe Journey Optimizer option enabled under the Adobe Experience Platform service, and one merge policy must have the Active-On-Edge Merge Policy option enabled.
* For reporting, the dataset used in your web datastream must be included in your reporting configuration; otherwise web data will not display in your reports.
* If you are not using the AEP Web SDK ExperienceEvent and Consumer Experience Event field groups, add the Experience Event - Proposition Interactions, Application Details, Commerce Details, and Web Details field groups.
* Web campaigns target new profiles not previously engaged on other channels, which increases the Engageable Profiles count and may have cost implications if the contractual number purchased is exceeded.
* When targeting pseudonymous profiles (unauthenticated visitors), consider setting a Time-To-Live (TTL) for automatic profile deletion to manage the engageable profile count and associated costs.

**Terminology:**

* Canonical name: Web channel prerequisites and guardrails — Acronym: n/a — variants: web prerequisites
* Synonyms: "Adobe Experience Cloud Visual Editing Helper" = "Visual Editing Helper browser extension"
* Do not confuse: "Client-side only" ≠ "Hybrid mode" ≠ "Server-side only" (server-side only is not supported with the Web channel)
* Do not confuse: "pseudonymous profiles" (unauthenticated visitors) ≠ "new profiles" (profiles not previously engaged on other channels)

**FAQ:**

* **Q: Which implementation types are supported for the web channel?** — Client-side only (Adobe Experience Platform Web SDK) and Hybrid mode; server-side only is not currently supported and you should use the Code-based experience channel instead.
* **Q: Which Web SDK version is required?** — Version 2.16 or above for a client-side only implementation.
* **Q: Which browsers support web authoring?** — Google Chrome and Microsoft Edge are currently the only browsers that support authoring web pages in Journey Optimizer.
* **Q: Why won't my website load in the web designer?** — Ensure the Visual Editing Helper extension is installed and that third-party cookies are allowed; some sites also fail due to strict security policies, iframes, or being internal.
* **Q: Why is web data missing from my reports?** — The dataset used in your web datastream must be included in your reporting configuration, and the required field groups must be present.
* **Q: Do web campaigns affect my Engageable Profiles count?** — Yes, they target new profiles not previously engaged on other channels, increasing the Engageable Profiles count with possible cost implications if your contractual number is exceeded.

+++

<!-- ai-section-version: 1 | source-hash: 69d3f246 -->
