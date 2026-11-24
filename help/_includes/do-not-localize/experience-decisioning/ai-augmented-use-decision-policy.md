---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Explains how to insert decision policy code into message content and how to use attributes from the returned decision items to personalize that content.

**Intents:**

* Insert the decision policy code into your code-based experience, web, email, mobile message, push notification, custom channel, or direct mail content.
* Personalize content with attributes from the returned decision items.
* Preview and test your content before activating your journey or campaign.
* View the details of a decision policy from the campaign summary of an action or API-triggered campaign, access its technical details, and copy them to the clipboard, which can be useful to troubleshoot issues with Adobe Support or your engineering team.
* See how your decisions are performing with out-of-the-box decisioning metrics in the campaign or journey report, or with custom Customer Journey Analytics dashboards.

**Glossary:**

* **Decision policy code** *(product-specific)*: the code that you insert into your content for a decision policy.
* **Decision items** *(product-specific)*: the items that are returned by the decision policy.
* **Offers catalog schema** *(product-specific)*: the "Offers" catalog schema, in which decision item attributes are stored.
* **Custom attributes**: decision item attributes displayed in the `_\<imsOrg\>` folder of the personalization editor.
* **Standard attributes**: decision item attributes displayed in the `_experience` folder of the personalization editor.
* **`trackingToken`** *(product-specific)*: the attribute to add to enable decision item tracking.
* **Code your own** *(product-specific)*: a mode of the Email Designer in which you can also insert the decision policy code.
* **Decision policies section (campaign summary)** *(product-specific)*: displayed on the campaign summary page when an action or API-triggered campaign uses decision policies in its content; it lists all policies used in the campaign. For each policy you can review the strategies used, the number of items to return, the collection, ranking method and eligibility rules used for each selection strategy, and the fallback offer used if no decision item is eligible.

**Guardrails:**

* Web channel: the total payload size of a web channel response must not exceed 64 KB (hard limit). Requests exceeding this limit will result in an error. Ensure your decision items and attributes remain within this threshold.
* Mobile and Push channels: only one decision item can be returned.
* Code your own mode: only one decision item can be returned per policy, because the Repeat Grid component is not available.
* Mobile and Push channels: make sure you insert attributes after the syntax code for the decision policy. This syntax should always be kept at line 1.
* Mobile or Push content: if you insert an image asset attribute (for example, in the title or body), the attribute value displays as a URL. The image itself is not rendered in those fields.
* Journey Optimizer fragments: decision item attributes and contextual attributes are not supported by default. However, you can use global variables instead.
* Email: if you use multiple decision policies in the same email (for example, one for the header and one for the footer), the same offer is deduplicated across placements and is not rendered twice. The second decision policy will not return any content and will display a blank space, unless you have configured a fallback offer, in which case the fallback will be displayed instead.

**Prerequisites and permissions:**

* To use attributes from the returned decision items for personalization, first insert the decision policy code into your content: once the decision policy code is added to your content, all attributes from the returned decision items become available for personalization.
* Push notification: Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the release notes to identify the required version and ensure you have upgraded accordingly.

**Applicability:**

* Decision policies are available to all customers for the Code-based Experience, Web, Email, Mobile message, Push notification, Custom channels, and Direct mail channels.
* Inserting decision policies in Code your own mode is in Limited Availability.

**Terminology:**

* Canonical name: Customer Journey Analytics — Acronym: CJA
* Labels used to add the decision policy code: Insert policy for Code-based Experience and Direct Mail; Insert syntax for Email, Mobile message, Push, Web, Custom channel and Code your own mode. In the Personalization Editor, the item to navigate to is named Decision policy for Code-based Experience and Decision policies for the other channels.

**FAQ:**

* **How many decision items can be returned?** For code-based experience, web, email and direct mail channels, repeat the sequence to insert the decision policy code once per decision item you want returned. For Mobile and Push channels, only one decision item can be returned. In Code your own mode (Email Designer), only one decision item can be returned per policy.
* **How do I add an attribute to my content?** Click the `+` icon next to the attribute. You can add as many attributes as needed and include other personalization attributes, such as profile data. For Email, Web, Code-based, and Direct Mail channels, wrap the attributes within the `#each` loop using square brackets `[ ]`, and add a comma before the closing `/each` tag.
* **How do I enable decision item tracking?** Add the `trackingToken` attribute: `trackingToken: {{item._experience.decisioning.decisionitem.trackingToken}}`.
* **How are decision items rendered when I preview and test my content?** Decision items render based on selected profiles in the simulation interface.
* **When are changes applied for code-based experiences?** As soon as your developer makes an API or SDK call to fetch content for the surface defined in your channel configuration, the changes will be applied to your web page or app.
* **What does the JSON copied from the campaign summary of an action or API-triggered campaign include?** It includes your organization name and ID, sandbox name, decision policy ID, and the full decision policy structure. You can share this information with Adobe Support or your engineering team to troubleshoot decision policy issues faster.

**Troubleshooting:**

* Email: the insertion option does not appear. A decision policy might already be configured for the parent component.

**Examples:**

* Code-based experience, web, email and direct mail channels: if you chose to return 2 items when creating the decision, repeat the sequence twice.

**Related pages:**

* For Custom channels: Custom channels (custom-channel/get-started-custom-channel.md)
* Code-based experiences with a decision policy that contains decision items including fragments: Learn how to leverage fragments (experience-decisioning/fragments-decision-policies.md)
* Inserting the decision policy code in Code your own mode of the Email Designer: Learn how to code your own email content (email/code-content.md)
* Number of items to return, chosen when creating the decision: creating the decision (experience-decisioning/create-decision-policy.md)
* For the Offers catalog schema: catalog schema (experience-decisioning/catalogs.md)
* Working with personalization once the decision policy code is added: Learn how to work with personalization (personalization/personalize.md)
* Previewing and testing content after building it: Learn how to preview and test content (content-management/preview-test.md)
* Once your content is ready, publishing a journey: Publish a journey (building-journeys/publish-journey.md)
* Once your content is ready, reviewing and activating a campaign: Review and activate a campaign (campaigns/review-activate-campaign.md)
* Seeing how decisions are performing: Learn more about Decisioning reporting (experience-decisioning/cja-reporting.md)

**Personas:**

* **marketer:** Can insert the decision policy code into code-based experience, web, email, mobile message, push notification, custom channel, and direct mail content. Can add the code with Insert policy for Code-based Experience and Direct Mail, or with Insert syntax for the other channels. Can repeat the insertion once per decision item to return for code-based experience, web, email, and direct mail channels. Can personalize content with attributes from the returned decision items and add the `trackingToken` attribute to enable decision item tracking. Can preview and test content before activating a journey or campaign. Can view the Decision policies section of the campaign summary for an action or API-triggered campaign. The page states that the total payload size of a web channel response must not exceed 64 KB. Where: "Insert the decision policy code".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** In email content, open the Personalization Editor, navigate to Decision policies, and select Insert syntax to add the code for your decision policy.
* **Success check:** The decision policy code is added to your content, and attributes from the returned decision items become available for personalization.
* **Previous:** You choose the number of decision items to return when creating the decision: creating the decision (experience-decisioning/create-decision-policy.md)
* **Next:** Your content is ready and you are using a journey: Publish a journey (building-journeys/publish-journey.md); Your content is ready and you are using a campaign: Review and activate a campaign (campaigns/review-activate-campaign.md)

+++

<!-- ai-section-version: 1 | source-hash: 97361a49 -->
