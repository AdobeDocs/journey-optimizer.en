---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for Decisioning
description: Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer, including the Decisioning Explainer and Rules & Ranking skills, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 1
---

# Coworker for Decisioning {#experience-decisioning-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer — understanding why an offer was or wasn't shown to a profile or segment, and creating, explaining, simulating, and optimizing eligibility rules and ranking formulas — with detailed guidance, example prompts, and best practices.

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

## Rules & Ranking {#rules-ranking}

>[!AVAILABILITY]
>
>Rules & Ranking is available for all customers who have access to Coworker and Decisioning.

Rules & Ranking gives marketers AI-powered assistance for creating, understanding, and testing decisioning logic, without needing to write or manually validate PQL syntax. It covers four core capabilities: natural language rule creation, plain-English rule and ranking formula explanation, simulation against test profiles, and PQL optimization.

### Key use cases

* **Natural language rule creation**

   Turn a plain-language description into PQL eligibility rule syntax, for both net-new rules and edits to existing ones.

   Sample prompts:
   * "Can you create an eligibility rule that targets users that meet XYZ conditions?"
   * "Create an eligibility rule targeting loyalty members in tier 2 or above."
   * "Write a PQL rule that excludes customers who made a purchase in the last 7 days."
   * "Modify this rule to also exclude customers in the suppression list."

* **Plain-English rule and formula explanation**

   Explain what an existing eligibility rule or ranking formula does — what it includes or excludes, and what each condition means — without needing to read PQL syntax.

   Sample prompts:
   * "Can you explain this rule to me in natural language?"
   * "What does this ranking formula actually do?"
   * "Who does this eligibility rule target and who does it exclude?"
   * "Summarize this rule in one sentence."
   * "Why does Offer A rank above Offer B for this customer?"
   * "Is this rule too restrictive for a broad awareness campaign?"
   * "Which condition in this rule is filtering out the most profiles?"

* **Simulation**

   Run an eligibility rule or ranking formula against up to 3 test profiles — manually entered or AI-generated, including edge cases — and get pass/fail results with the specific failing condition, or a ranked list of offers with numeric scores.

   Sample prompts:
   * "Simulate this rule with test profiles."
   * "Does this rule pass for a profile where loyalty_tier = gold?"
   * "Which profiles pass this eligibility rule: [profile A, profile B, profile C]?"
   * "Why did this profile fail the eligibility check?"
   * "Generate test profiles for this eligibility rule."
   * "Generate edge case profiles that stress-test this condition."
   * "Simulate this ranking formula across these offers and profiles."
   * "Which offer would rank highest for this profile given this formula?"
   * "Compare how this eligibility rule behaves for a gold vs. silver vs. basic tier customer."

* **PQL optimization**

   Rewrite an existing rule or formula with more concise syntax to meet Journey Optimizer's PQL size limits, without changing its logic or outcome.

   Sample prompts:
   * "Optimize this PQL rule for me."
   * "This rule is hitting PQL size limits — can you shorten it?"

### In scope

Rules & Ranking can currently:

* Create a new eligibility rule from a plain-language description, or edit an existing one.
* Explain an existing eligibility rule or ranking formula in plain English.
* Simulate an eligibility rule or ranking formula against up to 3 test profiles, manually entered or AI-generated.
* Rewrite a rule or formula to be more concise and fit within PQL size limits, while preserving its logic and outcome.

### Out of scope

The following functionalities are currently not supported:

* Simulating against more than 3 test profiles at a time.
* Creating or editing selection strategies or decision policies — Rules & Ranking is scoped to eligibility rules and ranking formulas.

### Prompting best practices

* **Provide the target condition explicitly**: When creating or modifying a rule, state the exact audience, attribute, or exclusion condition you want.
* **Reference the rule or formula directly**: When asking for an explanation, simulation, or optimization, make sure the rule or formula you mean is open or clearly identified.
* **Ask for edge cases**: When simulating, ask Coworker to generate edge-case profiles to stress-test a condition, not just typical ones.
* **Review before publishing**: Check a generated or optimized rule's logic and simulation results before publishing it.

{{$include /help/_includes/do-not-localize/start/ai-augmented-experience-decisioning-coworker-skills.md}}
