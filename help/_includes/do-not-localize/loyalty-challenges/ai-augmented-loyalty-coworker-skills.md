---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes the Coworker capabilities in Adobe Journey Optimizer for creating loyalty challenges and analyzing loyalty program performance: Loyalty Challenge Management, Loyalty Insights Skill, and the Challenge Recommendations Skill, including their use cases and what is out of scope.

**Intents**

* Create and manage loyalty challenges using natural language prompts with Loyalty Challenge Management.
* Query and analyze loyalty program performance data — points, tiers, redemptions, and revenue — using natural language with Loyalty Insights Skill.
* Use Challenge Recommendations to review an opportunity and its rationale and pass the recommendation to the Loyalty Challenge Management skill with **[!UICONTROL Create with AI]**.
* Review the challenge details and journey in challenge authoring before publishing.
* Learn which functionalities are currently not supported, such as challenge deletion and full content authoring automation for challenge messaging in all cases.
* Learn how to structure a prompt to create a loyalty challenge (audience, action, timing, reward).

**Glossary**

* **Loyalty Challenge Management** *(product-specific)*: Coworker skill that creates and manages loyalty challenges through natural language prompts.
* **Loyalty Insights Skill** *(product-specific)*: Coworker skill that analyzes and queries loyalty program performance data — points, tiers, redemptions, and revenue metrics — using natural language.
* **Challenge Recommendations** *(product-specific)*: Coworker feature that enables marketers to request grounded, specific challenge recommendations through natural language conversations, narrow them to their goals, and implement them as live challenges.

**Guardrails**

* Loyalty skills are available in Coworker for eligible organizations. Customers with a Loyalty license can access these loyalty skills, even if they do not have an additional Coworker license.
* Challenge deletion and full content authoring automation for challenge messaging in all cases are currently not supported (listed under out of scope skills in the Loyalty Challenge Management section).
* Challenge Recommendations uses loyalty program trends and performance data. It can pass a recommendation to Loyalty Challenge Management, which creates or edits the live challenge.

**Terminology**

* Do not confuse: "Loyalty Challenge Management" (creates and edits challenges), "Loyalty Insights Skill" (analyzes and queries loyalty program performance data), and "Challenge Recommendations" (provides challenge recommendations based on loyalty program trends and performance data) are described in separate sections of this page.

**FAQ**

* **Do I need a separate Coworker license to use Loyalty skills?** No, customers with a Loyalty license can access Loyalty skills even without an additional Coworker license.
* **Can Loyalty Challenge Management delete a challenge?** No, challenge deletion is currently not supported.
* **What kind of data can Loyalty Insights Skill query?** Loyalty points granted, earned, and redeemed; order revenue and loyalty discount trends; and program performance metrics by tier, program, product category, or time period.
* **What does Challenge Recommendations provide?** It provides grounded, specific challenge recommendations based on loyalty program trends and performance data, including recommendations for increasing member spend, winning back inactive members, improving underperforming challenges, focusing on products or categories, and addressing points expiry.
* **What happens after I select [!UICONTROL Create with AI]?** The recommendation is passed to the Loyalty Challenge Management skill. Continue the conversation to provide missing details and create or edit the challenge without leaving Coworker Chat. Then review the challenge details and journey in challenge authoring before publishing.
* **What should I include when asking Loyalty Challenge Management to create a challenge?** A clear title, the qualifying audience, the required action and how much/how often, the time window and timezone, the reward, and the qualifying event.

+++

<!-- ai-section-version: 3 | source-hash: d53c4586 -->
