---
solution: Journey Optimizer
product: journey optimizer
title: Choose how to test and validate your journey
description: Compare Journey Simulation, Test mode, and Journey Dry run, and choose the right validation method for your journey before publishing.
feature: Journeys, Get Started, Test Profiles
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: test, simulate, simulation, test mode, dry run, journey, validate, compare, choose, decision guide
version: Journey Orchestration
hide: true
---

# Choose how to test and validate your journey {#choose-validation-method}

>[!BEGINSHADEBOX]

**On this page:** Compare Journey Simulation, Test mode, and Journey Dry run, and learn which one fits your current stage of building a journey — from fast iteration during design to a final pre-launch check against your live audience.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] gives you three ways to validate a journey before it goes live. They are not interchangeable: each uses a different kind of data, fits a different stage of your build, and carries different real-world consequences. Understanding the difference up front helps you avoid two common mistakes — spending time creating test profiles when a quick simulation would do, or assuming a validation step is fully "safe" when it can still contact real inboxes or make real outbound calls.

## New to validation? Start here {#quick-pick}

If you are not sure which method applies to you, answer this one question:

* **I am still designing my journey and want to test a branch quickly, without creating test profiles.** → Use **[Journey Simulation](simulate-journey-gs.md)**.
* **I want to manually walk through my draft journey step by step, using real (but designated test) profiles.** → Use **[Test mode](testing-the-journey.md)**.
* **I am about to publish and want a final check against my real production audience, without contacting anyone.** → Use **[Journey Dry run](journey-dry-run.md)**.

Still not sure, or want the full picture? Keep reading — each method is explained in detail below.

## The three validation methods {#validation-methods}

>[!BEGINTABS]

>[!TAB Journey Simulation]

**When to use:** Fast iteration during journey design, especially right before a deadline or when testing new decision-policy branches.

[Journey Simulation](simulate-journey-gs.md) validates your journey with temporary simulated users, manually created or auto-generated — no need to create or wait for real Adobe Experience Platform (AEP) test profiles to propagate. The Journey Simulation Agent automatically generates the test events your journey needs and matches them to the right simulated users, triggering the journey in seconds.

Key mechanics:

* Simulated users are temporary and disposable; they are not real profiles in AEP.
* Exit criteria, consent policies, frequency/journey capping, opt-out/suppression, and quiet hours are not evaluated.
* Custom actions and external data source calls still make real outbound calls — they are not mocked.

