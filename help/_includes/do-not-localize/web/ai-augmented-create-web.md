---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a web experience through a journey or campaign in Journey Optimizer by adding a Web action, editing and testing its content, optionally redirecting visitors to another URL, and publishing, activating, or stopping it.

**Intents:**

* Add a Web activity to a journey or create a web campaign
* Select or create a web configuration matching a single page URL or multiple pages
* Edit web content using the web designer or the non-visual editor
* Preview and test a web experience before it goes live
* Redirect visitors to another existing URL instead of authoring a new variation
* Publish a web journey or activate a web campaign, and stop a live web experience

**Glossary:**

* **Web action**: An inbound action that displays a web experience to profiles when they reach that step of the journey; it references a web configuration that defines the content shown *(product-specific)*
* **Web configuration**: The definition that can match a single page URL or multiple pages (via a pages matching rule) to deliver content modifications across one or several web pages *(product-specific)*
* **Pages matching rule**: A rule that targets multiple URLs matching the same pattern, so changes apply across all pages matching the rule *(product-specific)*
* **Web designer**: The visual editor used to author the web experience *(product-specific)*
* **Non-visual editor**: An editing mode used to edit web content without loading the visual editor, reached by unselecting the Visual editor option and clicking Add a modification *(product-specific)*
* **Redirect to URL**: An option to redirect page visitors to another existing URL rather than authoring a new variation in the web designer *(product-specific)*

**Guardrails:**

* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using them continue to work without any changes and no migration is required.
* As Web is an inbound experience activity, it comes with a 3-days Wait activity.
* If this is your first time creating a web experience, you must follow the web prerequisites.
* If a campaign is subject to an approval policy, you must request approval before you can activate the web experience.
* If multiple journeys or campaigns update the same element(s) of a website, the highest priority journey/campaign takes precedence.
* After you click Publish (journey) or Activate (campaign), it can take up to 15 minutes for the changes to be available live on the website.
* Once a web journey or campaign is stopped, you cannot edit or activate it again; you can only duplicate it and activate the duplicate.
* A published web journey takes the Live status and becomes read-only.

**Terminology:**

* Canonical name: Web action — Acronym: n/a — variants: Web activity, Web experience activity, Web action type
* Synonyms: "web designer" = "visual editor"
* Do not confuse: "Simulate content" (test content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles and add a test profile)
* Do not confuse: "Publish" (option used to make a web journey live) ≠ "Activate" (used to make a web campaign live via Review to activate)
* Do not confuse: "Live" (status of a published/activated web experience) ≠ "Scheduled" (status of a web campaign with a defined schedule until the start date and time are reached)

**FAQ:**

* **Q: How do I create a web experience?** — Add a Web action to a journey (via an Action activity) or create a web campaign, then select or create a web configuration and edit the content.
* **Q: Can I apply changes across multiple pages?** — Yes, a web configuration can match multiple pages using a pages matching rule, and the changes apply to all pages matching the rule.
* **Q: How do I preview my web experience before it is live?** — Use Simulate content (sample input data or AI auto-generation) or Simulate content (AEP profiles) to preview with test profiles; you can also open it in the default browser or copy the test URL to share.
* **Q: How do I make my web experience live?** — Publish the journey (it takes the Live status and becomes read-only) or Review to activate and Activate the campaign; it can take up to 15 minutes for changes to appear live.
* **Q: Can I reuse a stopped web journey or campaign?** — No, once stopped you cannot edit or activate it again; you can only duplicate it and activate the duplicate.
* **Q: What happens if two live journeys/campaigns affect the same page?** — All changes are applied, and if multiple journeys or campaigns update the same element(s), the highest priority journey/campaign takes precedence.

+++

<!-- ai-section-version: 1 | source-hash: 494c17a0 -->
