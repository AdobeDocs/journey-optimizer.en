---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure reward providers and reward definitions for Loyalty Challenges, including the fields involved, the reward context passed to the rewardJsonata expression, and how to write that expression to build the payload posted to a reward provider's endpoint.

**Intents:**

* Configure a reward provider (endpoint, authentication, headers) and one or more reward definitions under it.
* Understand the fields available on reward providers and reward definitions, including which are required.
* Write a rewardJsonata expression that maps reward context fields onto the payload a provider expects.
* Use kvpCustom on a challenge to pass campaign-specific or provider-specific metadata without editing the expression.
* Use task accumulator data, such as the most recent item in item_list, inside an expression.
* Distinguish task, milestone, and challenge reward sources and access the milestone object correctly.
* Validate a rewardJsonata expression before publishing and troubleshoot common mistakes.

**Glossary:**

* **Reward Provider** *(product-specific)*: represents a single external rewards system; holds the delivery endpoint URL, authentication, and custom HTTP headers.
* **Reward Definition** *(product-specific)*: describes a distinct reward type or denomination offered by a provider, including its rewardJsonata expression.
* **rewardJsonata** *(product-specific)*: a JSONata expression configured on a reward definition that is evaluated at reward-issue time and must return the JSON payload to POST to the provider.
* **Reward context** *(product-specific)*: the single root object passed to rewardJsonata at evaluation time, containing rewardContext, reward, task, milestone, challenge, and timestamp.
* **kvpCustom** *(product-specific)*: custom key-value pairs configured on a challenge (challenge.kvpCustom) or available as constants on a reward (reward.kvpCustom), used to pass campaign IDs, product names, or provider-specific metadata.
* **isDefault** *(product-specific)*: marks a reward definition as the sandbox-wide default, used to auto-populate reward details on personalized challenges at publish time.
* **item_list** *(product-specific)*: the list of all qualifying items applied to a task's accumulators; item_list[-1] accesses the most recently applied item via JSONata negative indexing.

**Guardrails:**

* `name` and `url` are required fields on a reward provider; `guid` is system-assigned and read-only.
* `name` and `rewardJsonata` are required fields on a reward definition; `guid` is system-assigned and read-only.
* When a reward provider's `enabled` field is false, reward delivery is suspended for all definitions under that provider.
* When a reward definition's `enabled` field is false, that definition is inactive and will not issue rewards.
* Only one reward definition across all providers may be marked as default (`isDefault`) at a time; setting a new default clears the previous one.
* `maxRatePerSecond` on a reward provider accepts a value from 1 to 5000 (per provider); null means unlimited.
* `rewardContext.rewardValue` is always a string; it must be converted with `$number()` if the provider expects a numeric value.
* `milestone` is null when the reward source is `"task"` or `"challenge"`; it is populated (with `count` and `reward.rewardValue`) only when `rewardContext.source` is `"milestone"`.
* rewardJsonata expressions are validated for syntax at publish time; an invalid expression causes the API to return a 422 error with a description of the parse failure.
* `challenge.kvpCustom.someKey` returns null if the key was not set on the challenge at authoring time.
* `task.accumulators.item_list[-1]` is null if no items were applied before the reward was issued (a non-purchase event).
* If a rewardJsonata expression returns an array instead of an object, the provider receives an unexpected payload structure; it must be wrapped in an outer object.

**Terminology:**