>[!IMPORTANT]
>
>Simulation sends real messages to the [execution addresses](simulate-journey.md#test-users) (email, phone, push token) configured on the simulated users — for example, your own email address — using the same delivery pipeline as production. It does not contact real customers or update live profile data, but the messages themselves are real.

**Perfect for:** Validating a new branch (for example, two new decision-policy paths) without waiting on AEP test-profile propagation.

➡️ [Get started with journey simulation](simulate-journey-gs.md) | [Simulate your journey](simulate-journey.md)

>[!TAB Test mode]

**When to use:** Manually verifying branch and message logic step by step, with real (but designated test) profiles walking through your draft journey.

[Test mode](testing-the-journey.md) lets you validate a draft journey using persistent [AEP test profiles](../audience/creating-test-profiles.md). You fire events manually from the interface to confirm that branching logic and message delivery mechanics work as designed, before any production audience touches the journey.

Key mechanics:

* Only profiles flagged as "test profiles" in Real-time Customer Profile can enter a journey in test mode.
* Test mode is available only for draft journeys that use a [namespace](../audience/get-started-identity.md), since it must check against AEP whether a person is a test profile.
* A maximum of 100 test profiles can enter a journey during a single test session, and events can only be fired from the interface, not from external systems via API.
* Disabling test mode removes all profiles that entered the journey and clears reporting.

>[!IMPORTANT]
>
>Test mode sends real messages to the actual inboxes of your test profiles, using the same delivery pipeline as production. It does not contact real customers, but it is not a "dry" simulation either — make sure your test profiles use addresses you control.

**Pain point:** Creating and propagating new AEP test profiles takes time, which is limiting when you need to quickly validate a new branch. If that is your goal, [Journey Simulation](simulate-journey-gs.md) solves this specific problem instead.

➡️ [Test your journey](testing-the-journey.md)

>[!TAB Journey Dry run]

**When to use:** A final, production-realistic check right before you publish.

[Journey Dry run](journey-dry-run.md) is a special journey publication mode that runs your journey against real production audience and segmentation data, without contacting real customers or updating profile information. The journey activates like a live journey — profiles flow through branches and nodes exactly as they would in production — but [action nodes](about-journey-activities.md) such as email, SMS, and custom actions are bypassed.

Key mechanics:

* Uses your actual production audience, so you see real reach and targeting at scale (for example, catching a bug where an entire branch unexpectedly receives zero profiles).
* On each activation, you can choose to disable wait activities (so metrics come back faster) and disable external data source calls (so the journey stays fully siloed).
* This is currently a **Limited Availability** feature, being rolled out globally over time.

**Perfect for:** Catching issues like mistyped condition nodes or audiences that unexpectedly do not reach a branch, right before flipping the journey live.

➡️ [Journey Dry run](journey-dry-run.md)

>[!ENDTABS]

## Which method should you use? {#decision-guide}

The answer usually comes down to one question: *how close to production do you need this test to be?*

If you are still **iterating on journey design** — testing a new branch, working against a deadline — use **Journey Simulation**. It needs no real profiles and runs in seconds. Just remember it sends real messages to the execution addresses configured on the simulated users.

If you need to **manually verify branch and message logic step by step**, and you are willing to create or reuse AEP test profiles, use **Test mode**. Just remember it sends real messages to those test profiles' real inboxes.

If you are about to **publish** and want a final check against your actual production audience — without contacting anyone or changing any profile data — use **Journey Dry run**.

>[!TIP]
>
>**Not sure where to start?** Most teams use **Journey Simulation** while building, then a **Journey Dry run** right before publishing. Reach for **Test mode** when you need to manually walk through branch logic with real test profiles instead of simulated ones.

## Quick comparison {#quick-comparison}

| Method | Data used | Sends real messages? | Best for |
|---|---|---|---|
| [Journey Simulation](simulate-journey-gs.md) | Temporary simulated users, manually created or auto-generated | Yes — to the execution addresses configured on the simulated users | Fast iteration, especially for new decision-policy branches, without waiting on real test-profile propagation |
| [Test mode](testing-the-journey.md) | Persistent AEP test profiles | Yes — to the test profiles' real inboxes, using the production delivery pipeline | Manually verifying branch/message logic step by step in a draft journey |
| [Journey Dry run](journey-dry-run.md) | Real production audience/data | No (actions bypassed) | Final pre-launch check of actual audience reach, targeting, and branch logic at real scale |

None of these methods contact real customers. Profile data is also left untouched in every case, except that Test mode updates the test profiles used to run it (not real customer profiles).

## Common mistakes to avoid {#common-mistakes}

* **Assuming Journey Simulation is fully "safe."** It is the fastest way to test, but it still sends real messages to the execution address configured on each simulated user — usually your own inbox. Do not assume nothing gets sent.
* **Creating AEP test profiles when Journey Simulation would do.** If you just need to validate a new branch or decision-policy path quickly, Simulation skips the wait for test-profile propagation entirely — save Test mode for when you actually need real test profiles.
* **Treating Test mode as "dry."** Test mode profiles receive real messages through the production delivery pipeline. Make sure your test profiles only use addresses you control.
* **Expecting Journey Dry run to catch content or delivery issues.** Dry run bypasses action nodes entirely — it validates audience reach and branch logic, not message content or delivery mechanics. Use Simulation or Test mode for that.
* **Forgetting the namespace requirement for Test mode.** Test mode only works on draft journeys that use a namespace — without one, Journey Optimizer cannot check whether a profile is flagged as a test profile.

## Next steps {#next-steps}

* **[Get started with journey simulation](simulate-journey-gs.md)** — Run your first simulation
* **[Test your journey](testing-the-journey.md)** — Activate test mode with AEP test profiles
* **[Journey Dry run](journey-dry-run.md)** — Run a production-realistic dry run
* **[Publish your journey](publish-journey.md)** — Prerequisites and the publication process
* **[Get started with journeys](journey.md)** — Fundamentals and capabilities overview
* **[Journey Orchestration FAQ](journey-faq.md)** — Common questions answered

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page compares the three journey validation methods in Adobe Journey Optimizer — Journey Simulation, Test mode, and Journey Dry run — and provides a one-question quick pick, a decision guide, a quick-comparison table, and a list of common mistakes to help users choose the right one for their current stage of building a journey.

**Intents:**

* Choose the correct validation method for a given stage of journey building
* Compare Journey Simulation, Test mode, and Journey Dry run side by side
* Understand when to use Journey Simulation for fast iteration without real test profiles
* Understand when to use Test mode for step-by-step manual validation with real test profiles
* Understand when to use Journey Dry run for a final pre-launch check against production data
* Understand which validation methods send real messages or contact real customers
* Avoid common mistakes when picking or using a validation method

**Glossary:**

* **Journey Simulation**: A validation method that uses temporary simulated users, manually created or auto-generated, to test a journey without needing real AEP test profiles. *(product-specific)*
* **Test mode**: A validation method that uses persistent AEP test profiles, flagged in Real-time Customer Profile, to manually walk through a draft journey's branch and message logic. *(product-specific)*
* **Journey Dry run**: A publication mode that runs a journey against real production audience data without contacting customers or updating profile data; action nodes are bypassed. *(product-specific)*
* **Simulation Agent**: The mechanism that automatically generates test events and matches them to simulated users during Journey Simulation. *(product-specific)*

**Guardrails:**

* Test mode is only available for draft journeys that use a namespace, and supports a maximum of 100 test profiles per session
* Test mode events can only be fired from the interface, not from external systems via API
* Test mode sends real messages to test profiles' real inboxes using the production delivery pipeline
* Disabling test mode removes all profiles that entered the journey and clears its reporting
* Journey Simulation does not evaluate exit criteria, consent policies, frequency/journey capping, opt-out/suppression, or quiet hours
* Journey Simulation's custom actions and external data source calls are real, not mocked
* Journey Simulation sends real messages to the execution addresses (email, phone, push token) configured on the simulated users, using the same delivery pipeline as production — unlike Journey Dry run, which never sends real messages
* Journey Dry run is currently a Limited Availability feature, being rolled out globally over time
* Journey Dry run bypasses action nodes (email, SMS, custom actions) but still routes profiles through branches and nodes using real production data

**Terminology:**

* Canonical name: Journey Simulation — variants: simulate, simulation mode
* Canonical name: Test mode — variants: journey testing, test your journey
* Canonical name: Journey Dry run — variants: dry run, dry run mode
* Do not confuse: Journey Simulation (temporary simulated users, no AEP test profiles needed, sends real messages to the simulated users' configured execution addresses) ≠ Test mode (persistent AEP test profiles, sends real messages to those profiles' real inboxes) ≠ Journey Dry run (real production audience data, no contact, no profile update, action nodes bypassed, never sends real messages)

**FAQ:**

* **Q: Which validation method should I use while I am still designing a journey?** — Use Journey Simulation; it needs no real test profiles and runs in seconds, making it ideal for fast iteration.
* **Q: Does Journey Simulation send real messages?** — Yes. Simulation delivers real messages to the execution addresses (email, phone, push token) configured on the simulated users — often the tester's own address — using the same delivery pipeline as production. It does not contact real customers or update live profile data, but the messages themselves are real.
* **Q: Does Test mode send real emails or SMS?** — Yes. Test mode delivers real messages to the actual inboxes of your test profiles, using the same delivery pipeline as production. It does not contact real customers, but the messages themselves are real.
* **Q: Does Journey Dry run send any messages?** — No. Dry run bypasses action nodes such as email, SMS, and custom actions, so profiles flow through the journey logic without any message being sent.
* **Q: I need to validate a new branch quickly before a deadline. Which method fits?** — Journey Simulation; it generates disposable simulated users on demand instead of requiring you to pre-create and wait for real test profiles.
* **Q: Is Journey Dry run available to everyone?** — It is currently a Limited Availability feature being rolled out globally over time; check availability for your organization.
* **Q: Can I fire test mode events from an external system?** — No; in Test mode, events can only be fired from the interface, not from external systems via API.

+++
