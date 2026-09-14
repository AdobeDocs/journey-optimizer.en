---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to publish an Adobe Journey Optimizer journey, manage journey versions, and understand the constraints that apply once a journey is live.

**Intents:**
* Publish a journey to make it live and available for profile entry
* Verify journey validity and resolve errors before publishing
* Create a new version of a live journey to make modifications
* Understand read-only restrictions that apply after a journey is published
* Stop a journey permanently or manage transitions between versions

**Glossary:**
* **Journey version**: A numbered iteration of a journey; new versions are created to modify a live journey without disrupting profiles already in progress *(product-specific)*
* **Closed status**: The state a previous journey version enters automatically when a new version is published; no new profiles can enter a Closed journey *(product-specific)*
* **Approval policy**: An optional governance workflow requiring explicit approval before a journey can be published *(product-specific)*

**Guardrails:**
* A journey with errors cannot be published.
* Journey Optimizer validates the total journey payload size at save and publish time; publication may be blocked if the limit is exceeded.
* After publishing, a journey is in read-only mode; only labels, descriptions, and the journey name can be edited.
* A new version can only be created from the latest version of a journey.
* When a journey is stopped, it is permanently stopped; it must be duplicated to run again.
* Assets and images in delivered content are accessible for up to 730 days from first publication; re-publishing is required after that period.
* If an offer decision used in a journey message changes, the journey must be unpublished and republished.
* Specific guardrails apply to journey versioning (see guardrails page).

**Terminology:**
* Canonical name: Publish Journey — Acronym: none — variants: activate journey, go live
* Synonyms: "Publish" = "activate" = "go live"
* Do not confuse: Stop (emergency halt of all profiles) ≠ Close to new entrances (manual graceful close; existing profiles finish) ≠ Closed status (automatic when a new version is published, or after manual close to new entrances)
* Do not confuse: Simulation (temporary simulated users, no AEP test profiles needed) ≠ Test mode (persistent AEP test profiles, draft journeys only) ≠ Dry run (real production audience data, no contact, no profile update, action nodes bypassed)

**FAQ:**
* **Q: Can I edit a journey after it is published?** — Only labels, descriptions, and the journey name can be changed. To make other modifications, create a new version of the journey.
* **Q: What happens to profiles in an older journey version when a new version is published?** — Profiles already in the previous version stay there until they finish; new profiles enter the latest version.
* **Q: Can I republish a Closed journey version?** — No. Once a previous version is Closed, it stays closed even if the latest version is stopped.
* **Q: What should I do if an offer decision used in the journey changes?** — Unpublish the journey and republish it to incorporate the updated offer decision.
* **Q: Is approval required before publishing?** — Only if your journey is subject to an approval policy; in that case, publishing submits the journey for approval instead of publishing it right away, and it is published automatically once an approver signs off.

+++
