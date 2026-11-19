---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for Decisioning
description: Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer, including the Decisioning Explainer, Decisioning Rule Workflow, and Decisioning Offer Item Workflow skills, with in-depth guidance and sample prompts.
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

**On this page:** Discover the CX Enterprise Coworker skills available for Decisioning in Adobe Journey Optimizer — understanding why an offer was or wasn't shown to a profile or segment, creating, explaining, simulating, optimizing, and managing eligibility rules, ranking formulas, and frequency capping expressions, and creating decision items in chat — with detailed guidance, example prompts, and best practices.

>[!ENDSHADEBOX]

Decisioning capabilities in Adobe Journey Optimizer help you explain offer decisions, create decision items, and create, test, and optimize eligibility rules, ranking formulas, and frequency capping expressions through natural-language prompts. Use Decisioning Explainer to understand why an offer was or was not shown to a profile or segment. Use Decisioning Rule Workflow to create and simulate eligibility rules, ranking formulas, and frequency capping expressions before applying them to your decisioning strategy. Use Decisioning Offer Item Workflow to build decision items by describing what you need.

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

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 35%">
<col style="width: 15%">
<col style="width: 50%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Skill</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Why a specific offer was or wasn't shown</strong><br>Trace the decision for a profile or segment by reviewing eligibility rules, capping, ranking, and the candidate pool for a specific time window.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Explainer</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Why did profile 12345 see Offer X on May 15th?"<br><br>"Was profile X not eligible for this offer?"<br><br>"Which eligibility rule excluded this customer?"<br><br>"Show me which offers profile X was eligible for on June 3rd."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Why an offer's visibility changed over time</strong><br>Investigate changes in offer visibility by reviewing exposure frequency, fatigue or capping constraints, eligibility, and suppression over a selected period.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Explainer</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Why has Offer Y stopped showing to returning customers in the last 7 days?"<br><br>"How many times has this customer seen this offer?"<br><br>"Was this offer capped for profile X?"<br><br>"What offers are currently being suppressed for profile X due to capping constraints?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>How an offer was ranked or selected</strong><br>Explain why one offer ranked above another by showing the ranking scores, strategy or AI model, and other decision factors used for the profile.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Explainer</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Walk me through exactly how Offer Z was selected over the other eligible offers for this profile."<br><br>"What was the ranking score for each offer in this decision?"<br><br>"Why did Offer A rank above Offer B for this profile?"<br><br>"What factors most influenced the ranking outcome?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Segment-level explanations</strong><br>Aggregate decisioning logic across a segment to identify the dominant reasons profiles are not seeing an offer and which offers the segment is receiving.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Explainer</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"For customers in this audience, what's the most common reason they're excluded?"<br><br>"Which offers is this segment actually receiving?"<br><br>"Why isn't my loyalty segment seeing this offer?"</td></tr>
</table>

### Prompting best practices

* **Reference IDs when known**: Provide the profile ID, offer name, or segment name to get a precise trace rather than a general answer.
* **Include a time window**: Specify a date or date range when asking why an offer's visibility changed, so Coworker can scope the trace correctly.
* **Ask for the ranking breakdown directly**: If you want scoring detail, ask explicitly for the ranking score or the factors that influenced the outcome.
* **Use segment-level questions for trends**: When investigating why a group of profiles isn't seeing an offer, ask about the segment rather than a single profile to get the dominant reason.

## Decisioning Rule Workflow {#rules-ranking}

>[!AVAILABILITY]
>
>Decisioning Rule Workflow is available for all customers who have access to Coworker and Decisioning.

Decisioning Rule Workflow gives marketers AI-powered assistance for creating, understanding, testing, and managing decisioning logic, without needing to write or manually validate PQL syntax. It covers natural language rule creation, finding and reviewing existing rules and formulas, plain-English explanation, fixing and validating expressions, simulation against up to 3 test profiles, PQL optimization, and deletion. It's scoped to eligibility rules, ranking formulas, and offer-item frequency capping expressions — it doesn't create or edit selection strategies or decision policies.

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 35%">
<col style="width: 15%">
<col style="width: 50%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Skill</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Natural language rule creation</strong><br>Turn a plain-language eligibility requirement into PQL syntax for a new rule or an edit to an existing rule.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Can you create an eligibility rule that targets users that meet XYZ conditions?"<br><br>"Create an eligibility rule targeting loyalty members in tier 2 or above."<br><br>"Write a PQL rule that excludes customers who made a purchase in the last 7 days."<br><br>"Modify this rule to also exclude customers in the suppression list."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Plain-English rule and formula explanation</strong><br>Explain what an eligibility rule or ranking formula includes, excludes, and evaluates without requiring the user to read PQL syntax.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Can you explain this rule to me in natural language?"<br><br>"What does this ranking formula actually do?"<br><br>"Who does this eligibility rule target and who does it exclude?"<br><br>"Summarize this rule in one sentence."<br><br>"Why does Offer A rank above Offer B for this customer?"<br><br>"Is this rule too restrictive for a broad awareness campaign?"<br><br>"Which condition in this rule is filtering out the most profiles?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Simulation</strong><br>Test an eligibility rule or ranking formula against up to three profiles, including AI-generated edge cases, and return pass/fail results or ranked offers with numeric scores.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Simulate this rule with test profiles."<br><br>"Does this rule pass for a profile where loyalty_tier = gold?"<br><br>"Which profiles pass this eligibility rule: [profile A, profile B, profile C]?"<br><br>"Why did this profile fail the eligibility check?"<br><br>"Generate test profiles for this eligibility rule."<br><br>"Generate edge case profiles that stress-test this condition."<br><br>"Simulate this ranking formula across these offers and profiles."<br><br>"Which offer would rank highest for this profile given this formula?"<br><br>"Compare how this eligibility rule behaves for a gold vs. silver vs. basic tier customer."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>PQL optimization</strong><br>Rewrite an existing rule or formula with more concise syntax to meet Journey Optimizer's PQL size limits without changing its logic or outcome.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Optimize this PQL rule for me."<br><br>"This rule is hitting PQL size limits — can you shorten it?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Find and review rules and formulas</strong><br>List and find existing eligibility rules, ranking formulas, and frequency capping expressions, and review what they do.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"List ranking formulas."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Fix and validate expressions</strong><br>Repair a broken PQL expression and validate it before you finalize it.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Fix this eligibility rule."<br><br>"Validate this PQL expression."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Frequency capping expressions</strong><br>Create a frequency capping expression for decision items from a plain-language description.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Create a capping rule that counts click events."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Delete a rule or formula</strong><br>Remove an eligibility rule or ranking formula you no longer need.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Rule Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Delete this rule."</td></tr>
</table>

