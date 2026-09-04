---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page explains how to use path targeting in Adobe Journey Optimizer journeys to deterministically route specific audience segments into designated journey paths based on defined rules.

**Intents:**
- Configure deterministic path targeting using the Optimize activity with a Targeting rule method
- Create new targeting rules or reuse existing rules from the Rules menu
- Define a fallback path for profiles that do not qualify for any targeting rule
- Personalize journey paths for distinct audience segments (e.g., loyalty tiers, behavior, purchase history)
- Modify inline targeting rules without affecting the original rule definition

**Glossary:**
- **Optimize activity**: A journey canvas activity used to split profiles into different paths, either via experimentation (random) or targeting (deterministic) *(product-specific)*
- **Targeting rule**: A deterministic qualification condition that decides which journey path a profile enters, based on profile or audience attributes *(product-specific)*
- **Fallback path**: An alternate journey path for profiles that do not satisfy any of the defined targeting rules *(product-specific)*

**Guardrails:**
- Path targeting is currently in Limited Availability; contact your Adobe representative to request access.
- Creating targeting rules from the dedicated Journey Optimizer Rules menu requires the Decisioning add-on or is available on demand (Limited Availability).
- When a rule is selected from the Rules menu and copied into the journey, subsequent changes to the original rule do not affect the journey's copy.
- Editing a rule inline does not modify the original rule it was sourced from.
- If the fallback path option is not enabled, profiles that do not qualify for any targeting rule exit the journey entirely.

**Terminology:**
- Canonical name: Path Targeting — Acronym: none — variants: deterministic path routing, rule-based path split
- Synonyms: "Targeting rule" = "qualification rule" = "path condition"
- Do not confuse: "Targeting" ≠ "Experimentation" (targeting is deterministic; experimentation is random assignment)

**FAQ:**
- **Q: What is the difference between path targeting and path experimentation?** — Targeting is deterministic: profiles enter a path based on defined rules. Experimentation is random: profiles are assigned to paths by chance to compare performance.
- **Q: What happens to profiles that do not qualify for any targeting rule?** — If the fallback path option is enabled, they enter the fallback path. If not enabled, they exit the journey entirely.
- **Q: Can I reuse an existing rule from the Rules menu?** — Yes, but the rule formula is copied into the journey activity; subsequent changes to the original rule in the Rules menu will not affect the journey's copy.
- **Q: Does editing a targeting rule inline change the original rule?** — No, editing inline only updates the rule within the journey activity and does not affect the source rule.
- **Q: Who can access path targeting?** — It is currently in Limited Availability; contact your Adobe representative to request access.

+++
