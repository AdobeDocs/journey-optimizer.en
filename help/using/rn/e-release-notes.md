---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
hide: true
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
TQID: 'https://experienceleague.adobe.com/951PJzmmITN1nSUapVomlYnPws9pS0TosI1Gl3R9yL4'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Release notes
---

# Pre-release notes {#e-release-notes}

Adobe Journey Optimizer publishes pre-release notes one week before each monthly release to give you an early look at the new capabilities and improvements planned for that release. After the release, all changes are consolidated in the [release notes](release-notes.md).

## November '26 pre-release notes {#nov-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: November 17-18, 2026

### Journeys {#nov-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

<table>
<thead>
<tr>
<th><strong>AI recommendation cards for journey alerts</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Journey Optimizer home page now surfaces an <strong>AI recommendation card</strong> when a journey alert fires, covering <strong>Journey Custom Action failure</strong> and <strong>Journey Anomaly Detected</strong> alerts. Selecting the card opens the associated conversation history in the full, immersive Coworker chat experience.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-15706" target="_blank">DOCAC-15706</a></p>
</td>
</tr>
</tbody>
</table>

<!-- HELD: scope to confirm (CJM-165835 covers Dry-Run journeys only; no DOCAC task).
* **Reduced step events for wait and event activities** - Step events are no longer generated for **wait** activities and **event** activities when the profile was not actually processed at that activity.
-->

### Decisioning {#nov-26-decisioning}

The following improvements are coming to Decisioning in this release.

* **Decisioning item creation skill in Coworker** - You can now create decision items faster by describing what you need to Adobe CX Enterprise Coworker, which builds the item with you in chat. <!-- Documentation link: TBD --> Jira: [DOCAC-16258](https://jira.corp.adobe.com/browse/DOCAC-16258){target="_blank"}

* **Decisioning audit skill in Coworker** - You can now ask Adobe CX Enterprise Coworker about your Decisioning inventory, how Decisioning objects relate to each other, and who last edited an item, such as an offer. <!-- Documentation link: TBD --> Jira: [DOCAC-16259](https://jira.corp.adobe.com/browse/DOCAC-16259){target="_blank"}

* **Decisioning migration assistance skill in Coworker** - Get help migrating from Offer Decisioning to Journey Optimizer Decisioning directly in Adobe CX Enterprise Coworker. <!-- Documentation link: TBD --> Jira: [DOCAC-16260](https://jira.corp.adobe.com/browse/DOCAC-16260){target="_blank"}

* **AEM Managed Services content fragments support in Decisioning** - AEM Managed Services content fragments are now supported in Decisioning when managing decision items. <!-- Documentation link: TBD -->

### Orchestrated campaigns {#nov-26-orchestrated-campaigns}

The following improvements are coming to orchestrated campaigns in this release.

* **Increased message activity limit** - An orchestrated campaign can now contain up to **25 message actions**, such as email, push notification, or SMS sends, on its canvas. You can now build a larger campaign as one campaign instead of splitting it into several smaller ones. <!-- Documentation link: TBD --> Jira: [DOCAC-16143](https://jira.corp.adobe.com/browse/DOCAC-16143){target="_blank"}

* **Orchestrated campaigns skills in Coworker** - You can now find and inspect orchestrated campaigns conversationally from the Coworker chat interface. This release covers four read-only capabilities: listing and filtering campaigns by status, channel, tags, or name; pulling a specific campaign's details including its channel configuration and activity structure; visualizing a campaign's canvas as a graph of its activities and connections; and retrieving execution logs to surface errors for troubleshooting. This provides teams with live visibility into campaign data without requiring API access or navigation through the Journey Optimizer user interface. Creating, editing, or publishing campaigns via Coworker is not yet supported. <!-- Documentation link: TBD --> Jira: [DOCAC-14925](https://jira.corp.adobe.com/browse/DOCAC-14925){target="_blank"}

### Templates {#nov-26-templates}

The following improvements are coming to templates in this release.

* **Content template variants and localization** - You can now create multiple variants from a single master content template and localize templates directly at the template level. Manage all variants centrally under the master template to personalize content for different audiences, languages, and markets while reducing duplication and manual effort. <!-- Documentation link: TBD --> Jira: [DOCAC-16135](https://jira.corp.adobe.com/browse/DOCAC-16135){target="_blank"}

### Guardrails {#nov-26-guardrails}

The following improvements are coming to guardrails in this release.

* **Maximum payload size for journey business events** - Journey business events now enforce a maximum payload size of <TBC>. <!-- Documentation link: TBD --> Jira: [DOCAC-14772](https://jira.corp.adobe.com/browse/DOCAC-14772){target="_blank"}
