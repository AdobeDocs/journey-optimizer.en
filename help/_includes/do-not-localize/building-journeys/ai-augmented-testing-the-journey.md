---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use Test mode in Adobe Journey Optimizer to validate a journey with persistent test profiles before publishing, including activating test mode, triggering events, reading logs, and handling business and rule-based events.

**Intents:**
* Activate Test mode on a draft journey to validate it with pre-existing AEP test profiles
* Configure and trigger events for test profiles using the Trigger an event interface
* Override Wait activity durations in test mode to accelerate journey progression
* Read and interpret the Show log JSON output to verify profile progression and identify errors
* Test rule-based journeys and business event journeys in test mode
* Understand the limitations and behavioral differences of Test mode compared to Simulation

**Glossary:**
* **Test mode**: A journey validation state that allows persistent AEP test profiles to traverse a draft journey before it is published *(product-specific)*
* **Test profiles**: Profiles explicitly flagged as test profiles in the Adobe Experience Platform Real-time Customer Profile Service; the only profile type permitted to enter a journey in test mode *(product-specific)*
* **Visual flow**: The canvas representation that turns green to show the path a test profile has followed through the journey
* **Show log**: A test mode feature that displays journey execution state in JSON format for each test profile instance *(product-specific)*
* **Journey Orchestration Test Events**: The source name under which test mode experience events are stored in Adobe Experience Platform

**Guardrails:**
* Only profiles flagged as test profiles in AEP can enter a journey in test mode
* Test mode requires the journey to use a namespace to verify test profile identity
* Maximum 100 test profiles per single test session
* Events can only be triggered from the test mode UI; external API triggering is not supported
* Custom upload audience attribute enrichment is not supported in test mode
* Events triggered in Test mode generate real experience events that can also trigger other journeys listening to the same event
* In Test mode, Wait activities and most event timeouts default to 10 seconds; Reaction event timeouts default to a minimum of 40 seconds
* Automatic deactivation — Journeys that remain inactive in test mode for over a week automatically exit test mode and return to Draft status. No journey content is lost; only the test mode session ends.
* Journey edits are blocked while test mode is active, but direct publishing is allowed
* At a split, the top branch is always selected; reorder branches to test different paths
* Reaction event timeout minimum and default wait time is 40 seconds
* Events sent outside the journey's configured start/end date window are silently discarded
* Disabling test mode removes all profiles from the journey and clears reporting

**Terminology:**
* Canonical name: Test mode — Acronym: none — variants: test mode, journey test mode
* Canonical name: Test profiles — Acronym: none — variants: test users (Simulation UI label only)
* Synonyms: "Show log" = test results log; "visual flow" = canvas path visualization
* Do not confuse: "Test mode" ≠ "Simulation" — Test mode uses persistent AEP test profiles; Simulation uses temporary simulated users generated on the fly

**FAQ:**
* **Q: Who can enter a journey in test mode?** — Only profiles explicitly flagged as test profiles in the Adobe Experience Platform Real-time Customer Profile Service.
* **Q: How many test profiles can run in a single test session?** — A maximum of 100 test profiles per test session.
* **Q: What happens when I disable test mode?** — All profiles currently in or previously entered in the journey are removed and reporting is cleared.
* **Q: Can I edit a journey while test mode is active?** — No. The journey cannot be modified while test mode is active, but you can publish it directly without deactivating test mode first.
* **Q: Why are my test events being silently discarded?** — Events triggered outside the journey's configured active date/time window are silently discarded. Verify the journey start and end dates include the current time.
* **Q: What does the phase field in the test log indicate?** — It shows the profile's current status: running (active in journey), finished (reached end), error (stopped due to error), or timed out (stopped due to timeout).

+++
