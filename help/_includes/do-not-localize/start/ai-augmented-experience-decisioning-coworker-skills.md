---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents two CX Coworker skills for Decisioning in Adobe Journey Optimizer: Decisioning Explainer, which explains in natural language why a specific offer was or wasn't shown to a profile or segment; and Rules & Ranking, which creates, explains, simulates, and optimizes eligibility rules and ranking formulas in natural language, without requiring PQL syntax.

**Intents**

* Understand why a specific offer was or wasn't shown to a profile.
* Understand why an offer's visibility to a customer or segment changed over time.
* Understand how an offer was ranked or selected over other eligible offers.
* Get an aggregated explanation of why a segment of profiles isn't seeing an offer.
* Create a new eligibility rule, or edit an existing one, from a plain-language description.
* Get a plain-English explanation of what an existing eligibility rule or ranking formula does.
* Simulate an eligibility rule or ranking formula against test profiles.
* Rewrite a rule or formula to fit within PQL size limits without changing its logic.

**Glossary**

* **Decisioning Explainer** *(product-specific)*: CX Coworker skill that explains, in natural language, why an offer was or wasn't shown to a profile or segment, by tracing eligibility, capping, ranking, and candidate pool evaluation.
* **Rules & Ranking** *(product-specific)*: CX Coworker skill that creates, explains, simulates, and optimizes Decisioning eligibility rules and ranking formulas using natural language, without requiring the marketer to write or read PQL syntax directly.
* **Eligibility rule**: a condition that includes or excludes an offer as a candidate for a given profile; Decisioning Explainer identifies which rule included or excluded each candidate offer, and Rules & Ranking can create, explain, simulate, or optimize the rule itself.
* **Ranking formula**: the logic used to score and order eligible offers; Rules & Ranking can create, explain, simulate, or optimize a ranking formula, the same way it does for eligibility rules.
* **Capping**: frequency or fatigue suppression logic that can prevent an otherwise-eligible offer from being shown; Decisioning Explainer can identify when capping suppressed an offer.
* **Candidate pool (item collection)**: the set of offers a profile is evaluated against during a decisioning event; Decisioning Explainer reports which candidate pool was used.
* **PQL (Profile Query Language)**: the expression syntax underlying Decisioning eligibility rules and ranking formulas; Rules & Ranking generates, explains, and optimizes PQL without the marketer needing to write or validate it manually.

**Guardrails**

* Decisioning Explainer and Rules & Ranking are both available for all customers who have access to Coworker and Decisioning.
* Decisioning Explainer is read-only: it explains decisions but does not modify rules, ranking formulas, or selection strategies.
* Rules & Ranking simulation supports up to 3 test profiles at a time, manually entered or AI-generated.
* Rules & Ranking is scoped to eligibility rules and ranking formulas; it does not create or edit selection strategies or decision policies.

**Terminology**

* Do not confuse: "eligibility" (whether an offer qualifies as a candidate) is distinct from "ranking" (how qualifying candidates are ordered) and "capping" (frequency/fatigue suppression applied after eligibility and ranking) — Decisioning Explainer reports on all three separately.
* Do not confuse: Decisioning Explainer explains why a *decision already made* turned out the way it did for a real profile or segment; Rules & Ranking explains, creates, simulates, or optimizes the *rule or formula configuration itself*, independent of any specific real-world decisioning event.

**FAQ**

* **Can Decisioning Explainer explain a decision for a single profile?** Yes, ask why a specific profile did or didn't see a specific offer, on a specific date.
* **Can Decisioning Explainer explain decisions across a segment?** Yes, it can aggregate the explanation across a segment to surface the dominant reason a group of profiles isn't seeing an offer.
* **Does Decisioning Explainer show ranking scores?** Yes, it can return the final ranking score for each offer and which strategy or AI model produced it.
* **Can Decisioning Explainer change a rule or ranking formula?** No, it is read-only and does not modify decisioning configuration.
* **Can Rules & Ranking create a brand-new eligibility rule from scratch?** Yes, describe the target audience or condition in plain language and it generates the PQL rule.
* **Can Rules & Ranking explain a rule someone else built?** Yes, it can explain any existing eligibility rule or ranking formula in plain English, including what it includes, excludes, and each condition's meaning.
* **How many test profiles can Rules & Ranking simulate against at once?** Up to 3, manually entered or AI-generated, including edge cases.
* **Does Rules & Ranking change a rule's logic when optimizing it?** No, PQL optimization only makes the syntax more concise to fit size limits; it preserves the original logic and outcome.

+++
