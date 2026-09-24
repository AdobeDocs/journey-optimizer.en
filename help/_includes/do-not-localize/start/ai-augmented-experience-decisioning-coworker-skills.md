---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the CX Coworker Decisioning Explainer skill in Adobe Journey Optimizer, which explains in natural language why a specific offer was or wasn't shown to a profile or segment, tracing eligibility, capping, ranking, and the candidate pool involved in the decision.

**Intents**

* Understand why a specific offer was or wasn't shown to a profile.
* Understand why an offer's visibility to a customer or segment changed over time.
* Understand how an offer was ranked or selected over other eligible offers.
* Get an aggregated explanation of why a segment of profiles isn't seeing an offer.

**Glossary**

* **Decisioning Explainer** *(product-specific)*: CX Coworker skill that explains, in natural language, why an offer was or wasn't shown to a profile or segment, by tracing eligibility, capping, ranking, and candidate pool evaluation.
* **Eligibility rule**: a condition that includes or excludes an offer as a candidate for a given profile; Decisioning Explainer identifies which rule included or excluded each candidate offer.
* **Capping**: frequency or fatigue suppression logic that can prevent an otherwise-eligible offer from being shown; Decisioning Explainer can identify when capping suppressed an offer.
* **Candidate pool (item collection)**: the set of offers a profile is evaluated against during a decisioning event; Decisioning Explainer reports which candidate pool was used.

**Guardrails**

* Decisioning Explainer is available for all customers who have access to Coworker and Decisioning.
* Decisioning Explainer is read-only: it explains decisions but does not modify rules, ranking formulas, or selection strategies.

**Terminology**

* Do not confuse: "eligibility" (whether an offer qualifies as a candidate) is distinct from "ranking" (how qualifying candidates are ordered) and "capping" (frequency/fatigue suppression applied after eligibility and ranking) — Decisioning Explainer reports on all three separately.

**FAQ**

* **Can Decisioning Explainer explain a decision for a single profile?** Yes, ask why a specific profile did or didn't see a specific offer, on a specific date.
* **Can Decisioning Explainer explain decisions across a segment?** Yes, it can aggregate the explanation across a segment to surface the dominant reason a group of profiles isn't seeing an offer.
* **Does Decisioning Explainer show ranking scores?** Yes, it can return the final ranking score for each offer and which strategy or AI model produced it.
* **Can Decisioning Explainer change a rule or ranking formula?** No, it is read-only and does not modify decisioning configuration.

+++
