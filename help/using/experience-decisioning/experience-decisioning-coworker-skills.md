---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for Decisioning
description: Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer, including the Decisioning Explainer skill, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 1
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decisioning
---

# Coworker for Decisioning {#experience-decisioning-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer — understanding why an offer was or wasn't shown to a profile or segment — with detailed guidance, example prompts, and best practices.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, and Decisioning in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

>[!ENDSHADEBOX]

## Decisioning Explainer {#decisioning-explainer}

>[!AVAILABILITY]
>
>Decisioning Explainer is available for all customers who have access to Coworker and Decisioning.

Decisioning Explainer answers, in natural language, why a specific offer was or wasn't shown to a given profile — or, more broadly, why a segment of profiles isn't seeing an offer. It walks the full decisioning stack for the requested profile (or segment) and time window: which offers were eligible, which eligibility rule included or excluded each one, whether frequency or fatigue capping suppressed the offer, the final ranking scores and which strategy or AI model produced them, and which candidate pool (item collection) the profile was evaluated against.

This addresses a common challenge for marketers: explaining why one offer ranked above another, or why a specific offer decision happened the way it did.

### Key use cases

* **Why a specific offer was or wasn't shown**

   Sample prompts:
   * "Why did profile 12345 see Offer X on May 15th?"
   * "Was profile X not eligible for this offer?"
   * "Which eligibility rule excluded this customer?"
   * "Show me which offers profile X was eligible for on June 3rd."

* **Why an offer's visibility changed over time**

   Sample prompts:
   * "Why has Offer Y stopped showing to returning customers in the last 7 days?"
   * "How many times has this customer seen this offer?"
   * "Was this offer capped for profile X?"
   * "What offers are currently being suppressed for profile X due to capping constraints?"

* **How an offer was ranked or selected**

   Sample prompts:
   * "Walk me through exactly how Offer Z was selected over the other eligible offers for this profile."
   * "What was the ranking score for each offer in this decision?"
   * "Why did Offer A rank above Offer B for this profile?"
   * "What factors most influenced the ranking outcome?"

* **Segment-level explanations**

   Decisioning Explainer can aggregate this logic across a segment rather than a single profile, surfacing the dominant reason a group of profiles isn't seeing an offer.

   Sample prompts:
   * "For customers in this audience, what's the most common reason they're excluded?"
   * "Which offers is this segment actually receiving?"
   * "Why isn't my loyalty segment seeing this offer?"

### In scope

Decisioning Explainer can currently answer questions about:

* Offer eligibility, and the eligibility rule that included or excluded a candidate offer.
* Ranking outcomes, including scores and the selection strategy or AI model that produced them.
* Frequency and fatigue capping suppression.
* The candidate pool (item collection) a profile was evaluated against.
* Aggregated explanations across a segment, rather than a single profile.

### Out of scope

The following functionalities are currently not supported:

* Explaining decisions for channels or activities outside of Decisioning.
* Modifying rules, ranking formulas, or selection strategies — Decisioning Explainer is read-only.

### Prompting best practices

* **Reference IDs when known**: Provide the profile ID, offer name, or segment name to get a precise trace rather than a general answer.
* **Include a time window**: Specify a date or date range when asking why an offer's visibility changed, so Coworker can scope the trace correctly.
* **Ask for the ranking breakdown directly**: If you want scoring detail, ask explicitly for the ranking score or the factors that influenced the outcome.
* **Use segment-level questions for trends**: When investigating why a group of profiles isn't seeing an offer, ask about the segment rather than a single profile to get the dominant reason.

{{$include /help/_includes/do-not-localize/start/ai-augmented-experience-decisioning-coworker-skills.md}}
