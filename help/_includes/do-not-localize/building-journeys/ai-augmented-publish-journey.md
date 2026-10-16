---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to validate configuration, test behavior, and publish an Adobe Journey Optimizer journey, then manage its statuses and versions.

**Intents:**
* Publish a journey to make it live and available for profile entry
* Validate configuration and resolve errors before testing or publishing
* Choose Simulation, Test mode, or Dry run to test journey behavior
* Create a new version of a live journey to make modifications
* Understand read-only restrictions that apply after a journey is published
* Stop a journey permanently or manage transitions between versions

**Glossary:**
* **[!UICONTROL Validate]**: Checks the journey configuration, including message configuration; it does not simulate the journey or replace testing *(product-specific)*
* **Simulation**: Tests with temporary simulated users and sends real messages to their defined execution addresses *(product-specific)*
* **Test mode**: Tests branch and message logic in a draft journey with persistent AEP test profiles and sends real messages to their inboxes *(product-specific)*
* **Dry run**: Tests with real production audience data without delivering real communications or updating live profile data *(product-specific)*
* **Journey version**: A numbered version of a journey; when a new version is published, profiles already in a previous version stay there until they finish *(product-specific)*
* **[!UICONTROL Closed]**: The status a previous journey version enters automatically when a new version is published; it accepts no new entries *(product-specific)*
* **Approval policy**: When a journey is subject to an approval policy, **[!UICONTROL Publish]** submits it for approval; the journey is published automatically once an approver signs off *(product-specific)*

**Guardrails:**
* A journey with errors cannot be published.
* On-demand message configuration checks help keep the canvas responsive for smaller and larger journeys; the benefit grows as activities and messages are added. Basic activity checks continue automatically, with errors and warnings in the Alerts panel.
* Running message checks on demand frees up system capacity for basic activity checks, helping them respond more quickly and consistently, even on smaller journeys.
* Validation must be current and passed before testing or publishing; errors must be resolved and validation rerun before continuing.
* Warnings do not prevent testing, simulation, or dry runs.
* Validation is available in **[!UICONTROL Draft]** status, not in test, dry-run, or simulation mode, or while locked for approval.
* The journey is temporarily locked during validation. Changes after validation make the results no longer current.
* Until validation is current and passed, **[!UICONTROL Validate]** replaces **[!UICONTROL Publish]**.
* Journey Optimizer validates the total journey payload size at save and publish time; publication may be blocked if the limit is exceeded.
* Publishing requires completed testing with any issues resolved, the **[!DNL Publish journeys]** high-level permission, and a payload within the configured limit (4 MB by default).
* After publishing, a journey is in read-only mode; only activity labels and descriptions, the journey's name, and the journey's description can be edited.
* A new version can only be created from the latest version of a journey.
* When a journey is stopped, it is permanently stopped; to run it again, duplicate it and publish the new journey.
* Assets and images in delivered content are accessible for up to 2 years (730 days) from their first publication in any fragment/inline message. Re-publishing after 730 days keeps them accessible for another 2 years; re-publication within 730 days of first publication does not extend their expiry.
* If an offer decision used in a journey message changes, the journey must be unpublished and republished.

**Terminology:**
* **[!UICONTROL Publish]**: Publishing activates a journey, moves it to **[!UICONTROL Live]** status, and makes it available for new profiles to enter.
* **[!UICONTROL Finished]**: The journey has completed according to its end criteria.
* Do not confuse: Stop (permanently stops profiles flowing through the journey and prevents new entries) differs from **[!UICONTROL Closed]** (the previous version accepts no new entries, while profiles already in it finish).
* Do not confuse: **[!UICONTROL Validate]** checks configuration; Simulation, Test mode, and Dry run test journey behavior using different types of data.

**FAQ:**
* **Q: What should I do if validation fails?** - Resolve the errors in the Alerts panel and click **[!UICONTROL Validate]** again before testing or publishing. Validation does not rerun automatically after an error is fixed.
* **Q: Can I edit a journey after it is published?** - Only activity labels and descriptions, the journey's name, and the journey's description can be changed. To make other modifications, create a new version of the journey.
* **Q: What happens to profiles in an older journey version when a new version is published?** — Profiles already in the previous version stay there until they finish; new profiles enter the latest version.
* **Q: What should I do if an offer decision used in the journey changes?** — Unpublish the journey and republish it to incorporate the updated offer decision.
* **Q: Is approval required before publishing?** — Only if your journey is subject to an approval policy; in that case, publishing submits the journey for approval instead of publishing it right away, and it is published automatically once an approver signs off.

+++

<!-- ai-section-version: 1 | source-hash: fcf6184c -->
