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
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---

# Coworker for Decisioning {#experience-decisioning-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer — understanding why an offer was or wasn't shown to a profile or segment, and creating, explaining, simulating, and optimizing eligibility rules and ranking formulas — with detailed guidance, example prompts, and best practices.

>[!ENDSHADEBOX]

Decisioning capabilities in Adobe Journey Optimizer help you explain offer decisions and create, test, and optimize eligibility rules and ranking formulas through natural-language prompts. Use Decisioning Explainer to understand why an offer was or was not shown to a profile or segment. Use Rules & Ranking to create and simulate eligibility rules and ranking formulas before applying them to your decisioning strategy.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, and Decisioning in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

## Decisioning Explainer {#decisioning-explainer}

>[!AVAILABILITY]
>
>Decisioning Explainer is available for all customers who have access to Coworker and Decisioning.

Decisioning Explainer answers, in natural language, why a specific offer was or wasn't shown to a given profile — or, more broadly, why a segment of profiles isn't seeing an offer. It walks the full decisioning stack for the requested profile (or segment) and time window: which offers were eligible, which eligibility rule included or excluded each one, whether frequency or fatigue capping suppressed the offer, the final ranking scores and which strategy or AI model produced them, and which candidate pool (item collection) the profile was evaluated against.

This addresses a common challenge for marketers: explaining why one offer ranked above another, or why a specific offer decision happened the way it did. Decisioning Explainer is read-only — it explains decisions but does not modify rules, ranking formulas, or selection strategies.

### Key use cases

| Use Case | Description | Skills | Sample Prompts |
| --- | --- | --- | --- |
| Why a specific offer was or wasn't shown | Trace the decision for a profile or segment by reviewing eligibility rules, capping, ranking, and the candidate pool for a specific time window. | Decisioning Explainer | "Why did profile 12345 see Offer X on May 15th?"<br><br>"Was profile X not eligible for this offer?"<br><br>"Which eligibility rule excluded this customer?"<br><br>"Show me which offers profile X was eligible for on June 3rd." |
| Why an offer's visibility changed over time | Investigate changes in offer visibility by reviewing exposure frequency, fatigue or capping constraints, eligibility, and suppression over a selected period. | Decisioning Explainer | "Why has Offer Y stopped showing to returning customers in the last 7 days?"<br><br>"How many times has this customer seen this offer?"<br><br>"Was this offer capped for profile X?"<br><br>"What offers are currently being suppressed for profile X due to capping constraints?" |
| How an offer was ranked or selected | Explain why one offer ranked above another by showing the ranking scores, strategy or AI model, and other decision factors used for the profile. | Decisioning Explainer | "Walk me through exactly how Offer Z was selected over the other eligible offers for this profile."<br><br>"What was the ranking score for each offer in this decision?"<br><br>"Why did Offer A rank above Offer B for this profile?"<br><br>"What factors most influenced the ranking outcome?" |
| Segment-level explanations | Aggregate decisioning logic across a segment to identify the dominant reasons profiles are not seeing an offer and which offers the segment is receiving. | Decisioning Explainer | "For customers in this audience, what's the most common reason they're excluded?"<br><br>"Which offers is this segment actually receiving?"<br><br>"Why isn't my loyalty segment seeing this offer?" |

### Prompting best practices

* **Reference IDs when known**: Provide the profile ID, offer name, or segment name to get a precise trace rather than a general answer.
* **Include a time window**: Specify a date or date range when asking why an offer's visibility changed, so Coworker can scope the trace correctly.
* **Ask for the ranking breakdown directly**: If you want scoring detail, ask explicitly for the ranking score or the factors that influenced the outcome.
* **Use segment-level questions for trends**: When investigating why a group of profiles isn't seeing an offer, ask about the segment rather than a single profile to get the dominant reason.

## Rules & Ranking {#rules-ranking}

>[!AVAILABILITY]
>
>Rules & Ranking is available for all customers who have access to Coworker and Decisioning.

Rules & Ranking gives marketers AI-powered assistance for creating, understanding, and testing decisioning logic, without needing to write or manually validate PQL syntax. It covers four core capabilities: natural language rule creation, plain-English rule and ranking formula explanation, simulation against up to 3 test profiles, and PQL optimization. It's scoped to eligibility rules and ranking formulas — it doesn't create or edit selection strategies or decision policies.

### Key use cases

| Use Case | Description | Skills | Sample Prompts |
| --- | --- | --- | --- |
| Natural language rule creation | Turn a plain-language eligibility requirement into PQL syntax for a new rule or an edit to an existing rule. | Rules & Ranking | "Can you create an eligibility rule that targets users that meet XYZ conditions?"<br><br>"Create an eligibility rule targeting loyalty members in tier 2 or above."<br><br>"Write a PQL rule that excludes customers who made a purchase in the last 7 days."<br><br>"Modify this rule to also exclude customers in the suppression list." |
| Plain-English rule and formula explanation | Explain what an eligibility rule or ranking formula includes, excludes, and evaluates without requiring the user to read PQL syntax. | Rules & Ranking | "Can you explain this rule to me in natural language?"<br><br>"What does this ranking formula actually do?"<br><br>"Who does this eligibility rule target and who does it exclude?"<br><br>"Summarize this rule in one sentence."<br><br>"Why does Offer A rank above Offer B for this customer?"<br><br>"Is this rule too restrictive for a broad awareness campaign?"<br><br>"Which condition in this rule is filtering out the most profiles?" |
| Simulation | Test an eligibility rule or ranking formula against up to three profiles, including AI-generated edge cases, and return pass/fail results or ranked offers with numeric scores. | Rules & Ranking | "Simulate this rule with test profiles."<br><br>"Does this rule pass for a profile where loyalty_tier = gold?"<br><br>"Which profiles pass this eligibility rule: [profile A, profile B, profile C]?"<br><br>"Why did this profile fail the eligibility check?"<br><br>"Generate test profiles for this eligibility rule."<br><br>"Generate edge case profiles that stress-test this condition."<br><br>"Simulate this ranking formula across these offers and profiles."<br><br>"Which offer would rank highest for this profile given this formula?"<br><br>"Compare how this eligibility rule behaves for a gold vs. silver vs. basic tier customer." |
| PQL optimization | Rewrite an existing rule or formula with more concise syntax to meet Journey Optimizer's PQL size limits without changing its logic or outcome. | Rules & Ranking | "Optimize this PQL rule for me."<br><br>"This rule is hitting PQL size limits — can you shorten it?" |

### Prompting best practices

* **Provide the target condition explicitly**: When creating or modifying a rule, state the exact audience, attribute, or exclusion condition you want.
* **Reference the rule or formula directly**: When asking for an explanation, simulation, or optimization, make sure the rule or formula you mean is open or clearly identified.
* **Ask for edge cases**: When simulating, ask Coworker to generate edge-case profiles to stress-test a condition, not just typical ones.
* **Review before publishing**: Check a generated or optimized rule's logic and simulation results before publishing it.

{{$include /help/_includes/do-not-localize/start/ai-augmented-experience-decisioning-coworker-skills.md}}
