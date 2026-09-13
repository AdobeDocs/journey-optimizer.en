---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to validate a custom channel before activating a journey or campaign by testing the endpoint connection from the Channel Builder, simulating content with test profiles, sending proofs, testing in journey test mode, and simulating a journey.

**Intents:**

* Test the endpoint connection from the Channel Builder while the custom channel is in Draft status
* Simulate content against test profiles to inspect the resolved payload before any real message is sent
* Send a proof to test recipients to validate end-to-end delivery
* Validate the journey end to end using journey test mode
* Simulate a journey using simulated users without pre-created test profiles
* Work through the pre-activation checklist before activating

**Glossary:**

* **Test (Channel Builder)**: A button available while a custom channel is in Draft status that sends a test request to your endpoint to validate the end-to-end connection before activating *(product-specific)*
* **Simulate content**: A feature that resolves personalization expressions against test profiles so you can inspect the exact payload that would be sent before any real message is delivered *(product-specific)*
* **Send proof**: A tab in the Simulate content panel used to send a proof to test recipients by calling your external endpoint with the personalized payload for each selected profile *(product-specific)*
* **Test mode**: A journey activation mode for end-to-end journey validation, entered by clicking Test on the journey canvas and ended with Stop test *(product-specific)*
* **Simulation**: A mode that validates a journey end to end using simulated users—temporary profile-like entities—without requiring pre-created test profiles *(product-specific)*
* **Quick simulation**: An AI-powered option to generate simulated users for a journey simulation *(product-specific)*

**Guardrails:**

* The Test button in the Channel Builder is available while a custom channel is in Draft status.
* The connection test confirms the endpoint is reachable from Journey Optimizer's outbound IPs, that the configured authentication credentials are valid, and that the endpoint returns an HTTP 2xx response.
* In the Send proof tab you can upload a CSV file with profiles that are not defined as test profiles in Journey Optimizer.
* The proof result is displayed using the same validation patterns as email proofing: required fields, type mismatches, and schema validation errors are surfaced before the proof is sent.
* Simulation uses simulated users—temporary profile-like entities—without requiring pre-created test profiles.

**Terminology:**

* Canonical name: Simulate content — Acronym: n/a — variants: content simulation with test profiles
* Synonyms: "Test mode" = journey test mode; "Simulation" = journey simulation
* Do not confuse: "Simulate content" (resolves personalization expressions against test profiles to inspect the payload) ≠ "Send proof" (calls your external endpoint with the personalized payload for test recipients) ≠ "Simulation" (validates the journey end to end using simulated users without pre-created test profiles)
* Do not confuse: "Test profiles" (used by Simulate content and Send proof) ≠ "Simulated users" (temporary profile-like entities used by Simulation)

**FAQ:**

* **Q: How do I test the endpoint connection?** — While the custom channel is in Draft status, use the Test button in the Channel Builder to send a test request that confirms the endpoint is reachable, authentication is valid, and the endpoint returns an HTTP 2xx response.
* **Q: What does Simulate content do?** — It resolves personalization expressions against test profiles so you can inspect the exact payload that would be sent before any real message is delivered.
* **Q: Can I send a proof to profiles that are not test profiles?** — Yes, in the Send proof tab you can upload a CSV file with profiles that are not defined as test profiles in Journey Optimizer.
* **Q: What is the difference between Test mode and Simulation for journeys?** — Test mode activates the journey for end-to-end validation using a trigger event or test profile, while Simulation validates the journey end to end using simulated users—temporary profile-like entities—without requiring pre-created test profiles.
* **Q: How do I end a journey test?** — Click Stop test when done.
* **Q: What should I confirm before activating?** — The connection test succeeded, simulated payloads show expected values, no unresolved personalization tokens remain, all required payload fields are populated, a proof was sent and received correctly, and any configured error paths handle failure scenarios.

+++

<!-- ai-section-version: 1 | source-hash: d700d9c3 -->
