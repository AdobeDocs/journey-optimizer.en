---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to insert and manage links in Journey Optimizer emails, add a mirror page, and enable open and click tracking to monitor recipient engagement.

**Intents:**

* Enable open and click tracking on an email message in a journey or campaign
* Insert links (external, landing page, opt-out, opt-in, mirror page, deeplink) into email content
* Track the same URL across multiple emails by assigning unique labels
* Add and configure a mirror page link
* Manage tracked URLs and set the tracking type for each link
* Locate reporting on openings and clicks

**Glossary:**

* **Email opens**: Tracking option/metric that checks how many messages have been opened *(product-specific)*
* **Click on email**: Tracking option/metric that calculates the number of clicks on links in an email *(product-specific)*
* **urlID**: A unique tracking identifier generated only when both the URL and the label are unique; links sharing the same URL and effective label reuse the same urlID *(product-specific)*
* **Mirror page**: An online version of the email that contains all personalization data and is displayed in the recipient's default web browser when the mirror page link is clicked *(product-specific)*
* **Tracking Type**: The per-URL setting controlling how a link is tracked *(product-specific)*

**Guardrails:**

* Links included in content expire 25 months after the message is sent, except links to a mirror page, which expire after 90 days; once that delay elapses the links are no longer available.
* Both Email opens and Click on email options are enabled by default.
* A unique urlID is generated only when both the URL and the label are unique; otherwise the same urlID is reused and you cannot tell which link was clicked — use a unique label for each similar URL (in the Email Designer or via the `data-label` HTML attribute).
* Journey Optimizer complies with URI syntax (RFC 3986), which disables some special international characters in URLs; URL-encode unsupported characters (for example, use `%27` for an apostrophe) to avoid errors when sending a proof or email.
* Marketing-type email messages must include an opt-out link; this is not required for transactional messages. The category (Marketing or Transactional) is defined in the channel configuration.
* Mirror page links are auto-generated and cannot be edited; heavy runtime personalization can make mirror page URLs excessively large and cause HTTP errors (404, 422, 502).
* In a proof sent to test profiles, the mirror page link is not active; it is only active in the final messages.
* When both the label and URL of a button are made editable in a customizable fragment, tracking reports show the URL instead of the button label.

**Terminology:**

* Canonical name: URL tracking identifier — Acronym: n/a — variants: urlID
* Synonyms: "Email opens" = "opens metric"; "Click on email" = "clicks metric"
* Do not confuse: "Tracked" (activates tracking on a URL) ≠ "Opt out" (treats URL as opt-out/unsubscription) ≠ "Mirror page" (treats URL as a mirror page URL) ≠ "Never" (never activates tracking of a URL)
* Do not confuse: link retention "25 months" (content links) ≠ "90 days" (mirror page)

**FAQ:**

* **Q: How do I enable tracking?** — At the email message level, check the Email opens and/or Click on email options when creating your message in a journey or campaign; both are enabled by default.
* **Q: Why can't I tell which of two identical links was clicked?** — Links that share the same URL and the same effective label (including a blank label) reuse the same urlID; assign a unique label to each similar URL.
* **Q: How long do links stay available?** — 25 months after the message is sent for content links, and 90 days for mirror page links.
* **Q: What is a mirror page?** — An online version of the email containing all personalization data, useful when recipients experience rendering issues, for accessibility, or for social sharing.
* **Q: Which tracking types can I set for a URL?** — Tracked, Opt out, Mirror page, or Never.
* **Q: Where is open and click reporting available?** — In the Live report and the Customer Journey Analytics report.

+++

<!-- ai-section-version: 1 | source-hash: 1fcd5252 -->