<!-- TO CONFIRM (PM/dev): the use cases for finding, fixing, validating, capping expressions, and deleting come from the skill description in Coworker. Confirm they are live, and validate the sample prompts for fixing and validating. -->

### Prompting best practices

* **Provide the target condition explicitly**: When creating or modifying a rule, state the exact audience, attribute, or exclusion condition you want.
* **Reference the rule or formula directly**: When asking for an explanation, simulation, or optimization, make sure the rule or formula you mean is open or clearly identified.
* **Ask for edge cases**: When simulating, ask Coworker to generate edge-case profiles to stress-test a condition, not just typical ones.
* **Review before publishing**: Check a generated or optimized rule's logic and simulation results before publishing it.
* **Be explicit before deleting**: Name the rule or formula you want to delete, and check where it is used first.

## Decisioning Offer Item Workflow {#decisioning-offer-item-workflow}

<!-- TO CONFIRM (PM): availability date, permissions, and any limitations. Add an AVAILABILITY block here once confirmed. -->

Decisioning Offer Item Workflow lets you create [decision items](items.md) faster by describing what you need to Coworker in chat. Coworker builds the item with you, so you don't have to manually fill in each field of the decision item creation form.

When you describe an item, Coworker can help you define the item's labels or tags, eligibility (based on an audience or an existing rule), schedule, frequency capping, content fragments, and custom attributes. For frequency capping, you can use named web or email placements, or custom PQL conditions. You can also use the skill to update, approve, unapprove, archive, or permanently delete decision items, and to create or update several items at once from a CSV file or a list. To learn more about these settings, see [Create your first decision item](items.md).

<!-- TO CONFIRM (PM/dev): supported item types, CSV/list format and size limits, and whether Coworker creates items in Draft status. -->

Decisioning Offer Item Workflow does not author eligibility rules or manage catalogs, collections, or selection strategies. To create or edit eligibility rules and ranking formulas, use [Decisioning Rule Workflow](#rules-ranking).

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 35%">
<col style="width: 15%">
<col style="width: 50%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Skill</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Create a decision item from a description</strong><br>Describe the offer or item you want, and Coworker builds it with you in chat.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Offer Item Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Create a decision item for a 20% off summer sale offer."<br><br>"Create an offer capped on a placement named like drc."<br><br>"Help me create a new decision item for our premium loyalty upgrade."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Set eligibility, schedule, and capping</strong><br>Add the conditions that control who sees the item, when it is available, and how often it is shown.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Offer Item Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Make this item available from December 1 to December 31."<br><br>"Limit this item to three impressions per profile per week."<br><br>"Make this item eligible for members of the Gold loyalty audience."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Manage existing decision items</strong><br>Update an item, change its approval status, archive it, or permanently delete it.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Offer Item Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Approve the Summer Sale item."<br><br>"Move the Summer Sale item back to Draft."<br><br>"Archive this offer."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Create or update several items at once</strong><br>Provide a CSV file or a list to create or update multiple decision items in one conversation.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Decisioning Offer Item Workflow</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Create decision items from this CSV file."<br><br>"Update the end date of these five items to December 31."</td></tr>
</table>

<!-- TO CONFIRM (PM/dev): sample prompts above are drafted from the skill description and the decision item documentation; validate them against the skill's actual behavior in Coworker. -->

### Prompting best practices

* **Describe the item up front**: Include the item name and the purpose of the offer in your first message so Coworker can create the item with fewer follow-up questions.
* **State the constraints you need**: Mention the audience, dates, or frequency limits you want, rather than leaving them for later.
* **Review before presenting the item to profiles**: Check the attributes and constraints of the item Coworker created before you approve it. Learn more about [approving decision items](items.md#approve).
* **Be explicit before deleting**: Permanent deletion can't be undone. Name the item you want to delete, and consider archiving it instead.

{{$include /help/_includes/do-not-localize/start/ai-augmented-experience-decisioning-coworker-skills.md}}
