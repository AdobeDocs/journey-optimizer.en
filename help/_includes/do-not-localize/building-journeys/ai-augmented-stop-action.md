---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Stop action removes a profile from selected upstream inbound experiences without ending the profile's journey.

**Intents:**

* Remove a profile from selected inbound experiences while continuing the journey
* Configure Stop action downstream of inbound activities on the same path
* Distinguish Stop action from stopping a journey
* Replace a code-based experience while continuing the journey
* Resolve selection errors and avoid redundant Stop action activities

**Glossary:**

* **Stop action**: A journey activity that removes the profile reaching it from selected upstream inbound activities while the profile continues progressing in the journey. *(product-specific)*
* **Inbound activities**: The in-app, content card, web, or code-based experience activities that Stop action can target. *(product-specific)*

**Guardrails:**

* Stop action must be downstream of the selected inbound activities on the same journey path. Wait or Reaction can be placed between the inbound activity and Stop action.
* Select one to five upstream inbound activities (hard limit). Selecting none, more than five, or the same activity more than once generates an error.
* Selecting an activity that is not upstream on the same path or has been deleted generates an error. Deleted selections appear as [!UICONTROL Unavailable activity].
* Warnings identify an activity already stopped earlier, an activity stopped immediately after activation, or a redundant Stop action immediately before End.
* Avoid stopping an inbound activity immediately after activation, as this can prevent the profile from seeing the experience.
* Inbound activities are already removed when a profile exits the journey. Stop action immediately before End is redundant.
* Give inbound activities distinct labels because the Action dropdown shows only activity names, which can be identical.
* Other inbound activities are not affected.

**Terminology:**

* Canonical activity name: [!UICONTROL Stop action]
* Target selection field: [!UICONTROL Action]
* Additional target control: [!UICONTROL Stop another action]
* Deleted selection label: [!UICONTROL Unavailable activity]
* Do not confuse Stop action with stopping a journey: Stop action applies to selected inbound activities for the profile reaching it; stopping a journey halts all profiles progressing through it.

**FAQ:**

* **Q: Does Stop action end the profile's journey?** The profile stops qualifying for the selected experiences and continues progressing in the journey.
* **Q: Which inbound activities can Stop action target?** In-app, content card, web, or code-based experience activities upstream of Stop action.
* **Q: How many inbound activities can be selected?** Up to five (hard limit).
* **Q: Are other inbound activities affected?** Other inbound activities are not affected.
* **Q: Must Stop action immediately follow an inbound activity?** Wait or Reaction can be placed between the inbound activity and Stop action on the same path. Avoid stopping an inbound activity immediately after activation, as this can prevent the profile from seeing the experience.
* **Q: What happens when a profile re-enters the journey?** The inbound experience activates again when the profile reaches that activity.

+++

<!-- ai-section-version: 2 | source-hash: e0844bc6 -->