* Canonical name: Reward Provider — holds the endpoint, authentication, and headers for an external rewards system.
* Canonical name: Reward Definition — describes a reward type or denomination and its rewardJsonata expression; belongs to one Reward Provider.
* Do not confuse: "Reward Provider" (the external system's endpoint, auth, and headers) ≠ "Reward Definition" (a specific reward type/denomination with its own rewardJsonata, nested under a provider).
* Do not confuse: "challenge.kvpCustom" (per-challenge custom metadata) ≠ "reward.kvpCustom" (constants fixed for a given reward type).
* Do not confuse: `rewardContext.rewardValue` (the reward value string that triggered issuance) ≠ `milestone.reward.rewardValue` (the reward value specific to a milestone).

**FAQ:**

* **Q: What triggers a reward to be issued?** — When a challenge task, milestone, or challenge completes and has a reward value configured, the platform issues a reward by calling the reward provider's HTTP endpoint with a JSON payload.
* **Q: What fields are required to create a reward provider?** — `name` and `url` are required; `guid` is system-assigned and read-only.
* **Q: What fields are required to create a reward definition?** — `name` and `rewardJsonata` are required; `guid` is system-assigned and read-only.
* **Q: How many reward definitions can be marked as default?** — Only one definition across all providers may be default at a time; setting a new default clears the previous one.
* **Q: Why does rewardContext.rewardValue need conversion before use as a number?** — Because rewardContext.rewardValue is always a string; use $number() to convert it if the provider expects a numeric value.
* **Q: Why would challenge.kvpCustom.someKey return null?** — Because the key was not set on the challenge at authoring time; ensure the key is present in kvpCustom on every challenge that uses the definition.
* **Q: What happens if an invalid rewardJsonata expression is published?** — The API returns a 422 error with a description of the parse failure.
* **Q: Where can I test a rewardJsonata expression before publishing?** — In the JSONata Exerciser, by pasting the reward context JSON as the input document and the expression to verify the output.

**Troubleshooting:**

* `task.accumulators.item_list[-1] is null` — Cause: no items were applied before the reward was issued (a non-purchase event). Fix: guard with a conditional or use timestamp from context instead.
* `milestone accessed when source is "task" or "challenge"` — Cause: milestone is null in that case. Fix: check rewardContext.source before accessing milestone, or only use milestone in definitions attached to milestone rewards.
* `Expression returns an array instead of an object` — Cause: the provider receives an unexpected payload structure. Fix: wrap array-returning expressions in an outer object, for example `{ "items": [...] }`.
* `challenge.kvpCustom.someKey returns null` — Cause: the key was not set on the challenge at authoring time. Fix: ensure the key is present in kvpCustom on every challenge that uses this definition.
* `422 error` — Cause: the rewardJsonata expression is invalid at publish time. Fix: the API returns a description of the parse failure; use the JSONata Exerciser to develop and test the expression before publishing.

**Examples:**

* Simple fixed payload: maps `challenge.profileId`, `$number(rewardContext.rewardValue)`, and `reward.denomination` into a memberId/points/currency object, producing `{"memberId": "ADB-0000030", "points": 50, "currency": "Stars"}`.
* Using kvpCustom: an expression references `challenge.kvpCustom.campaignId` alongside `challenge.profileId` and `rewardContext.rewardValue` to keep the expression reusable across campaigns.
* Using task accumulator data: an expression uses `task.accumulators.item_list[-1].transactionId` and `.timestamp` for audit trails and deduplication on the provider side.
* Constructing a text message: an expression concatenates strings with `&`, for example `"You just earned " & rewardContext.rewardValue & " " & reward.denomination & "!"`, producing `{"text": "You just earned 50 Stars!"}`.
* Example 1 — Simple points provider: a Reward Definition with rewardJsonata mapping `challenge.profileId`, `$number(rewardContext.rewardValue)`, and `reward.denomination` to `memberId`, `pointQuantity`, and `denomination`, producing a payload with `pointQuantity: 50`.
* Example 2 — Provider payload with campaign metadata: a Reward Definition builds an `awardPoints` array using `challenge.kvpCustom.parentCampaignId` and `challenge.kvpCustom.productName` (set on the challenge) plus task accumulator transaction data, so the same definition works across campaigns without editing the expression.
* Example 3 — Milestone reward: an expression includes `milestone.count` and `task.schedule.currentStreak`; when `rewardContext.source` is `"milestone"`, the milestone object is populated with `count` and `reward.rewardValue`.

**Personas:**

* **admin:** Can configure a reward provider with its endpoint URL, authentication, and additional headers, and create reward definitions under it. Can set maxRatePerSecond between 1 and 5000, or leave it null for unlimited. Can mark enabled to false on a provider or definition to suspend or stop reward delivery. The page states that only one reward definition across all providers may be isDefault at a time. Where: "Reward provider & definition fields".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Paste the reward context JSON as the input document in the JSONata Exerciser and add your rewardJsonata expression.
* **Success check:** The output matches what your provider expects.

+++

<!-- ai-section-version: 1 | source-hash: 1e8b3805 -->
